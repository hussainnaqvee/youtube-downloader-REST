
# youtube-downloader-REST

A small script that downloads YouTube playlist with Rest API.


## Run Locally

Clone the project

```bash
git clone https://github.com/hussainnaqvee/youtube-downloader-REST.git
```

Go to the project directory

```bash
cd youtube-downloader-REST
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start the script

```bash
uvicorn server:app --reload
```

Request
```bash
curl -X POST https://reqbin.com/echo/post/json 
   -H "Content-Type: application/json"
   -d '{"url": ""https://www.youtube.com/playlist?list=PLb2aaNHUy_gF17YAsy887aIk26go-9Ia8""}'
```

Hello World