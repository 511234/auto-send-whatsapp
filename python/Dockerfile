FROM python:3.9
RUN apt-get update && apt-get install python3 python3-pip curl unzip -yf
RUN apt-get update -y
RUN apt-get install -y dbus-x11
USER root
RUN apt update
RUN apt-get clean
RUN apt install -y python3 python3-pip
RUN DEBIAN_FRONTEND=noninteractive apt install -y python3-xlib python3-tk python3-dev
RUN apt install -y xvfb xserver-xephyr
RUN Xvfb :99 -ac &
RUN export DISPLAY=:99
RUN pip3 install virtualenv
RUN virtualenv .venv
RUN /bin/bash -c "source .venv/bin/activate"
RUN pip3 install --upgrade setuptools pip
RUN pip3 install flask keyboard pyvirtualdisplay pyautogui pandas python-xlib
COPY . .
EXPOSE 28311
RUN pwd && ls
ENTRYPOINT ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=28311"]