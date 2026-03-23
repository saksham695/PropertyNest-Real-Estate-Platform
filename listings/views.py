import json

from django.shortcuts import render

ROLES = ['Buyer / Tenant', 'Agent', 'Property Owner', 'Admin']

LISTINGS = [
    {
        'id': 1,
        'title': 'Skyline Penthouse',
        'location': 'New York',
        'type': 'Condo',
        'intent': 'buy',
        'price': 1850000,
        'beds': 3,
        'baths': 2,
        'area': 2100,
        'agent': 'Maya Chen',
        'rating': 4.9,
        'image': 'https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?auto=format&fit=crop&w=1200&q=80',
        'description': 'Floor-to-ceiling skyline views, concierge access, and a flexible den for remote work.',
        'tags': ['Rooftop lounge', 'Floor plan', 'Smart home'],
    },
    {
        'id': 2,
        'title': 'Sunset Family Villa',
        'location': 'Austin',
        'type': 'House',
        'intent': 'buy',
        'price': 920000,
        'beds': 4,
        'baths': 3,
        'area': 2850,
        'agent': 'Jordan Alvarez',
        'rating': 4.8,
        'image': 'https://images.unsplash.com/photo-1568605114967-8130f3a36994?auto=format&fit=crop&w=1200&q=80',
        'description': 'Large backyard, updated kitchen, and excellent access to top school zones.',
        'tags': ['Pool', 'Garage', 'Owner docs ready'],
    },
    {
        'id': 3,
        'title': 'Harbor Loft Rental',
        'location': 'Seattle',
        'type': 'Apartment',
        'intent': 'rent',
        'price': 4100,
        'beds': 2,
        'baths': 2,
        'area': 1180,
        'agent': 'Nina Patel',
        'rating': 4.7,
        'image': 'https://images.unsplash.com/photo-1494526585095-c41746248156?auto=format&fit=crop&w=1200&q=80',
        'description': 'Warehouse-style loft with exposed beams, private balcony, and pet-friendly policy.',
        'tags': ['Waterfront', 'Transit nearby', 'Virtual tour'],
    },
    {
        'id': 4,
        'title': 'Garden Terrace Townhome',
        'location': 'Chicago',
        'type': 'Townhome',
        'intent': 'buy',
        'price': 640000,
        'beds': 3,
        'baths': 2.5,
        'area': 1900,
        'agent': 'Liam Brooks',
        'rating': 4.6,
        'image': 'https://images.unsplash.com/photo-1449844908441-8829872d2607?auto=format&fit=crop&w=1200&q=80',
        'description': 'Bi-level townhome featuring a private terrace, EV charging, and quick CTA access.',
        'tags': ['EV ready', 'Floor plan', 'Corner unit'],
    },
    {
        'id': 5,
        'title': 'Beachfront Executive Lease',
        'location': 'Miami',
        'type': 'Condo',
        'intent': 'rent',
        'price': 7800,
        'beds': 3,
        'baths': 3,
        'area': 1680,
        'agent': 'Avery Scott',
        'rating': 5.0,
        'image': 'https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80',
        'description': 'Resort-style amenities, furnished interiors, and direct beach access for premium tenants.',
        'tags': ['Furnished', 'Beach access', 'Doorman'],
    },
    {
        'id': 6,
        'title': 'Tech Corridor Starter Home',
        'location': 'San Jose',
        'type': 'House',
        'intent': 'buy',
        'price': 1125000,
        'beds': 3,
        'baths': 2,
        'area': 1560,
        'agent': 'Sofia Martinez',
        'rating': 4.8,
        'image': 'https://images.unsplash.com/photo-1570129477492-45c003edd2be?auto=format&fit=crop&w=1200&q=80',
        'description': 'Move-in ready home with backyard studio, upgraded HVAC, and close-in commuter access.',
        'tags': ['ADU potential', 'Near light rail', 'Inspections uploaded'],
    },
]

DOCUMENTS = [
    {'name': 'Proof of Funds', 'owner': 'Buyer / Tenant', 'status': 'approved'},
    {'name': 'Seller Disclosure Packet', 'owner': 'Property Owner', 'status': 'approved'},
    {'name': 'Lease Application Bundle', 'owner': 'Admin', 'status': 'pending'},
    {'name': 'Inspection Report', 'owner': 'Agent', 'status': 'missing'},
]

REVIEWS = [
    {'agent': 'Maya Chen', 'stars': 5, 'summary': 'Outstanding responsiveness, transparent negotiation guidance, and a seamless digital closing flow.'},
    {'agent': 'Jordan Alvarez', 'stars': 5, 'summary': 'Deep market expertise and excellent scheduling coordination for multi-property tours.'},
    {'agent': 'Nina Patel', 'stars': 4, 'summary': 'Great local recommendations and a strong understanding of tenant needs near transit corridors.'},
]

ANALYTICS = [
    {'area': 'New York', 'walk_score': 96, 'schools': 'A', 'yoy_growth': '+7.8%', 'avg_dom': 22},
    {'area': 'Austin', 'walk_score': 71, 'schools': 'A-', 'yoy_growth': '+6.1%', 'avg_dom': 28},
    {'area': 'Seattle', 'walk_score': 88, 'schools': 'B+', 'yoy_growth': '+4.4%', 'avg_dom': 19},
    {'area': 'Miami', 'walk_score': 83, 'schools': 'B', 'yoy_growth': '+5.7%', 'avg_dom': 31},
]


def dashboard(request):
    context = {
        'roles': ROLES,
        'listings_count': len(LISTINGS),
        'locations': sorted({listing['location'] for listing in LISTINGS}),
        'property_types': sorted({listing['type'] for listing in LISTINGS}),
        'documents': DOCUMENTS,
        'reviews': REVIEWS,
        'analytics': ANALYTICS,
        'visit_options': LISTINGS,
        'seed_data_json': json.dumps(
            {
                'listings': LISTINGS,
                'favorites': [2, 5],
            }
        ),
    }
    return render(request, 'listings/dashboard.html', context)
