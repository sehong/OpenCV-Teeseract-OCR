<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>임베디드 프로젝트</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="./css/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Gamja+Flower&display=swap" rel="stylesheet">
  </head>
  <body>
    <div class="headbar">
        <a href="https://deu.ac.kr/" target="_blank"><img src="./image/logo.png" alt="동의대로고"></a>
        <h1>임베디드 8조 프로젝트</h1>
    </div>
    <div class="name">
      저희는
      <div class="name-job">
        <ul class="name-job-list">
          <li>임베디드 8조</li>
          <li>한글 문서화 웹페이지</li>
          <li>컴퓨터 공학과 14학번 유시준</li>
          <li>컴퓨터 공학과 14학번 박승진</li>
          <li>컴퓨터 공학과 14학번 최세홍</li>
          <li>컴퓨터 공학과 17학번 김주연</li>
          <li>컴퓨터 공학과 18학번 박은지</li>
          <li>임베디드 8조</li>
        </ul>
      </div>
    </div>
    <div class="main">
      <h1>
        한글 문서화 프로그램
      </h1>
      <form action="upload.jsp" enctype="multipart/form-data" method="post">
        <div class="btn-group" role="group" aria-label="..."></div>
          <input type="file" name="file" accept="image/*">
          <input type="submit" class="btn btn-default" value="변환"></input>
        </div>
      </form>
    </div>
    <div class="section">
      <h1>개요</h1>
      <h2>프로젝트 설명 넣기</h2>
    </div>
  </body>
</html>