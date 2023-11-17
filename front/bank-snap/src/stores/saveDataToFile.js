const axios = require('axios');
const fs = require('fs');

const fetchDataAndSaveToFile = async () => {
  try {
    const response = await axios.get('https://api.example.com/data'); // 실제 API 엔드포인트에 맞게 수정

    // 받아온 데이터를 JSON 파일로 저장
    fs.writeFileSync('data.json', JSON.stringify(response.data, null, 2));

    console.log('데이터를 JSON 파일로 저장했습니다.');
  } catch (error) {
    console.error('데이터를 저장하는 중에 에러가 발생했습니다:', error);
  }
};

fetchDataAndSaveToFile();
