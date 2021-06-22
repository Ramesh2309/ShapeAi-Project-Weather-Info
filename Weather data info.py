{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "08e02472",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter Your City = delhi\n",
      "temprature: 37.05000000000001\n",
      "hmdt: 36\n",
      "weather_desc: haze\n",
      "wind_spd: 1.03\n",
      "cordinatelon: 1.03\n",
      "cordinatelat: 28.6667\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "\n",
    "city=input(\"Enter Your City = \")\n",
    "Api_Key = \"eeeed4e6927bc2d22e1cc8a319b4f6ab\" \n",
    "\n",
    "final_URL = \"http://api.openweathermap.org/data/2.5/weather?q={}&appid={}\".format(city,Api_Key)\n",
    "\n",
    "result = requests.get(final_URL)\n",
    "data = result.json()\n",
    "\n",
    "temprature = ((data['main']['temp']) - 273.15)\n",
    "hmdt = data['main']['humidity']\n",
    "weather_desc = data['weather'][0]['description']\n",
    "wind_spd = data['wind']['speed']\n",
    "cordinatelon = data['coord']['lon']\n",
    "cordinatelat = data['coord']['lat']\n",
    "\n",
    "print(\"temprature:\",temprature,)\n",
    "print(\"hmdt:\",hmdt,)\n",
    "print(\"weather_desc:\",weather_desc,)\n",
    "print(\"wind_spd:\",wind_spd,)\n",
    "print(\"cordinatelon:\",wind_spd,)\n",
    "print(\"cordinatelat:\",cordinatelat,)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90ca8787",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
