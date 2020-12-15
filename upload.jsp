<%@page import="java.util.Enumeration" %>
<%@page import="com.oreilly.servlet.multipart.DefaultFileRenamePolicy"%>
<%@page import="com.oreilly.servlet.MultipartRequest"%>
<%@page import="javax.servlet.http.*" %>
<%@page import="org.python.util.PythonInterpreter" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	String ip="";
	String fileName="";
	String orgfileName="";
	String filePath="";
	String uploadPath=request.getRealPath("/");
	try {
		MultipartRequest multi = new MultipartRequest( // MultipartRequest 인스턴스 생성(cos.jar의 라이브러리)
				request, 
				uploadPath, // 파일을 저장할 디렉토리 지정
				1000 * 1024, // 첨부파일 최대 용량 설정(bite) / 10KB / 용량 초과 시 예외 발생
				"utf-8", // 인코딩 방식 지정
				new DefaultFileRenamePolicy() // 중복 파일 처리(동일한 파일명이 업로드되면 뒤에 숫자 등을 붙여 중복 회피)
		);
		ip=request.getHeader("X-FORWARDED-FOR");
		if (ip == null || ip.length() == 0) {
			ip= request.getHeader("Proxy-Client-IP");
		}
		if (ip == null || ip.length() == 0) {
			ip= request.getHeader("WL-Proxy-Client-IP");
		}
		if (ip == null || ip.length() == 0) {
			ip= request.getRemoteAddr();
		}
		fileName = multi.getFilesystemName("file"); 
		orgfileName = multi.getOriginalFileName("file");
		
	} catch (Exception e) {
		e.getStackTrace();
	} // 업로드 종료
%>
<!DOCTYPE html>
<html>
	<head>
	    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
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
      	<form action="callJython.jsp" method="post">
			<input type="hidden" name="ip" value="<%=ip%>">
			<input type="hidden" name="fileName" value="<%=fileName%>"> 
			<input type="hidden" name="orgfileName" value="<%=orgfileName%>">
			<input type="submit" value="업로드 확인">
		</form>
	<a href="/index.jsp">새로운 파일 업로드 하기</a>
    </div>
    <div class="section">
      <h1>개요</h1>
      <h2>프로젝트 설명 넣기</h2>
    </div>
</html>