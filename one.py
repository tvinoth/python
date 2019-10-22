{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>day</th>\n",
       "      <th>tem</th>\n",
       "      <th>windspeed</th>\n",
       "      <th>event</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10-05-2019</td>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>11-05-2019</td>\n",
       "      <td>19</td>\n",
       "      <td>19</td>\n",
       "      <td>hot</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>12-05-2019</td>\n",
       "      <td>9</td>\n",
       "      <td>3</td>\n",
       "      <td>sunny</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>13-05-2019</td>\n",
       "      <td>05</td>\n",
       "      <td>6</td>\n",
       "      <td>snow</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>14-05-2019</td>\n",
       "      <td>20</td>\n",
       "      <td>10</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>15-05-2019</td>\n",
       "      <td>15</td>\n",
       "      <td>5</td>\n",
       "      <td>suuny</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          day tem windspeed  event\n",
       "0  10-05-2019  10         1   rain\n",
       "1  11-05-2019  19        19    hot\n",
       "2  12-05-2019   9         3  sunny\n",
       "3  13-05-2019  05         6   snow\n",
       "4  14-05-2019  20        10   rain\n",
       "5  15-05-2019  15         5  suuny"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "data = {\n",
    "\t\"day\" : [\"10-05-2019\",\"11-05-2019\",\"12-05-2019\",\"13-05-2019\",\"14-05-2019\",\"15-05-2019\"],\n",
    "\t\"tem\" : [\"10\",\"19\",\"9\",\"05\",\"20\",\"15\"],\n",
    "    \"windspeed\" : [\"1\",\"19\",\"3\",\"6\",\"10\",\"5\"],\n",
    "\t\"event\" : [\"rain\",\"hot\",\"sunny\",\"snow\",\"rain\",\"suuny\"]\n",
    "}\n",
    "df = pd.DataFrame(data)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(6, 4)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rows,columns = df.shape\n",
    "rows,columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>day</th>\n",
       "      <th>tem</th>\n",
       "      <th>windspeed</th>\n",
       "      <th>event</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10-05-2019</td>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>11-05-2019</td>\n",
       "      <td>19</td>\n",
       "      <td>19</td>\n",
       "      <td>hot</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>12-05-2019</td>\n",
       "      <td>9</td>\n",
       "      <td>3</td>\n",
       "      <td>sunny</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>13-05-2019</td>\n",
       "      <td>05</td>\n",
       "      <td>6</td>\n",
       "      <td>snow</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>14-05-2019</td>\n",
       "      <td>20</td>\n",
       "      <td>10</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          day tem windspeed  event\n",
       "0  10-05-2019  10         1   rain\n",
       "1  11-05-2019  19        19    hot\n",
       "2  12-05-2019   9         3  sunny\n",
       "3  13-05-2019  05         6   snow\n",
       "4  14-05-2019  20        10   rain"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>day</th>\n",
       "      <th>tem</th>\n",
       "      <th>windspeed</th>\n",
       "      <th>event</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>11-05-2019</td>\n",
       "      <td>19</td>\n",
       "      <td>19</td>\n",
       "      <td>hot</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>12-05-2019</td>\n",
       "      <td>9</td>\n",
       "      <td>3</td>\n",
       "      <td>sunny</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>13-05-2019</td>\n",
       "      <td>05</td>\n",
       "      <td>6</td>\n",
       "      <td>snow</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>14-05-2019</td>\n",
       "      <td>20</td>\n",
       "      <td>10</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>15-05-2019</td>\n",
       "      <td>15</td>\n",
       "      <td>5</td>\n",
       "      <td>suuny</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          day tem windspeed  event\n",
       "1  11-05-2019  19        19    hot\n",
       "2  12-05-2019   9         3  sunny\n",
       "3  13-05-2019  05         6   snow\n",
       "4  14-05-2019  20        10   rain\n",
       "5  15-05-2019  15         5  suuny"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0     rain\n",
       "1      hot\n",
       "2    sunny\n",
       "3     snow\n",
       "4     rain\n",
       "5    suuny\n",
       "Name: event, dtype: object"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['event']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>day</th>\n",
       "      <th>tem</th>\n",
       "      <th>windspeed</th>\n",
       "      <th>event</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>unique</th>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>top</th>\n",
       "      <td>12-05-2019</td>\n",
       "      <td>19</td>\n",
       "      <td>19</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>freq</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               day tem windspeed event\n",
       "count            6   6         6     6\n",
       "unique           6   6         6     5\n",
       "top     12-05-2019  19        19  rain\n",
       "freq             1   1         1     2"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>day</th>\n",
       "      <th>tem</th>\n",
       "      <th>windspeed</th>\n",
       "      <th>event</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>12-05-2019</td>\n",
       "      <td>9</td>\n",
       "      <td>3</td>\n",
       "      <td>sunny</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          day tem windspeed  event\n",
       "2  12-05-2019   9         3  sunny"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.tem == df['tem'].max()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RangeIndex(start=0, stop=6, step=1)"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "ename": "ValueError",
     "evalue": "No axis named 15-05-2019 for object type <class 'type'>",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-26-1ebb59c79153>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mloc\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"15-05-2019\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;32mc:\\users\\elcot\\appdata\\local\\programs\\python\\python37-32\\lib\\site-packages\\pandas\\core\\indexing.py\u001b[0m in \u001b[0;36m__call__\u001b[1;34m(self, axis)\u001b[0m\n\u001b[0;32m    100\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    101\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0maxis\u001b[0m \u001b[1;32mis\u001b[0m \u001b[1;32mnot\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 102\u001b[1;33m             \u001b[0maxis\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mobj\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_get_axis_number\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0maxis\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    103\u001b[0m         \u001b[0mnew_self\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0maxis\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0maxis\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    104\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mnew_self\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32mc:\\users\\elcot\\appdata\\local\\programs\\python\\python37-32\\lib\\site-packages\\pandas\\core\\generic.py\u001b[0m in \u001b[0;36m_get_axis_number\u001b[1;34m(cls, axis)\u001b[0m\n\u001b[0;32m    359\u001b[0m                 \u001b[1;32mpass\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    360\u001b[0m         raise ValueError('No axis named {0} for object type {1}'\n\u001b[1;32m--> 361\u001b[1;33m                          .format(axis, type(cls)))\n\u001b[0m\u001b[0;32m    362\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    363\u001b[0m     \u001b[1;33m@\u001b[0m\u001b[0mclassmethod\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mValueError\u001b[0m: No axis named 15-05-2019 for object type <class 'type'>"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
