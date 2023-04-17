package main

import (
	"log"
	"net/http"

	"github.com/gorilla/mux"
	"github.com/rs/cors"

	"Room/Endpoints"
)

func main() {
	// Create a new router
	r := mux.NewRouter()

	// Define your API routes
	r.HandleFunc("/", Endpoints.HomeHandler)
	r.HandleFunc("/users", Endpoints.UsersHandler)

	// Create a new CORS handler
	c := cors.Default().Handler(r)

	// Start the server
	log.Fatal(http.ListenAndServe(":8080", c))
}
