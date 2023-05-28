if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/infinitybots07/ctom2m.git /ctom2m
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /ctom2m
fi
cd /ctom2m
pip3 install -U -r requirements.txt
echo "Starting...."
python3 bot.py
