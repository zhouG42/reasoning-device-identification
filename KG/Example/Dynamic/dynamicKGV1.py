from flask import Flask, Response
from rdflib import Graph, Namespace
import threading
import time

app = Flask(__name__)

# Define namespace
EX = Namespace("http://example.com/")

# Load RDF graph
rdf_file = "./try1.ttl"
graph = Graph()
graph.parse(rdf_file, format="turtle")

# Define the person and current location predicate
person = EX.Alice
current = EX.currentLocation

# List of locations to iterate over
locations = ["Office", "CopyRoom", "IoTLab"]


def update_graph():
    while True:
        for location in locations:
            # Remove existing occupancy triple
            graph.remove((person, current, None))

            # Create the resource for the location (e.g., :CopyRoom, :Office, etc.)
            location_resource = EX[location]

            # Add new occupancy triple with the resource (not a literal)
            graph.add((person, current, location_resource))

            # Save updated graph back to file
            with open(rdf_file, "wb") as f:
                graph.serialize(destination=f, format="turtle")
                f.flush()

            time.sleep(1)  # Wait for 1 second before updating


# Start the graph update loop in a separate thread
threading.Thread(target=update_graph, daemon=True).start()


@app.route('/graph')
def serve_graph():
    return Response(graph.serialize(format="turtle"), mimetype="text/turtle")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
