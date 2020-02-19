from starlette.templating import Jinja2Templates
from models import Property

templates = Jinja2Templates(directory='templates')

async def homepage(request):
    try:
        filter = request.query_params['filter']

        if filter == 'under-100':
            data = request.state.db.listingsAndReviews.find({'$and':[{'cleaning_fee':{'$exists': True}},{'price': {'$lt': 100}}]}, limit=15)
        elif filter == 'highly-rated':
            data = request.state.db.listingsAndReviews.find({'$and':[{'cleaning_fee':{'$exists': True}},{'price': {'$lt': 100}},{'review_scores.review_scores_rating': {'$gt': 90}}]}, limit=15)
        elif filter == 'surprise':
            data = request.state.db.listingsAndReviews.find({'cleaning_fee':{'$exists': True},'amenities': {'$in': ["Pets allowed", "Patio or balcony", "Self check-in"]}}, limit=15)
    except KeyError:
        data = request.state.db.listingsAndReviews.find({'cleaning_fee':{'$exists': True}}, limit=15)

    response = []

    for doc in data:
        response.append(
            Property(
                doc['_id'],
                doc['name'], 
                doc['summary'], 
                doc['address']['street'], 
                str(doc['price']), 
                str(doc['cleaning_fee']),
                str(doc['accommodates']),
                doc['images']['picture_url'],
                doc['amenities']
            )
        )
    
    return templates.TemplateResponse('index.html', {'request': request, 'response': response})

async def listing(request):
    id = request.path_params['id']

    doc = request.state.db.listingsAndReviews.find_one({'_id': id})

    response = Property(
                doc['_id'],
                doc['name'], 
                doc['summary'], 
                doc['address']['street'], 
                str(doc['price']), 
                str(doc['cleaning_fee']),
                str(doc['accommodates']),
                doc['images']['picture_url'],
                doc['amenities']
            )

    return templates.TemplateResponse('listing.html', {'request': request, 'property': response})

async def confirmation(request):
    id = request.path_params['id']

    doc = request.state.db.bookings.insert({"property": id})

    return templates.TemplateResponse('confirmation.html', {'request': request, 'confirmation': doc})