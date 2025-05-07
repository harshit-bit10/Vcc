FROM mysterysd/wzmlx:heroku

WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app

# Update and install dependencies including ffmpeg
RUN apt -qq update && \
    apt -qq install -y fontconfig ffmpeg

COPY . .

RUN pip3 install -r requirements.txt

CMD ["bash", "run.sh"]
