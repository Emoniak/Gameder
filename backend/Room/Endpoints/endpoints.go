package Endpoints

import (
	"fmt"
	"net/http"
)

func HomeHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Welcome to my API!")
}

func UsersHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "This is the users API!")
}
