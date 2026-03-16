from fastapi  import FastAPI


app = FastAPI(title= "Blog",version="0.1.0")

@app.get("/")
def hello():
    return {"msg":"Hello FAPI I am Faastttt, I have added this new line to test the commit and push functionality of git, I am learning fastapi and I am loving it"} 
