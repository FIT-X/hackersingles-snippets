import json

from clarifai.rest import ClarifaiApp

from math import sqrt

from numpy import linalg

from numpy import array

 

# Initalize Clarifai and get the Face Embedding model

app = ClarifaiApp(api_key='74abff9bee1541ddbf19dd104e10d602')

model = app.models.get("d02b4508df58432fbb84e800597b8959")

 

# Dataset

testPhoto = "https://storage.googleapis.com/pennappsfacebucket/petertest.jpg"

peterPhoto = "https://storage.googleapis.com/pennappsfacebucket/peter.jpg"

chrisPhoto = "https://storage.googleapis.com/pennappsfacebucket/chris.jpg"

 

# Function to get embedding from image

def getEmbedding(image_url):

# Call the Face Embedding Model

    jsonTags = model.predict_by_url(url=image_url)

 

# Storage for all the vectors in a given photo

    faceEmbed = []

 

# Iterate through every person and store each face embedding in an array

    for faces in jsonTags['outputs'][0]['data']['regions']:

        for face in faces['data']['embeddings']:

            embeddingVector = face['vector']

            faceEmbed.append(embeddingVector)

    return faceEmbed[0]

 

# Get embeddings and put them in an array format that Numpy can use

testEmbedding = array(getEmbedding(testPhoto))

peterEmbedding = array(getEmbedding(peterPhoto))

chrisEmbedding = array(getEmbedding(chrisPhoto))

 

# Get Distances useing Numpy

peterDistance = linalg.norm(testEmbedding-peterEmbedding)


print ("peter Distance: "+str(peterDistance))

 

chrisDistance = linalg.norm(testEmbedding-chrisEmbedding)

print ("chris Distance: "+str(chrisDistance))

 

# Print results

print ("")

print ("**************** Results are In: ******************")

if peterDistance < chrisDistance:

    print ("test looks more similar to his peter")

elif peterDistance > chrisDistance:

    print ("test looks more similar to his chris")

else:

    print ("test looks equally similar to both his peter and chris")


print ("")
