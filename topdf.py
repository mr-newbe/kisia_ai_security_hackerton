from fpdf import FPDF

pdf = FPDF(format='A4')
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", 'B', 16)

# 제목
pdf.cell(0, 10, "SecurePy VSCode Extension", ln=True, align='C')
pdf.set_font("Arial", '', 12)
pdf.ln(5)
pdf.multi_cell(0, 6, "핵심 메시지: pip 설치 전 라이브러리 악성 여부를 실시간 분석하여 안전한 개발 환경 제공")
pdf.ln(5)

# 문제 정의
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "1. 문제 정의", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 6, "- 공급망 공격 증가 → 개인 개발자/인디 개발사 피해 위험\n- 기존 도구는 설치 후 분석 → 선제적 차단 불가\n- CVE 중심 분석 → 신규 악성 라이브러리 탐지 한계")
pdf.ln(5)

# 솔루션
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "2. 솔루션", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 6, "VSCode 확장 기반 실시간 분석\n- 이중 분석 방식:\n  1. 메타데이터 분석: 해시, 다운로드 수, 이름 유사도\n  2. 코드 분석: CodeQL + AI 기반 취약점/악성 행위 탐지\n- 보고서 제공: 악성 여부, 위험도, 근거, 대응 가이드")
pdf.ln(5)

# 경쟁 제품 대비 장점
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "3. 경쟁 제품 대비 장점", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 6, "분석 시점: 설치 직전 IDE 내\n탐지 범위: CVE + 신규 악성 패턴 + 취약점\n사용자 타겟: 개인/인디 개발자 중심\n결과 제공: 악성 여부 + 근거 + 대응 가이드")
pdf.ln(5)

# 프로토타입 플로우
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "4. 프로토타입 플로우", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 6, "pip 설치 → VSCode 훅 → 메타데이터 분석 + 코드 분석 → 결과 종합 → 보고서 → 설치 결정")
pdf.ln(5)

# 기능 다이어그램
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "5. 기능 다이어그램", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 6, "- 메타데이터 분석 모듈\n- 코드 정적 분석 모듈 (CodeQL + AI)\n- 결과 종합 및 리포팅 모듈\n- VSCode UI/UX 모듈")
pdf.ln(5)

# 개발 단계 To-Do
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "6. 개발 단계 To-Do", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 6, "1. VSCode Extension 개발 환경 세팅\n2. pip install Hook 구현\n3. 메타데이터 분석 모듈 구현\n4. CodeQL 기반 정적 분석 연결\n5. AI 모델 학습 및 API 연결\n6. 결과 리포트 UI 구현\n7. 테스트 환경 구성 (정상/악성 샘플)\n8. 성능/속도 최적화\n9. 약관 검토 및 배포 전략 수립")
pdf.ln(5)

# 프로젝트 목적
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "7. 프로젝트 목적", ln=True)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 6, "공급망 공격으로 인한 피해를 줄이고, 인디 개발사와 개인 개발자가 안전하게 라이브러리를 설치·사용할 수 있도록 하는 개발자 친화형 보안 솔루션 개발")
pdf.ln(5)

# PDF 저장
pdf_path = "/mnt/data/SecurePy_VSCode_Extension.pdf"
pdf.output(pdf_path)
pdf_path
