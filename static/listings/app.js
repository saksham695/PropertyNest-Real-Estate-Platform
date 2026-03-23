const seedElement = document.getElementById('propertynest-seed-data');
const seedData = JSON.parse(seedElement.textContent);
const listings = seedData.listings;

const state = {
  favorites: new Set(seedData.favorites),
  filters: { location: 'all', type: 'all', intent: 'all', maxPrice: 2500000, favoritesOnly: false },
};

const currency = new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD', maximumFractionDigits: 0 });
const listingGrid = document.querySelector('#listing-grid');
const shortlist = document.querySelector('#shortlist');
const resultsSummary = document.querySelector('#results-summary');
const filterForm = document.querySelector('#filters');
const template = document.querySelector('#listing-template');
const maxPriceLabel = document.querySelector('#max-price-label');
const visitForm = document.querySelector('#visit-form');
const visitConfirmation = document.querySelector('#visit-confirmation');
const mortgageForm = document.querySelector('#mortgage-form');

function formatPrice(listing) {
  return listing.intent === 'rent' ? `${currency.format(listing.price)}/mo` : currency.format(listing.price);
}

function applyFilters() {
  return listings.filter((listing) => {
    const matchesLocation = state.filters.location === 'all' || listing.location === state.filters.location;
    const matchesType = state.filters.type === 'all' || listing.type === state.filters.type;
    const matchesIntent = state.filters.intent === 'all' || listing.intent === state.filters.intent;
    const matchesPrice = listing.price <= Number(state.filters.maxPrice);
    const matchesFavorites = !state.filters.favoritesOnly || state.favorites.has(listing.id);
    return matchesLocation && matchesType && matchesIntent && matchesPrice && matchesFavorites;
  });
}

function renderListings() {
  const filtered = applyFilters();
  listingGrid.innerHTML = '';
  resultsSummary.textContent = `${filtered.length} properties matching current filters`;

  filtered.forEach((listing) => {
    const node = template.content.cloneNode(true);
    node.querySelector('.listing-photo').src = listing.image;
    node.querySelector('.listing-photo').alt = `${listing.title} in ${listing.location}`;
    node.querySelector('.listing-price').textContent = formatPrice(listing);
    node.querySelector('.listing-title').textContent = listing.title;
    node.querySelector('.listing-meta').textContent = `${listing.location} • ${listing.type} • ${listing.beds} bd • ${listing.baths} ba • ${listing.area} sq ft`;
    node.querySelector('.listing-description').textContent = listing.description;
    node.querySelector('.agent-name').textContent = listing.agent;
    node.querySelector('.agent-rating').textContent = `⭐ ${listing.rating} agent rating`;

    const tagRow = node.querySelector('.tag-row');
    listing.tags.forEach((tag) => {
      const chip = document.createElement('span');
      chip.className = 'tag';
      chip.textContent = tag;
      tagRow.append(chip);
    });

    const favoriteButton = node.querySelector('.favorite-button');
    favoriteButton.dataset.id = listing.id;
    favoriteButton.classList.toggle('active', state.favorites.has(listing.id));
    favoriteButton.textContent = state.favorites.has(listing.id) ? '♥' : '♡';
    listingGrid.append(node);
  });
}

function renderShortlist() {
  const favoriteListings = listings.filter((listing) => state.favorites.has(listing.id));
  shortlist.innerHTML = '';

  if (!favoriteListings.length) {
    shortlist.innerHTML = '<li class="empty-state">No favorites yet. Save listings to compare later.</li>';
    return;
  }

  favoriteListings.forEach((listing) => {
    const item = document.createElement('li');
    item.innerHTML = `<div><strong>${listing.title}</strong><p>${listing.location} • ${formatPrice(listing)}</p></div><span>${listing.type}</span>`;
    shortlist.append(item);
  });
}

function updateMortgage() {
  const principal = Number(mortgageForm.elements.principal.value);
  const downPayment = Number(mortgageForm.elements.downPayment.value) / 100;
  const interestRate = Number(mortgageForm.elements.interestRate.value) / 100 / 12;
  const termMonths = Number(mortgageForm.elements.termYears.value) * 12;
  const loanAmount = principal * (1 - downPayment);
  const payment = interestRate === 0
    ? loanAmount / termMonths
    : (loanAmount * interestRate) / (1 - (1 + interestRate) ** -termMonths);

  document.querySelector('#mortgage-payment').textContent = `${currency.format(payment)}/mo`;
  document.querySelector('#mortgage-breakdown').textContent = `Loan amount ${currency.format(loanAmount)} over ${termMonths} months.`;
}

filterForm.addEventListener('input', (event) => {
  const { name, value, type, checked } = event.target;
  state.filters[name] = type === 'checkbox' ? checked : value;
  if (name === 'maxPrice') {
    maxPriceLabel.textContent = `Up to ${currency.format(Number(value))}`;
  }
  renderListings();
});

filterForm.addEventListener('reset', () => {
  requestAnimationFrame(() => {
    state.filters = { location: 'all', type: 'all', intent: 'all', maxPrice: 2500000, favoritesOnly: false };
    maxPriceLabel.textContent = `Up to ${currency.format(2500000)}`;
    renderListings();
  });
});

listingGrid.addEventListener('click', (event) => {
  const button = event.target.closest('.favorite-button');
  if (!button) return;

  const id = Number(button.dataset.id);
  if (state.favorites.has(id)) {
    state.favorites.delete(id);
  } else {
    state.favorites.add(id);
  }

  renderListings();
  renderShortlist();
});

mortgageForm.addEventListener('input', updateMortgage);

visitForm.addEventListener('submit', (event) => {
  event.preventDefault();
  const propertyId = Number(visitForm.elements.propertyId.value);
  const listing = listings.find((item) => item.id === propertyId);
  const date = visitForm.elements.visitDate.value;
  const time = visitForm.elements.visitTime.value;

  visitConfirmation.textContent = `Visit confirmed for ${listing.title} on ${date} at ${time}.`;
  visitConfirmation.className = 'form-message success';
});

renderListings();
renderShortlist();
updateMortgage();
