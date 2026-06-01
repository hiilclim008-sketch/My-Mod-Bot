FROM ubuntu:20.04

# एनवायरनमेंट सेट करें ताकि कोई सवाल न पूछे
ENV DEBIAN_FRONTEND=noninteractive

# सिस्टम को अपडेट करें और जरूरी टूल्स इंस्टॉल करें
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    openjdk-11-jre-headless \
    wget \
    && rm -rf /var/lib/apt/lists/*

# APKTool सेटअप करें
RUN wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.9.3.jar -O /usr/local/bin/apktool.jar && \
    echo '#!/bin/bash\njava -jar /usr/local/bin/apktool.jar "$@"' > /usr/local/bin/apktool && \
    chmod +x /usr/local/bin/apktool

WORKDIR /app

# पायथन लाइब्रेरी इंस्टॉल करें
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# बाकी फाइल्स कॉपी करें
COPY . .

# बॉट शुरू करें
CMD ["python3", "bot.py"]
