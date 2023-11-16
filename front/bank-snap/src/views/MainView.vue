<script setup>
// 네이버 검색 API 예제 - 블로그 검색
import express from 'express';
import request from 'request';
const app = express();
const client_id = '2KPHeGdbQvNEOM1Aly4d';
const client_secret = 'w194LdQlzo';
const PORT = 5173;

app.get('/search/blog', (req, res) => {
  const api_url = `https://openapi.naver.com/v1/search/blog?query=${encodeURI(req.query.query)}`;
  
  const options = {
    url: api_url,
    headers: { 'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
  };

  request.get(options, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      res.writeHead(200, { 'Content-Type': 'text/json;charset=utf-8' });
      res.end(body);
    } else {
      res.status(response.statusCode).end();
      console.log(`error = ${response.statusCode}`);
    }
  });
});

app.listen(PORT, () => {
  console.log(`http://127.0.0.1:${PORT}/search/blog?query=검색어 app listening on port ${PORT}!`);
});


</script>

<template>
    <div>
        <h1>Main Page</h1>
    </div>
    <div>

    </div>
</template>

<style scoped>

</style>
