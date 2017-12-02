import httplib, urllib, base64, json
from collections import Counter

phone_photos = []
location_photos = []

def mode(lst):
	return Counter(lst).most_common(1)[0][0]


# Recognize a person using Microsoft Face API
def get_face_ids(url):
	subscription_key = '2b82041a72624f58a9b4423799f13889'

	uri_base = 'https://westcentralus.api.cognitive.microsoft.com/'

	# Request headers.
	headers = {
	    'Content-Type': 'application/json',
	    'Ocp-Apim-Subscription-Key': subscription_key,
	}

	# Request parameters.
	params = urllib.urlencode({
	    'returnFaceId': 'true',
	})

	# The URL of a JPEG image to analyze.
	body = "{'url': '" + url + "'}"

	try:
	    # Execute the REST API call and get the response.
	    conn = httplib.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
	    conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
	    response = conn.getresponse()
	    data = response.read()

	    # 'data' contains the JSON data. The following formats the JSON data for display.
	    parsed = json.loads(data)
	    print ("Response:")
	    print (json.dumps(parsed, sort_keys=True, indent=2))
	    conn.close()

	except Exception as e:
	    print('Error:')
	    print(e)

	faceIds = []
	for face in parsed:
		faceIds.append(face['faceId'])

	return faceIds

print(get_face_ids('https://upload.wikimedia.org/wikipedia/commons/c/c3/RH_Louise_Lillian_Gish.jpg'))

# Using all of the recent photos tagged at a location, try to find the user's profile
def get_user_profile_from_location(photo_paths, faceId):
	return []

# Using the photos on a phone, return the face id of the owner (face id that appears most number of times in photos)
def get_phone_owner_faceId(photo_paths):
	faceIds = []
	for path in photo_paths:
		faceIds.extend(get_photos_ids(path))
	return mode(faceIds)

