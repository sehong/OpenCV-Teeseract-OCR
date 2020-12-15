<%@page import="java.util.Enumeration" %>
<%@page import="com.oreilly.servlet.multipart.DefaultFileRenamePolicy"%>
<%@page import="com.oreilly.servlet.MultipartRequest"%>
<%@page import="javax.servlet.http.*" %>
<%@page import="org.python.util.PythonInterpreter" %>
<%@page import="java.io.FileInputStream"%>
<%@page import="java.io.File"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<%	
	PythonInterpreter python=new PythonInterpreter();
	python.set("fileName",request.getParameter("fileName"));
	python.execfile("/home/pi/Downloads/tomcat9/webapps/ROOT/test1.py");
	Process p = Runtime.getRuntime().exec("sudo python3 /home/pi/Downloads/tomcat9/webapps/ROOT/test.py");
	python.close();
	Thread.sleep(12000);
	String filePath = "/home/pi/Downloads/tomcat9/webapps/ROOT/convert.hwp";

	File file = new File(filePath);

	// MIMETYPE 설정
	String mimeType = getServletContext().getMimeType(filePath);
	if (mimeType == null)
		mimeType = "application/octet-stream";
	response.setContentType(mimeType);

	// 다운로드 설정 및 한글 파일명 깨지는 것 방지
	String encoding = new String(filePath.getBytes("UTF-8"), "8859_1");
	response.setHeader("Content-Disposition", "attachment; filename= " + encoding);

	// 요청 파일을 읽어서 클라이언트에 전송
	FileInputStream in = new FileInputStream(file);
	ServletOutputStream outStream = response.getOutputStream();

	byte b[] = new byte[3000000];
	int data = 0;
	while ((data = in.read(b, 0, b.length)) != -1) {
		outStream.write(b, 0, data);
	}

	outStream.flush();
	outStream.close();
	in.close();
%>
