package main

import (
	"context"
	"encoding/json"
	"log"
	"net/http"
	"time"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

// Item represents the structure for an API item
type Item struct {
	ID   string `json:"id" bson:"id"`
	Name string `json:"name" bson:"name"`
}

var mongoClient *mongo.Client

func main() {
	// Connect to MongoDB
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	client, err := mongo.Connect(ctx, options.Client().ApplyURI("mongodb://localhost:27017"))
	if err != nil {
		log.Fatal(err)
	}
	mongoClient = client

	http.HandleFunc("/items", itemsHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func itemsHandler(w http.ResponseWriter, r *http.Request) {
	switch r.Method {
	case http.MethodGet:
		getItems(w, r)
	case http.MethodPost:
		postItem(w, r)
	default:
		http.Error(w, "Unsupported request method.", http.StatusMethodNotAllowed)
	}
}

func getItems(w http.ResponseWriter, r *http.Request) {
	var items []Item
	collection := mongoClient.Database("mydb").Collection("items")

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	cursor, err := collection.Find(ctx, bson.M{})
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	defer cursor.Close(ctx)

	for cursor.Next(ctx) {
		var item Item
		cursor.Decode(&item)
		items = append(items, item)
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(items)
}

func postItem(w http.ResponseWriter, r *http.Request) {
	var item Item
	if err := json.NewDecoder(r.Body).Decode(&item); err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	collection := mongoClient.Database("mydb").Collection("items")
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	_, err := collection.InsertOne(ctx, item)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(item)
}
