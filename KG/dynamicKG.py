from flask import Flask, Response
from rdflib import Graph, Namespace, Literal
import threading
import time

app = Flask(__name__)

# Define namespace
EX = Namespace("http://example.org/")

# Load RDF graph
rdf_file = "./kg.ttl"
graph = Graph()
graph.parse(rdf_file, format="turtle")


# Define the room and predicate
person = EX.Alice
sits_in = EX.sitsIn

# List of locations to iterate over
locations = ["office", "copy_room", "IoT lab"]

def update_graph():
    while True:
        for location in locations:
            # Remove existing occupancy triple
            graph.remove((person, sits_in, None))

            # Add new occupancy triple
            graph.add((person, sits_in, Literal(location)))

            # Save updated graph back to file
            graph.serialize(destination=rdf_file, format="turtle")

            time.sleep(1)  # Wait for 1 second before updating

# Start the graph update loop in a separate thread
threading.Thread(target=update_graph, daemon=True).start()

@app.route('/graph')
def serve_graph():
    return Response(graph.serialize(format="turtle"), mimetype="text/turtle")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
