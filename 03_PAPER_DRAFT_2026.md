# [Part A] 2026 리빌딩 원고 (국문/Korean) - Expanded

## Abstract (초록)
본 논문은 자율주행 레벨 4 시대의 차량용 디스플레이 표준을 재정립하기 위해, 1200 nits의 고휘도와 1.8% 미만의 크로스토크(Crosstalk)를 동시에 달성한 **Active Matrix Micro-LED 듀얼 뷰 디스플레이**를 제안한다. 제작된 프로토타입은 RGB 스트라이프 구조의 326 PPI 고해상도(320x390, 2.1인치 PoC)를 기반으로, 12.3인치 모듈로 확장 가능한 공정 플랫폼을 검증했다. 기존 OLED 기술은 차량 내 가혹 환경(85℃)에서의 휘도 저하와 고정형 UI(속도계 등)에 의한 번인(Burn-in) 문제로 인해 안전성에 치명적인 한계를 보여왔다.

우리는 이를 극복하기 위해 세 가지 핵심 기술을 통합했다. 
1. **Pixel Partitioning**: 독자적인 픽셀 분할 광학 구조를 통해 운전자와 동승자의 시야를 완벽히 분리했다(각 시야각 45도 확보). 
2. **PWM Driving**: LTPS TFT 백플레인과 PWM 구동 방식을 결합하여, 저계조에서의 색 틀어짐(Wavelength Shift) 없이 정확한 색상을 구현했다. 
3. **Selective Stamp Transfer**: 선택적 스탬프 전사 공정과 리페어 알고리즘을 도입하여 99.99% 이상의 공정 수율을 확보했다. 

제작된 모듈은 **-30℃에서 85℃**에 이르는 열충격 테스트와 고온고습(85℃/85%RH/168h) 환경에서 OLED 대비 탁월한 신뢰성(휘도 저하 0%, 2% 미만 열화)을 입증하였다.

## 1. Introduction (서론)
### 1.1 The Paradigm Shift: From Dashboard to "Digital Canvas"
자율주행 기술이 고도화됨에 따라 자동차의 칵핏(Cockpit)은 단순한 정보 표시 창에서 탑승자의 경험을 극대화하는 '제3의 생활 공간'으로 진화하고 있다. 운전석 전면의 **FID(Front Information Display)**는 주행 필수 정보를, 조수석의 **PID(Passenger Information Display)**는 엔터테인먼트를 제공하며, 이를 통합 제어하는 **CID(Central Information Display)**로 세분화된다. 이러한 진화 속에서 칵핏 디스플레이는 '지능형 듀얼 뷰(Intelligent Dual-View)' 기능을 필수적으로 요구받고 있다. 이러한 듀얼 뷰 기술은 단순한 편의 기능을 넘어 안전의 영역으로 확장된다. 조수석 영상이 운전자 시야를 방해하지 않아야 한다는 것은 유로 NCAP 등 국제 안전 규제의 핵심이다.

### 1.2 Limitations of Conventional Technologies
그러나 현재 상용화된 기술들은 엄격한 안전 및 신뢰성 기준을 충족시키지 못한다. LCD 방식은 배리어 구조로 인한 광 손실과 낮은 명암비로 시인성이 떨어진다. 특히 BOE 등의 선행 연구는 LCD 기반 듀얼뷰를 제시했으나 낮은 휘도로 인해 주간 주행 시 시인성 확보에 실패했다. OLED 방식은 완벽한 블랙 표현이 가능하나, 치명적인 약점을 가진다. 
* **Burn-in**: 내비게이션 바나 속도계와 같은 고정 UI가 장시간 표시될 경우 번인 현상이 발생하여 영구적 잔상이 남는다. 
* **ABL Hazard**: 고온(80℃ 이상) 환경에서 발열 제어를 위한 ABL(Auto Brightness Limiter) 작동으로 화면이 강제로 어두워져, 고조도 환경에서 사고를 유발할 수 있다.

### 1.3 The Micro-LED Proposal
우리는 무기물(Inorganic) 기반의 Active Matrix Micro-LED 듀얼 뷰 디스플레이를 제안한다. 본 연구는 단순한 소자 변경을 넘어, **광학 설계(Optical), 구동 회로(Driving), 공정(Fabrication)**의 3박자를 갖춘 통합 솔루션을 통해 차세대 칵핏 디스플레이의 새로운 레퍼런스를 제시한다.

## 2. Design & Fabrication (설계 및 제작)
### 2.1 Optical Architecture: Managing Light Paths
우리는 몬테카를로 시뮬레이션을 통해 픽셀 분할 구조를 최적화했다. 듀얼 뷰 디스플레이의 핵심 광학 성능은 아래 식이 지배한다.

$$ \theta = \arctan(a / 2d) \tag{1} $$
$$ CT(\%) = (L_{leak} / L_{target}) \times 100 \tag{2} $$
$$ L_{eff} = L_{view} / L_{max} \tag{3} $$

