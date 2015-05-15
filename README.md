# engine
Engine - DB

목적: shodan copycat

구조: engine - DB - WAS - WEB - 사용자
  step 1. engine - DB
  step 2. DB - WAS - WEB


세부 정의:

1. HTTP 응답코드 200 OK 일 때만 WAS 로그인 시도하는 로직으로 가기

2. 특정 http header(x-powered-by, server) 존재할 때, 해당 WAS 패턴에 대해서만 로그인 시도
   존재하지 않을 때, 모든 종류의 WAS 패턴 다 시도
