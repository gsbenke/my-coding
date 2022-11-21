
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/login/{password}")
def login(password):
    if password == "dragon":
        return "Login successful."
    else:
        raise HTTPException(status_code=403, detail="Password incorrect.")

@app.post("test")
def testingpost(username):
    return f"Your username is {username}"

