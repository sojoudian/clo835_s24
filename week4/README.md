## Test "POST API"
To use the curl command to post data to your Go API, you would typically use the POST method and include the necessary data as JSON in the body of the request. Assuming your API is running locally on port 8080 and expects data for items, here is an example of how you could structure the curl command to add an item:

Example Curl Command

```bash
curl -X POST http://localhost:8080/items \
     -H "Content-Type: application/json" \
     -d '{"id": "1", "name": "Example Item"}'
```
## Explanation
-X POST: Specifies the request method as POST.
http://localhost:8080/items: The URL where your API endpoint is exposed. Adjust the hostname and port if your setup is different.
-H "Content-Type: application/json": Sets the header to indicate that the data being sent is in JSON format.
-d '{"id": "1", "name": "Example Item"}': The data being sent to the API. This JSON object contains the id and name fields as defined in your Go struct. Modify the JSON string to include the actual data you want to post.
Make sure that the JSON structure you send matches the data structure expected by your API. In this case, the Item struct expects fields for id and name. If your API is hosted elsewhere or uses different field names or types, you'll need to adjust the curl command accordingly.