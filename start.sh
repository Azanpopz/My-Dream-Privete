if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Azanpopz/My-Dream-Privete.git /My-Dream-Privete
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /My-Dream-Privete
fi
cd /My-Dream-Privete
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
