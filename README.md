# weventure REST api


### Sending current location to get the closest historical picture
```
/check-location?lng=23.78&lat=56.34 POST
```

returns
```json
{"found": 1, "image": <encoded-image-string> , "challenge-id": 1234 }
```

OR

```json
{"found": 0}
```

### Get points of the user

```
/get-points?user-id=1   POST
```

```json
{"points": 345}
```

### Submit the taken picture

```
/submit-challenge-photo POST
```
```json
{"challenge-id": 4123, "picture": <encoded-image-string>}
```

return

```json
{"challenge-id": 4123, "points": 80}
```