여기서 $a$는 배리어 개구 폭, $d$는 발광면과의 거리이다. 식(1)과 (2)에 의거하여, 우리는 BM1 오프셋 +8μm, OC 두께 6μm, BM2 오프셋 +3.5μm라는 최적의 설계치(Sweet Spot)를 도출했다. 이를 통해 배리어의 측면 경사각을 85도 이상으로 설계하고 흡광 코팅을 적용하여 'Secondary Crosstalk'를 90% 이상 억제했다. 또한 **정렬 오차(Misalignment Tolerance)** 분석을 통해 ±2μm 공정 오차 내에서도 크로스토크 2% 미만을 보장하는 강건 설계(Robust Design)를 확보했다.

### 2.2 Device Structure & Setup
사용된 Micro-LED 칩은 R(15×30μm), G/B(13×28μm) 크기를 가지며, RGB 스트라이프 형태로 배열되었다. 홀수 열(Odd Column)은 운전자 시야(Right View)로, 짝수 열(Even Column)은 동승자 시야(Left View)로 광 경로가 제어되도록 설계되었다.

### 2.3 Active Matrix Backplane Strategy
Micro-LED는 전류 밀도에 따라 파장이 변하는 특성이 있어 아날로그 제어(PAM) 시 색 틀어짐이 발생한다. 이를 해결하기 위해 **Digital PWM 구동 방식**을 채택했다. 전류 크기는 고정하고 발광 시간만 조절하여, 0.1 nit부터 1200 nits까지 전 구간에서 색좌표 변화(Δu'v')를 0.002 이내로 유지했다.

### 2.4 Scalable Fabrication: Stamp Transfer & Yield Management
본 연구는 12.3인치 대면적 구현을 위해 스탬프 전사 공정을 최적화했다. 스탬프 속도 제어(Kinetic Control)로 99.9% 전사 성공률을 달성했으며, **진공 채널 기반 척(Smart Chuck)**으로 12인치 기판 휨을 실시간 보정하여 위치 정밀도를 ±3μm 이내로 제어했다. AOI(Automated Optical Inspection) 시스템을 통해 본딩 후, 뱅크 형성 후, 봉지 후 등 각 단계별 전수 검사를 수행하여 신뢰성을 확보했다.

## 3. Experimental Results (실험 결과)
### 3.1 Optical Performance Assessment
제작된 12.3인치 프로토타입은 백색 전체 화면 시 **1208 nits**를 기록했다 (Gamma 2.2 보정 기준). 이는 ABL로 500 nits 수준에 머무는 OLED 대비 2배 이상이다. 또한 10,000 lux 조명 하에서도 **Ambient Contrast Ratio 50,000:1**을 달성하여 직사광선 하에서도 선명한 정보를 전달한다. 시야각 측정 결과 좌우 각각 45도 범위 내에서 균일한 영상을 제공하며, 크로스토크는 1.8% 미만으로 유지되어 'Ghost-free' 상태를 구현했다(EZ Contrast 측정 기준).

### 3.2 Environmental Reliability: The Ultimate Differentiator
업계 표준을 상회하는 **'Torture Test'**를 진행했다. 열충격 500 사이클에서 불량률 0%를 기록했으며, 85℃/85%RH 고온고습 테스트(168시간) 후에도 휘도 변화율 <2%, 색좌표 변화 <0.005를 달성했다. 반면, 동일 조건의 OLED 패널은 휘도가 22% 감소하고 화면이 노랗게 변색되었다. 또한 번인 테스트에서도 마이크로 LED는 변화가 없었으나 OLED는 선명한 자국을 남겼다.

## 4. Discussion (고찰)
### 4.1 Technical Superiority & Cost Analysis
마이크로 LED는 화면 밝기나 온도에 상관없이 '일관성(Consistency)'을 유지한다. 이는 안전과 직결된다. BOE 등 기존 연구가 언급한 양산 수율 문제는 본 연구의 픽셀 단위 리페어 공정으로 해결되었다. 비용 우려에 대해서는, 공정 수율 안정화와 칩 효율 개선으로 2028년경 프리미엄 OLED와 **가격 경쟁력(Price Parity)**을 확보할 것으로 전망된다. 특히 번인으로 인한 수명주기 교체 비용(Lifecycle Cost)을 고려하면 총 소유 비용(TCO) 면에서 우위에 있다.

### 4.2 Regulatory Readiness: Euro NCAP & NHTSA
Euro NCAP과 NHTSA는 운전자 주의 분산 방지 규제를 강화하고 있다. 본 연구의 1.8% 미만 크로스토크 성능은 별도의 물리적 차단 필름 없이 디스플레이 광학 설계만으로 이 엄격한 규제를 선제적으로 만족시키는 유일한 솔루션이다.

## 5. Conclusion (결론)
본 연구는 1200 nits, 1.8% 크로스토크, 차량 등급 신뢰성을 갖춘 Active Matrix Micro-LED 듀얼 뷰 디스플레이를 실증했다. LTPS-PWM 구동으로 색 정확도를 확보하고, 스탬프 전사로 대면적 양산성을 증명했다. 이는 자율주행 시대의 '움직이는 생활 공간'을 완성하는 가장 안전하고 신뢰할 수 있는 표준이 될 것이다.

---

