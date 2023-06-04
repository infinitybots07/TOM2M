if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/infinitybots07/TOM2M.git /TOM2M
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Tom2M
fi
cd /Tom2M
pip3 install -U -r requirements.txt
echo "Starting...."
python3 bot.py
