const express = require('express');
const app = express();
const dotenv = require('dotenv');
const mongodb = require('mongodb');

dotenv.config();

const MONGODB_URI = process.env.MONGODB_URI;
const PORT = process.env.PORT || 3000;

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// MongoDB 연결 함수
async function connectToDB() {
  try {
    const client = await mongodb.MongoClient.connect('mongodb://localhost:27017/mydatabase', {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
    return client.db();
  } catch (err) {
    console.error('Error connecting to the database:', err);
    throw err;
  }
}

// 식당 정보 검색 API
app.get('/search', async (req, res) => {
  const query = req.query.name;

  if (!query) {
    return res.status(400).json({ error: '식당 이름을 입력해주세요.' });
  }

  try {
    const db = await connectToDB();
    const restaurants = db.collection('restaurants');
    const result = await restaurants.findOne({ name: query });

    if (result) {
      res.json(result);
    } else {
      res.status(404).json({ error: '해당 식당을 찾을 수 없습니다.' });
    }
  } catch (err) {
    console.error('Error searching for restaurants:', err);
    res.status(500).json({ error: '서버 오류가 발생했습니다.' });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
/*
  // MongoDB에 샘플 데이터 추가
  async function seedData() {
    const client = new mongodb.MongoClient('mongodb://localhost:27017/mydatabase', {
      useNewUrlParser: true,
      useUnifiedTopology: true,
    });
  
    try {
      await client.connect();
      const db = client.db('restaurant');
      const restaurants = db.collection('restaurant');
  
      // 샘플 데이터 추가
      await restaurants.insertMany([
        {
          name: '레스토랑A',
          location: '서울시 강남구',
          cuisine: '한식',
          rating: 4.5,
        },
        {
          name: '레스토랑B',
          location: '서울시 마포구',
          cuisine: '양식',
          rating: 4.2,
        },
        // 추가적인 샘플 데이터 작성 가능
      ]);
  
      console.log('Sample data inserted successfully.');
    } catch (err) {
      console.error('Error seeding data:', err);
    } finally {
      client.close();
    }
  }
  
  // 샘플 데이터 삽입
  seedData();
  */