# [Part B] 2026 Paper Draft (English/영문) - Expanded

## Abstract
This paper proposes an Active Matrix Micro-LED Dual-View Display achieving high luminance of 1200 nits and ultra-low crosstalk (<1.8%) to redefine automotive display standards. The prototype features a high pixel density of 326 PPI with an RGB stripe architecture (320x390, 2.1-inch PoC), validating a scalable platform for 12.3-inch modules. Conventional OLED-based technologies have shown critical safety limitations due to luminance reproduction issues under harsh in-vehicle environments (-30℃ to 85℃) and permanent burn-in artifacts.

We integrated three core technologies. 
1. **Pixel Partitioning**: A proprietary Pixel Partitioning architecture perfectly separates fields of view (FOV 45° per view). 
2. **PWM Driving**: We combined an LTPS TFT backplane with a PWM driving scheme to achieve accurate color reproduction without wavelength shift at low greyscales. 
3. **Selective Stamp Transfer**: We introduced a Selective Stamp Transfer process securing >99.99% yield. 

The fabricated module demonstrated superior reliability with zero luminance degradation under thermal shock cycling (-30℃ to 85℃) and high-temp/humidity tests (85℃/85%RH/168h), maintaining degradation below 2%.

## 1. Introduction
### 1.1 The Paradigm Shift
As autonomous driving advances, the cockpit is evolving into a "Third Living Space." The **FID (Front Information Display)** provides essential driving data, while the **PID (Passenger Information Display)** offers entertainment, both integrated via the **CID (Central Information Display)**. Ensuring passenger content does not distract the driver is a core requirement of safety regulations like Euro NCAP.

### 1.2 Limitations of Conventional Technologies
Current technologies fail to meet safety standards. LCDs suffer from low luminance due to barrier losses. Prior works like BOE's LCD dual-view failed to achieve daylight visibility. OLEDs have fatal weaknesses: 
* **Burn-in**: Causes permanent afterimages on static UIs. 
* **ABL (Auto Brightness Limiter)**: Forcibly dims screens in high temperatures, hindering visibility on bright roads.

### 1.3 The Micro-LED Proposal
We propose an inorganic Active Matrix Micro-LED Dual-View Display. This study presents a new reference through an integrated solution encompassing **Optical Design, Circuit Driving, and Fabrication Process**.

## 2. Design & Fabrication
### 2.1 Optical Architecture
We optimized pixel partitioning via Monte-Carlo simulations based on the following governing equations:

$$ \theta = \arctan(a / 2d) \tag{1} $$
$$ CT(\%) = (L_{leak} / L_{target}) \times 100 \tag{2} $$
$$ L_{eff} = L_{view} / L_{max} \tag{3} $$

Using these parameters, we derived a 'Sweet Spot' (BM1 +8μm, OC 6μm, BM2 +3.5μm) ensuring performance even with ±2μm process variations. This robust design confines secondary crosstalk to negligible levels.

### 2.2 Device Structure & Setup
The Micro-LED chips utilized were R(15×30μm) and G/B(13×28μm) in size, arranged in an RGB stripe configuration. Odd columns were assigned to the driver's view (Right View) and even columns to the passenger's view (Left View).

### 2.3 Active Matrix Backplane Strategy
To resolve wavelength shift in Micro-LEDs, we adopted a **Digital PWM driving scheme**. This fixes peak current and modulates emission time, maintaining color shift (Δu'v') within 0.002 across all luminance ranges.

### 2.4 Scalable Fabrication
We optimized Stamp Transfer for 12.3-inch displays. Using **Kinetic Control** and a **Smart Chuck** for warpage correction, we achieved ±3μm precision on large glass. AOI (Automated Optical Inspection) was implemented at each stage to ensure zero defects.

## 3. Experimental Results
### 3.1 Optical Performance Assessment
The prototype achieved **1208 nits**, double that of OLEDs. We achieved an **Ambient Contrast Ratio of 50,000:1** under 10,000 lux, ensuring clear visibility in sunlight. Crosstalk remained <1.8% within the 45° viewing cone (EZ Contrast).

### 3.2 Environmental Reliability
We conducted **'Torture Tests'**. Thermal shock (-30℃ to 85℃) showed 0% failure. After 168 hours at 85℃/85%RH, luminance changed <2%. In contrast, OLEDs showed a **22% luminance drop** and severe yellowing. Burn-in tests also favored Micro-LEDs significantly.

## 4. Discussion
### 4.1 Technical Superiority & Cost Analysis
Micro-LED offers superior consistency and longevity. Regarding cost, we project **Price Parity** with OLED by 2028. Considering lifecycle costs (no burn-in replacements), Micro-LED offers better Total Cost of Ownership (TCO).

### 4.2 Regulatory Readiness
The sub-1.8% crosstalk performance proactively meets Euro NCAP strict driver distraction regulations through optical design alone.

## 5. Conclusion
We demonstrated a 1200 nits, <1.8% crosstalk Active Matrix Micro-LED display. With LTPS-PWM driving and scalable transfer processes, we solved OLED's burn-in and reliability issues. This technology will be the reference standard for the autonomous driving era.
