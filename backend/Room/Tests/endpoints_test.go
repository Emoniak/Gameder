package test

import (
	"net/http"
	"net/http/httptest"
	"testing"

	"Room/Endpoints"
)

func TestHomeHandler(t *testing.T) {
	// Create a new HTTP request with a GET method and an empty request body
	req, err := http.NewRequest("GET", "/", nil)
	if err != nil {
		t.Fatal(err)
	}

	// Create a new HTTP response recorder to capture the response
	rr := httptest.NewRecorder()

	// Call the HomeHandler function with the HTTP response recorder and HTTP request
	Endpoints.HomeHandler(rr, req)

	// Check the status code of the HTTP response
	if status := rr.Code; status != http.StatusOK {
		t.Errorf("handler returned wrong status code: got %v want %v",
			status, http.StatusOK)
	}

	// Check the body of the HTTP response
	expected := "Welcome to my API!\n"
	if rr.Body.String() != expected {
		t.Errorf("handler returned unexpected body: got %v want %v",
			rr.Body.String(), expected)
	}
}

func TestUsersHandler(t *testing.T) {
	// Create a new HTTP request with a GET method and an empty request body
	req, err := http.NewRequest("GET", "/users", nil)
	if err != nil {
		t.Fatal(err)
	}

	// Create a new HTTP response recorder to capture the response
	rr := httptest.NewRecorder()

	// Call the UsersHandler function with the HTTP response recorder and HTTP request
	Endpoints.UsersHandler(rr, req)

	// Check the status code of the HTTP response
	if status := rr.Code; status != http.StatusOK {
		t.Errorf("handler returned wrong status code: got %v want %v",
			status, http.StatusOK)
	}

	// Check the body of the HTTP response
	expected := "This is the users API!\n"
	if rr.Body.String() != expected {
		t.Errorf("handler returned unexpected body: got %v want %v",
			rr.Body.String(), expected)
	}
}
