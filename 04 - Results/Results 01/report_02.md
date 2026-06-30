# k6 Performance Smell Analysis
Generated: 08/06/2026 16:00

S1 = Costly init | S2 = No thresholds | S3 = No checks | S4 = No tags

| File | LLM | S1 | S2 | S3 | S4 | Lines with smells |
|------|-----|:--:|:--:|:--:|:--:|-------------------|
| `script_03.js` | claude |  | x |  | x | S2:L27, S2:L31, S4:L60, S4:L85, S4:L103, S4:L128 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x |  | x | S1:L38, S2:L27, S2:L31, S4:L60, S4:L85, S4:L103, S4:L128 |
| `script_07.js` | claude | x | x | x | x | S1:L22, S2:L7, S2:L8, S2:L9, S2:L10, S3:L48, S3:L49, S3:L50, S4:L48 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x | x | x | S1:L22, S2:L7, S2:L8, S2:L9, S2:L10, S3:L48, S4:L48 |
| `script_10.js` | claude |  | x |  | x | S2:L16, S4:L29, S4:L92, S4:L132, S4:L178, S4:L217, S4:L260, S4:L328, S4:L401, S4:L501, S4:L567, S4:L633, S4:L700, S4:L766, S4:L832, S4:L898, S4:L967, S4:L1035, S4:L1108, S4:L1176, S4:L1244, S4:L1328, S4:L1389, S4:L1450, S4:L1512, S4:L1573, S4:L1634, S4:L1695, S4:L1759, S4:L1827, S4:L1900, S4:L1968, S4:L2027, S4:L2077, S4:L2128, S4:L2179, S4:L2231, S4:L2282, S4:L2333, S4:L2384, S4:L2438, S4:L2506, S4:L2574, S4:L2633, S4:L2683, S4:L2734, S4:L2785, S4:L2837, S4:L2888, S4:L2939, S4:L2990, S4:L3044, S4:L3112, S4:L3185, S4:L3245, S4:L3304, S4:L3354, S4:L3405, S4:L3456, S4:L3508, S4:L3559, S4:L3610, S4:L3661, S4:L3715, S4:L3775, S4:L3825, S4:L3878, S4:L3931, S4:L3985, S4:L4038, S4:L4091, S4:L4144, S4:L4200, S4:L4268, S4:L4350, S4:L4411, S4:L4472, S4:L4534, S4:L4595, S4:L4656, S4:L4717 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L16, S4:L29, S4:L92, S4:L132, S4:L178, S4:L217 |
| `script_100.js` | claude |  |  |  |  | - |
|  | chatgpt |  | x |  | x | S4:L15, S4:L30, S4:L43, S4:L58, S4:L71, S4:L85 |
|  | gemini |  |  |  | x | S4:L15, S4:L30, S4:L43, S4:L58, S4:L71, S4:L85 |
| `script_104.js` | claude |  |  |  | x | S4:L15, S4:L16, S4:L17, S4:L18 |
|  | chatgpt |  |  |  | x | S4:L15, S4:L16, S4:L20, S4:L21 |
|  | gemini |  |  | x | x | S3:L24, S4:L15, S4:L16 |
| `script_109.js` | claude |  | x |  |  | S2:L269, S2:L270, S2:L271 |
|  | chatgpt |  | x |  | x | S4:L254, S4:L255, S4:L256, S4:L257, S4:L258, S4:L259, S4:L260 |
|  | gemini |  | x |  | x | S2:L1, S2:L271, S4:L254, S4:L260 |
| `script_112.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  | x | x | S3:L57, S3:L58, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S3:L64, S3:L65, S3:L66, S3:L67, S3:L68, S3:L69, S3:L70, S3:L71, S4:L57, S4:L58, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63, S4:L64, S4:L65, S4:L66, S4:L67, S4:L68, S4:L69, S4:L70, S4:L71 |
|  | gemini |  |  | x | x | S3:L57, S3:L58, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S3:L64, S3:L65, S3:L66, S3:L67, S3:L68, S3:L69, S3:L70, S3:L71, S4:L57, S4:L58, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63, S4:L64, S4:L65, S4:L66, S4:L67, S4:L68, S4:L69, S4:L70, S4:L71 |
| `script_12.js` | claude | x |  |  | x | S1:L21, S1:L22, S1:L23, S1:L24, S1:L27, S1:L28, S1:L29, S1:L30, S1:L31, S1:L32, S1:L33, S1:L34, S1:L36, S4:L43, S4:L50, S4:L64, S4:L72, S4:L110, S4:L122, S4:L134, S4:L141, S4:L148, S4:L158, S4:L170, S4:L176, S4:L195, S4:L210 |
|  | chatgpt | x |  |  | x | S1:L36, S4:L43, S4:L50, S4:L64, S4:L72, S4:L110, S4:L122, S4:L134, S4:L141, S4:L148, S4:L158, S4:L170, S4:L176, S4:L195, S4:L210 |
|  | gemini | x |  |  | x | S1:L36, S4:L43, S4:L50, S4:L64, S4:L72, S4:L110, S4:L122, S4:L134, S4:L141, S4:L148, S4:L158, S4:L170, S4:L176, S4:L195, S4:L210 |
| `script_120.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  |  | - |
| `script_129.js` | claude |  |  |  | x | S4:L20, S4:L27 |
|  | chatgpt |  |  |  | x | S4:L20, S4:L21, S4:L27, S4:L28 |
|  | gemini |  | x |  | x | S2:L13, S2:L14, S2:L15, S4:L20, S4:L27 |
| `script_130.js` | claude |  | x |  | x | S4:L14, S4:L22, S2:L7, S2:L8, S2:L9 |
|  | chatgpt |  |  |  | x | S4:L14, S4:L22 |
|  | gemini |  |  |  | x | S4:L14, S4:L22 |
| `script_145.js` | claude |  | x |  | x | S2:L67, S2:L79, S2:L83, S2:L91, S2:L106, S4:L233, S4:L263, S4:L297, S4:L344, S4:L399, S4:L476 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L67, S2:L79, S2:L83, S2:L91, S2:L106, S3:L297, S3:L344, S4:L297 |
| `script_146.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L34, S4:L34 |
| `script_149.js` | claude |  |  |  |  | - |
|  | chatgpt |  | x |  |  | S2:L9 |
|  | gemini |  | x |  |  | S2:L9 |
| `script_15.js` | claude |  |  | x | x | S3:L149, S3:L150, S3:L151, S3:L152, S3:L153, S3:L154, S3:L155, S3:L156, S3:L157, S3:L158, S3:L159, S3:L160, S3:L161, S3:L162, S3:L163, S3:L164, S3:L165, S3:L166, S3:L167, S3:L168, S3:L248, S3:L249, S3:L250, S3:L251, S3:L252, S3:L253, S3:L254, S3:L255, S3:L256, S3:L257, S4:L121, S4:L122, S4:L123, S4:L124, S4:L153, S4:L154, S4:L155, S4:L156, S4:L199, S4:L200, S4:L201, S4:L202, S4:L231, S4:L232, S4:L233, S4:L234, S4:L235, S4:L236, S4:L237, S4:L238, S4:L239, S4:L240, S4:L241, S4:L249, S4:L250, S4:L251, S4:L252, S4:L253, S4:L254, S4:L255, S4:L260, S4:L261, S4:L262, S4:L263, S4:L264, S4:L302, S4:L303, S4:L304, S4:L305, S4:L306, S4:L314, S4:L315, S4:L316, S4:L317, S4:L326, S4:L327, S4:L328, S4:L329, S4:L330, S4:L331, S4:L332, S4:L333, S4:L334, S4:L343, S4:L344, S4:L345, S4:L346, S4:L347, S4:L348, S4:L349, S4:L350 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L161, S3:L162, S3:L163, S3:L164, S3:L165, S3:L166, S3:L167, S4:L121, S4:L122, S4:L123, S4:L124 |
| `script_158.js` | claude |  |  | x | x | S3:L53, S3:L58, S3:L59, S4:L47, S4:L53, S4:L58 |
|  | chatgpt |  |  | x | x | S3:L47, S3:L53, S3:L58, S4:L47, S4:L53, S4:L58, S4:L59 |
|  | gemini |  |  | x | x | S3:L53, S3:L58, S4:L53, S4:L58 |
| `script_162.js` | claude | x |  | x | x | S1:L45, S3:L57, S3:L58, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S3:L64, S3:L65, S3:L66, S3:L67, S4:L58, S4:L59, S4:L60, S4:L61 |
|  | chatgpt |  |  |  | x | S4:L62, S4:L65, S4:L66, S4:L69, S4:L70 |
|  | gemini |  |  |  | x | S4:L62, S4:L65, S4:L66, S4:L69, S4:L70 |
| `script_176.js` | claude |  |  |  | x | S4:L63, S4:L64, S4:L65, S4:L66 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  | x | S4:L67, S4:L70, S4:L71, S4:L74, S4:L75 |
| `script_180.js` | claude |  |  |  |  | - |
|  | chatgpt |  | x |  |  | S2:L9 |
|  | gemini |  | x |  |  | S2:L9 |
| `script_183.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L73, S3:L80, S3:L88, S3:L93, S3:L100, S4:L82, S4:L89, S4:L101 |
| `script_19.js` | claude | x |  | x |  | S1:L110, S1:L111, S1:L112, S1:L113, S1:L114, S1:L115, S1:L116, S3:L128, S3:L132, S3:L136, S3:L140, S3:L144 |
|  | chatgpt | x |  | x |  | S1:L110, S1:L112, S1:L120, S3:L128, S3:L132, S3:L136, S3:L140, S3:L144 |
|  | gemini | x |  | x |  | S1:L110, S1:L111, S1:L112, S1:L113, S1:L114, S1:L115, S1:L116, S1:L117, S1:L118, S1:L119, S1:L120, S1:L121, S1:L122, S1:L123, S1:L124, S3:L128, S3:L132, S3:L136, S3:L140, S3:L144 |
| `script_194.js` | claude |  | x | x | x | S2:L33, S2:L34, S2:L35, S2:L36, S3:L66, S3:L67, S3:L68, S3:L69, S3:L70, S3:L71, S4:L66, S4:L67, S4:L68, S4:L69, S4:L70, S4:L71, S4:L73 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L33, S2:L34, S2:L35, S2:L36, S3:L66, S3:L67, S3:L68, S3:L69, S3:L70, S3:L71, S4:L73 |
| `script_201.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L9 |
| `script_202.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  |  | - |
| `script_205.js` | claude |  | x | x | x | S2:L39, S2:L40, S2:L41, S2:L42, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x | x | x | S1:L22, S2:L39, S2:L40, S2:L41, S2:L42, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S4:L65 |
| `script_210.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L9 |
| `script_213.js` | claude |  |  |  |  | - |
|  | chatgpt |  | x |  |  | S2:L9 |
|  | gemini |  | x |  |  | S2:L9 |
| `script_224.js` | claude |  |  | x | x | S3:L36, S3:L38, S4:L36 |
|  | chatgpt |  |  | x | x | S3:L36, S4:L36, S4:L38 |
|  | gemini |  |  |  |  | - |
| `script_227.js` | claude |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L12 |
|  | chatgpt |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L12 |
|  | gemini |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L12 |
| `script_229.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10, S4:L12 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
| `script_23.js` | claude | x | x |  | x | S1:L37, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L44 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L44, S4:L72 |
|  | gemini |  | x |  | x | S2:L5, S2:L11, S4:L44 |
| `script_230.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L9 |
| `script_231.js` | claude |  |  | x | x | S3:L14, S3:L15, S4:L14 |
|  | chatgpt |  |  | x | x | S3:L14, S4:L14, S4:L15 |
|  | gemini |  |  | x | x | S3:L14, S4:L14 |
| `script_232.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S4:L13 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S4:L13, S4:L14, S4:L15, S4:L16, S4:L17 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S4:L13 |
| `script_233.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L9 |
| `script_234.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L32, S3:L25, S3:L29, S3:L30, S3:L31, S4:L15, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20, S4:L21 |
|  | chatgpt |  | x | x | x | S2:L1, S2:L32, S3:L25, S3:L29, S3:L30, S3:L31, S4:L4, S4:L5, S4:L6, S4:L7, S4:L8, S4:L19 |
|  | gemini |  | x | x | x | S2:L1, S3:L25, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20 |
| `script_235.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S4:L23 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S4:L23 |
| `script_236.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L26, S4:L27, S4:L28, S4:L29, S4:L30, S4:L33 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L26, S4:L27, S4:L28, S4:L29, S4:L30, S4:L33, S4:L36, S4:L37, S4:L38 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L33 |
| `script_237.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S3:L6, S4:L6 |
|  | chatgpt |  | x | x | x | S2:L1, S2:L2, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S3:L6, S4:L6 |
|  | gemini |  | x | x | x | S2:L1, S2:L2, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S3:L6, S4:L6 |
| `script_238.js` | claude |  |  | x | x | S3:L39, S3:L41, S4:L39, S4:L41 |
|  | chatgpt | x |  | x | x | S1:L26, S1:L27, S1:L28, S3:L39, S4:L39, S4:L41 |
|  | gemini | x |  | x | x | S1:L26, S1:L27, S1:L28, S3:L39, S4:L41 |
| `script_239.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S3:L7, S4:L7 |
|  | chatgpt |  | x | x | x | S2:L1, S2:L2, S2:L5, S3:L7, S4:L7 |
|  | gemini |  | x | x | x | S2:L5, S3:L7, S4:L7 |
| `script_24.js` | claude |  | x | x | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S2:L21, S2:L22, S2:L23, S3:L76, S3:L77, S3:L78, S3:L84, S3:L85, S3:L86, S4:L60, S4:L61, S4:L62, S4:L76, S4:L77, S4:L84, S4:L85 |
|  | chatgpt |  | x | x | x | S2:L14, S2:L18, S2:L20, S2:L21, S2:L23, S3:L76, S3:L77, S3:L84, S3:L85, S4:L60, S4:L61, S4:L62, S4:L76, S4:L77, S4:L84, S4:L85 |
|  | gemini |  | x | x | x | S2:L14, S2:L23, S3:L76, S3:L84, S4:L60, S4:L76, S4:L84 |
| `script_240.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23, S4:L25, S4:L26, S4:L27, S4:L28, S4:L29 |
|  | gemini |  | x | x | x | S2:L5, S2:L6, S2:L7, S2:L8, S3:L25, S3:L26, S3:L27, S3:L28, S3:L29, S4:L21, S4:L22, S4:L23 |
| `script_241.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L19 |
|  | chatgpt |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L19, S4:L22, S4:L28 |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L19 |
| `script_242.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L26 |
|  | chatgpt |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L26, S4:L29, S4:L35 |
|  | gemini |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S3:L35, S3:L36, S3:L37, S3:L38, S3:L39, S3:L40, S3:L41, S3:L42, S3:L43, S3:L44, S3:L45, S3:L46, S4:L26, S4:L29 |
| `script_245.js` | claude |  |  | x | x | S3:L43, S3:L45, S4:L43 |
|  | chatgpt |  |  | x | x | S3:L43, S4:L43, S4:L45 |
|  | gemini |  |  | x | x | S3:L43, S3:L45, S4:L43, S4:L45 |
| `script_247.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S2:L21, S3:L14, S4:L7, S4:L8, S4:L9, S4:L10, S4:L11, S4:L12, S4:L14 |
|  | chatgpt |  | x | x | x | S2:L6, S3:L14, S4:L7, S4:L8, S4:L9, S4:L10, S4:L11, S4:L12, S4:L14 |
|  | gemini |  | x | x | x | S2:L6, S2:L21, S3:L14, S4:L7, S4:L12 |
| `script_248.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19, S4:L22, S4:L23, S4:L24 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19, S4:L25 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19 |
| `script_249.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L20 |
|  | chatgpt |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L20, S4:L23, S4:L29 |
|  | gemini |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S3:L29, S3:L30, S3:L31, S3:L32, S3:L33, S3:L34, S4:L20, S4:L23 |
| `script_25.js` | claude |  | x |  | x | S2:L26, S2:L30, S4:L38, S4:L144, S4:L145, S4:L147, S4:L163 |
|  | chatgpt |  | x |  | x | S2:L26, S2:L30, S4:L38, S4:L126, S4:L147, S4:L163 |
|  | gemini |  | x |  | x | S2:L26, S2:L30, S4:L38, S4:L126, S4:L147 |
| `script_250.js` | claude |  |  | x | x | S3:L23, S3:L32, S3:L33, S3:L34, S3:L35, S3:L36, S4:L23 |
|  | chatgpt |  |  |  | x | S4:L23, S4:L26, S4:L29, S4:L33, S4:L35 |
|  | gemini |  |  | x | x | S3:L32, S3:L33, S3:L34, S3:L35, S3:L36, S4:L23 |
| `script_251.js` | claude |  |  | x | x | S3:L57, S3:L58, S4:L57, S4:L58 |
|  | chatgpt |  |  | x | x | S3:L57, S4:L1, S4:L57, S4:L58 |
|  | gemini |  |  | x | x | S3:L57, S3:L58, S4:L58 |
| `script_252.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L22 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L22, S4:L24 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L22 |
| `script_253.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S2:L21, S2:L22, S2:L23, S2:L24, S2:L25, S2:L26, S2:L27, S2:L28, S2:L29, S2:L30, S2:L31, S2:L32, S3:L25, S3:L29, S3:L30, S3:L31, S4:L15, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20, S4:L21 |
|  | chatgpt |  | x | x | x | S2:L1, S2:L32, S3:L25, S3:L29, S3:L30, S3:L31, S4:L4, S4:L5, S4:L6, S4:L7, S4:L8, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20 |
|  | gemini |  | x | x | x | S2:L1, S2:L32, S3:L25, S3:L32, S4:L15, S4:L21 |
| `script_254.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L20, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L20, S4:L21, S4:L22, S4:L23 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L20, S4:L21, S4:L22, S4:L23 |
| `script_255.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L29 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L27, S4:L29, S4:L32 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L29 |
| `script_257.js` | claude |  |  |  |  | - |
|  | chatgpt | x |  | x | x | S1:L26, S1:L27, S1:L28, S3:L39, S4:L39, S4:L41 |
|  | gemini | x |  | x | x | S1:L26, S1:L27, S1:L28, S3:L39, S3:L41, S4:L39 |
| `script_259.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S3:L8, S4:L8 |
|  | chatgpt |  | x | x | x | S2:L7, S3:L8, S4:L8 |
|  | gemini |  | x | x | x | S2:L1, S2:L18, S3:L8, S4:L8 |
| `script_26.js` | claude |  | x |  |  | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5 |
|  | chatgpt |  | x | x |  | S2:L132, S2:L133, S2:L134, S3:L1031, S3:L1032, S3:L1033, S3:L1034, S3:L1035 |
|  | gemini |  | x | x | x | S2:L1, S3:L1031, S4:L1031 |
| `script_260.js` | claude |  |  |  |  | - |
|  | chatgpt |  | x |  |  | S2:L9 |
|  | gemini |  | x |  |  | S2:L9 |
| `script_262.js` | claude |  | x | x | x | S2:L5, S2:L6, S2:L7, S2:L8, S3:L25, S3:L26, S3:L27, S3:L28, S3:L29, S3:L30, S3:L31, S3:L32, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
| `script_264.js` | claude |  | x |  | x | S2:L39, S2:L40, S2:L41, S2:L42, S4:L73, S4:L74, S4:L75 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L39, S2:L40, S2:L41, S2:L42, S3:L73, S3:L74, S3:L75, S4:L77 |
| `script_265.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S3:L7, S4:L7 |
|  | chatgpt |  | x | x | x | S2:L6, S3:L7, S4:L7 |
|  | gemini |  | x | x | x | S2:L6, S3:L7, S4:L7 |
| `script_266.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  | x | x | S3:L56, S3:L62, S3:L64, S3:L70, S4:L56, S4:L62, S4:L65, S4:L70, S4:L71 |
|  | gemini | x |  | x | x | S1:L36, S1:L37, S1:L38, S1:L39, S1:L40, S3:L62, S3:L63, S3:L64, S4:L65, S4:L71 |
| `script_267.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
| `script_268.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22, S4:L24, S4:L25, S4:L26, S4:L27 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
| `script_269.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S3:L7, S4:L7 |
|  | chatgpt |  | x | x | x | S2:L6, S3:L7, S4:L7 |
|  | gemini |  | x | x | x | S2:L3, S3:L7, S4:L7 |
| `script_27.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L32, S4:L33, S4:L34, S4:L35, S4:L36, S4:L42 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L32, S4:L33, S4:L34, S4:L35, S4:L36, S4:L42, S4:L70 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L32, S4:L33, S4:L34, S4:L35, S4:L36, S4:L42 |
| `script_270.js` | claude |  | x |  | x | S2:L7, S2:L8, S2:L9, S2:L10, S4:L22 |
|  | chatgpt |  | x |  | x | S2:L7, S2:L8, S2:L9, S2:L10, S4:L22, S4:L25, S4:L26, S4:L27 |
|  | gemini |  | x |  | x | S2:L7, S2:L8, S2:L9, S2:L10, S4:L22 |
| `script_271.js` | claude |  | x | x | x | S2:L6, S3:L7, S4:L7 |
|  | chatgpt |  | x | x | x | S2:L6, S3:L7, S4:L7 |
|  | gemini |  | x | x | x | S2:L5, S3:L7, S4:L7 |
| `script_272.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L9 |
| `script_273.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19, S4:L22, S4:L23, S4:L24 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19 |
|  | gemini |  | x |  | x | S2:L5, S2:L16, S4:L19 |
| `script_276.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S4:L12 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S4:L12, S4:L15, S4:L16, S4:L17 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S4:L12 |
| `script_277.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L22, S4:L23, S4:L24, S4:L25 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19, S4:L25 |
|  | gemini |  | x |  | x | S2:L5, S2:L16, S4:L19 |
| `script_278.js` | claude | x |  |  | x | S1:L45, S4:L58, S4:L59, S4:L60, S4:L61 |
|  | chatgpt | x |  |  | x | S1:L45, S4:L62, S4:L65, S4:L66, S4:L69, S4:L70 |
|  | gemini |  |  |  | x | S4:L62, S4:L65, S4:L66, S4:L69, S4:L70 |
| `script_279.js` | claude |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L25 |
|  | chatgpt |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L25, S4:L28 |
|  | gemini |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L25 |
| `script_28.js` | claude | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L81, S1:L82, S1:L83, S1:L84, S1:L85, S1:L86, S1:L87, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
|  | chatgpt | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
|  | gemini | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
| `script_280.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L27 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L22, S4:L23, S4:L24, S4:L27, S4:L30, S4:L31, S4:L32, S4:L33 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L27 |
| `script_281.js` | claude |  |  | x | x | S3:L20, S4:L20 |
|  | chatgpt |  |  | x | x | S3:L20, S4:L20 |
|  | gemini |  |  | x | x | S3:L20, S4:L20 |
| `script_282.js` | claude |  | x |  | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L24 |
|  | chatgpt |  | x |  | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L24, S4:L25, S4:L26, S4:L27 |
|  | gemini |  | x |  | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L24 |
| `script_285.js` | claude |  |  | x | x | S3:L47, S3:L49, S4:L47 |
|  | chatgpt |  |  | x | x | S3:L47, S4:L47, S4:L49 |
|  | gemini | x |  | x | x | S1:L27, S1:L28, S1:L29, S1:L30, S1:L31, S3:L47, S4:L47 |
| `script_286.js` | claude |  | x | x | x | S2:L39, S2:L40, S2:L41, S2:L42, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63 |
|  | chatgpt |  | x |  | x | S2:L39, S2:L40, S2:L41, S2:L42, S4:L65 |
|  | gemini |  | x | x | x | S2:L39, S2:L40, S2:L41, S2:L42, S3:L59, S3:L65, S4:L60, S4:L61, S4:L62, S4:L65 |
| `script_287.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10, S4:L11 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
| `script_288.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x |  | S3:L73, S3:L74, S3:L75, S3:L80, S3:L81, S3:L82, S3:L83, S3:L88, S3:L89, S3:L93, S3:L94, S3:L95, S3:L100, S3:L101 |
| `script_289.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L31, S3:L24, S3:L28, S3:L29, S3:L30, S3:L31, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20 |
|  | chatgpt |  | x | x | x | S2:L1, S2:L31, S3:L24, S3:L28, S3:L29, S3:L30, S4:L4, S4:L8, S4:L16, S4:L20 |
|  | gemini |  | x | x | x | S2:L10, S3:L24, S3:L25, S3:L26, S3:L27, S3:L28, S3:L29, S3:L30, S4:L15, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20, S4:L21 |
| `script_29.js` | claude | x | x |  |  | S1:L11, S1:L12, S1:L13, S1:L14, S1:L15, S1:L16, S1:L17, S1:L18, S1:L19, S1:L20, S1:L21, S2:L28, S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S2:L36 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L28, S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S2:L36 |
| `script_290.js` | claude |  |  | x | x | S3:L54, S3:L55, S3:L56, S3:L57, S3:L61, S3:L63, S4:L54, S4:L61 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L54, S3:L61, S4:L54, S4:L61, S4:L63 |
| `script_291.js` | claude |  | x |  | x | S2:L22, S2:L23, S2:L24, S2:L25, S4:L28 |
|  | chatgpt |  | x |  | x | S2:L22, S2:L23, S2:L24, S2:L25, S4:L28 |
|  | gemini |  | x |  | x | S2:L22, S2:L23, S2:L24, S2:L25, S4:L28 |
| `script_292.js` | claude |  | x |  | x | S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S2:L36, S2:L37, S2:L38, S4:L58, S4:L59, S4:L60 |
|  | chatgpt |  | x |  | x | S2:L29, S2:L34, S2:L36, S2:L38, S4:L58, S4:L59, S4:L60, S4:L62, S4:L63, S4:L64, S4:L65 |
|  | gemini |  | x |  | x | S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S2:L36, S2:L37, S2:L38, S4:L58, S4:L59, S4:L60 |
| `script_295.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L32 |
|  | chatgpt |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L32, S4:L35, S4:L41 |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L32, S4:L35 |
| `script_296.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S3:L11, S3:L14, S3:L17, S4:L11, S4:L14, S4:L17 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S3:L11, S3:L14, S3:L17, S4:L11, S4:L14, S4:L17 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S3:L11, S3:L14, S3:L17, S4:L11, S4:L14, S4:L17 |
| `script_30.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L30, S4:L31, S4:L32, S4:L33, S4:L34, S4:L40 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L30, S4:L31, S4:L32, S4:L33, S4:L34, S4:L40, S4:L68 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L40 |
| `script_31.js` | claude |  | x |  | x | S2:L14, S4:L50 |
|  | chatgpt |  | x | x | x | S2:L14, S3:L28, S3:L29, S3:L30, S3:L62, S4:L28, S4:L29, S4:L30, S4:L50, S4:L62 |
|  | gemini |  | x | x | x | S2:L14, S3:L62, S4:L50 |
| `script_32.js` | claude | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L81, S1:L82, S1:L83, S1:L84, S1:L85, S1:L86, S1:L87, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
|  | chatgpt | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
|  | gemini | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
| `script_33.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L42, S4:L43, S4:L44, S4:L45, S4:L46 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L42, S4:L43, S4:L44, S4:L45, S4:L46, S4:L52, S4:L80 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L42, S4:L43, S4:L44, S4:L45, S4:L46, S4:L52 |
| `script_34.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L36 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L36, S4:L65, S4:L66, S4:L67, S4:L68, S4:L69, S4:L70, S4:L71, S4:L72, S4:L73, S4:L74, S4:L75, S4:L76, S4:L77, S4:L78, S4:L79, S4:L80, S4:L81, S4:L82, S4:L83, S4:L84, S4:L85, S4:L86, S4:L87, S4:L88, S4:L89, S4:L90, S4:L91, S4:L92, S4:L93, S4:L94, S4:L95, S4:L96 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L36 |
| `script_35.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L14, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L14, S4:L15, S4:L23, S4:L24 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L14, S4:L23 |
| `script_36.js` | claude | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L81, S1:L82, S1:L83, S1:L84, S1:L85, S1:L86, S1:L87, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
|  | chatgpt | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
|  | gemini | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
| `script_37.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S4:L25, S4:L26, S4:L27, S4:L28, S4:L29, S4:L30, S4:L31 |
|  | chatgpt |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S4:L19, S4:L20, S4:L21, S4:L22, S4:L23, S4:L29, S4:L38, S4:L40 |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S4:L19, S4:L36, S4:L38, S4:L40 |
| `script_38.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S4:L19, S4:L20, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S4:L19, S4:L20, S4:L21, S4:L22, S4:L23, S4:L29, S4:L36, S4:L37, S4:L38, S4:L40 |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S4:L25, S4:L38, S4:L40 |
| `script_39.js` | claude |  |  | x | x | S3:L29, S3:L30, S3:L31, S3:L32, S3:L39, S4:L29, S4:L39 |
|  | chatgpt |  |  | x |  | S3:L29, S3:L39 |
|  | gemini |  |  |  |  | - |
| `script_40.js` | claude |  |  | x | x | S3:L18, S3:L22, S4:L18, S4:L22 |
|  | chatgpt |  |  | x | x | S3:L18, S3:L22, S4:L18, S4:L19, S4:L22, S4:L23 |
|  | gemini |  |  | x | x | S3:L18, S3:L22, S4:L18, S4:L19, S4:L22, S4:L23 |
| `script_41.js` | claude |  | x |  | x | S2:L4010, S2:L4011, S2:L4012, S2:L4013, S2:L4014, S2:L4015, S2:L4016, S2:L4017, S2:L4018, S2:L4019, S4:L4026, S4:L4027, S4:L4028, S4:L4029, S4:L4030, S4:L4031, S4:L4052, S4:L4053, S4:L4054 |
|  | chatgpt | x | x |  | x | S1:L5, S1:L4006, S2:L4010, S2:L4019, S4:L4026, S4:L4031, S4:L4052, S4:L4054 |
|  | gemini | x | x |  | x | S1:L5, S1:L4006, S2:L4010, S2:L4019, S4:L4026, S4:L4052 |
| `script_42.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L45, S4:L46, S4:L47, S4:L48, S4:L49, S4:L54 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L45, S4:L46, S4:L47, S4:L48, S4:L49, S4:L54, S4:L82, S4:L113 |
|  | gemini |  | x |  | x | S2:L5, S2:L11, S4:L54 |
| `script_45.js` | claude | x | x |  | x | S1:L22, S1:L23, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S4:L41, S4:L42, S4:L43 |
|  | chatgpt | x | x |  | x | S1:L22, S1:L23, S2:L6, S2:L15, S4:L41, S4:L42, S4:L43, S4:L45, S4:L46, S4:L47, S4:L48 |
|  | gemini | x | x |  | x | S1:L22, S1:L23, S2:L6, S2:L15, S4:L41, S4:L43 |
| `script_47.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S3:L12, S4:L12 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S3:L12, S4:L12 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S3:L12, S4:L12 |
| `script_51.js` | claude |  | x | x | x | S2:L6, S2:L7, S2:L8, S2:L9, S3:L18, S4:L18 |
|  | chatgpt |  | x | x | x | S2:L6, S2:L7, S2:L8, S2:L9, S3:L18, S4:L18 |
|  | gemini |  | x | x | x | S2:L6, S2:L7, S2:L8, S2:L9, S3:L18, S4:L18 |
| `script_52.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S3:L18, S4:L18 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S3:L18, S4:L18 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S3:L18, S4:L18 |
| `script_53.js` | claude |  | x | x |  | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S3:L22, S3:L23, S3:L24, S3:L25, S3:L26, S3:L27, S3:L28 |
|  | chatgpt |  | x | x |  | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S3:L22, S3:L23, S3:L24, S3:L25, S3:L26, S3:L27, S3:L28 |
|  | gemini |  | x | x |  | S2:L4, S2:L16, S3:L22, S3:L28 |
| `script_55.js` | claude | x | x |  | x | S1:L19, S1:L20, S1:L21, S1:L22, S1:L23, S1:L24, S1:L25, S1:L26, S1:L27, S1:L28, S1:L29, S1:L30, S1:L31, S1:L32, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L34 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x |  | x | S1:L19, S2:L8, S2:L17, S4:L27, S4:L31 |
| `script_56.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
| `script_59.js` | claude | x | x |  | x | S1:L16, S1:L17, S2:L20, S2:L21, S2:L22, S2:L23, S2:L24, S2:L25, S2:L26, S2:L27, S2:L28, S2:L29, S4:L46, S4:L47, S4:L48 |
|  | chatgpt | x | x |  | x | S1:L16, S1:L17, S2:L20, S2:L29, S4:L46, S4:L48 |
|  | gemini | x | x |  | x | S1:L16, S1:L17, S2:L20, S2:L21, S2:L22, S2:L23, S2:L24, S2:L25, S2:L26, S2:L27, S2:L28, S2:L29, S4:L46, S4:L47, S4:L48 |
| `script_60.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
| `script_61.js` | claude | x | x |  | x | S1:L19, S1:L20, S1:L21, S1:L22, S1:L23, S1:L24, S1:L25, S1:L26, S1:L27, S1:L28, S1:L29, S1:L30, S1:L31, S1:L32, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L34 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x |  | x | S1:L19, S1:L20, S1:L21, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L27, S4:L28, S4:L29, S4:L30, S4:L31 |
| `script_62.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
| `script_63.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S3:L13, S4:L13 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S3:L13, S4:L13 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S3:L13, S4:L13 |
| `script_69.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S3:L17, S4:L17 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S3:L17, S4:L17 |
|  | gemini |  | x | x | x | S2:L4, S3:L17, S4:L17 |
| `script_70.js` | claude |  | x | x | x | S2:L5, S2:L6, S2:L7, S2:L8, S3:L11, S4:L11 |
|  | chatgpt |  | x | x | x | S2:L5, S2:L6, S2:L7, S2:L8, S3:L11, S4:L11 |
|  | gemini |  | x | x | x | S2:L5, S2:L6, S2:L7, S2:L8, S3:L11, S4:L11 |
| `script_71.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S3:L18, S4:L18 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S3:L18, S4:L18 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S3:L18, S4:L18 |
| `script_76.js` | claude |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L21, S3:L22, S4:L16, S4:L17, S4:L18, S4:L19 |
|  | chatgpt |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L21, S4:L16, S4:L17, S4:L18, S4:L19 |
|  | gemini |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L21, S4:L16, S4:L17, S4:L18, S4:L19, S4:L21 |
| `script_77.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L15, S4:L15 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L15, S4:L15 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L15, S4:L15 |
| `script_78.js` | claude |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S3:L14, S4:L14 |
|  | chatgpt |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S3:L14, S4:L14 |
|  | gemini |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S3:L14, S4:L14 |
| `script_80.js` | claude |  | x | x | x | S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S3:L20, S3:L29, S3:L30, S3:L31, S3:L32, S3:L33, S4:L20 |
|  | chatgpt |  | x | x | x | S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S3:L20, S3:L29, S3:L30, S3:L31, S3:L32, S3:L33, S4:L20, S4:L23, S4:L26, S4:L30, S4:L32 |
|  | gemini |  | x | x | x | S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S3:L29, S3:L30, S3:L31, S3:L32, S3:L33, S4:L20 |
| `script_82.js` | claude |  | x | x | x | S2:L7, S2:L8, S2:L9, S3:L12, S4:L12 |
|  | chatgpt |  | x | x | x | S2:L7, S2:L8, S2:L9, S3:L12, S4:L12 |
|  | gemini |  | x | x | x | S2:L7, S2:L8, S2:L9, S3:L12, S4:L12 |
| `script_83.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L24, S4:L24 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L24, S4:L24 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L24, S3:L25, S3:L26, S4:L24 |
| `script_85.js` | claude |  |  |  |  | - |
|  | chatgpt | x | x |  |  | S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L49, S1:L50, S1:L51, S1:L52, S1:L53, S1:L54, S1:L55, S1:L56, S1:L57, S2:L67, S2:L68, S2:L69, S2:L70, S2:L71, S2:L72, S2:L73, S2:L74, S2:L75, S2:L76, S2:L77 |
|  | gemini | x | x |  |  | S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L49, S1:L50, S1:L51, S1:L52, S1:L53, S1:L54, S1:L55, S1:L56, S1:L57, S2:L67, S2:L68, S2:L69, S2:L70, S2:L71, S2:L72, S2:L73, S2:L74, S2:L75, S2:L76, S2:L77 |
| `script_89.js` | claude |  | x | x | x | S2:L9, S2:L10, S2:L11, S3:L16, S4:L16 |
|  | chatgpt |  | x | x | x | S2:L9, S2:L10, S2:L11, S3:L16, S4:L16 |
|  | gemini |  | x | x | x | S2:L9, S2:L10, S2:L11, S3:L16, S4:L16 |
| `script_90.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L10, S4:L10 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L10, S4:L10 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L10, S4:L10 |
| `script_92.js` | claude |  |  |  | x | S4:L45, S4:L63, S4:L87, S4:L104, S4:L131, S4:L150, S4:L167, S4:L230 |
|  | chatgpt |  |  |  | x | S4:L38, S4:L39, S4:L40, S4:L41, S4:L42, S4:L43, S4:L45, S4:L63, S4:L87, S4:L104, S4:L131, S4:L150, S4:L167, S4:L230 |
|  | gemini |  |  |  | x | S4:L45, S4:L63, S4:L87, S4:L104, S4:L131, S4:L150, S4:L167, S4:L230 |
| `script_93.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S3:L12, S3:L22, S3:L40, S3:L49, S3:L81, S3:L98, S3:L113, S4:L12, S4:L22, S4:L40, S4:L49, S4:L67, S4:L81, S4:L98, S4:L113 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L1, S2:L123, S3:L12, S3:L22, S3:L40, S3:L49, S3:L81, S3:L98, S3:L113, S4:L12, S4:L22, S4:L40, S4:L49, S4:L67, S4:L81, S4:L98, S4:L113 |
| `script_94.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  | x | x | S3:L96, S3:L97, S3:L98, S3:L99, S3:L100, S3:L101, S3:L102, S3:L103, S3:L104, S3:L105, S3:L106, S3:L107, S3:L108, S3:L109, S3:L110, S3:L111, S3:L112, S4:L39, S4:L40, S4:L41, S4:L42, S4:L43, S4:L44, S4:L45, S4:L46, S4:L47, S4:L56, S4:L57, S4:L58, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63, S4:L64, S4:L65, S4:L66, S4:L67, S4:L68, S4:L69, S4:L80, S4:L81, S4:L82, S4:L83, S4:L84, S4:L85, S4:L86, S4:L87, S4:L96, S4:L97, S4:L98, S4:L99, S4:L100, S4:L101, S4:L102, S4:L103, S4:L104, S4:L105, S4:L106, S4:L107, S4:L108, S4:L109, S4:L110, S4:L111, S4:L116, S4:L117, S4:L118, S4:L119, S4:L120, S4:L121, S4:L122, S4:L123, S4:L132, S4:L133, S4:L134, S4:L135, S4:L136, S4:L137, S4:L138, S4:L139, S4:L140, S4:L141, S4:L142, S4:L143, S4:L144, S4:L145, S4:L146, S4:L147, S4:L156, S4:L157, S4:L158, S4:L159, S4:L160, S4:L161, S4:L162, S4:L163, S4:L164, S4:L165, S4:L166, S4:L167, S4:L168, S4:L169, S4:L178, S4:L179, S4:L180, S4:L181, S4:L182, S4:L183, S4:L184, S4:L185, S4:L186 |
|  | gemini |  |  | x | x | S3:L96, S3:L97, S3:L98, S3:L99, S3:L100, S3:L101, S3:L102, S3:L103, S3:L104, S3:L105, S3:L106, S3:L107, S3:L108, S3:L109, S3:L110, S3:L111, S4:L39, S4:L40, S4:L41, S4:L42, S4:L43, S4:L44, S4:L45, S4:L46, S4:L47 |
| `script_95.js` | claude |  | x |  | x | S2:L6, S4:L19, S4:L28, S4:L39, S4:L40, S4:L41, S4:L47, S4:L58, S4:L70, S4:L72, S4:L76, S4:L88, S4:L99, S4:L110, S4:L111, S4:L112, S4:L116 |
|  | chatgpt |  | x |  | x | S4:L22, S4:L23, S4:L24, S4:L33, S4:L34, S4:L35, S4:L51, S4:L52, S4:L53, S4:L63, S4:L64, S4:L65, S4:L82, S4:L83, S4:L84, S4:L93, S4:L94, S4:L95, S4:L104, S4:L105, S4:L106, S4:L121, S4:L122, S4:L123 |
|  | gemini |  | x |  | x | S2:L6, S4:L18, S4:L27, S4:L57, S4:L87 |
| `script_96.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S3:L13, S3:L21, S3:L23, S3:L36, S3:L41, S3:L48, S3:L50, S3:L65, S3:L82, S3:L97, S3:L99, S3:L112, S4:L13, S4:L23, S4:L41, S4:L50, S4:L68, S4:L82, S4:L99 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L1, S2:L6, S3:L13, S3:L21, S4:L13, S4:L21 |
| `script_97.js` | claude |  | x |  |  | S2:L1, S2:L199 |
|  | chatgpt |  | x |  |  | S2:L197, S2:L198, S2:L199 |
|  | gemini |  | x |  |  | S2:L35 |
| `script_98.js` | claude |  | x |  |  | S2:L203, S2:L204, S2:L205 |
|  | chatgpt |  | x |  |  | S2:L203, S2:L204, S2:L205 |
|  | gemini |  | x |  |  | S2:L25 |
| `script_99.js` | claude |  | x |  |  | S2:L502, S2:L503, S2:L504 |
|  | chatgpt |  | x |  |  | S2:L502, S2:L503, S2:L504 |
|  | gemini |  | x |  |  | S2:L1, S2:L504 |

## Refactoring Suggestions

### `script_03.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [27, 31]
- **Snippet:**
```js
const to = {}

export const options = {
  thresholds: to,
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<2000'],
    errors_chunked_upload: ['count<5'],
    upload_duration: ['p(95)<5000'],
  },
  summaryTrendStats: trends,
  scenarios: {
    storage_multipart: sc(rampingDuration, consecutiveDuration, conns),
  },
}
```

**Smell 4: Not using tags**

- **Lines:** [60, 85, 103, 128]
- **Snippet:**
```js
const uploadRes = http.post(`${storageMultipartUri}`, null, { headers: ... })
...
const offsetRes = http.head(location, { headers })
...
const uploadChunkRes = http.patch(location, chunk, { headers: ... })
...
const removeRes = http.del(`${storageObjectUri}/tus`, ..., { headers: ... })
```
- **Refactored:**
```js
const uploadRes = http.post(`${storageMultipartUri}`, null, {
  headers: Object.assign({ 'Upload-Length': length, 'Content-Length': 0, 'Upload-Metadata': `...` }, headers),
  tags: { name: 'create_upload', endpoint: 'storage_multipart' },
})

const offsetRes = http.head(location, {
  headers,
  tags: { name: 'check_offset', endpoint: 'storage_multipart' },
})

const uploadChunkRes = http.patch(location, chunk, {
  headers: Object.assign({ 'Content-Type': 'application/offset+octet-stream', 'Upload-Offset': offset, 'Content-Length': chunk.byteLength }, headers),
  tags: { name: 'upload_chunk', endpoint: 'storage_multipart' },
})

const removeRes = http.del(`${storageObjectUri}/tus`, JSON.stringify({ prefixes: [path] }), {
  headers: { authorization: `Bearer ${serviceToken}`, apikey: serviceToken, 'Content-Type': 'application/json' },
  tags: { name: 'delete_object', endpoint: 'storage_object' },
})
```

### `script_03.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [38]
- **Snippet:**
```js
const binFile = open('./large_file.png', 'b')
```
- **Refactored:**
```js
export function setup() {
  // File is opened only once before the test starts
  const binFile = open('./large_file.png', 'b');
  return { binFile };
}

// The data from setup() is passed to the VUs
export default (data) => {
  const length = data.binFile.byteLength;
  // ...
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [27, 31]
- **Snippet:**
```js
const to = {}
...
  thresholds: to,
```
- **Refactored:**
```js
export const options = {
  // ...
  thresholds: {
    'http_req_duration': ['p(95)<2000'],
    'checks': ['rate>0.99'],
    'errors_chunked_upload': ['count==0']
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [60, 85, 103, 128]
- **Snippet:**
```js
const uploadRes = http.post(`${storageMultipartUri}`, null, {
    headers: Object.assign(
      //...
    ),
  })
```
- **Refactored:**
```js
const uploadRes = http.post(`${storageMultipartUri}`, null, {
    headers: Object.assign(
      //...
    ),
    tags: {
      name: 'TUS-CreateFile',
      flow: 'multipart-upload'
    },
  })
```

### `script_07.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [22]
- **Snippet:**
```js
let payload = JSON.parse(open('./testdata_v1.json'));
```
- **Refactored:**
```js
// Use SharedArray to perform the costly JSON parse only once and share across VUs
const payload = new SharedArray('testdata', function() {
    return [JSON.parse(open('./testdata_v1.json'))];
});
// Then inside default function, access it as: let user = Object.assign({}, payload[0]);
```

**Smell 2: Do not use thresholds**

- **Lines:** [7, 8, 9, 10]
- **Snippet:**
```js
export const options = {
    vus: 2,
    duration: '2s',
};
```
- **Refactored:**
```js
export const options = {
    vus: 2,
    duration: '2s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [48, 49, 50]
- **Snippet:**
```js
const res = http.post(`https://echo.hoppscotch.io`, f);
console.log("HTTP Status:" + res.status);
console.log("Sent Data:" + res.request.body);
```
- **Refactored:**
```js
import { check } from 'k6';

// ...

const res = http.post(`https://echo.hoppscotch.io`, f);
check(res, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
});
console.log("HTTP Status:" + res.status);
console.log("Sent Data:" + res.request.body);
```

**Smell 4: Not using tags**

- **Lines:** [48]
- **Snippet:**
```js
const res = http.post(`https://echo.hoppscotch.io`, f);
```
- **Refactored:**
```js
const res = http.post(`https://echo.hoppscotch.io`, f, {
    tags: { name: 'PostEchoHoppscotch', endpoint: '/echo' },
});
```

### `script_07.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [22]
- **Snippet:**
```js
let payload = JSON.parse(open('./testdata_v1.json'));
```
- **Refactored:**
```js
// Move the file reading and parsing to the setup function, so it only runs once.
export function setup() {
    const payload = JSON.parse(open('./testdata_v1.json'));
    return { payloadData: payload };
}

// Access the data in the default function via the parameter.
export default function(data) {
    let user = JSON.parse(JSON.stringify(data.payloadData)); // Deep copy to prevent VUs from modifying the same object
    // ... rest of the script
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [7, 8, 9, 10]
- **Snippet:**
```js
export const options = {
    vus: 2,
    duration: '2s',
};
```
- **Refactored:**
```js
export const options = {
    vus: 2,
    duration: '2s',
    thresholds: {
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [48]
- **Snippet:**
```js
const res = http.post(`https://echo.hoppscotch.io`, f);
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const res = http.post(`https://echo.hoppscotch.io`, f);
check(res, {
    'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [48]
- **Snippet:**
```js
const res = http.post(`https://echo.hoppscotch.io`, f);
```
- **Refactored:**
```js
const params = {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'EchoEndpoint' }, // Add a tag to identify this request
};
const res = http.post(`https://echo.hoppscotch.io`, f, params);
```

### `script_10.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [16]
- **Snippet:**
```js
export let options = { maxRedirects: 4 };
```
- **Refactored:**
```js
export let options = {
  maxRedirects: 4,
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<2000'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [29, 92, 132, 178, 217, 260, 328, 401, 501, 567, 633, 700, 766, 832, 898, 967, 1035, 1108, 1176, 1244, 1328, 1389, 1450, 1512, 1573, 1634, 1695, 1759, 1827, 1900, 1968, 2027, 2077, 2128, 2179, 2231, 2282, 2333, 2384, 2438, 2506, 2574, 2633, 2683, 2734, 2785, 2837, 2888, 2939, 2990, 3044, 3112, 3185, 3245, 3304, 3354, 3405, 3456, 3508, 3559, 3610, 3661, 3715, 3775, 3825, 3878, 3931, 3985, 4038, 4091, 4144, 4200, 4268, 4350, 4411, 4472, 4534, 4595, 4656, 4717]
- **Snippet:**
```js
postman[Request]({
  name: "Registration",
  method: "POST",
  address: "{{APIURL}}/users",
  // no tags property
  ...
```
- **Refactored:**
```js
postman[Request]({
  name: "Registration",
  method: "POST",
  address: "{{APIURL}}/users",
  tags: { endpoint: "registration", group: "Registration and Authentication" },
  ...
```

### `script_10.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [16]
- **Snippet:**
```js
export let options = { maxRedirects: 4 };
```
- **Refactored:**
```js
export let options = {
  maxRedirects: 4,
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<1500'], // 95% of requests must complete below 1.5s
    'checks': ['rate>0.99'], // 99% of checks must pass
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [29, 92, 132, 178, 217]
- **Snippet:**
```js
postman[Request]({
      name: "Registration",
      id: "2024-02-23-06-45-22-022",
      method: "POST",
      options: { timeout: timeout },
```
- **Refactored:**
```js
postman[Request]({
      name: "Registration",
      id: "2024-02-23-06-45-22-022",
      method: "POST",
      options: {
        timeout: timeout,
        tags: { 
          endpoint: "Registration" 
        },
      },
```

### `script_100.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** []
- **Snippet:**
```js
No thresholds are defined in the provided k6 code.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [15, 30, 43, 58, 71, 85]
- **Snippet:**
```js
http.get(ordersUrl, { headers: this.headers });
http.get(ordersTableUrl, { headers: this.headers });
http.get(orderDetailUrl, { headers: this.headers });
http.get(itemListTableUrl, { headers: this.headers });
http.get(totalItemListUrl, { headers: this.headers });
http.get(triggerEventUrl, { headers: this.headers });
```
- **Refactored:**
```js
const ordersResponse = http.get(ordersUrl, { headers: this.headers, tags: { endpoint: 'orders', flow: 'orders_all' } });
const ordersTableResponse = http.get(ordersTableUrl, { headers: this.headers, tags: { endpoint: 'orders_table_data', flow: 'orders_all' } });
const orderDetailResponse = http.get(orderDetailUrl, { headers: this.headers, tags: { endpoint: 'order_detail', flow: 'order_get' } });
const itemListTableResponse = http.get(itemListTableUrl, { headers: this.headers, tags: { endpoint: 'item_list_table_data', flow: 'order_get' } });
const totalItemListResponse = http.get(totalItemListUrl, { headers: this.headers, tags: { endpoint: 'total_item_list', flow: 'order_total_item_list' } });
const triggerEventResponse = http.get(triggerEventUrl, { headers: this.headers, tags: { endpoint: 'trigger_event', flow: 'order_trigger_event', event } });
```

### `script_100.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [15, 30, 43, 58, 71, 85]
- **Snippet:**
```js
const ordersResponse = http.get(ordersUrl, { headers: this.headers });
```
- **Refactored:**
```js
const params = {
  headers: this.headers,
  tags: {
    name: 'OrdersPage-All' // Using the 'name' tag groups metrics for this specific endpoint
  },
};
const ordersResponse = http.get(ordersUrl, params);
// This pattern should be applied to all other http requests in the file for better observability.
```

### `script_104.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [15, 16, 17, 18]
- **Snippet:**
```js
res = http.get('https://quickpizza.grafana.com/api/status/500');
  check(res, {
    'status is 500': (r) => r.status == 500,
  });
```
- **Refactored:**
```js
res = http.get('https://quickpizza.grafana.com/api/status/500', { tags: { myTag: 'status500' } });
  check(
    res,
    { 'status is 500': (r) => r.status == 500 },
    { myTag: 'status500' }
  );
```

### `script_104.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [15, 16, 20, 21]
- **Snippet:**
```js
res = http.get('https://quickpizza.grafana.com/api/status/500');
check(res, {
...
res = http.get('https://quickpizza.grafana.com/api/status/200');
check(
```
- **Refactored:**
```js
res = http.get('https://quickpizza.grafana.com/api/status/500', {
  tags: { endpoint: 'status_500', flow: 'status_api' },
});
check(
  res,
  {
    'status is 500': (r) => r.status == 500,
  },
  { endpoint: 'status_500', flow: 'status_api' }
);

res = http.get('https://quickpizza.grafana.com/api/status/200', {
  tags: { endpoint: 'status_200', flow: 'status_api' },
});
check(
  res,
  {
    'status is 200': (r) => r.status == 200,
  },
  { endpoint: 'status_200', flow: 'status_api' }
);
```

### `script_104.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [24]
- **Snippet:**
```js
'status is 200': (r) => r.status == 201,
```
- **Refactored:**
```js
'status is 200': (r) => r.status == 200,
```

**Smell 4: Not using tags**

- **Lines:** [15, 16]
- **Snippet:**
```js
res = http.get('https://quickpizza.grafana.com/api/status/500');
  check(res, {
    'status is 500': (r) => r.status == 500,
  });
```
- **Refactored:**
```js
const get500Tags = { endpoint: 'status-500' };
  res = http.get('https://quickpizza.grafana.com/api/status/500', { tags: get500Tags });
  check(
    res,
    {
      'status is 500': (r) => r.status == 500,
    },
    get500Tags
  );
```

### `script_109.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [269, 270, 271]
- **Snippet:**
```js
export default function () {
	checkoutCustomerLogin();
}
```
- **Refactored:**
```js
export const options = {
	thresholds: {
		http_req_failed: ['rate<0.01'],
		http_req_duration: ['p(95)<2000'],
		'http_req_duration{name:"Shopper - View Checkout"}': ['p(95)<2000'],
		'http_req_duration{name:"Shopper - Login to Checkout"}': ['p(95)<2000'],
		'http_req_duration{name:"Shopper - Store API update-customer"}': ['p(95)<2000'],
		'http_req_duration{name:"Shopper - Store API checkout"}': ['p(95)<2000'],
		'http_req_duration{name:"Shopper - Order Received"}': ['p(95)<2000'],
		'http_req_duration{name:"Shopper - wc-ajax=get_refreshed_fragments"}': ['p(95)<2000'],
	},
};

export default function () {
	checkoutCustomerLogin();
}
```

### `script_109.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** []
- **Snippet:**
```js
No export const options with thresholds is defined in the script.
```
- **Refactored:**
```js
export const options = {
	thresholds: {
		http_req_failed: ['rate<0.01'],
		http_req_duration: ['p(95)<1000'],
		checks: ['rate>0.99'],
	},
};
```

**Smell 4: Not using tags**

- **Lines:** [254, 255, 256, 257, 258, 259, 260]
- **Snippet:**
```js
const refreshResponse = http.post(
	`${ base_url }/?wc-ajax=get_refreshed_fragments`,
	{
		headers: requestHeadersPost,
		tags: { name: 'Shopper - wc-ajax=get_refreshed_fragments' },
	}
);
```
- **Refactored:**
```js
const refreshResponse = http.post(
	`${ base_url }/?wc-ajax=get_refreshed_fragments`,
	null,
	{
		headers: requestHeadersPost,
		tags: { name: 'Shopper - wc-ajax=get_refreshed_fragments' },
	}
);
```

### `script_109.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 271]
- **Snippet:**
```js
The entire script is missing an `export const options = { ... }` block, which is where thresholds are defined. Without it, the test will always pass in a CI/CD environment, regardless of the system's performance.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    // 95% of requests must complete within 2000ms.
    'http_req_duration': ['p(95)<2000'],
    // The error rate must be less than 1%.
    'http_req_failed': ['rate<0.01'],
    // The rate of successful checks must be greater than 99%.
    'checks': ['rate>0.99'],
  },
};

export default function () {
	checkoutCustomerLogin();
}
```

**Smell 4: Not using tags**

- **Lines:** [254, 260]
- **Snippet:**
```js
const refreshResponse = http.post(
	`${ base_url }/?wc-ajax=get_refreshed_fragments`,
	{
		headers: requestHeadersPost,
		tags: { name: 'Shopper - wc-ajax=get_refreshed_fragments' },
	}
);
```
- **Refactored:**
```js
const refreshResponse = http.post(
	`${ base_url }/?wc-ajax=get_refreshed_fragments`,
	null, // The second argument is the request body, which is empty here.
	{
		// The third argument is for parameters like headers and tags.
		headers: requestHeadersPost,
		tags: { name: 'Shopper - wc-ajax=get_refreshed_fragments' },
	}
);
```

### `script_112.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
- **Snippet:**
```js
response = http.get('https://doctor.mountsinai.org/fad/autocomplete/lite', {
  headers: {
    ...
  },
})
```
- **Refactored:**
```js
response = http.get('https://doctor.mountsinai.org/fad/autocomplete/lite', {
  tags: {
    my_tag: 'Autocomplete tag'
  },
  headers: {
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'iframe',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
  },
})
check(response, {
  'autocomplete status is ok 200': (r) => r.status === 200,
})
```

**Smell 4: Not using tags**

- **Lines:** [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
- **Snippet:**
```js
response = http.get('https://doctor.mountsinai.org/fad/autocomplete/lite', {
  headers: {
    ...
  },
})
```
- **Refactored:**
```js
response = http.get('https://doctor.mountsinai.org/fad/autocomplete/lite', {
  tags: {
    endpoint: 'autocomplete',
    page: 'Page_1'
  },
  headers: {
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'iframe',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
  },
})
```

### `script_112.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
- **Snippet:**
```js
response = http.get('https://doctor.mountsinai.org/fad/autocomplete/lite', {
      headers: {
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        accept:
          'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'iframe',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
      },
    })
```
- **Refactored:**
```js
response = http.get('https://doctor.mountsinai.org/fad/autocomplete/lite', {
      headers: {
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        accept:
          'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'iframe',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
      },
    })
    check(response, {
        'autocomplete status is 200': (r) => r.status === 200,
    })
```

**Smell 4: Not using tags**

- **Lines:** [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
- **Snippet:**
```js
response = http.get('https://doctor.mountsinai.org/fad/autocomplete/lite', {
      headers: {
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        accept:
          'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'iframe',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
      },
    })
```
- **Refactored:**
```js
response = http.get('https://doctor.mountsinai.org/fad/autocomplete/lite', {
      tags: {
        my_tag: "Autocomplete tag"
      },
      headers: {
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        accept:
          'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'iframe',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
      },
    })
```

### `script_12.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [21, 22, 23, 24, 27, 28, 29, 30, 31, 32, 33, 34, 36]
- **Snippet:**
```js
const mobileNumber = generateRandomMobileNumber();
const sentPayload = JSON.stringify({
    mobile: mobileNumber
})

let XAccessToken;
const verifyPayload = JSON.stringify({
    "mobile": mobileNumber,
    "otp": "123456",
    ...
})

const fileData = open('./download.pdf', 'b');
```
- **Refactored:**
```js
// Move payload generation and mobile number generation inside the default function
// open() is acceptable in init context, but heavy computation should be deferred
// generateRandomMobileNumber() and JSON.stringify calls should be inside default()

export default function () {
    const mobileNumber = generateRandomMobileNumber();
    const sentPayload = JSON.stringify({ mobile: mobileNumber });
    const verifyPayload = JSON.stringify({
        "mobile": mobileNumber,
        "otp": "123456",
        "os": "android",
        "deviceId": "1234567891",
        "osVersion": "10",
        "manufacturer": "samsung"
    });
    // rest of the test logic...
}
```

**Smell 4: Not using tags**

- **Lines:** [43, 50, 64, 72, 110, 122, 134, 141, 148, 158, 170, 176, 195, 210]
- **Snippet:**
```js
const sendOtpResponse = http.post(`${baseUrl}/users/v1/public/send-otp`, sentPayload, { headers });
const verifyOtp = http.post(`${baseUrl}/users/v1/public/verify-otp`, verifyPayload, { headers });
const profileGet = http.get(`${baseUrl}/users/v1/profile`, { headers });
// ... all other requests lack tags
```
- **Refactored:**
```js
const sendOtpResponse = http.post(
    `${baseUrl}/users/v1/public/send-otp`,
    sentPayload,
    { headers, tags: { name: 'send-otp', group: 'Send and Verify OTP' } }
);

const verifyOtp = http.post(
    `${baseUrl}/users/v1/public/verify-otp`,
    verifyPayload,
    { headers, tags: { name: 'verify-otp', group: 'Send and Verify OTP' } }
);

const profileGet = http.get(
    `${baseUrl}/users/v1/profile`,
    { headers, tags: { name: 'profile-get', group: 'Personal Details' } }
);

// Apply similar tags pattern to all other requests:
// tags: { name: '<endpoint-identifier>', group: '<group-name>' }
```

### `script_12.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [36]
- **Snippet:**
```js
const fileData = open('./download.pdf', 'b');
```
- **Refactored:**
```js
// Avoid loading a potentially large binary file into every VU's init context.
// Prefer a small fixture for upload tests, or use k6's experimental filesystem API to avoid duplicating large file contents per VU.
import { open as fsOpen } from 'k6/experimental/fs';

const pdfFile = await fsOpen('./download.pdf');

export default async function () {
  const fileData = await pdfFile.read();
  const fd = new FormData();
  fd.append('type', 'health_records');
  fd.append('file', http.file(fileData, 'download.pdf', 'application/pdf'));
}
```

**Smell 4: Not using tags**

- **Lines:** [43, 50, 64, 72, 110, 122, 134, 141, 148, 158, 170, 176, 195, 210]
- **Snippet:**
```js
http.post(`${baseUrl}/users/v1/public/send-otp`, sentPayload, { headers });
http.get(`${baseUrl}/users/v1/profile`, { headers });
http.post(`${baseUrl}/uploads/v1/upload`, fd.body(), { headers });
```
- **Refactored:**
```js
const params = (flow, endpoint) => ({
  headers,
  tags: { flow, endpoint }
});

const sendOtpResponse = http.post(
  `${baseUrl}/users/v1/public/send-otp`,
  sentPayload,
  params('auth', 'send-otp')
);

const profileGet = http.get(
  `${baseUrl}/users/v1/profile`,
  params('profile', 'get-profile')
);

const uploadPost = http.post(
  `${baseUrl}/uploads/v1/upload`,
  fd.body(),
  params('health-records', 'upload-document')
);

// Apply the same pattern to all other HTTP requests.
```

### `script_12.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [36]
- **Snippet:**
```js
const fileData = open('./download.pdf', 'b');
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

const fileData = new SharedArray('pdf file', function () {
  // The file is now read only once for all VUs and the data is shared,
  // reducing memory consumption and test setup time.
  return open('./download.pdf', 'b');
});
```

**Smell 4: Not using tags**

- **Lines:** [43, 50, 64, 72, 110, 122, 134, 141, 148, 158, 170, 176, 195, 210]
- **Snippet:**
```js
const sendOtpResponse = http.post(`${baseUrl}/users/v1/public/send-otp`, sentPayload, { headers });
```
- **Refactored:**
```js
// All http requests should include a `tags` object for better metric filtering.
// Example for the request on line 43:
const sendOtpResponse = http.post(`${baseUrl}/users/v1/public/send-otp`, sentPayload, {
  headers,
  tags: { 
    name: 'SendOTP' 
  },
});
```

### `script_129.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [20, 27]
- **Snippet:**
```js
const res1 = http.get('https://test-api.k6.io/public/crocodiles');
    const res2 = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
const res1 = http.get('https://test-api.k6.io/public/crocodiles', { tags: { name: 'GetAllCrocodiles', endpoint: '/public/crocodiles' } });
const res2 = http.get('https://test-api.k6.io/public/crocodiles/1/', { tags: { name: 'GetCrocodileById', endpoint: '/public/crocodiles/:id' } });
```

### `script_129.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [20, 21, 27, 28]
- **Snippet:**
```js
const res1 = http.get('https://test-api.k6.io/public/crocodiles');
check(res1, {
  'status code is 200 get all': (r) => r.status === 200
})

const res2 = http.get('https://test-api.k6.io/public/crocodiles/1/');
check(res2, {
  'status code is 200 get id': (r) => r.status === 200
})
```
- **Refactored:**
```js
group('request all crocodiles', function () {
  const tags = { endpoint: 'crocodiles_all', flow: 'crocodiles' };
  const res1 = http.get('https://test-api.k6.io/public/crocodiles', { tags });
  check(res1, {
    'status code is 200 get all': (r) => r.status === 200
  }, tags);
})

group('request crocodiles by id', function() {
  const tags = { endpoint: 'crocodiles_by_id', flow: 'crocodiles' };
  const res2 = http.get('https://test-api.k6.io/public/crocodiles/1/', { tags });
  check(res2, {
    'status code is 200 get id': (r) => r.status === 200
  }, tags);
})
```

### `script_129.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [13, 14, 15]
- **Snippet:**
```js
thresholds: {
    'http_req_duration{group:::request crocodiles by id}': ['p(95) < 500']
  }
```
- **Refactored:**
```js
export const options = {
  vus: 4,
  duration: '5s',
  thresholds: {
    // A global threshold for all requests
    'http_req_duration': ['p(95) < 500'],
    // Specific threshold for the 'get all' group
    'http_req_duration{group:::request all crocodiles}': ['p(95) < 600'],
    // Specific threshold for the 'get by id' group
    'http_req_duration{group:::request crocodiles by id}': ['p(95) < 400'],
    // Threshold on the rate of successful checks
    'checks': ['rate>0.99']
  }
}
```

**Smell 4: Not using tags**

- **Lines:** [20, 27]
- **Snippet:**
```js
const res1 = http.get('https://test-api.k6.io/public/crocodiles');
// ...
const res2 = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
group('request all crocodiles', function () {
    const res1 = http.get('https://test-api.k6.io/public/crocodiles', {
      tags: { name: 'GetAllCrocodiles' },
    });
    check(res1, {
      'status code is 200 get all': (r) => r.status === 200,
    });
  });

  group('request crocodiles by id', function () {
    const res2 = http.get('https://test-api.k6.io/public/crocodiles/1/', {
      tags: { name: 'GetCrocodileById' },
    });
    check(res2, {
      'status code is 200 get id': (r) => r.status === 200,
    });
  });
```

### `script_130.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [14, 22]
- **Snippet:**
```js
const response1 = http.get('https://test-api.k6.io/public/crocodiles/');
        const response2 = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
const response1 = http.get('https://test-api.k6.io/public/crocodiles/', { tags: { name: 'get_all_crocodiles', endpoint: '/public/crocodiles/' } });
const response2 = http.get('https://test-api.k6.io/public/crocodiles/1/', { tags: { name: 'get_crocodile_by_id', endpoint: '/public/crocodiles/:id' } });
```

**Smell 2: Do not use thresholds**

- **Lines:** [7, 8, 9]
- **Snippet:**
```js
thresholds: {
        'http_req_duration{group:::requisição por id}': ['p(95) < 500']
    }
```
- **Refactored:**
```js
thresholds: {
        'http_req_duration{group:::requisição por id}': ['p(95) < 500'],
        'http_req_duration{group:::requisição todos os crocodilos}': ['p(95) < 500'],
        'http_req_failed': ['rate < 0.01'],
        'checks': ['rate > 0.99']
    }
```

### `script_130.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [14, 22]
- **Snippet:**
```js
const response1 = http.get('https://test-api.k6.io/public/crocodiles/');
const response2 = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
export default function(){
    group('requisição todos os crocodilos', function(){
        const response1 = http.get('https://test-api.k6.io/public/crocodiles/', {
            tags: { endpoint: 'get_all_crocodiles', flow: 'crocodiles' }
        });
        check(response1, {
            'status code 200 get all': (r) => r.status === 200
        }, { endpoint: 'get_all_crocodiles', flow: 'crocodiles' });
    });

    group('requisição por id', function(){
        const response2 = http.get('https://test-api.k6.io/public/crocodiles/1/', {
            tags: { endpoint: 'get_crocodile_by_id', flow: 'crocodiles' }
        });
        check(response2, {
            'status code 200 get id': (r) => r.status === 200
        }, { endpoint: 'get_crocodile_by_id', flow: 'crocodiles' });
    });
}
```

### `script_130.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [14, 22]
- **Snippet:**
```js
const response1 = http.get('https://test-api.k6.io/public/crocodiles/');
// ...
const response2 = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
const response1 = http.get('https://test-api.k6.io/public/crocodiles/', {
  tags: { name: 'PublicCrocodiles-GetAll' },
});
// ...
const response2 = http.get('https://test-api.k6.io/public/crocodiles/1/', {
  tags: { name: 'PublicCrocodiles-GetById' },
});
```

### `script_145.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [67, 79, 83, 91, 106]
- **Snippet:**
```js
export let loadOptions = {
    stages: [...],
};
export let smokeOptions = {
    vus: 1,
    iterations: 1,
};
// ... other option objects
```
- **Refactored:**
```js
export let loadOptions = {
    stages: [
        { duration: "2m", target: rampVus },
        { duration: "3m", target: rampVus },
        { duration: "3m", target: maxVus },
        { duration: "3m", target: maxVus },
        { duration: "2m", target: rampVus },
        { duration: "3m", target: rampVus },
        { duration: "2m", target: 0 },
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'],
        errors: ['rate<0.01'],
        authentication_successful: ['rate>0.99'],
    },
};

export let smokeOptions = {
    vus: 1,
    iterations: 1,
    thresholds: {
        http_req_duration: ['p(95)<500'],
        errors: ['rate<0.01'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [233, 263, 297, 344, 399, 476]
- **Snippet:**
```js
let response = http.get(ConfigurationUrl);
// ...
let response = http.get(OpenIdConnect.AuthorityEndpoint + "/.well-known/openid-configuration");
// ...
var res = http.post(OpenIdConnect.TokenEndpoint, auth_form_data, { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } });
// ...
let res = http.post(OpenIdConnect.TokenEndpoint, refresh_form_data);
// ...
"comments": { method: "GET", url: ServiceEndpoints.GatewayApi + "UserProfile/" + user.hdid + "/Comment", params: params(user) },
```
- **Refactored:**
```js
// In getConfigurations()
let response = http.get(ConfigurationUrl, { tags: { name: 'getConfigurations', endpoint: 'configuration' } });

// In getOpenIdConfigurations()
let response = http.get(OpenIdConnect.AuthorityEndpoint + '/.well-known/openid-configuration', { tags: { name: 'getOpenIdConfig', endpoint: 'openid-configuration' } });

// In authenticateUser()
var res = http.post(OpenIdConnect.TokenEndpoint, auth_form_data, {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    tags: { name: 'authenticateUser', endpoint: 'token' },
});

// In refreshUser()
let res = http.post(OpenIdConnect.TokenEndpoint, refresh_form_data, { tags: { name: 'refreshToken', endpoint: 'token' } });

// In timelineRequests()
"comments": {
    method: "GET",
    url: ServiceEndpoints.GatewayApi + "UserProfile/" + user.hdid + "/Comment",
    params: { ...params(user), tags: { name: 'getComments', endpoint: 'comments' } },
},
"encounter": {
    method: "GET",
    url: ServiceEndpoints.Encounter + "Encounter/" + user.hdid,
    params: { ...params(user), tags: { name: 'getEncounter', endpoint: 'encounter' } },
},
// ... apply tags to all other requests similarly
```

### `script_145.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [67, 79, 83, 91, 106]
- **Snippet:**
```js
export let loadOptions = {
    stages: [
        { duration: "2m", target: rampVus }, 
        { duration: "3m", target: rampVus },
        { duration: "3m", target: maxVus },
        { duration: "3m", target: maxVus }, 
        { duration: "2m", target: rampVus }, 
        { duration: "3m", target: rampVus }, 
        { duration: "2m", target: 0 },
    ],
};
```
- **Refactored:**
```js
export let loadOptions = {
    stages: [
        { duration: "2m", target: rampVus }, 
        { duration: "3m", target: rampVus },
        { duration: "3m", target: maxVus },
        { duration: "3m", target: maxVus }, 
        { duration: "2m", target: rampVus }, 
        { duration: "3m", target: rampVus }, 
        { duration: "2m", target: 0 },
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
        'errors': ['rate<0.01'],
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [297, 344]
- **Snippet:**
```js
var res = http.post(OpenIdConnect.TokenEndpoint, auth_form_data,
    {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    });
if (res.status == 200) { ... }
```
- **Refactored:**
```js
var res = http.post(OpenIdConnect.TokenEndpoint, auth_form_data,
    {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    });
check(res, {
    'authentication status is 200': (r) => r.status === 200,
});
if (res.status == 200) { ... }
```

**Smell 4: Not using tags**

- **Lines:** [297]
- **Snippet:**
```js
var res = http.post(OpenIdConnect.TokenEndpoint, auth_form_data,
    {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    });
```
- **Refactored:**
```js
var res = http.post(OpenIdConnect.TokenEndpoint, auth_form_data,
    {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        tags: { name: 'Authentication' },
    });
```

### `script_146.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [34]
- **Snippet:**
```js
http.post(url,  JSON.stringify(payload), params);
```
- **Refactored:**
```js
import { check } from 'k6';

// ... inside default function
const res = http.post(url,  JSON.stringify(payload), params);
check(res, {
  'response code was 201': (r) => r.status == 201,
});
```

**Smell 4: Not using tags**

- **Lines:** [34]
- **Snippet:**
```js
http.post(url,  JSON.stringify(payload), params);
```
- **Refactored:**
```js
var params = {
  headers: {
    'Content-Type': 'application/json',
  },
  tags: {
    name: 'CreateUser',
  },
};
http.post(url,  JSON.stringify(payload), params);
```

### `script_149.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
export let options = {
  ...test_options,
  thresholds: {
    ...(test_options.thresholds || {}),
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

### `script_149.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
export let options = Object.assign({}, test_options, {
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
    'checks': ['rate>0.99'],
  },
});
```

### `script_15.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168]
- **Snippet:**
```js
// Hold connections open
  const batch = [];
  for (let i = 0; i < 10; i++) {
    batch.push(
      http.get(`${BASE_URL}/api/v1/assets?page=${i + 1}&limit=100&include=metadata,versions`, {
        headers,
        timeout: '30s',
      })
    );
  }
  
  // Check all responses
  batch.forEach((res) => {
    if (res.status === 0) {
      apiTimeouts.add(1);
    } else if (res.status >= 500) {
      apiErrors.add(1);
    }
  });
```
- **Refactored:**
```js
const batch = [];
for (let i = 0; i < 10; i++) {
  batch.push(
    http.get(`${BASE_URL}/api/v1/assets?page=${i + 1}&limit=100&include=metadata,versions`, {
      headers,
      timeout: '30s',
      tags: { endpoint: 'list_assets', scenario: 'connection_exhaustion' },
    })
  );
}

batch.forEach((res, i) => {
  check(res, {
    'status is 200': (r) => r.status === 200,
    'has data': (r) => r.json('data') !== null,
  });
  if (res.status === 0) {
    apiTimeouts.add(1);
  } else if (res.status >= 500) {
    apiErrors.add(1);
  }
  endpointDuration.add(res.timings.duration);
});
```

**Smell 3: Not checking requests**

- **Lines:** [248, 249, 250, 251, 252, 253, 254, 255, 256, 257]
- **Snippet:**
```js
// Update metadata multiple times
      for (let i = 0; i < 10; i++) {
        http.patch(
          `${BASE_URL}/api/v1/assets/${assetId}/metadata`,
          JSON.stringify({
            additionalData: randomString(5000),
            iteration: i,
          }),
          { headers, timeout: '5s' }
        );
      }
```
- **Refactored:**
```js
for (let i = 0; i < 10; i++) {
  const patchRes = http.patch(
    `${BASE_URL}/api/v1/assets/${assetId}/metadata`,
    JSON.stringify({
      additionalData: randomString(5000),
      iteration: i,
    }),
    { headers, timeout: '5s', tags: { endpoint: 'update_metadata', scenario: 'memory_leak_test' } }
  );
  check(patchRes, {
    'metadata update successful': (r) => r.status === 200,
  });
  if (patchRes.status >= 500) apiErrors.add(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [121, 122, 123, 124, 153, 154, 155, 156, 199, 200, 201, 202, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 249, 250, 251, 252, 253, 254, 255, 260, 261, 262, 263, 264, 302, 303, 304, 305, 306, 314, 315, 316, 317, 326, 327, 328, 329, 330, 331, 332, 333, 334, 343, 344, 345, 346, 347, 348, 349, 350]
- **Snippet:**
```js
const res = http.get(`${BASE_URL}/api/v1/assets`, { 
    headers,
    timeout: '2s',
  });
// ...
http.get(`${BASE_URL}/api/v1/assets?page=${i + 1}&limit=100&include=metadata,versions`, { headers, timeout: '30s' })
// ...
http.post(`${BASE_URL}/api/v1/assets`, payload, { headers, timeout: '30s' });
// ...
http.post(`${BASE_URL}/api/v1/search/advanced`, JSON.stringify(complexQuery), { headers, timeout: '10s' });
// etc.
```
- **Refactored:**
```js
// rateLimitTest
const res = http.get(`${BASE_URL}/api/v1/assets`, {
  headers,
  timeout: '2s',
  tags: { endpoint: 'list_assets', scenario: 'rate_limit_test' },
});

// connectionExhaustionTest
http.get(`${BASE_URL}/api/v1/assets?page=${i + 1}&limit=100&include=metadata,versions`, {
  headers,
  timeout: '30s',
  tags: { endpoint: 'list_assets_paged', scenario: 'connection_exhaustion' },
});

// largePayloadTest
http.post(`${BASE_URL}/api/v1/assets`, payload, {
  headers,
  timeout: '30s',
  tags: { endpoint: 'create_asset_large', scenario: 'large_payload_stress' },
});

// memoryLeakTest - create
http.post(`${BASE_URL}/api/v1/assets`, JSON.stringify({...}), {
  headers,
  timeout: '10s',
  tags: { endpoint: 'create_asset', scenario: 'memory_leak_test' },
});

// cascadingFailureTest - advanced search
http.post(`${BASE_URL}/api/v1/search/advanced`, JSON.stringify(complexQuery), {
  headers,
  timeout: '10s',
  tags: { endpoint: 'advanced_search', scenario: 'cascading_failure' },
});
// (apply similar tags pattern to all other requests in cascadingFailureTest)
```

### `script_15.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [161, 162, 163, 164, 165, 166, 167]
- **Snippet:**
```js
  batch.forEach((res) => {
    if (res.status === 0) {
      apiTimeouts.add(1);
    } else if (res.status >= 500) {
      apiErrors.add(1);
    }
  });
```
- **Refactored:**
```js
  batch.forEach((res) => {
    const isSuccess = check(res, {
      'status is 200': (r) => r.status === 200,
    });

    if (!isSuccess) {
      apiErrors.add(1);
    }

    if (res.status === 0) {
      apiTimeouts.add(1);
    }
  });
```

**Smell 4: Not using tags**

- **Lines:** [121, 122, 123, 124]
- **Snippet:**
```js
  const res = http.get(`${BASE_URL}/api/v1/assets`, { 
    headers,
    timeout: '2s',
  });
```
- **Refactored:**
```js
  const res = http.get(`${BASE_URL}/api/v1/assets`, { 
    headers,
    timeout: '2s',
    tags: { name: 'GetAssets' },
  });
```

### `script_158.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [53, 58, 59]
- **Snippet:**
```js
orderReference = JSON.parse(checkoutResource.checkout().body).data.attributes.orderReference;
...
const response = cartReorderResource.reorder();
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
import { check } from 'k6';

// Inside 'Checkout' group:
const checkoutResponse = checkoutResource.checkout();
check(checkoutResponse, {
  'checkout status is 201': (r) => r.status === 201,
  'checkout has orderReference': (r) => JSON.parse(r.body).data.attributes.orderReference !== undefined,
});
orderReference = JSON.parse(checkoutResponse.body).data.attributes.orderReference;

// Inside Cart Reorder group:
const response = cartReorderResource.reorder();
check(response, {
  'cart reorder status is 201': (r) => r.status === 201,
});
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```

**Smell 4: Not using tags**

- **Lines:** [47, 53, 58]
- **Snippet:**
```js
bearerToken = AuthUtil.getInstance().getBearerToken(customerEmail);
...
orderReference = JSON.parse(checkoutResource.checkout().body).data.attributes.orderReference;
...
const response = cartReorderResource.reorder();
```
- **Refactored:**
```js
// Add tags to each request to allow filtering and grouping of metrics by endpoint/flow.

// Authorization request:
bearerToken = AuthUtil.getInstance().getBearerToken(customerEmail, { tags: { name: 'Authorization', flow: 'cart-reorder' } });

// Checkout request:
const checkoutResponse = checkoutResource.checkout({ tags: { name: 'Checkout', flow: 'cart-reorder' } });
orderReference = JSON.parse(checkoutResponse.body).data.attributes.orderReference;

// Cart Reorder request:
const response = cartReorderResource.reorder({ tags: { name: 'CartReorder', flow: 'cart-reorder' } });
metrics[testConfiguration.metrics[0]].add(response.timings.duration, { tags: { name: 'CartReorder', flow: 'cart-reorder' } });
```

### `script_158.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [47, 53, 58]
- **Snippet:**
```js
bearerToken = AuthUtil.getInstance().getBearerToken(customerEmail);
orderReference = JSON.parse(checkoutResource.checkout().body).data.attributes.orderReference;
const response = cartReorderResource.reorder();
```
- **Refactored:**
```js
import { group, check } from 'k6';

export default function (data) {
  const { customerEmail, idCart } = fixture.iterateData(data);

  let bearerToken;
  group('Authorization', () => {
    bearerToken = AuthUtil.getInstance().getBearerToken(customerEmail);
    check(bearerToken, {
      'bearer token is present': (token) => Boolean(token),
    });
  });

  let orderReference;
  group('Checkout', () => {
    const checkoutResource = new CheckoutResource(idCart, customerEmail, bearerToken);
    const checkoutResponse = checkoutResource.checkout();
    check(checkoutResponse, {
      'checkout status is 2xx': (r) => r.status >= 200 && r.status < 300,
      'checkout response has order reference': (r) => Boolean(JSON.parse(r.body).data.attributes.orderReference),
    });
    orderReference = JSON.parse(checkoutResponse.body).data.attributes.orderReference;
  });

  group(testConfiguration.group, () => {
    const cartReorderResource = new CartReorderResource(orderReference, bearerToken);
    const response = cartReorderResource.reorder();
    check(response, {
      'cart reorder status is 2xx': (r) => r.status >= 200 && r.status < 300,
    });
    metrics[testConfiguration.metrics[0]].add(response.timings.duration);
  });
}
```

**Smell 4: Not using tags**

- **Lines:** [47, 53, 58, 59]
- **Snippet:**
```js
bearerToken = AuthUtil.getInstance().getBearerToken(customerEmail);
orderReference = JSON.parse(checkoutResource.checkout().body).data.attributes.orderReference;
const response = cartReorderResource.reorder();
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
export default function (data) {
  const { customerEmail, idCart } = fixture.iterateData(data);

  let bearerToken;
  group('Authorization', () => {
    bearerToken = AuthUtil.getInstance().getBearerToken(customerEmail, {
      tags: { flow: 'cart-reorder', endpoint: 'authorization' },
    });
  });

  let orderReference;
  group('Checkout', () => {
    const checkoutResource = new CheckoutResource(idCart, customerEmail, bearerToken);
    const checkoutResponse = checkoutResource.checkout({
      tags: { flow: 'cart-reorder', endpoint: 'checkout' },
    });
    orderReference = JSON.parse(checkoutResponse.body).data.attributes.orderReference;
  });

  group(testConfiguration.group, () => {
    const cartReorderResource = new CartReorderResource(orderReference, bearerToken);
    const response = cartReorderResource.reorder({
      tags: { flow: 'cart-reorder', endpoint: 'cart-reorder' },
    });
    metrics[testConfiguration.metrics[0]].add(response.timings.duration, {
      flow: 'cart-reorder',
      endpoint: 'cart-reorder',
    });
  });
}
```

### `script_158.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [53, 58]
- **Snippet:**
```js
const response = cartReorderResource.reorder();
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const response = cartReorderResource.reorder();
check(response, {
  'Reorder successful (status 201)': (r) => r.status === 201,
});
```

**Smell 4: Not using tags**

- **Lines:** [53, 58]
- **Snippet:**
```js
const response = cartReorderResource.reorder();
```
- **Refactored:**
```js
// Assuming the resource method accepts a tags parameter
const tags = { name: testConfiguration.metrics[0] }; // e.g. 'SAPI15_post_cart_reorder'
const response = cartReorderResource.reorder(tags);
```

### `script_162.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [45]
- **Snippet:**
```js
const db = sql.open('postgres', pgConnectionString)
```
- **Refactored:**
```js
// Move the database connection inside the default function or setup function to avoid opening connections in the init context for every VU
export function setup() {
  // If a single shared connection is acceptable, open it here
  // Otherwise, open inside default() per VU
}

export default () => {
  const db = sql.open('postgres', pgConnectionString)
  // ... rest of the logic
  db.close()
}
```

**Smell 3: Not checking requests**

- **Lines:** [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]
- **Snippet:**
```js
try {
  db.exec(
    'insert into positions ...'
  )
  myFailRate.add(false)
} catch (e) {
  console.log(e)
  myFailRate.add(true)
  counterFailed.add(1)
}
```
- **Refactored:**
```js
try {
  const result = db.exec(
    'insert into positions (stud_id,first_name,last_name,title,reports_to,timestamp,location,email) ' +
      `values(${name}, 'Virtual ${name}', 'User ${name}', 'Load Tester', 1, ${Date.now()}, st_point(-73.946${x}, 40.807${y}), 'vu${name}@chinookcorp.com');`
  )
  const insertSucceeded = check(result, {
    'insert affected at least one row': (r) => r && r.rowsAffected() >= 1,
  })
  myFailRate.add(!insertSucceeded)
} catch (e) {
  console.log(e)
  check(null, { 'insert did not throw': () => false })
  myFailRate.add(true)
  counterFailed.add(1)
}
```

**Smell 4: Not using tags**

- **Lines:** [58, 59, 60, 61]
- **Snippet:**
```js
db.exec(
  'insert into positions (stud_id,first_name,last_name,title,reports_to,timestamp,location,email) ' +
    `values(${name}, 'Virtual ${name}', 'User ${name}', 'Load Tester', 1, ${Date.now()}, st_point(-73.946${x}, 40.807${y}), 'vu${name}@chinookcorp.com');`
)
```
- **Refactored:**
```js
// Use k6 tags via exec context or group tagging to annotate metrics with meaningful labels
import { tagWithCurrentStageIndex } from 'k6/execution'

// Wrap the operation in a group with a descriptive name and apply tags using k6 built-in mechanisms
group('pg_insert_position', () => {
  const tags = { operation: 'insert', table: 'positions', vu: String(name) }
  const exStart = new Date()
  try {
    db.exec(
      'insert into positions (stud_id,first_name,last_name,title,reports_to,timestamp,location,email) ' +
        `values(${name}, 'Virtual ${name}', 'User ${name}', 'Load Tester', 1, ${Date.now()}, st_point(-73.946${x}, 40.807${y}), 'vu${name}@chinookcorp.com');`
    )
    myFailRate.add(false, tags)
  } catch (e) {
    console.log(e)
    myFailRate.add(true, tags)
    counterFailed.add(1, tags)
  }
  const exFinish = new Date()
  counterInserts.add(1, tags)
  insertTrend.add(exFinish - exStart, tags)
})
```

### `script_162.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [62, 65, 66, 69, 70]
- **Snippet:**
```js
myFailRate.add(false)
myFailRate.add(true)
counterFailed.add(1)
counterInserts.add(1)
insertTrend.add(exFinish - exStart)
```
- **Refactored:**
```js
const tags = { operation: 'insert_position', scenario: 'pg_single_insert' }

try {
  db.exec(
    'insert into positions (stud_id,first_name,last_name,title,reports_to,timestamp,location,email) ' +
      `values(${name}, 'Virtual ${name}', 'User ${name}', 'Load Tester', 1, ${Date.now()}, st_point(-73.946${x}, 40.807${y}), 'vu${name}@chinookcorp.com');`
  )
  myFailRate.add(false, tags)
} catch (e) {
  console.log(e)
  myFailRate.add(true, tags)
  counterFailed.add(1, tags)
}

counterInserts.add(1, tags)
insertTrend.add(exFinish - exStart, tags)
```

### `script_162.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [62, 65, 66, 69, 70]
- **Snippet:**
```js
myFailRate.add(false)
// ...
myFailRate.add(true)
counterFailed.add(1)
// ...
counterInserts.add(1)
insertTrend.add(exFinish - exStart)
```
- **Refactored:**
```js
const tags = { query: 'positions_insert' };
try {
  db.exec(
    'insert into positions (stud_id,first_name,last_name,title,reports_to,timestamp,location,email) ' +
      `values(${name}, 'Virtual ${name}', 'User ${name}', 'Load Tester', 1, ${Date.now()}, st_point(-73.946${x}, 40.807${y}), 'vu${name}@chinookcorp.com');`
  )
  myFailRate.add(false, tags)
} catch (e) {
  console.log(e)
  myFailRate.add(true, tags)
  counterFailed.add(1, tags)
}
const exFinish = new Date()
counterInserts.add(1, tags)
insertTrend.add(exFinish - exStart, tags)
```

### `script_176.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [63, 64, 65, 66]
- **Snippet:**
```js
db.exec(
  'insert into positions (stud_id,first_name,last_name,title,reports_to,timestamp,location,email) ' +
    `values(${name}, 'Virtual ${name}', 'User ${name}', 'Load Tester', 1, ${Date.now()}, st_point(-73.946${x}, 40.807${y}), 'vu${name}@chinookcorp.com');`
)
```
- **Refactored:**
```js
db.exec(
  'insert into positions (stud_id,first_name,last_name,title,reports_to,timestamp,location,email) ' +
    `values(${name}, 'Virtual ${name}', 'User ${name}', 'Load Tester', 1, ${Date.now()}, st_point(-73.946${x}, 40.807${y}), 'vu${name}@chinookcorp.com');`,
  { tags: { operation: 'insert_position', table: 'positions' } }
)
```

### `script_176.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [67, 70, 71, 74, 75]
- **Snippet:**
```js
      try {
        db.exec(
          'insert into positions (stud_id,first_name,last_name,title,reports_to,timestamp,location,email) ' +
            `values(${name}, 'Virtual ${name}', 'User ${name}', 'Load Tester', 1, ${Date.now()}, st_point(-73.946${x}, 40.807${y}), 'vu${name}@chinookcorp.com');`
        )
        myFailRate.add(false)
      } catch (e) {
        console.log(e)
        myFailRate.add(true)
        counterFailed.add(1)
      }
      const exFinish = new Date()
      counterInserts.add(1)
      insertTrend.add(exFinish - exStart)
```
- **Refactored:**
```js
      const tags = { name: 'insert_positions' };
      try {
        db.exec(
          'insert into positions (stud_id,first_name,last_name,title,reports_to,timestamp,location,email) ' +
            `values(${name}, 'Virtual ${name}', 'User ${name}', 'Load Tester', 1, ${Date.now()}, st_point(-73.946${x}, 40.807${y}), 'vu${name}@chinookcorp.com');`
        );
        myFailRate.add(false, tags);
      } catch (e) {
        console.log(e);
        myFailRate.add(true, tags);
        counterFailed.add(1, tags);
      }
      const exFinish = new Date();
      counterInserts.add(1, tags);
      insertTrend.add(exFinish - exStart, tags);
```

### `script_180.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
export let options = {
  ...test_options,
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

### `script_180.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
export let options = {
  ...test_options,
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
    'checks': ['rate>0.99'],
  },
};
```

### `script_183.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [73, 80, 88, 93, 100]
- **Snippet:**
```js
const response = checkoutResource.checkout();
const responseJson = JSON.parse(response.body);
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const response = checkoutResource.checkout();
check(response, {
  'Checkout was successful': (r) => r.status >= 200 && r.status < 300,
});
const responseJson = JSON.parse(response.body);
```

**Smell 4: Not using tags**

- **Lines:** [82, 89, 101]
- **Snippet:**
```js
metrics['SAPI16_post_cart_reorder'].add(response.timings.duration);
```
- **Refactored:**
```js
metrics['SAPI16_post_cart_reorder'].add(response.timings.duration, {
  name: 'Start Order Amendment',
});
```

### `script_19.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [110, 111, 112, 113, 114, 115, 116]
- **Snippet:**
```js
const binFile = open('zh.wav', 'b');
const paddledata = {
  audio: encoding.b64encode(binFile),
  audio_format: "wav",
  sample_rate: 16000,
  lang: "zh_cn",
}
```
- **Refactored:**
```js
// Keep file open in init context (this is correct), but avoid heavy encoding per VU if possible.
// If the file is large, consider pre-encoding it offline and storing the result.
// If encoding must stay here, ensure the file is as small as needed.
const binFile = open('zh.wav', 'b');
// encoding.b64encode is a heavy operation on large binary files;
// move encoding inside the function only if dynamic per-iteration variation is needed,
// otherwise keeping it in init is acceptable but be aware of the cost per VU.
const paddledata = {
  audio: encoding.b64encode(binFile),
  audio_format: 'wav',
  sample_rate: 16000,
  lang: 'zh_cn',
};
```

**Smell 3: Not checking requests**

- **Lines:** [128, 132, 136, 140, 144]
- **Snippet:**
```js
export function shufflenet() {
  http.get(shufflenet_model.url);
}
export function squeezenet() {
  http.get(squeezenet_model.url);
}
export function mobilenet() {
  http.get(mobilenet_model.url);
}
export function bert() {
  http.get(bertsquad_model.url);
}
export function paddle() {
  http.post(paddle_model.url, paddle_model.body, paddle_model.params)
}
```
- **Refactored:**
```js
import { check } from 'k6';

export function shufflenet() {
  const res = http.get(shufflenet_model.url);
  check(res, { 'shufflenet status 200': (r) => r.status === 200 });
}

export function squeezenet() {
  const res = http.get(squeezenet_model.url);
  check(res, { 'squeezenet status 200': (r) => r.status === 200 });
}

export function mobilenet() {
  const res = http.get(mobilenet_model.url);
  check(res, { 'mobilenet status 200': (r) => r.status === 200 });
}

export function bert() {
  const res = http.get(bertsquad_model.url);
  check(res, { 'bert status 200': (r) => r.status === 200 });
}

export function paddle() {
  const res = http.post(paddle_model.url, paddle_model.body, paddle_model.params);
  check(res, { 'paddle status 200': (r) => r.status === 200 });
}
```

### `script_19.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [110, 112, 120]
- **Snippet:**
```js
const binFile = open('zh.wav', 'b');
const paddledata = {
  audio: encoding.b64encode(binFile),
  ...
}
...
body: JSON.stringify(paddledata),
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

const paddleBodies = new SharedArray('paddle request body', () => {
  const binFile = open('zh.wav', 'b');
  return [JSON.stringify({
    audio: encoding.b64encode(binFile),
    audio_format: 'wav',
    sample_rate: 16000,
    lang: 'zh_cn',
  })];
});

let paddle_model = {
  method: 'POST',
  url: 'http://10.106.46.112:8080/function/paddlespeech/paddlespeech/asr',
  body: paddleBodies[0],
  params: {
    headers: { 'Content-Type': 'application/json' },
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [128, 132, 136, 140, 144]
- **Snippet:**
```js
export function shufflenet() {
  http.get(shufflenet_model.url);
}
...
export function paddle() {
  http.post(paddle_model.url, paddle_model.body, paddle_model.params)
}
```
- **Refactored:**
```js
import { check } from 'k6';

export function shufflenet() {
  const res = http.get(shufflenet_model.url);
  check(res, { 'shufflenet status is 200': (r) => r.status === 200 });
}

export function squeezenet() {
  const res = http.get(squeezenet_model.url);
  check(res, { 'squeezenet status is 200': (r) => r.status === 200 });
}

export function mobilenet() {
  const res = http.get(mobilenet_model.url);
  check(res, { 'mobilenet status is 200': (r) => r.status === 200 });
}

export function bert() {
  const res = http.get(bertsquad_model.url);
  check(res, { 'bert status is 200': (r) => r.status === 200 });
}

export function paddle() {
  const res = http.post(paddle_model.url, paddle_model.body, paddle_model.params);
  check(res, { 'paddle status is 200': (r) => r.status === 200 });
}
```

### `script_19.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124]
- **Snippet:**
```js
const binFile = open('zh.wav', 'b');
const paddledata = {
  audio: encoding.b64encode(binFile),
  //...
}
let paddle_model = {
  //...
  body: JSON.stringify(paddledata),
  //...
};
```
- **Refactored:**
```js
// Use the setup lifecycle function to prepare data once for the entire test run.
export function setup() {
  const binFile = open('zh.wav', 'b');
  const paddledata = {
    audio: encoding.b64encode(binFile),
    audio_format: "wav",
    sample_rate: 16000,
    lang: "zh_cn",
  };
  return { paddle_body: JSON.stringify(paddledata) };
}

// The paddle function now receives the pre-processed data from the setup function.
export function paddle(data) {
  const paddle_url = 'http://10.106.46.112:8080/function/paddlespeech/paddlespeech/asr';
  const paddle_params = {
      headers: { 'Content-Type': 'application/json'},
  };
  http.post(paddle_url, data.paddle_body, paddle_params);
}
```

**Smell 3: Not checking requests**

- **Lines:** [128, 132, 136, 140, 144]
- **Snippet:**
```js
export function shufflenet() {
  http.get(shufflenet_model.url);
}
```
- **Refactored:**
```js
import http from 'k6/http';
import { check } from 'k6';

// This refactoring pattern should be applied to all request functions 
// (squeezenet, mobilenet, bert, paddle).
export function shufflenet() {
  const res = http.get(shufflenet_model.url);
  check(res, {
    'shufflenet response status is 200': (r) => r.status === 200,
  });
}
```

### `script_194.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [33, 34, 35, 36]
- **Snippet:**
```js
export const options = {
  duration: `${baseDuration}s`,
  vus: virtualUsers,
}
```
- **Refactored:**
```js
export const options = {
  duration: `${baseDuration}s`,
  vus: virtualUsers,
  thresholds: {
    'inserts': ['count>0'],
    'iteration_duration': ['p(95)<2000'],
  },
}
```

**Smell 3: Not checking requests**

- **Lines:** [66, 67, 68, 69, 70, 71]
- **Snippet:**
```js
db.exec(
    `insert into load_messages(room_id) values('room${getRandomInt(
      0,
      rooms
    )}');`
  )
```
- **Refactored:**
```js
import { check } from 'k6';

// inside default function:
try {
  db.exec(
    `insert into load_messages(room_id) values('room${getRandomInt(0, rooms)}');`
  );
  check(true, { 'insert succeeded': (val) => val === true });
} catch (e) {
  check(false, { 'insert succeeded': (val) => val === true });
  console.error(`Insert failed: ${e}`);
}
```

**Smell 4: Not using tags**

- **Lines:** [66, 67, 68, 69, 70, 71, 73]
- **Snippet:**
```js
db.exec(
    `insert into load_messages(room_id) values('room${getRandomInt(
      0,
      rooms
    )}');`
  )
  ...
  counterInserts.add(1)
```
- **Refactored:**
```js
db.exec(
    `insert into load_messages(room_id) values('room${getRandomInt(0, rooms)}');`,
  );
  counterInserts.add(1, { operation: 'insert', table: 'load_messages' });
```

### `script_194.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [33, 34, 35, 36]
- **Snippet:**
```js
export const options = {
  duration: `${baseDuration}s`,
  vus: virtualUsers,
}
```
- **Refactored:**
```js
export const options = {
  duration: `${baseDuration}s`,
  vus: virtualUsers,
  thresholds: {
    'iteration_duration': ['p(95)<500'], // 95% of iterations must be below 500ms
    'inserts': ['count>0'], // Ensure at least some inserts were successful
  },
}
```

**Smell 3: Not checking requests**

- **Lines:** [66, 67, 68, 69, 70, 71]
- **Snippet:**
```js
db.exec(
  `insert into load_messages(room_id) values('room${getRandomInt(
    0,
    rooms
  )}');`
)
```
- **Refactored:**
```js
import { check } from 'k6';

// ... inside default function
const room = `room${getRandomInt(0, rooms)}`;
check(null, {
  'insert was successful': () => {
    try {
      db.exec(`insert into load_messages(room_id) values('${room}');`);
      return true;
    } catch (e) {
      console.error(`Insert failed: ${e}`);
      return false;
    }
  },
});
```

**Smell 4: Not using tags**

- **Lines:** [73]
- **Snippet:**
```js
counterInserts.add(1)
```
- **Refactored:**
```js
// ... inside default function, after generating a random room_id
const room = `room${getRandomInt(0, rooms)}`;
db.exec(`insert into load_messages(room_id) values('${room}');`)

// ... later in the function
counterInserts.add(1, { room_id: room });
```

### `script_201.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
export let options = {
  ...test_options,
  thresholds: {
    'http_req_failed': ['rate<0.01'], // fail if more than 1% of requests fail
    'http_req_duration': ['p(95)<500'], // 95th percentile response time is > 500ms
  },
};
```

### `script_205.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [39, 40, 41, 42]
- **Snippet:**
```js
export const options = {
  duration: `${baseDuration}s`,
  vus: virtualUsers,
}
```
- **Refactored:**
```js
export const options = {
  duration: `${baseDuration}s`,
  vus: virtualUsers,
  thresholds: {
    'inserts': ['count>0'],
  },
}
```

**Smell 3: Not checking requests**

- **Lines:** [59, 60, 61, 62, 63]
- **Snippet:**
```js
db.exec(
    `insert into rls_messages (domain) values ('${
      domains[getRandomInt(0, 5)]
    }');`
  )
```
- **Refactored:**
```js
import { check } from 'k6';

// Inside the default function:
try {
  db.exec(
    `insert into rls_messages (domain) values ('${
      domains[getRandomInt(0, 5)]
    }');`
  );
  check(true, { 'insert succeeded': (v) => v === true });
} catch (e) {
  check(false, { 'insert succeeded': (v) => v === true });
  console.error(`Insert failed: ${e}`);
}
```

**Smell 4: Not using tags**

- **Lines:** [59, 60, 61, 62, 63]
- **Snippet:**
```js
db.exec(
    `insert into rls_messages (domain) values ('${
      domains[getRandomInt(0, 5)]
    }');`
  )
```
- **Refactored:**
```js
// Tag the metric counter and use tagged grouping for the db operation
import { group } from 'k6';

group('db_insert', function () {
  const start = new Date();
  db.exec(
    `insert into rls_messages (domain) values ('${
      domains[getRandomInt(0, 5)]
    }');`
  );
  const finish = new Date();
  counterInserts.add(1, { operation: 'insert', table: 'rls_messages' });
});
```

### `script_205.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [22]
- **Snippet:**
```js
const db = sql.open('postgres', pdConnectionString)
```
- **Refactored:**
```js
/*
 The database connection pool should be created only once for the entire test, not once per Virtual User. Move the connection logic to the setup() function.
*/
export function setup() {
  const db = sql.open('postgres', pdConnectionString);
  return { db: db };
}

/*
 The default function and teardown will then receive the connection object via the 'data' parameter.
*/
export default function(data) {
  // use data.db instead of the global db
}

export function teardown(data) {
  data.db.close();
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [39, 40, 41, 42]
- **Snippet:**
```js
export const options = {
  duration: `${baseDuration}s`,
  vus: virtualUsers,
}
```
- **Refactored:**
```js
export const options = {
  duration: `${baseDuration}s`,
  vus: virtualUsers,
  thresholds: {
    // Example: Fail the test if the insert rate is less than the target rate.
    'inserts': [`rate>${rate}`],
    // Example: Fail the test if more than 1% of checks fail.
    'checks': ['rate>0.99'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [59, 60, 61, 62, 63]
- **Snippet:**
```js
db.exec(
    `insert into rls_messages (domain) values ('${
      domains[getRandomInt(0, 5)]
    }');`
  )
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const domainToInsert = domains[getRandomInt(0, 5)];
const query = `insert into rls_messages (domain) values ('${domainToInsert}');`;

// Use a check to validate that the database operation was successful.
// The xk6-sql extension will throw an exception on failure.
check(null, {
  'insert was successful': () => {
    try {
      db.exec(query);
      return true;
    } catch (e) {
      return false;
    }
  },
});
```

**Smell 4: Not using tags**

- **Lines:** [65]
- **Snippet:**
```js
counterInserts.add(1)
```
- **Refactored:**
```js
// Store the domain in a variable to reuse it for tagging.
const domainToInsert = domains[getRandomInt(0, 5)];

// ... perform the db.exec with domainToInsert ...

// Add a tag to the metric to allow for more granular analysis.
counterInserts.add(1, { domain: domainToInsert });
```

### `script_210.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
export let options = {
  ...test_options, // Preserve existing options from the import
  thresholds: {
    'http_req_failed': ['rate<0.01'], // Fail test if more than 1% of requests fail
    'http_req_duration{name:GET}': ['p(95)<500'], // 95th percentile response time for 'GET' requests must be below 500ms
    'checks': ['rate>0.99'], // More than 99% of checks must pass
  },
};
```

### `script_213.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
export const options = {
  ...test_options,
  thresholds: {
    ...(test_options.thresholds || {}),
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

### `script_213.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
export let options = {
  ...test_options, // Keep existing options
  thresholds: {
    'http_req_failed': ['rate<0.01'], // <1% errors
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    'checks': ['rate>0.99'], // >99% of checks must pass
  },
};
```

### `script_224.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [36, 38]
- **Snippet:**
```js
const response = concreteProductsResource.get(product.sku);

    metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
import { check } from 'k6';

// inside the group:
const response = concreteProductsResource.get(product.sku);

check(response, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```

**Smell 4: Not using tags**

- **Lines:** [36]
- **Snippet:**
```js
const response = concreteProductsResource.get(product.sku);
```
- **Refactored:**
```js
const response = concreteProductsResource.get(product.sku, {
  tags: { name: 'get_concrete_products', group: testConfiguration.group, endpoint: `/concrete-products/${product.sku}` },
});
```

### `script_224.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [36]
- **Snippet:**
```js
const response = concreteProductsResource.get(product.sku);
```
- **Refactored:**
```js
import { group, check } from 'k6';

export default function (data) {
  const product = fixture.iterateData(data);

  group(testConfiguration.group, () => {
    const concreteProductsResource = new ConcreteProductsResource();
    const response = concreteProductsResource.get(product.sku);

    check(response, {
      'get concrete products status is 200': (r) => r.status === 200,
    });

    metrics[testConfiguration.metrics[0]].add(response.timings.duration);
  });
}
```

**Smell 4: Not using tags**

- **Lines:** [36, 38]
- **Snippet:**
```js
const response = concreteProductsResource.get(product.sku);
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
export default function (data) {
  const product = fixture.iterateData(data);
  const tags = {
    api: testConfiguration.id,
    endpoint: 'get_concrete_products',
    flow: testConfiguration.group,
  };

  group(testConfiguration.group, () => {
    const concreteProductsResource = new ConcreteProductsResource();
    const response = concreteProductsResource.get(product.sku, { tags });

    metrics[testConfiguration.metrics[0]].add(response.timings.duration, tags);
  });
}
```

### `script_227.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9]
- **Snippet:**
```js
export let options = {
  vus: 10,
  duration: '30s',
};
```
- **Refactored:**
```js
export let options = {
  vus: 10,
  duration: '30s',
  thresholds: {
    http_req_failed: ['rate<0.01'],      // less than 1% of requests should fail
    http_req_duration: ['p(95)<500'],    // 95% of requests should complete within 500ms
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
const res = http.get('http://api:3000/');
```
- **Refactored:**
```js
const res = http.get('http://api:3000/', {
  tags: { name: 'homepage', endpoint: '/' },
});
```

### `script_227.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9]
- **Snippet:**
```js
export let options = {
  vus: 10,
  duration: '30s',
};
```
- **Refactored:**
```js
export let options = {
  vus: 10,
  duration: '30s',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
const res = http.get('http://api:3000/');
```
- **Refactored:**
```js
const res = http.get('http://api:3000/', {
  tags: {
    endpoint: 'root',
    flow: 'homepage',
  },
});
check(res, {
  'status is 200': (r) => r.status === 200,
}, {
  endpoint: 'root',
  flow: 'homepage',
});
```

### `script_227.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9]
- **Snippet:**
```js
export let options = {
  vus: 10,         // 10 virtual users
  duration: '30s', // for 30 seconds
};
```
- **Refactored:**
```js
export let options = {
  vus: 10,
  duration: '30s',
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<200'], // 95% of requests should be below 200ms
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
const res = http.get('http://api:3000/');
```
- **Refactored:**
```js
const res = http.get('http://api:3000/', {
  tags: { name: 'Homepage' },
});
```

### `script_229.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
    vus: 100,
    duration: '30s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 100,
    duration: '30s',
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
        'checks': ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [10]
- **Snippet:**
```js
let res = http.get('http://localhost:3000/endpoint');
```
- **Refactored:**
```js
let res = http.get('http://localhost:3000/endpoint', { tags: { name: 'endpoint', endpoint: '/endpoint' } });
```

### `script_229.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
    vus: 100,
    duration: '30s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 100,
    duration: '30s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [10, 12]
- **Snippet:**
```js
let res = http.get('http://localhost:3000/endpoint');
check(res, {'status was 200': (r) => r.status === 200});
```
- **Refactored:**
```js
let res = http.get('http://localhost:3000/endpoint', {
    tags: { endpoint: 'endpoint', flow: 'default' },
});
check(res, { 'status was 200': (r) => r.status === 200 }, {
    endpoint: 'endpoint',
    flow: 'default',
});
```

### `script_229.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
    vus: 100, // 100 users looping during 30 seconds
    duration: '30s', // duration of the test is 30 seconds
};
```
- **Refactored:**
```js
export let options = {
    vus: 100,
    duration: '30s',
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should complete below 500ms
        'checks': ['rate>0.99'], // 99% of checks must pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [10]
- **Snippet:**
```js
let res = http.get('http://localhost:3000/endpoint');
```
- **Refactored:**
```js
let res = http.get('http://localhost:3000/endpoint', { tags: { name: 'GetEndpoint' } });
```

### `script_23.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [37]
- **Snippet:**
```js
file: http.file('D:/Document/Semester 8/SQA/swagger-petstore-sqa/pet_s3/cat.jpeg'),
```
- **Refactored:**
```js
// Move the file read to the init context (outside default function)
const fileData = open('D:/Document/Semester 8/SQA/swagger-petstore-sqa/pet_s3/cat.jpeg', 'b');

export default function () {
  let baseUrl = 'https://petstore.swagger.io/v2/pet';
  const petId = __VU;
  const url = `${baseUrl}/${petId}/uploadImage`;

  const payload = {
    file: http.file(fileData, 'cat.jpeg', 'image/jpeg'),
    additionalMetadata: `Metadata for pet ${petId}`,
  };
  // ... rest of function
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export let options = {
  stages: [
    { duration: '2m', target: 70 },
    { duration: '6m', target: 700 },
    { duration: '2m', target: 70 },
  ],
};
```
- **Refactored:**
```js
export let options = {
  stages: [
    { duration: '2m', target: 70 },
    { duration: '6m', target: 700 },
    { duration: '2m', target: 70 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],          // Less than 1% of requests should fail
    http_req_duration: ['p(95)<2000'],        // 95% of requests must complete below 2s
    'checks{check:✅ Status is 200 (Success)}': ['rate>0.95'], // 95%+ should be successful
    total_failures: ['count<10'],             // Total failures should be minimal
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [44]
- **Snippet:**
```js
res = http.post(url, payload);
```
- **Refactored:**
```js
res = http.post(url, payload, {
  tags: {
    name: 'uploadPetImage',
    endpoint: '/pet/:id/uploadImage',
    flow: 'pet_image_upload',
  },
});
```

### `script_23.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export let options = {
  stages: [
    { duration: '2m', target: 70 },
    { duration: '6m', target: 700 },
    { duration: '2m', target: 70 },
  ],
};
```
- **Refactored:**
```js
export let options = {
  stages: [
    { duration: '2m', target: 70 },
    { duration: '6m', target: 700 },
    { duration: '2m', target: 70 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.05'],
    http_req_duration: ['p(95)<1000'],
    total_failures: ['count<10'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [44, 72]
- **Snippet:**
```js
res = http.post(url, payload);

check(res, {
  '✅ Status is 200 (Success)': (r) => {
    let result = r.status === 200;
    if (result) checkSuccess.add(1);
    return result;
  },
});
```
- **Refactored:**
```js
const tags = {
  endpoint: 'uploadImage',
  flow: 'pet_image_upload',
  method: 'POST',
};

const params = { tags };
res = http.post(url, payload, params);

check(res, {
  '✅ Status is 200 (Success)': (r) => {
    let result = r.status === 200;
    if (result) checkSuccess.add(1, tags);
    return result;
  },
}, tags);
```

### `script_23.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 11]
- **Snippet:**
```js
export let options = {
  stages: [
    { duration: '2m', target: 70 },  // Load normal
    { duration: '6m', target: 700 }, // Lonjakan (simulasi kegagalan)
    { duration: '2m', target: 70 },  // Pemulihan (cek kapan kembali ke normal)
  ],
};
```
- **Refactored:**
```js
export let options = {
  stages: [
    { duration: '2m', target: 70 },  // Load normal
    { duration: '6m', target: 700 }, // Lonjakan (simulasi kegagalan)
    { duration: '2m', target: 70 },  // Pemulihan (cek kapan kembali ke normal)
  ],
  thresholds: {
    'http_req_failed': ['rate<0.01'], // less than 1% of requests should fail
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks{✅ Status is 200 (Success)}': ['rate>0.95'] // over 95% of checks for 200 status should pass
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [44]
- **Snippet:**
```js
res = http.post(url, payload);
```
- **Refactored:**
```js
const params = {
  tags: { name: 'UploadPetImage' },
};
res = http.post(url, payload, params);
```

### `script_230.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
export let options = {
  ...test_options, // Keep existing options from ./options.js
  thresholds: {
    'http_req_failed': ['rate<0.01'], // less than 1% of requests should fail
    'http_req_duration': ['p(95)<500'], // 95th percentile of request duration must be below 500ms
  },
};
```

### `script_231.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [14, 15]
- **Snippet:**
```js
const res = http.get('https://quickpizza.grafana.com');
GaugeContentSize.add(res.body.length);
```
- **Refactored:**
```js
import { check } from 'k6';

const res = http.get('https://quickpizza.grafana.com');
check(res, {
  'status is 200': (r) => r.status === 200,
  'body is not empty': (r) => r.body && r.body.length > 0,
});
GaugeContentSize.add(res.body.length);
```

**Smell 4: Not using tags**

- **Lines:** [14]
- **Snippet:**
```js
const res = http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
const res = http.get('https://quickpizza.grafana.com', { tags: { name: 'QuickPizzaHome', endpoint: '/' } });
```

### `script_231.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [14]
- **Snippet:**
```js
const res = http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default function () {
  const res = http.get('https://quickpizza.grafana.com');
  check(res, {
    'status is 200': (r) => r.status === 200,
    'body is not empty': (r) => r.body && r.body.length > 0,
  });
  GaugeContentSize.add(res.body.length);
  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [14, 15]
- **Snippet:**
```js
const res = http.get('https://quickpizza.grafana.com');
GaugeContentSize.add(res.body.length);
```
- **Refactored:**
```js
export default function () {
  const tags = { endpoint: 'home', flow: 'quickpizza_homepage' };
  const res = http.get('https://quickpizza.grafana.com', { tags });
  GaugeContentSize.add(res.body.length, tags);
  sleep(1);
}
```

### `script_231.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [14]
- **Snippet:**
```js
const res = http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
import http from 'k6/http';
import { sleep, check } from 'k6';
// ...

export default function () {
  const res = http.get('https://quickpizza.grafana.com');
  check(res, { 'status was 200': (r) => r.status == 200 });
  GaugeContentSize.add(res.body.length);
  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [14]
- **Snippet:**
```js
const res = http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
const res = http.get('https://quickpizza.grafana.com', {
  tags: { name: 'Homepage' },
});
```

### `script_232.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10]
- **Snippet:**
```js
export let options = {
  stages: [
    { duration: '30s', target: 10 },
    { duration: '1m', target: 50 },
    { duration: '30s', target: 0 },
  ],
};
```
- **Refactored:**
```js
export let options = {
  stages: [
    { duration: '30s', target: 10 },
    { duration: '1m', target: 50 },
    { duration: '30s', target: 0 },
  ],
  thresholds: {
    'http_req_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
    'checks': ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [13]
- **Snippet:**
```js
let res = http.get('https://www.cruzeiro.com.br/');
```
- **Refactored:**
```js
let res = http.get('https://www.cruzeiro.com.br/', {
  tags: { name: 'homepage', endpoint: '/' },
});
```

### `script_232.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10]
- **Snippet:**
```js
export let options = {
  stages: [
    { duration: '30s', target: 10 },
    { duration: '1m', target: 50 },
    { duration: '30s', target: 0 },
  ],
};
```
- **Refactored:**
```js
export let options = {
  stages: [
    { duration: '30s', target: 10 },
    { duration: '1m', target: 50 },
    { duration: '30s', target: 0 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [13, 14, 15, 16, 17]
- **Snippet:**
```js
let res = http.get('https://www.cruzeiro.com.br/');
check(res, {
  'status foi 200': (r) => r.status === 200,
  'tempo de resposta foi menor que 500ms': (r) => r.timings.duration < 500,
});
```
- **Refactored:**
```js
const tags = { endpoint: 'home', flow: 'homepage' };
let res = http.get('https://www.cruzeiro.com.br/', { tags });
check(res, {
  'status foi 200': (r) => r.status === 200,
  'tempo de resposta foi menor que 500ms': (r) => r.timings.duration < 500,
}, tags);
```

### `script_232.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10]
- **Snippet:**
```js
export let options = {
  stages: [
    { duration: '30s', target: 10 }, 
    { duration: '1m', target: 50 },  
    { duration: '30s', target: 0 },  
  ],
};
```
- **Refactored:**
```js
export let options = {
  stages: [
    { duration: '30s', target: 10 }, 
    { duration: '1m', target: 50 },  
    { duration: '30s', target: 0 },  
  ],
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [13]
- **Snippet:**
```js
let res = http.get('https://www.cruzeiro.com.br/');
```
- **Refactored:**
```js
let res = http.get('https://www.cruzeiro.com.br/', {
    tags: { name: 'Homepage' },
  });
```

### `script_233.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
import { test_options } from './options.js';

export let options = {
  ...test_options, // Keep existing options from the import
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration{name:GET}': ['p(95)<200'], // 95% of tagged requests should be below 200ms
    'checks': ['rate>0.99'], // 99% of checks should pass
  },
};
```

### `script_234.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 32]
- **Snippet:**
```js
export default function () { ... }
```
- **Refactored:**
```js
export const options = {
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
    },
};

export default function () { ... }
```

**Smell 3: Not checking requests**

- **Lines:** [25, 29, 30, 31]
- **Snippet:**
```js
const responses = http.batch(request);
// check(responses[2], {
//     'form data OK': (res) => JSON.parse(res.body)['form']['hello'] == 'world!',
// });
```
- **Refactored:**
```js
const responses = http.batch(request);
responses.forEach((res, index) => {
    check(res, {
        [`response ${index} status is 200`]: (r) => r.status === 200,
        [`response ${index} body is not empty`]: (r) => r.body && r.body.length > 0,
    });
});
```

**Smell 4: Not using tags**

- **Lines:** [15, 16, 17, 18, 19, 20, 21]
- **Snippet:**
```js
request.push({
    method: 'GET',
    url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
    params: params
});
```
- **Refactored:**
```js
request.push({
    method: 'GET',
    url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
    params: {
        ...params,
        tags: { name: 'user_search', endpoint: '/user/search' },
    },
});
```

### `script_234.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [1, 32]
- **Snippet:**
```js
No export const options with thresholds is defined in the script.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [25, 29, 30, 31]
- **Snippet:**
```js
const responses = http.batch(request);

// check(responses[2], {
//     'form data OK': (res) => JSON.parse(res.body)['form']['hello'] == 'world!',
// });
```
- **Refactored:**
```js
const responses = http.batch(request);

responses.forEach((res) => {
  check(res, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
  });
});
```

**Smell 4: Not using tags**

- **Lines:** [4, 5, 6, 7, 8, 19]
- **Snippet:**
```js
const params = {
    headers: {
        'Authorization': 'Bearer ...',
    },
};
...
params: params
```
- **Refactored:**
```js
const params = {
  headers: {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTI3OCwibmJmIjoxNzA0MTEwNDAwfQ.GP6RzCN4Z1bf_G3E_G2CsnA3QD4iq1YDLSvmVl7VySU',
  },
  tags: {
    endpoint: 'user_search',
    flow: 'search_user',
  },
};

request.push({
  method: 'GET',
  url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
  params: params,
});
```

### `script_234.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1]
- **Snippet:**
```js
import http from 'k6/http';
```
- **Refactored:**
```js
import http from 'k6/http';

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [25]
- **Snippet:**
```js
const responses = http.batch(request);
```
- **Refactored:**
```js
const responses = http.batch(request);

    responses.forEach(res => {
        check(res, {
            'status is 200': (r) => r.status === 200,
        });
    });
```

**Smell 4: Not using tags**

- **Lines:** [16, 17, 18, 19, 20]
- **Snippet:**
```js
request.push({
            method: 'GET',
            url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
            params: params
        });
```
- **Refactored:**
```js
request.push({
            method: 'GET',
            url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
            params: {
                ...params,
                tags: { name: 'UserSearch' },
            },
        });
```

### `script_235.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
- **Snippet:**
```js
export const options = {
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '30s',
      preAllocatedVUs: 50,
      rate: 50,
      timeUnit: '1s',
    },
  },
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '30s',
      preAllocatedVUs: 50,
      rate: 50,
      timeUnit: '1s',
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    'checks': ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [23]
- **Snippet:**
```js
const res = http.post('https://httpbin.test.k6.io/post', payload, { headers });
```
- **Refactored:**
```js
const res = http.post('https://httpbin.test.k6.io/post', payload, { headers, tags: { name: 'post_lorem_ipsum', endpoint: '/post' } });
```

### `script_235.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]
- **Snippet:**
```js
export const options = {
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '30s',
      preAllocatedVUs: 50,
      rate: 50,
      timeUnit: '1s',
    },
  },
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '30s',
      preAllocatedVUs: 50,
      rate: 50,
      timeUnit: '1s',
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [23]
- **Snippet:**
```js
const res = http.post('https://httpbin.test.k6.io/post', payload, { headers });
```
- **Refactored:**
```js
const params = {
  headers,
  tags: {
    endpoint: 'httpbin_post',
    method: 'POST',
    flow: 'create_user',
  },
};

const res = http.post('https://httpbin.test.k6.io/post', payload, params);

check(res, {
  'Post status is 200': (r) => r.status === 200,
  'Post Content-Type header': (r) => r.headers['Content-Type'] === 'application/json',
  'Post response name': (r) => r.status === 200 && r.json().json.name === 'lorem',
}, { endpoint: 'httpbin_post', flow: 'create_user' });
```

### `script_235.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
- **Snippet:**
```js
export const options = {
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '30s', // total duration
      preAllocatedVUs: 50, // to allocate runtime resources

      rate: 50, // number of constant iterations given `timeUnit`
      timeUnit: '1s',
    },
  },
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '30s', // total duration
      preAllocatedVUs: 50, // to allocate runtime resources

      rate: 50, // number of constant iterations given `timeUnit`
      timeUnit: '1s',
    },
  },
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'checks': ['rate>0.99'], // 99% of checks must pass
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [23]
- **Snippet:**
```js
const res = http.post('https://httpbin.test.k6.io/post', payload, { headers });
```
- **Refactored:**
```js
const res = http.post('https://httpbin.test.k6.io/post', payload, {
    headers,
    tags: {
      name: 'CreateItem',
    },
  });
```

### `script_236.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 50,
    duration: '30s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 50,
    duration: '30s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [26, 27, 28, 29, 30, 33]
- **Snippet:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json',
    },
};

let response = http.post('http://localhost:8080/api/members', body, params);
```
- **Refactored:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json',
    },
    tags: {
        name: 'RegisterMember',
        endpoint: '/api/members',
    },
};

let response = http.post('http://localhost:8080/api/members', body, params);
```

### `script_236.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 50,
    duration: '30s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 50,
    duration: '30s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [26, 27, 28, 29, 30, 33, 36, 37, 38]
- **Snippet:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json',
    },
};
let response = http.post('http://localhost:8080/api/members', body, params);
check(response, {
    'is status 200': (r) => r.status === 200,
});
```
- **Refactored:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json',
    },
    tags: {
        endpoint: 'create_member',
        method: 'POST',
        flow: 'member_registration',
    },
};
let response = http.post('http://localhost:8080/api/members', body, params);
check(response, {
    'is status 200': (r) => r.status === 200,
}, {
    endpoint: 'create_member',
    flow: 'member_registration',
});
```

### `script_236.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 50, // 가상 사용자 수
    duration: '30s', // 테스트 지속 시간
};
```
- **Refactored:**
```js
export let options = {
    vus: 50, // 가상 사용자 수
    duration: '30s', // 테스트 지속 시간
    thresholds: {
        http_req_failed: ['rate<0.01'], // http errors should be less than 1%
        http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
        'checks': ['rate>0.99'], // 99% of checks must pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [33]
- **Snippet:**
```js
let response = http.post('http://localhost:8080/api/members', body, params);
```
- **Refactored:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json',
    },
    tags: {
        name: 'CreateMember',
    },
};
let response = http.post('http://localhost:8080/api/members', body, params);
```

### `script_237.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8]
- **Snippet:**
```js
export default function() { ... }
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};

export default function() {
  const BASE_URL = __ENV.URL
  const response = http.get(BASE_URL)
  sleep(1)
}
```

**Smell 3: Not checking requests**

- **Lines:** [6]
- **Snippet:**
```js
const response = http.get(BASE_URL)
```
- **Refactored:**
```js
import { check, sleep } from 'k6';

export default function() {
  const BASE_URL = __ENV.URL
  const response = http.get(BASE_URL)
  check(response, {
    'status is 200': (r) => r.status === 200,
  });
  sleep(1)
}
```

**Smell 4: Not using tags**

- **Lines:** [6]
- **Snippet:**
```js
const response = http.get(BASE_URL)
```
- **Refactored:**
```js
const response = http.get(BASE_URL, { tags: { name: 'homepage', endpoint: 'GET /' } })
```

### `script_237.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 4, 5, 6, 7, 8]
- **Snippet:**
```js
No export const options object with thresholds is defined in the script.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500']
  }
};
```

**Smell 3: Not checking requests**

- **Lines:** [6]
- **Snippet:**
```js
const response = http.get(BASE_URL)
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default function() {
  const BASE_URL = __ENV.URL;
  const response = http.get(BASE_URL);
  check(response, {
    'status is 200': (r) => r.status === 200
  });
  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [6]
- **Snippet:**
```js
const response = http.get(BASE_URL)
```
- **Refactored:**
```js
const response = http.get(BASE_URL, {
  tags: {
    endpoint: 'base_url',
    flow: 'homepage'
  }
});
```

### `script_237.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 4, 5, 6, 7, 8]
- **Snippet:**
```js
import http from 'k6/http'
import { sleep, sllep } from 'k6'

export default function() {
  const BASE_URL = __ENV.URL
  const response = http.get(BASE_URL)
  sleep(1)
}
```
- **Refactored:**
```js
import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95 percent of response times must be below 500ms
  },
};

export default function() {
  const BASE_URL = __ENV.URL;
  const response = http.get(BASE_URL);
  sleep(1);
}
```

**Smell 3: Not checking requests**

- **Lines:** [6]
- **Snippet:**
```js
const response = http.get(BASE_URL)
```
- **Refactored:**
```js
import http from 'k6/http';
import { sleep, check } from 'k6'; // import check

export default function() {
  const BASE_URL = __ENV.URL;
  const response = http.get(BASE_URL);
  check(response, { // add a check for the response status
    'is status 200': (r) => r.status === 200,
  });
  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [6]
- **Snippet:**
```js
const response = http.get(BASE_URL)
```
- **Refactored:**
```js
const response = http.get(BASE_URL, {
  tags: { name: 'Homepage' },
});
```

### `script_238.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [39, 41]
- **Snippet:**
```js
const response = productPage.get(product.url);

    metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
import { check } from 'k6';

const response = productPage.get(product.url);

check(response, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```

**Smell 4: Not using tags**

- **Lines:** [39, 41]
- **Snippet:**
```js
const response = productPage.get(product.url);

    metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
const response = productPage.get(product.url, { tags: { name: 'S8_get_product', group: testConfiguration.group } });

metrics[testConfiguration.metrics[0]].add(response.timings.duration, { tags: { name: 'S8_get_product', group: testConfiguration.group } });
```

### `script_238.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [26, 27, 28]
- **Snippet:**
```js
const fixture = FullProductFixture.createFixture({
  productCount: testConfiguration.vus ?? EnvironmentUtil.getRampVus(),
});
```
- **Refactored:**
```js
export function setup() {
  const fixture = FullProductFixture.createFixture({
    productCount: testConfiguration.vus ?? EnvironmentUtil.getRampVus(),
  });
  return fixture.getData();
}

export default function (data) {
  const product = data[(__VU - 1) % data.length];
  // continue test flow
}
```

**Smell 3: Not checking requests**

- **Lines:** [39]
- **Snippet:**
```js
const response = productPage.get(product.url);
```
- **Refactored:**
```js
import { group, check } from 'k6';

const response = productPage.get(product.url);
check(response, {
  'product page status is 200': (r) => r.status === 200,
  'product page body is not empty': (r) => !!r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [39, 41]
- **Snippet:**
```js
const response = productPage.get(product.url);

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
const tags = {
  test_id: testConfiguration.id,
  group: testConfiguration.group,
  endpoint: 'get_product',
};

const response = productPage.get(product.url, { tags });
metrics[testConfiguration.metrics[0]].add(response.timings.duration, tags);
```

### `script_238.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [26, 27, 28]
- **Snippet:**
```js
const fixture = FullProductFixture.createFixture({
  productCount: testConfiguration.vus ?? EnvironmentUtil.getRampVus(),
});
```
- **Refactored:**
```js
// Fixture creation should be moved to the setup function to run only once per test, not per VU.
export function setup() {
  const fixture = FullProductFixture.createFixture({
    productCount: testConfiguration.vus ?? EnvironmentUtil.getRampVus(),
  });
  return fixture.getData();
}
// Note: The default function must be adapted to use the data array from setup.
```

**Smell 3: Not checking requests**

- **Lines:** [39]
- **Snippet:**
```js
const response = productPage.get(product.url);
```
- **Refactored:**
```js
// The 'check' function from the 'k6' module should be imported.
const response = productPage.get(product.url);
check(response, {
  'Product page status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [41]
- **Snippet:**
```js
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
const tags = { product_url: product.url };
metrics[testConfiguration.metrics[0]].add(response.timings.duration, tags);
```

### `script_239.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- **Snippet:**
```js
export default function(){
    const res = http.get(__ENV.URL);
    sleep(1);
}
```
- **Refactored:**
```js
import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};

export default function(){
    const res = http.get(__ENV.URL);
    sleep(1);
}
```

**Smell 3: Not checking requests**

- **Lines:** [7]
- **Snippet:**
```js
const res = http.get(__ENV.URL);
```
- **Refactored:**
```js
import { check } from 'k6';

const res = http.get(__ENV.URL);
check(res, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [7]
- **Snippet:**
```js
const res = http.get(__ENV.URL);
```
- **Refactored:**
```js
const res = http.get(__ENV.URL, { tags: { name: 'MainEndpoint', endpoint: 'GET /' } });
```

### `script_239.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 5]
- **Snippet:**
```js
import http from 'k6/http';
import { sleep } from 'k6';

export default function(){
```
- **Refactored:**
```js
import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500']
  }
};

export default function() {
  const res = http.get(__ENV.URL);
  sleep(1);
}
```

**Smell 3: Not checking requests**

- **Lines:** [7]
- **Snippet:**
```js
const res = http.get(__ENV.URL);
```
- **Refactored:**
```js
import http from 'k6/http';
import { sleep, check } from 'k6';

export default function() {
  const res = http.get(__ENV.URL);
  check(res, {
    'status is 200': (r) => r.status === 200
  });
  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [7]
- **Snippet:**
```js
const res = http.get(__ENV.URL);
```
- **Refactored:**
```js
import http from 'k6/http';
import { sleep } from 'k6';

export default function() {
  const params = {
    tags: {
      endpoint: 'target_url',
      flow: 'default'
    }
  };
  const res = http.get(__ENV.URL, params);
  sleep(1);
}
```

### `script_239.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5]
- **Snippet:**
```js
export default function(){
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<200'], // 95% of requests should be below 200ms
  },
};

export default function(){
//...
```

**Smell 3: Not checking requests**

- **Lines:** [7]
- **Snippet:**
```js
const res = http.get(__ENV.URL);
```
- **Refactored:**
```js
import http from 'k6/http';
import { check } from 'k6';

//... inside default function
const res = http.get(__ENV.URL);
check(res, {
    'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [7]
- **Snippet:**
```js
const res = http.get(__ENV.URL);
```
- **Refactored:**
```js
const res = http.get(__ENV.URL, {
    tags: {
        name: 'Homepage',
    },
});
```

### `script_24.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
- **Snippet:**
```js
export let options = {
	stages: [
        { duration: "10s", target: 100 },
		{ duration: "10s", target: 100 },
      ],
};
```
- **Refactored:**
```js
export let options = {
	stages: [
        { duration: "10s", target: 100 },
		{ duration: "10s", target: 100 },
      ],
	thresholds: {
		'http_req_failed': ['rate<0.01'],
		'http_req_duration': ['p(95)<500'],
		'checks': ['rate>0.99'],
	},
};
```

**Smell 3: Not checking requests**

- **Lines:** [76, 77, 78, 84, 85, 86]
- **Snippet:**
```js
let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, {
			headers: headers});
			if(verifyOTPres.status !== 200){...
let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
				headers: headers});
				if(signUpRes.status !== 200){...
```
- **Refactored:**
```js
let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, { headers: headers });
check(verifyOTPres, {
	'verifyOTP status is 200': (r) => r.status === 200,
	'verifyOTP response time < 200ms': (r) => r.timings.duration < 200,
});

// ...

let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, { headers: headers });
check(signUpRes, {
	'signup status is 200': (r) => r.status === 200,
	'signup response time < 200ms': (r) => r.timings.duration < 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [60, 61, 62, 76, 77, 84, 85]
- **Snippet:**
```js
let userExistRes = http.post(`${baseUrl}/v1/userExists`, userExistsJSON, { headers: headers });
// ...
let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, { headers: headers });
// ...
let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, { headers: headers });
```
- **Refactored:**
```js
let userExistRes = http.post(`${baseUrl}/v1/userExists`, userExistsJSON, {
	headers: headers,
	tags: { name: 'userExists', flow: 'signup' },
});

let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, {
	headers: headers,
	tags: { name: 'verifyOTP', flow: 'signup' },
});

let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
	headers: headers,
	tags: { name: 'signup', flow: 'signup' },
});
```

### `script_24.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [14, 18, 20, 21, 23]
- **Snippet:**
```js
export let options = {
	stages: [
        { duration: "10s", target: 100 },
		{ duration: "10s", target: 100 },
      ],
};
```
- **Refactored:**
```js
export let options = {
  stages: [
    { duration: '10s', target: 100 },
    { duration: '10s', target: 100 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [76, 77, 84, 85]
- **Snippet:**
```js
let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, {
	headers: headers});
...
let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
	headers: headers});
```
- **Refactored:**
```js
let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, {
  headers: headers,
  tags: { endpoint: 'verifyOTP', flow: 'signup' },
});

check(verifyOTPres, {
  'verifyOTP status is 200': (r) => r.status === 200,
  'verifyOTP status is OK': (r) => r.json().status === 'OK',
});

let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
  headers: headers,
  tags: { endpoint: 'signup', flow: 'signup' },
});

check(signUpRes, {
  'signup status is 200': (r) => r.status === 200,
  'signup user id exists': (r) => Boolean(r.json().data.user_info.id),
  'signup access token exists': (r) => Boolean(r.json().data.token.access_token),
});
```

**Smell 4: Not using tags**

- **Lines:** [60, 61, 62, 76, 77, 84, 85]
- **Snippet:**
```js
let userExistRes = http.post(`${baseUrl}/v1/userExists`, userExistsJSON, {
	headers: headers
});
...
let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, {
	headers: headers});
...
let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
	headers: headers});
```
- **Refactored:**
```js
let userExistRes = http.post(`${baseUrl}/v1/userExists`, userExistsJSON, {
  headers: headers,
  tags: { endpoint: 'userExists', flow: 'signup' },
});

let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, {
  headers: headers,
  tags: { endpoint: 'verifyOTP', flow: 'signup' },
});

let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
  headers: headers,
  tags: { endpoint: 'signup', flow: 'signup' },
});
```

### `script_24.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [14, 23]
- **Snippet:**
```js
export let options = {
	stages: [
        { duration: "10s", target: 100 },
		{ duration: "10s", target: 100 },
      ],
};
```
- **Refactored:**
```js
export let options = {
	stages: [
        { duration: "10s", target: 100 },
		{ duration: "10s", target: 100 },
      ],
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
        'checks': ['rate>0.95'], // 95% of checks must pass
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [76, 84]
- **Snippet:**
```js
let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, {
			headers: headers});
...
let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
					headers: headers});
```
- **Refactored:**
```js
// After the verifyOTPres request on line 76
check(verifyOTPres, {
    'verifyOTP: status is 200': (r) => r.status === 200,
    'verifyOTP: response is OK': (r) => r.status === 200 && r.json().status === 'OK',
});

// After the signUpRes request on line 84
check(signUpRes, {
    'signup: status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [60, 76, 84]
- **Snippet:**
```js
let userExistRes = http.post(`${baseUrl}/v1/userExists`, userExistsJSON, {
		headers: headers
	});
...
let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, {
			headers: headers});
...
let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
					headers: headers});
```
- **Refactored:**
```js
let userExistRes = http.post(`${baseUrl}/v1/userExists`, userExistsJSON, {
		headers: headers,
        tags: { name: 'userExists' },
	});

let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, {
			headers: headers,
            tags: { name: 'verifyOTP' },
        });

let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
					headers: headers,
                    tags: { name: 'signup' },
                });
```

### `script_240.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 5000,
    duration: '20s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 5000,
    duration: '20s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        'checks': ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/k12-course-service/api/v1/programs?batch_id=201`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/k12-course-service/api/v1/programs?batch_id=201`, {
    headers: headers,
    tags: { name: 'GetPrograms', endpoint: '/k12-course-service/api/v1/programs', batch_id: '201' }
});
```

### `script_240.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 5000,
    duration: '20s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 5000,
    duration: '20s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23, 25, 26, 27, 28, 29]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/k12-course-service/api/v1/programs?batch_id=201`, {
    headers: headers
});

check(res, {
    'status is 200': (r) => r.status === 200,
    'status is 502': (r) => r.status === 502,
    'response time > 200ms': (r) => r.timings.duration > 100,
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/k12-course-service/api/v1/programs?batch_id=201`, {
    headers: headers,
    tags: {
        endpoint: 'programs',
        service: 'k12-course-service',
        flow: 'get-programs',
    },
});

check(res, {
    'status is 200': (r) => r.status === 200,
    'response time <= 200ms': (r) => r.timings.duration <= 200,
}, {
    endpoint: 'programs',
    service: 'k12-course-service',
    flow: 'get-programs',
});
```

### `script_240.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 5000,
    duration: '20s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 5000,
    duration: '20s',
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should complete within 500ms
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [25, 26, 27, 28, 29]
- **Snippet:**
```js
check(res, {
    'status is 200': (r) => r.status === 200,
    'status is 502': (r) => r.status === 502,
    'response time > 200ms': (r) => r.timings.duration > 100,
});
```
- **Refactored:**
```js
check(res, {
    'status is 200': (r) => r.status === 200,
    'response time is acceptable': (r) => r.timings.duration < 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/k12-course-service/api/v1/programs?batch_id=201`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/k12-course-service/api/v1/programs?batch_id=201`, {
    headers: headers,
    tags: {
        name: 'GetProgramsAPI',
    },
});
```

### `script_241.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 1650,
  iterations: 1650,
};
```
- **Refactored:**
```js
export const options = {
  vus: 1650,
  iterations: 1650,
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500', 'p(99)<1000'],
    'response_time': ['p(95)<500'],
    'checks': ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [19]
- **Snippet:**
```js
const res = http.get(url, { headers });
```
- **Refactored:**
```js
const res = http.get(url, {
  headers,
  tags: { name: 'user_logout', endpoint: '/v2/user/logout' },
});
```

### `script_241.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 1650,
  iterations: 1650,
};
```
- **Refactored:**
```js
export const options = {
  vus: 1650,
  iterations: 1650,
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500', 'p(99)<1000'],
    checks: ['rate>0.95'],
    response_time: ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [19, 22, 28]
- **Snippet:**
```js
const res = http.get(url, { headers });
responseTime.add(res.timings.duration);
check(res, { ... });
```
- **Refactored:**
```js
const tags = { endpoint: 'user_logout', method: 'GET', flow: 'logout' };

const res = http.get(url, {
  headers,
  tags,
});

responseTime.add(res.timings.duration, tags);

check(res, {
  'Status is 200': (r) => r.status === 200,
  'Response time < 500ms': (r) => r.timings.duration < 500,
}, tags);
```

### `script_241.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 1650, // Jumlah VUs
  iterations: 1650,
};
```
- **Refactored:**
```js
export const options = {
  vus: 1650,
  iterations: 1650,
  thresholds: {
    // The error rate must be below 1%
    'http_req_failed': ['rate<0.01'],
    // 95% of requests must complete below 500ms
    'http_req_duration': ['p(95)<500'],
    // 99% of checks must pass
    'checks': ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [19]
- **Snippet:**
```js
const res = http.get(url, { headers });
```
- **Refactored:**
```js
const res = http.get(url, {
  headers,
  tags: {
    name: 'UserLogout', // Tag to identify this specific request
  },
});
```

### `script_242.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 50,
  duration: '10m',
};
```
- **Refactored:**
```js
export const options = {
  vus: 50,
  duration: '10m',
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
    'checks': ['rate>0.99'],
    'response_time': ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [26]
- **Snippet:**
```js
const res = http.post(url, payload);
```
- **Refactored:**
```js
const res = http.post(url, payload, {
  tags: { name: 'post_pet_by_id', endpoint: '/v2/pet/:id' },
});
```

### `script_242.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 50,
  duration: '10m',
};
```
- **Refactored:**
```js
export const options = {
  vus: 50,
  duration: '10m',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.95'],
    response_time: ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [26, 29, 35]
- **Snippet:**
```js
const res = http.post(url, payload);
responseTime.add(res.timings.duration);
check(res, { ... });
```
- **Refactored:**
```js
const tags = { endpoint: 'pet_by_id', operation: 'update_pet', method: 'POST' };
const params = { tags };

const res = http.post(url, payload, params);
responseTime.add(res.timings.duration, tags);

check(res, {
  'Status is 200': (r) => r.status === 200,
  'Response time < 500ms': (r) => r.timings.duration < 500,
}, tags);
```

### `script_242.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 50, // Jumlah VUs
  duration: '10m', // Durasi pengujian
};
```
- **Refactored:**
```js
export const options = {
  vus: 50, // Jumlah VUs
  duration: '10m', // Durasi pengujian
  thresholds: {
    'http_req_failed': ['rate<0.01'], // Fail test if error rate > 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    'checks': ['rate>0.99'], // >99% of checks must pass
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
- **Snippet:**
```js
check(res, {
    'Status is 200': (r) => r.status === 200,
    'Status is 400': (r) => r.status === 400,
    'Status is 404': (r) => r.status === 404,
    'Status is 405': (r) => r.status === 405,
    'Status is 429': (r) => r.status === 429,
    'Status is 500': (r) => r.status === 500,
    'Response time < 200ms': (r) => r.timings.duration < 200,
    'Response time < 350ms': (r) => r.timings.duration < 350,
    'Response time < 500ms': (r) => r.timings.duration < 500,
    'Response time < 1000ms': (r) => r.timings.duration < 1000,
  });
```
- **Refactored:**
```js
check(res, {
    'Pet update successful (status 200)': (r) => r.status === 200,
  });
```

**Smell 4: Not using tags**

- **Lines:** [26, 29]
- **Snippet:**
```js
const res = http.post(url, payload);

  // Menyimpan metrik tambahan
  responseTime.add(res.timings.duration);
```
- **Refactored:**
```js
const params = {
    tags: {
      name: 'UpdatePet',
    },
  };
  const res = http.post(url, payload, params);

  // Menyimpan metrik tambahan dengan tag
  responseTime.add(res.timings.duration, params.tags);
```

### `script_245.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [43, 45]
- **Snippet:**
```js
const response = guestCartsResource.addItem(null, product.sku, 1);

    metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
import { check } from 'k6';

// inside the group:
const response = guestCartsResource.addItem(null, product.sku, 1);

check(response, {
  'add guest cart item status is 201': (r) => r.status === 201,
  'add guest cart item has body': (r) => r.body && r.body.length > 0,
});

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```

**Smell 4: Not using tags**

- **Lines:** [43]
- **Snippet:**
```js
const response = guestCartsResource.addItem(null, product.sku, 1);
```
- **Refactored:**
```js
const response = guestCartsResource.addItem(null, product.sku, 1, {
  tags: { name: 'SAPI31_post_guest_cart_items', group: testConfiguration.group, endpoint: 'guest-cart-items' },
});
```

### `script_245.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [43]
- **Snippet:**
```js
const response = guestCartsResource.addItem(null, product.sku, 1);
```
- **Refactored:**
```js
import { group, check } from 'k6';

// ...

const response = guestCartsResource.addItem(null, product.sku, 1);
check(response, {
  'add guest cart item returns 2xx': (r) => r.status >= 200 && r.status < 300,
});
```

**Smell 4: Not using tags**

- **Lines:** [43, 45]
- **Snippet:**
```js
const response = guestCartsResource.addItem(null, product.sku, 1);
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
const tags = {
  endpoint: 'POST /guest-carts/{anonymousCustomerUniqueId}/items',
  flow: 'guest-cart-add-item',
  group: testConfiguration.group,
};

const response = guestCartsResource.addItem(null, product.sku, 1, { tags });
metrics[testConfiguration.metrics[0]].add(response.timings.duration, tags);
```

### `script_245.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [43, 45]
- **Snippet:**
```js
const response = guestCartsResource.addItem(null, product.sku, 1);

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const response = guestCartsResource.addItem(null, product.sku, 1);

const isSuccess = check(response, {
  'add item to cart successfully (status 2xx)': (r) => r.status >= 200 && r.status < 300,
});

// Only record the metric if the request was successful
if (isSuccess) {
  metrics[testConfiguration.metrics[0]].add(response.timings.duration);
}
```

**Smell 4: Not using tags**

- **Lines:** [43, 45]
- **Snippet:**
```js
const response = guestCartsResource.addItem(null, product.sku, 1);

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
const tags = { name: 'SAPI31:POST_guest_cart_items' };

// Assuming the resource method can accept a params object with tags
const response = guestCartsResource.addItem(null, product.sku, 1, { tags });

// Add tags to the custom metric for better filterability in results
metrics[testConfiguration.metrics[0]].add(response.timings.duration, tags);
```

### `script_247.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
- **Snippet:**
```js
export default function () { ... }
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};

export default function () { ... }
```

**Smell 3: Not checking requests**

- **Lines:** [14]
- **Snippet:**
```js
const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);
```
- **Refactored:**
```js
import { check } from 'k6';

const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);
check(response, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [7, 8, 9, 10, 11, 12, 14]
- **Snippet:**
```js
const params = {
    headers: {
      'my-header-one': 'hello',
      'my-header-two': 'world',
    },
  };

  const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);
```
- **Refactored:**
```js
const params = {
    headers: {
      'my-header-one': 'hello',
      'my-header-two': 'world',
    },
    tags: {
      name: 'delete-echo',
      endpoint: '/api/basic/echo',
    },
  };

  const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);
```

### `script_247.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [6]
- **Snippet:**
```js
export default function () {
  ...
}
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};

export default function () {
  ...
}
```

**Smell 3: Not checking requests**

- **Lines:** [14]
- **Snippet:**
```js
const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);
```
- **Refactored:**
```js
import { sleep, check } from 'k6';
import http from 'k6/http';

const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);

check(response, {
  'DELETE echo returned 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [7, 8, 9, 10, 11, 12, 14]
- **Snippet:**
```js
const params = {
  headers: {
    'my-header-one': 'hello',
    'my-header-two': 'world',
  },
};

const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);
```
- **Refactored:**
```js
const params = {
  headers: {
    'my-header-one': 'hello',
    'my-header-two': 'world',
  },
  tags: {
    endpoint: 'basic_echo',
    method: 'DELETE',
    flow: 'echo_delete',
  },
};

const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);
```

### `script_247.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [6, 21]
- **Snippet:**
```js
export default function () {
  // ...
}
```
- **Refactored:**
```js
import { sleep } from 'k6';
import http from 'k6/http';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
};

const BASE_URL = 'http://localhost:8888/alphamart';

export default function () {
  // ...
}
```

**Smell 3: Not checking requests**

- **Lines:** [14]
- **Snippet:**
```js
const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);
```
- **Refactored:**
```js
import { sleep, check } from 'k6';
import http from 'k6/http';

// ...

export default function () {
  // ...
  const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);

  check(response, {
    'is status 204': (r) => r.status === 204,
  });

  // ...
}
```

**Smell 4: Not using tags**

- **Lines:** [7, 12]
- **Snippet:**
```js
const params = {
  headers: {
    'my-header-one': 'hello',
    'my-header-two': 'world',
  },
};
```
- **Refactored:**
```js
const params = {
  headers: {
    'my-header-one': 'hello',
    'my-header-two': 'world',
  },
  tags: {
    name: 'DeleteEchoAPI',
  },
};
```

### `script_248.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
- **Snippet:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: __ENV.RPS,
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100,
            maxVUs: 200,
        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: __ENV.RPS,
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100,
            maxVUs: 200,
        },
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        'checks{check:A status was 200}': ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [19, 22, 23, 24]
- **Snippet:**
```js
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {headers: { 'Content-Type': 'application/json' }})
```
- **Refactored:**
```js
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: `POST /SYNC-${task}`, endpoint: `/SYNC-${task}` }
})
```

### `script_248.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
- **Snippet:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: __ENV.RPS,
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100,
            maxVUs: 200,
        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: Number(__ENV.RPS),
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100,
            maxVUs: 200,
        },
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [19, 25]
- **Snippet:**
```js
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {headers: { 'Content-Type': 'application/json' }})
...
check(resCo, { 'A status was 200': (r) => r.status == 200 });
```
- **Refactored:**
```js
const httppost = (task, body) => http.post(
    `${hostprefix}/SYNC-${task}`,
    JSON.stringify(body),
    {
        headers: { 'Content-Type': 'application/json' },
        tags: { endpoint: `SYNC-${task}`, operation: body.operation }
    }
);

export default function () {
    const task = 'G-4096';
    const resCo = httppost(task, {
        operation: 'test',
    });
    check(resCo, { 'A status was 200': (r) => r.status === 200 }, { endpoint: `SYNC-${task}`, operation: 'test' });
}
```

### `script_248.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
- **Snippet:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: __ENV.RPS, // Equals to RPS
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100, // how large the initial pool of VUs would be
            maxVUs: 200, // if the preAllocatedVUs are not enough, we can initialize more
        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: __ENV.RPS, // Equals to RPS
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100, // how large the initial pool of VUs would be
            maxVUs: 200, // if the preAllocatedVUs are not enough, we can initialize more
        },
    },
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
        'checks': ['rate>0.99'], // 99% of checks should pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [19]
- **Snippet:**
```js
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {headers: { 'Content-Type': 'application/json' }})
```
- **Refactored:**
```js
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: `SYNC-${task}` },
})
```

### `script_249.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 1600,
  iterations: 1600,
};
```
- **Refactored:**
```js
export const options = {
  vus: 1600,
  iterations: 1600,
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
    'response_time': ['p(95)<500'],
    'checks': ['rate>0.95'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [20]
- **Snippet:**
```js
const res = http.del(url);
```
- **Refactored:**
```js
const res = http.del(url, null, {
  tags: { name: 'delete_pet', endpoint: 'DELETE /pet/:id' },
});
```

### `script_249.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 1600,
  iterations: 1600,
};
```
- **Refactored:**
```js
export const options = {
  vus: 1600,
  iterations: 1600,
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.95'],
    response_time: ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [20, 23, 29]
- **Snippet:**
```js
const res = http.del(url);
responseTime.add(res.timings.duration);
check(res, { ... });
```
- **Refactored:**
```js
const tags = { endpoint: 'delete_pet', operation: 'deletePet' };
const res = http.del(url, null, { tags: { ...tags, name: 'DELETE /pet/{petId}' } });
responseTime.add(res.timings.duration, tags);
check(res, {
  'Status is acceptable': (r) => [200, 400, 404, 429, 500].includes(r.status),
  'Response time < 500ms': (r) => r.timings.duration < 500,
}, tags);
```

### `script_249.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 1600, // Jumlah VUs
  iterations: 1600,
};
```
- **Refactored:**
```js
export const options = {
  vus: 1600,
  iterations: 1600,
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks': ['rate>0.95'], // 95% of checks should pass
    'response_time': ['p(90) < 400', 'p(95) < 800'], // Custom metric thresholds
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [29, 30, 31, 32, 33, 34]
- **Snippet:**
```js
check(res, {
    'Status is 200': (r) => r.status === 200,
    'Status is 400': (r) => r.status === 400,
    'Status is 404': (r) => r.status === 404,
    'Status is 429': (r) => r.status === 429,
    'Status is 500': (r) => r.status === 500,
```
- **Refactored:**
```js
// A check should validate the expected 'correct' outcome. Including checks for error statuses
// will result in a 100% check pass rate even if the server is returning errors,
// creating a false positive.
check(res, {
    'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [20, 23]
- **Snippet:**
```js
// Kirim request DELETE ke API
const res = http.del(url);

// Menyimpan metrik tambahan
responseTime.add(res.timings.duration);
```
- **Refactored:**
```js
const params = {
  tags: {
    endpoint: 'delete_pet',
  },
};

// Kirim request DELETE ke API dengan tag
const res = http.del(url, null, params);

// Menyimpan metrik tambahan dengan tag
responseTime.add(res.timings.duration, { endpoint: 'delete_pet' });
```

### `script_25.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [26, 30]
- **Snippet:**
```js
const to = {}

export const options = {
  vus: 1,
  thresholds: to,
```
- **Refactored:**
```js
export const options = {
  vus: 1,
  thresholds: {
    'latency_trend': ['p(95)<500', 'p(99)<1000'],
    'received_updates': ['count>0'],
    'checks': ['rate>0.99'],
    'ws_connecting': ['p(95)<1000'],
  },
  summaryTrendStats: trends,
  scenarios: {
    replication: scenario(baseDuration, conns),
  },
}
```

**Smell 4: Not using tags**

- **Lines:** [38, 144, 145, 147, 163]
- **Snippet:**
```js
const res = ws.connect(URL, {}, (socket) => {
  ...
  latencyTrend.add(now - updated, { type: type })
  counterReceived.add(1)
  check(msg, { 'got realtime notification': ... })
})
check(res, { 'status is 101': ... })
```
- **Refactored:**
```js
const res = ws.connect(URL, { tags: { endpoint: 'realtime_ws', flow: 'subscribe' } }, (socket) => {
  ...
  latencyTrend.add(now - updated, { type: type, endpoint: 'realtime_ws', event: 'postgres_changes' })
  counterReceived.add(1, { endpoint: 'realtime_ws', event: 'postgres_changes' })
  check(msg, { 'got realtime notification': (msg) => msg.topic === 'realtime:any' }, { tags: { endpoint: 'realtime_ws', event: 'postgres_changes' } })
})
check(res, { 'status is 101': (r) => r && r.status === 101 }, { tags: { endpoint: 'realtime_ws', flow: 'connect' } })
```

### `script_25.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [26, 30]
- **Snippet:**
```js
const to = {}
...
thresholds: to,
```
- **Refactored:**
```js
export const options = {
  vus: 1,
  thresholds: {
    'checks': ['rate>0.95'],
    'ws_connecting': ['p(95)<1000'],
    'latency_trend': ['p(95)<500'],
    'received_updates': ['count>0'],
  },
  summaryTrendStats: trends,
  scenarios: {
    replication: scenario(baseDuration, conns),
  },
}
```

**Smell 4: Not using tags**

- **Lines:** [38, 126, 147, 163]
- **Snippet:**
```js
const res = ws.connect(URL, {}, (socket) => {
...
check(msg, {
  'subscribed to realtime': ...
})
...
check(res, { 'status is 101': ... })
```
- **Refactored:**
```js
const wsParams = {
  tags: {
    endpoint: 'realtime_websocket',
    flow: 'replication',
  },
}

const res = ws.connect(URL, wsParams, (socket) => {
  socket.on('message', (msg) => {
    msg = JSON.parse(msg)

    if (msg.event === 'system') {
      check(msg, {
        'subscribed to realtime': (msg) =>
          msg.topic === 'realtime:any' && msg.payload.status === 'ok',
      }, { endpoint: 'realtime_websocket', flow: 'replication', event: 'system' })
    }

    if (msg.event !== 'postgres_changes') {
      return
    }

    const type = msg.payload.type
    let updated = 0
    if (msg.payload.data.record) {
      updated = Date.parse(msg.payload.data.record.created_at)
    } else {
      updated = new Date(msg.payload.data.commit_timestamp)
    }

    latencyTrend.add(Date.now() - updated, { endpoint: 'realtime_websocket', flow: 'replication', type })
    counterReceived.add(1, { endpoint: 'realtime_websocket', flow: 'replication', type })

    check(msg, {
      'got realtime notification': (msg) => msg.topic === 'realtime:any',
    }, { endpoint: 'realtime_websocket', flow: 'replication', event: 'postgres_changes' })
  })
})

check(res, { 'status is 101': (r) => r && r.status === 101 }, { endpoint: 'realtime_websocket', flow: 'replication' })
```

### `script_25.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [26, 30]
- **Snippet:**
```js
const to = {}

export const options = {
  // ...
  thresholds: to,
  // ...
}
```
- **Refactored:**
```js
export const options = {
  // ...
  thresholds: {
    'checks': ['rate>0.99'],
    'latency_trend': ['p(95)<500'],
    'ws_connecting': ['p(95)<1000']
  },
  // ...
}
```

**Smell 4: Not using tags**

- **Lines:** [38, 126, 147]
- **Snippet:**
```js
const res = ws.connect(URL, {}, (socket) => { ... });

// ...

check(msg, {
  'subscribed to realtime': (msg) =>
    msg.topic === 'realtime:any' && msg.payload.status === 'ok',
})
```
- **Refactored:**
```js
const params = { tags: { name: 'realtime-connection' } };
const res = ws.connect(URL, params, (socket) => { ... });

// ...

check(
  msg,
  {
    'subscribed to realtime': (msg) =>
      msg.topic === 'realtime:any' && msg.payload.status === 'ok',
  },
  { check_type: 'subscription' }
);
```

### `script_250.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [23, 32, 33, 34, 35, 36]
- **Snippet:**
```js
const response = http.get('http://test.k6.io');

    if (response.status === 200) {
        successRate.add(true);
    } else {
        successRate.add(false);
    }
```
- **Refactored:**
```js
import { check } from 'k6';

const response = http.get('http://test.k6.io');

const success = check(response, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
});
successRate.add(success);
```

**Smell 4: Not using tags**

- **Lines:** [23]
- **Snippet:**
```js
const response = http.get('http://test.k6.io');
```
- **Refactored:**
```js
const response = http.get('http://test.k6.io', {
    tags: { name: 'homepage', endpoint: 'test.k6.io' },
});
```

### `script_250.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [23, 26, 29, 33, 35]
- **Snippet:**
```js
const response = http.get('http://test.k6.io');
requestCounter.add(1);
requestTrend.add(response.timings.duration);
successRate.add(true);
```
- **Refactored:**
```js
const tags = { endpoint: 'home', flow: 'homepage' };
const response = http.get('http://test.k6.io', { tags });
requestCounter.add(1, tags);
requestTrend.add(response.timings.duration, tags);
successRate.add(response.status === 200, tags);
```

### `script_250.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [32, 33, 34, 35, 36]
- **Snippet:**
```js
if (response.status === 200) {
        successRate.add(true);
    } else {
        successRate.add(false);
    }
```
- **Refactored:**
```js
import { check } from 'k6';

// In default function, replace the if/else block:
const wasSuccessful = check(response, {
    'status is 200': (r) => r.status === 200,
});
successRate.add(wasSuccessful);
```

**Smell 4: Not using tags**

- **Lines:** [23]
- **Snippet:**
```js
const response = http.get('http://test.k6.io');
```
- **Refactored:**
```js
const response = http.get('http://test.k6.io', {
  tags: { name: 'Homepage' },
});
```

### `script_251.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [57, 58]
- **Snippet:**
```js
const response = checkoutResource.checkout();
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
import { check } from 'k6';

// Inside the group block:
const response = checkoutResource.checkout();
const success = check(response, {
  'checkout status is 200 or 201': (r) => r.status === 200 || r.status === 201,
  'checkout response has body': (r) => r.body && r.body.length > 0,
}, { tags: { endpoint: 'post_checkout' } });
if (success) {
  metrics[testConfiguration.metrics[0]].add(response.timings.duration);
}
```

**Smell 4: Not using tags**

- **Lines:** [57, 58]
- **Snippet:**
```js
const response = checkoutResource.checkout();
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
// Ensure the request inside CheckoutResource.checkout() is tagged, and add tags when recording metrics:
const response = checkoutResource.checkout({ tags: { endpoint: 'post_checkout', group: testConfiguration.group, testId: testConfiguration.id } });
metrics[testConfiguration.metrics[0]].add(response.timings.duration, { endpoint: 'post_checkout', group: testConfiguration.group, testId: testConfiguration.id });
```

### `script_251.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [57]
- **Snippet:**
```js
const response = checkoutResource.checkout();
```
- **Refactored:**
```js
import { group, check } from 'k6';

...

group(testConfiguration.group, () => {
  const checkoutResource = new CheckoutResource(idCart, customerEmail, bearerToken);
  const response = checkoutResource.checkout();

  check(response, {
    'checkout status is 200': (r) => r.status === 200,
    'checkout response body is not empty': (r) => !!r.body,
  });

  metrics[testConfiguration.metrics[0]].add(response.timings.duration);
});
```

**Smell 4: Not using tags**

- **Lines:** [1, 57, 58]
- **Snippet:**
```js
// tags: smoke, load, soak, checkout, SAPI
const response = checkoutResource.checkout();
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
import { group, check } from 'k6';

...

group(testConfiguration.group, () => {
  const tags = {
    test_id: testConfiguration.id,
    group: testConfiguration.group,
    endpoint: 'checkout',
    operation: 'post_checkout',
  };

  const checkoutResource = new CheckoutResource(idCart, customerEmail, bearerToken);
  const response = checkoutResource.checkout({ tags });

  check(response, {
    'checkout status is 200': (r) => r.status === 200,
  }, tags);

  metrics[testConfiguration.metrics[0]].add(response.timings.duration, tags);
});
```

### `script_251.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [57, 58]
- **Snippet:**
```js
const response = checkoutResource.checkout();
    metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
import { check, group } from 'k6'; // Add 'check' to imports
// ...
const response = checkoutResource.checkout();
check(response, {
  'POST /checkout returns status 200': (r) => r.status === 200,
});
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```

**Smell 4: Not using tags**

- **Lines:** [58]
- **Snippet:**
```js
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
const tags = { name: 'SAPI7_post_checkout' };
const response = checkoutResource.checkout(); // Best practice: also tag the request itself if possible
metrics[testConfiguration.metrics[0]].add(response.timings.duration, tags);
```

### `script_252.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
- **Snippet:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'ramping-arrival-rate',
      ...
    },
  },
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'ramping-arrival-rate',
      preAllocatedVUs: 50,
      timeUnit: '1s',
      startRate: 50,
      stages: [
        { target: 200, duration: '30s' },
        { target: 500, duration: '0' },
        { target: 500, duration: '5m' },
      ],
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    'checks{check:success login}': ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [22]
- **Snippet:**
```js
let res = http.post('http://localhost:5680/api/v1/auth/token', data)
```
- **Refactored:**
```js
let res = http.post('http://localhost:5680/api/v1/auth/token', data, {
  tags: { name: 'auth_token', endpoint: '/api/v1/auth/token' },
})
```

### `script_252.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
- **Snippet:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'ramping-arrival-rate',
      preAllocatedVUs: 50,
      timeUnit: '1s',
      startRate: 50,
      stages: [
        { target: 200, duration: '30s' },
        { target: 500, duration: '0' },
        { target: 500, duration: '5m' },
      ],
    },
  },
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'ramping-arrival-rate',
      preAllocatedVUs: 50,
      timeUnit: '1s',
      startRate: 50,
      stages: [
        { target: 200, duration: '30s' },
        { target: 500, duration: '0' },
        { target: 500, duration: '5m' },
      ],
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [22, 24]
- **Snippet:**
```js
let res = http.post('http://localhost:5680/api/v1/auth/token', data)

check(res, { 'success login': (r) => r.status === 200 })
```
- **Refactored:**
```js
const tags = { endpoint: 'auth_token', flow: 'login' }
let res = http.post('http://localhost:5680/api/v1/auth/token', data, { tags })

check(res, { 'success login': (r) => r.status === 200 }, tags)
```

### `script_252.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
- **Snippet:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'ramping-arrival-rate',
      preAllocatedVUs: 50,
      timeUnit: '1s',
      startRate: 50,
      stages: [
        { target: 200, duration: '30s' }, // linearly go from 50 iters/s to 200 iters/s for 30s
        { target: 500, duration: '0' }, // instantly jump to 500 iters/s
        { target: 500, duration: '5m' }, // continue with 500 iters/s for 10 minutes
      ],
    },
  },
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'ramping-arrival-rate',
      preAllocatedVUs: 50,
      timeUnit: '1s',
      startRate: 50,
      stages: [
        { target: 200, duration: '30s' },
        { target: 500, duration: '0' },
        { target: 500, duration: '5m' },
      ],
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests must complete below 500ms
    'checks{success login}': ['rate>0.99'], // 99% of login checks should pass
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [22]
- **Snippet:**
```js
let res = http.post('http://localhost:5680/api/v1/auth/token', data)
```
- **Refactored:**
```js
const params = {
  tags: { name: 'AuthToken' },
};
let res = http.post('http://localhost:5680/api/v1/auth/token', data, params);
```

### `script_253.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
- **Snippet:**
```js
export default function () { ... }
```
- **Refactored:**
```js
export const options = {
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
    },
};

export default function () { ... }
```

**Smell 3: Not checking requests**

- **Lines:** [25, 29, 30, 31]
- **Snippet:**
```js
const responses = http.batch(request);
// check(responses[2], {
//     'form data OK': (res) => JSON.parse(res.body)['form']['hello'] == 'world!',
// });
```
- **Refactored:**
```js
const responses = http.batch(request);
responses.forEach((res, i) => {
    check(res, {
        [`response ${i} status is 200`]: (r) => r.status === 200,
        [`response ${i} has body`]: (r) => r.body && r.body.length > 0,
    });
});
```

**Smell 4: Not using tags**

- **Lines:** [15, 16, 17, 18, 19, 20, 21]
- **Snippet:**
```js
request.push({
    method: 'GET',
    url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
    params: params
});
```
- **Refactored:**
```js
request.push({
    method: 'GET',
    url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
    params: {
        ...params,
        tags: { name: 'user_search', endpoint: '/user/search' },
    },
});
```

### `script_253.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [1, 32]
- **Snippet:**
```js
No export const options = { thresholds: ... } is defined anywhere in the script.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [25, 29, 30, 31]
- **Snippet:**
```js
const responses = http.batch(request);

// check(responses[2], {
//     'form data OK': (res) => JSON.parse(res.body)['form']['hello'] == 'world!',
// });
```
- **Refactored:**
```js
const responses = http.batch(request);

responses.forEach((res) => {
  check(res, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
  });
});
```

**Smell 4: Not using tags**

- **Lines:** [4, 5, 6, 7, 8, 16, 17, 18, 19, 20]
- **Snippet:**
```js
const params = {
    headers: {
        'Authorization': 'Bearer ...',
    },
};

request.push({
    method: 'GET',
    url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
    params: params
});
```
- **Refactored:**
```js
const params = {
  headers: {
    'Authorization': 'Bearer ...',
  },
  tags: {
    endpoint: 'user_search',
    flow: 'search_user',
  },
};

request.push({
  method: 'GET',
  url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
  params,
});
```

### `script_253.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 32]
- **Snippet:**
```js
The script does not export an `options` object with a `thresholds` property. The entire script is missing this configuration.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
};

export default function () { /* ... */ }
```

**Smell 3: Not checking requests**

- **Lines:** [25, 32]
- **Snippet:**
```js
const responses = http.batch(request);

// httpbin.test.k6.io should return our POST data in the response body, so
// we check the third response object to see that the POST worked.
// check(responses[2], {
//     'form data OK': (res) => JSON.parse(res.body)['form']['hello'] == 'world!',
// });
```
- **Refactored:**
```js
const responses = http.batch(request);

responses.forEach((res) => {
    check(res, {
        'is status 200': (r) => r.status === 200,
    });
});
```

**Smell 4: Not using tags**

- **Lines:** [15, 21]
- **Snippet:**
```js
for (let req = 0; req < countRequest; req++) {
    request.push({
        method: 'GET',
        url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
        params: params
    });
}
```
- **Refactored:**
```js
for (let req = 0; req < countRequest; req++) {
    request.push({
        method: 'GET',
        url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
        params: {
            headers: params.headers,
            tags: { name: 'user-search' },
        }
    });
}
```

### `script_254.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
  vus: 10,
  duration: '30s',
};
```
- **Refactored:**
```js
export let options = {
  vus: 10,
  duration: '30s',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [20, 21, 22, 23]
- **Snippet:**
```js
const params = {
  headers: { 'Content-Type': 'application/json' },
};
let res = http.post(url, payload, params);
```
- **Refactored:**
```js
const params = {
  headers: { 'Content-Type': 'application/json' },
  tags: { name: 'post_api_payload', endpoint: '/api/payload' },
};
let res = http.post(url, payload, params);
```

### `script_254.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
  vus: 10,
  duration: '30s',
};
```
- **Refactored:**
```js
export let options = {
  vus: 10,
  duration: '30s',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [20, 21, 22, 23]
- **Snippet:**
```js
const params = {
  headers: { 'Content-Type': 'application/json' },
};
let res = http.post(url, payload, params);
```
- **Refactored:**
```js
const params = {
  headers: { 'Content-Type': 'application/json' },
  tags: { endpoint: 'payload', method: 'POST', flow: 'create_payload' },
};
let res = http.post(url, payload, params);
```

### `script_254.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
  vus: 10,
  duration: '30s',
};
```
- **Refactored:**
```js
export let options = {
  vus: 10,
  duration: '30s',
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [20, 21, 22, 23]
- **Snippet:**
```js
const params = {
    headers: { 'Content-Type': 'application/json' },
  };
  let res = http.post(url, payload, params);
```
- **Refactored:**
```js
const params = {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'CreatePayload' },
  };
  let res = http.post(url, payload, params);
```

### `script_255.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
    vus: 1,
    // duration: '10s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 1,
    // duration: '10s',
    thresholds: {
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
        'checks': ['rate>0.95'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [29]
- **Snippet:**
```js
let res = http.post(url, invalidPayload, params);
```
- **Refactored:**
```js
let params = {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'createWithArray', endpoint: '/v2/user/createWithArray', scenario: 'invalid_payload' },
};
let res = http.post(url, invalidPayload, params);
```

### `script_255.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
    vus: 1,
    // duration: '10s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 1,
    thresholds: {
        http_req_duration: ['p(95)<1000'],
        http_req_failed: ['rate<0.01']
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [27, 29, 32]
- **Snippet:**
```js
let params = { headers: { 'Content-Type': 'application/json' } };

let res = http.post(url, invalidPayload, params);

check(res, { ... });
```
- **Refactored:**
```js
let params = {
    headers: { 'Content-Type': 'application/json' },
    tags: {
        endpoint: 'createWithArray',
        flow: 'user_creation_invalid',
        method: 'POST'
    }
};

let res = http.post(url, invalidPayload, params);

check(res, {
    'Status is expected': (r) => [200, 400, 429, 500].includes(r.status),
    'response contains message': (r) => r.body.includes('message')
}, {
    endpoint: 'createWithArray',
    flow: 'user_creation_invalid'
});
```

### `script_255.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
    vus: 1,
    // duration: '10s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 1,
    // duration: '10s',
    thresholds: {
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
        'checks': ['rate>0.95'], // 95% of checks must pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [29]
- **Snippet:**
```js
let res = http.post(url, invalidPayload, params);
```
- **Refactored:**
```js
let params = {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'CreateUserWithArray' },
};
let res = http.post(url, invalidPayload, params);
```

### `script_257.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [26, 27, 28]
- **Snippet:**
```js
const fixture = FullProductFixture.createFixture({
  productCount: testConfiguration.vus ?? EnvironmentUtil.getRampVus(),
});
```
- **Refactored:**
```js
export function setup() {
  const fixture = FullProductFixture.createFixture({
    productCount: testConfiguration.vus ?? EnvironmentUtil.getRampVus(),
  });
  return fixture.getData();
}

export default function (data) {
  const product = data[(__VU - 1 + __ITER) % data.length];
  // continue test flow using product
}
```

**Smell 3: Not checking requests**

- **Lines:** [39]
- **Snippet:**
```js
const response = catalogSearchResource.get({ q: product.sku });
```
- **Refactored:**
```js
import { group, check } from 'k6';

// ...

const response = catalogSearchResource.get({ q: product.sku });

check(response, {
  'catalog search status is 200': (r) => r.status === 200,
  'catalog search response is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [39, 41]
- **Snippet:**
```js
const response = catalogSearchResource.get({ q: product.sku });

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
const tags = {
  endpoint: 'catalog_search',
  flow: 'product_search',
};

const response = catalogSearchResource.get(
  { q: product.sku },
  { tags }
);

metrics[testConfiguration.metrics[0]].add(response.timings.duration, tags);
```

### `script_257.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [26, 27, 28]
- **Snippet:**
```js
const fixture = FullProductFixture.createFixture({
  productCount: testConfiguration.vus ?? EnvironmentUtil.getRampVus(),
});
```
- **Refactored:**
```js
/* Fixture creation should be moved from the init context to the setup function, which runs only once per test. The default function should be updated to select data from the array returned by setup. */
export function setup() {
  const fixture = FullProductFixture.createFixture({
    productCount: testConfiguration.vus ?? EnvironmentUtil.getRampVus(),
  });
  return fixture.getData(); // Assuming this returns an array of products
}

export default function (data) {
  const product = data[__VU % data.length]; // Logic to select data per iteration
  // ... rest of the test
}
```

**Smell 3: Not checking requests**

- **Lines:** [39, 41]
- **Snippet:**
```js
const response = catalogSearchResource.get({ q: product.sku });

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const response = catalogSearchResource.get({ q: product.sku });

check(response, {
  'GET /catalog-search - status is 200': (r) => r.status === 200,
});

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```

**Smell 4: Not using tags**

- **Lines:** [39]
- **Snippet:**
```js
const response = catalogSearchResource.get({ q: product.sku });
```
- **Refactored:**
```js
/* Assuming the resource wrapper can accept and apply tags to the underlying HTTP request. */
const params = {
  tags: {
    name: 'SAPI2_get_catalog_search',
  },
};
const response = catalogSearchResource.get({ q: product.sku }, params);
```

### `script_259.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
- **Snippet:**
```js
export default function () { ... }
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};

export default function () { ... }
```

**Smell 3: Not checking requests**

- **Lines:** [8]
- **Snippet:**
```js
const res = http.get('https://www.google.com');
```
- **Refactored:**
```js
import { check } from 'k6';

const res = http.get('https://www.google.com');
check(res, {
  'status is 200': (r) => r.status === 200,
  'body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [8]
- **Snippet:**
```js
const res = http.get('https://www.google.com');
```
- **Refactored:**
```js
const res = http.get('https://www.google.com', {
  tags: { name: 'google_homepage', endpoint: 'GET_/' },
});
```

### `script_259.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [7]
- **Snippet:**
```js
export default function () { ... } // no export const options with thresholds is defined
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99']
  }
};

export default function () {
  // test logic
}
```

**Smell 3: Not checking requests**

- **Lines:** [8]
- **Snippet:**
```js
const res = http.get('https://www.google.com');
```
- **Refactored:**
```js
import { check, sleep } from 'k6';

const res = http.get('https://www.google.com');
check(res, {
  'GET google home returns 200': (r) => r.status === 200,
  'GET google home has body': (r) => r.body && r.body.length > 0
});
```

**Smell 4: Not using tags**

- **Lines:** [8]
- **Snippet:**
```js
const res = http.get('https://www.google.com');
```
- **Refactored:**
```js
const res = http.get('https://www.google.com', {
  tags: {
    endpoint: 'google_home',
    flow: 'homepage'
  }
});
```

### `script_259.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 18]
- **Snippet:**
```js
The script lacks an exported 'options' object containing a 'thresholds' property. Without thresholds, the test will always pass in a CI/CD environment, regardless of the system's performance.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [8]
- **Snippet:**
```js
const res = http.get('https://www.google.com');
```
- **Refactored:**
```js
import { check } from 'k6';
// ... in default function
const res = http.get('https://www.google.com');
check(res, {
  'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [8]
- **Snippet:**
```js
const res = http.get('https://www.google.com');
```
- **Refactored:**
```js
const res = http.get('https://www.google.com', {
  tags: { name: 'Homepage' },
});
```

### `script_26.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5]
- **Snippet:**
```js
import k6 from 'k6';
import http from 'k6/http';

/* Load dynamic variables */
import { dynamicGenerators, dynamicGeneratorsRegex } from './dynamic.js';
```
- **Refactored:**
```js
import k6 from 'k6';
import http from 'k6/http';

/* Load dynamic variables */
import { dynamicGenerators, dynamicGeneratorsRegex } from './dynamic.js';

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

### `script_26.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [132, 133, 134]
- **Snippet:**
```js
const setting = {
  options: {},
};
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};

const setting = {
  options,
};
```

**Smell 3: Not checking requests**

- **Lines:** [1031, 1032, 1033, 1034, 1035]
- **Snippet:**
```js
const response = http.request(...args);
if (post) {
  enterPost(response);
  executePostrequest(postman[Post], post, response);
  executeTests();
}
```
- **Refactored:**
```js
const response = http.request(...args);

k6.check(response, {
  'request status is successful': r => r.status >= 200 && r.status < 400,
});

if (post) {
  enterPost(response);
  executePostrequest(postman[Post], post, response);
  executeTests();
}
```

### `script_26.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1]
- **Snippet:**
```js
import k6 from 'k6';
import http from 'k6/http';
```
- **Refactored:**
```js
/* Add at the top of the script */
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95 percent of response times must be below 500ms
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [1031]
- **Snippet:**
```js
const response = http.request(...args);
```
- **Refactored:**
```js
/* In the executeRequest function, add a k6.check after the request */
    const args = makeRequestArgs(config);
    const response = http.request(...args);
    k6.check(response, {
      [`'${name}' status is OK`]: (r) => r.status < 400,
    });
    if (post) {
      enterPost(response);
      //...
```

**Smell 4: Not using tags**

- **Lines:** [1031]
- **Snippet:**
```js
const response = http.request(...args);
```
- **Refactored:**
```js
/* In the executeRequest function, automatically add the request name as a tag */
function executeRequest({
  name, id = guid(), method, address, data, headers, options, tags, pre, auth, post
}) {
  try {
    enterRequest(name, id, method, address, data, headers);
    executePrerequest(postman[Pre], pre);
    const requestTags = Object.assign({ name: name }, tags);
    const config = makeRequestConfig(
      method, address, data, headers, options, requestTags
    );
    //...
```

### `script_260.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
export let options = {
  ...test_options,
  thresholds: {
    ...(test_options.thresholds || {}),
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

### `script_260.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
export let options = {
  ...test_options,
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // Fail if more than 1% of requests error
    'http_req_duration': ['p(95)<500'], // 95th percentile response time must be below 500ms
    'checks': ['rate>0.99']              // More than 99% of checks must pass
  },
};
```

### `script_262.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 5000,
    duration: '10s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 5000,
    duration: '10s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        'checks{check:status is 200}': ['rate>0.99'],
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [25, 26, 27, 28, 29, 30, 31, 32]
- **Snippet:**
```js
check(res, {
    'status is 200': (r) => r.status === 200,
    'status is 502': (r) => r.status === 502,
    'status is 503': (r) => r.status === 503,
    'status is 500': (r) => r.status === 500,
    'status is 520': (r) => r.status === 520,
    'response time > 200ms': (r) => r.timings.duration > 100,
});
```
- **Refactored:**
```js
const success = check(res, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
    'response time < 500ms': (r) => r.timings.duration < 500,
});
if (!success) {
    console.error(`Request failed with status ${res.status} and body: ${res.body}`);
}
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/notice-service/api/v1/notices?identification_id=101&identification_type=segments&page=1&type=notice&limit=1`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/notice-service/api/v1/notices?identification_id=101&identification_type=segments&page=1&type=notice&limit=1`, {
    headers: headers,
    tags: {
        name: 'GetNotices',
        endpoint: '/notice-service/api/v1/notices',
        flow: 'notice_fetch'
    }
});
```

### `script_262.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 5000,
    duration: '10s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 5000,
    duration: '10s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/notice-service/api/v1/notices?identification_id=101&identification_type=segments&page=1&type=notice&limit=1`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/notice-service/api/v1/notices?identification_id=101&identification_type=segments&page=1&type=notice&limit=1`, {
    headers: headers,
    tags: {
        endpoint: 'get_notices',
        flow: 'notice_service',
        method: 'GET'
    }
});

check(res, {
    'status is 200': (r) => r.status === 200,
    'response time <= 200ms': (r) => r.timings.duration <= 200,
}, {
    endpoint: 'get_notices',
    flow: 'notice_service'
});
```

### `script_262.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 5000,
    duration: '10s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 5000,
    duration: '10s',
    thresholds: {
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/notice-service/api/v1/notices?identification_id=101&identification_type=segments&page=1&type=notice&limit=1`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/notice-service/api/v1/notices?identification_id=101&identification_type=segments&page=1&type=notice&limit=1`, {
    headers: headers,
    tags: {
        name: 'GetNotices',
    },
});
```

### `script_264.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [39, 40, 41, 42]
- **Snippet:**
```js
export const options = {
  duration: `${duration}s`,
  vus: virtualUsers,
}
```
- **Refactored:**
```js
export const options = {
  duration: `${duration}s`,
  vus: virtualUsers,
  thresholds: {
    'inserts': ['count>0'],
  },
}
```

**Smell 4: Not using tags**

- **Lines:** [73, 74, 75]
- **Snippet:**
```js
db.exec(
  `insert into load_messages (room_id, data) values ('${room}', '...');`
)
```
- **Refactored:**
```js
db.exec(
  `insert into load_messages (room_id, data) values ('${room}', '...');`,
  { tags: { operation: 'insert', room: room } }
)
```

### `script_264.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [39, 40, 41, 42]
- **Snippet:**
```js
export const options = {
  duration: `${duration}s`,
  vus: virtualUsers,
}
```
- **Refactored:**
```js
export const options = {
  duration: `${duration}s`,
  vus: virtualUsers,
  thresholds: {
    // Fail test if the insert rate is below the target rate.
    'inserts': [`rate>=${rate}`],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [73, 74, 75]
- **Snippet:**
```js
db.exec(
    `insert into load_messages (room_id, data) values ('${room}', '{"id": "1","type": "message","attributes": {"text": "Hello world","player1_name": "John Doe","player2_name": "Jane Doe","player1_score": 0,"player2_score": 0,"bracket": "A","round": 1,"match": 1,"winner": 0,"loser": 0,"player1_id": 1,"player2_id": 2,"player1_rank": 1,"player2_rank": 2,"player1_hero": "Donkey Kong","player2_hero": "Donkey Kong"}}');`
  )
```
- **Refactored:**
```js
// Add 'check' to k6 import: import { sleep, check } from 'k6'

check(null, {
  'database insert was successful': () => {
    try {
      db.exec(
        `insert into load_messages (room_id, data) values ('${room}', '{"id": "1", ... }');`
      );
      return true;
    } catch (e) {
      return false;
    }
  },
});
```

**Smell 4: Not using tags**

- **Lines:** [77]
- **Snippet:**
```js
counterInserts.add(1)
```
- **Refactored:**
```js
counterInserts.add(1, { room: room });
```

### `script_265.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9]
- **Snippet:**
```js
export default function () {
  const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
  sleep(1);
}
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};

export default function () {
  const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
  sleep(1);
}
```

**Smell 3: Not checking requests**

- **Lines:** [7]
- **Snippet:**
```js
const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
```
- **Refactored:**
```js
import { check } from 'k6';

export default function () {
  const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
  check(res, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
  });
  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [7]
- **Snippet:**
```js
const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
```
- **Refactored:**
```js
const res = http.get(`https://${__ENV.MY_HOSTNAME}`, {
  tags: { name: 'homepage', endpoint: '/' },
});
```

### `script_265.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [6]
- **Snippet:**
```js
export default function () {
  const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
  sleep(1);
}
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};

export default function () {
  const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
  sleep(1);
}
```

**Smell 3: Not checking requests**

- **Lines:** [7]
- **Snippet:**
```js
const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default function () {
  const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
  check(res, {
    'status is 200': (r) => r.status === 200,
  });
  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [7]
- **Snippet:**
```js
const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
```
- **Refactored:**
```js
export default function () {
  const res = http.get(`https://${__ENV.MY_HOSTNAME}`, {
    tags: {
      endpoint: 'home',
      flow: 'homepage',
    },
  });
  sleep(1);
}
```

### `script_265.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [6]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<200'], // 95% of requests must complete below 200ms
  },
};

export default function () { ... }
```

**Smell 3: Not checking requests**

- **Lines:** [7]
- **Snippet:**
```js
const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
check(res, {
    'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [7]
- **Snippet:**
```js
const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
```
- **Refactored:**
```js
const res = http.get(`https://${__ENV.MY_HOSTNAME}`, {
  tags: { name: 'Homepage' },
});
```

### `script_266.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [56, 62, 64, 70]
- **Snippet:**
```js
checkoutResource.checkout();
const response = ordersResource.all();
orderId = JSON.parse(response.body).data[0].id;
const response = ordersResource.get(orderId, ['order-shipments', 'concrete-products', 'abstract-products']);
```
- **Refactored:**
```js
import { group, check } from 'k6';

// ...

group('Place orders', () => {
  const checkoutResource = new CheckoutResource(idCart, customerEmail, bearerToken);
  const response = checkoutResource.checkout();
  check(response, {
    'checkout status is 2xx': (r) => r.status >= 200 && r.status < 300,
  });
});

group('Get orders', () => {
  const ordersResource = new OrdersResource(bearerToken);
  const response = ordersResource.all();

  check(response, {
    'get orders status is 200': (r) => r.status === 200,
    'get orders has data': (r) => JSON.parse(r.body).data.length > 0,
  });

  orderId = JSON.parse(response.body).data[0].id;
  metrics['SAPI38_get_orders'].add(response.timings.duration);
});

group('Get order details', () => {
  const ordersResource = new OrdersResource(bearerToken);
  const response = ordersResource.get(orderId, ['order-shipments', 'concrete-products', 'abstract-products']);

  check(response, {
    'get order details status is 200': (r) => r.status === 200,
    'get order details has body': (r) => !!r.body,
  });

  metrics['SAPI39_get_orders_details'].add(response.timings.duration);
});
```

**Smell 4: Not using tags**

- **Lines:** [56, 62, 65, 70, 71]
- **Snippet:**
```js
checkoutResource.checkout();
const response = ordersResource.all();
metrics['SAPI38_get_orders'].add(response.timings.duration);
const response = ordersResource.get(orderId, ['order-shipments', 'concrete-products', 'abstract-products']);
metrics['SAPI39_get_orders_details'].add(response.timings.duration);
```
- **Refactored:**
```js
group('Place orders', () => {
  const checkoutResource = new CheckoutResource(idCart, customerEmail, bearerToken);
  const response = checkoutResource.checkout({ tags: { flow: 'checkout', endpoint: 'checkout' } });
});

group('Get orders', () => {
  const ordersResource = new OrdersResource(bearerToken);
  const tags = { flow: 'order-history', endpoint: 'get-orders' };
  const response = ordersResource.all({ tags });

  orderId = JSON.parse(response.body).data[0].id;
  metrics['SAPI38_get_orders'].add(response.timings.duration, tags);
});

group('Get order details', () => {
  const ordersResource = new OrdersResource(bearerToken);
  const tags = { flow: 'order-history', endpoint: 'get-order-details' };
  const response = ordersResource.get(orderId, ['order-shipments', 'concrete-products', 'abstract-products'], { tags });
  metrics['SAPI39_get_orders_details'].add(response.timings.duration, tags);
});
```

### `script_266.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [36, 37, 38, 39, 40]
- **Snippet:**
```js
const fixture = new CheckoutFixture({
  customerCount: testConfiguration.vus,
  cartCount: testConfiguration.iterations,
  itemCount: 70,
});
```
- **Refactored:**
```js
/* The fixture instantiation should be moved from the init context to the setup function to ensure it runs only once. The default function should be made stateless, using the VU's execution context to select data. */

// (Remove `const fixture = ...` from the init context)

export function setup() {
  const fixture = new CheckoutFixture({
    customerCount: testConfiguration.vus,
    cartCount: testConfiguration.iterations,
    itemCount: 70,
  });
  return fixture.getData(); // Assume this returns an array of user data
}

export default function (data) {
  // Select data based on the unique iteration number in the scenario
  const { customerEmail, idCart } = data[exec.scenario.iterationInTest % data.length];
  // ... rest of the script
}
```

**Smell 3: Not checking requests**

- **Lines:** [62, 63, 64]
- **Snippet:**
```js
const response = ordersResource.all();

orderId = JSON.parse(response.body).data[0].id;
```
- **Refactored:**
```js
import { check } from 'k6';
import exec from 'k6/execution';
// ...
const response = ordersResource.all();

const isSuccessful = check(response, {
  'GET Orders | status is 200': (r) => r.status === 200,
});

if (!isSuccessful) {
  // Stop the current VU's execution if the check fails
  exec.test.abort('Aborting VU: GET Orders failed.');
}

// Safely access response data after a successful check
orderId = response.json().data[0].id;
```

**Smell 4: Not using tags**

- **Lines:** [65, 71]
- **Snippet:**
```js
metrics['SAPI38_get_orders'].add(response.timings.duration);
```
- **Refactored:**
```js
// Add tags to the metric to allow for more granular filtering and analysis.
metrics['SAPI38_get_orders'].add(response.timings.duration, {
  name: 'GetOrdersList'
});
```

### `script_267.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 2000,
    duration: '10s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 2000,
    duration: '10s',
    thresholds: {
        'http_req_duration': ['p(95)<2000', 'p(99)<2500'],
        'http_req_failed': ['rate<0.01'],
        'checks': ['rate>0.95'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/skillup-service/api/v3/premium/content/courses/enrolled?limit=-1`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/skillup-service/api/v3/premium/content/courses/enrolled?limit=-1`, {
    headers: headers,
    tags: { name: 'GetEnrolledCourses', endpoint: '/skillup-service/api/v3/premium/content/courses/enrolled' },
});
```

### `script_267.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 2000,
    duration: '10s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 2000,
    duration: '10s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/skillup-service/api/v3/premium/content/courses/enrolled?limit=-1`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/skillup-service/api/v3/premium/content/courses/enrolled?limit=-1`, {
    headers: headers,
    tags: {
        endpoint: 'enrolled_courses',
        flow: 'premium_content',
        method: 'GET'
    }
});
```

### `script_267.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 2000,
    duration: '10s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 2000,
    duration: '10s',
    thresholds: {
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<2000'], // 95% of requests must complete below 2000ms
        'checks': ['rate>0.99'], // 99% of checks must pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/skillup-service/api/v3/premium/content/courses/enrolled?limit=-1`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/skillup-service/api/v3/premium/content/courses/enrolled?limit=-1`, {
    headers: headers,
    tags: {
        name: 'GetEnrolledCourses',
    },
});
```

### `script_268.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
    stages: [
        { duration: "10s", target: 20 },
        { duration: "50s", target: 20 }
    ]
};
```
- **Refactored:**
```js
export const options = {
    stages: [
        { duration: "10s", target: 20 },
        { duration: "50s", target: 20 }
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
        'checks': ['rate>0.99']
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [20, 21, 22]
- **Snippet:**
```js
const response = http.post(`${apiUrl}/v-throw/users`, JSON.stringify(request), {
        headers: { "Content-Type": "application/json" }
    });
```
- **Refactored:**
```js
const response = http.post(`${apiUrl}/v-throw/users`, JSON.stringify(request), {
        headers: { "Content-Type": "application/json" },
        tags: { name: 'create_user', endpoint: '/v-throw/users' }
    });
```

### `script_268.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
    stages: [
        { duration: "10s", target: 20 },
        { duration: "50s", target: 20 }
    ]
};
```
- **Refactored:**
```js
export const options = {
    stages: [
        { duration: "10s", target: 20 },
        { duration: "50s", target: 20 }
    ],
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.95']
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [20, 21, 22, 24, 25, 26, 27]
- **Snippet:**
```js
const response = http.post(`${apiUrl}/v-throw/users`, JSON.stringify(request), {
    headers: { "Content-Type": "application/json" }
});

check(response, {
    "response code was 400": (res) => res.status == 400,
    "response code was 409": (res) => res.status == 409
})
```
- **Refactored:**
```js
const tags = { endpoint: 'create_user_validation', flow: 'user_creation_error' };

const response = http.post(`${apiUrl}/v-throw/users`, JSON.stringify(request), {
    headers: { "Content-Type": "application/json" },
    tags
});

check(response, {
    "response code was 400 or 409": (res) => res.status === 400 || res.status === 409
}, tags);
```

### `script_268.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
    stages: [
        { duration: "10s", target: 20 },
        { duration: "50s", target: 20 }
    ]
};
```
- **Refactored:**
```js
export const options = {
    stages: [
        { duration: "10s", target: 20 },
        { duration: "50s", target: 20 }
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [20, 21, 22]
- **Snippet:**
```js
const response = http.post(`${apiUrl}/v-throw/users`, JSON.stringify(request), {
    headers: { "Content-Type": "application/json" }
});
```
- **Refactored:**
```js
const response = http.post(`${apiUrl}/v-throw/users`, JSON.stringify(request), {
    headers: { "Content-Type": "application/json" },
    tags: { name: "CreateUser-Invalid" }
});
```

### `script_269.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9]
- **Snippet:**
```js
export default function () {
    http.get('https://self-signed.badssl.com/');
    sleep(1);
}
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};

export default function () {
    http.get('https://self-signed.badssl.com/');
    sleep(1);
}
```

**Smell 3: Not checking requests**

- **Lines:** [7]
- **Snippet:**
```js
http.get('https://self-signed.badssl.com/');
```
- **Refactored:**
```js
import { check } from 'k6';

export default function () {
    const res = http.get('https://self-signed.badssl.com/');
    check(res, {
        'status is 200': (r) => r.status === 200,
    });
    sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [7]
- **Snippet:**
```js
http.get('https://self-signed.badssl.com/');
```
- **Refactored:**
```js
http.get('https://self-signed.badssl.com/', { tags: { name: 'badssl-homepage', endpoint: 'self-signed' } });
```

### `script_269.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [6]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500']
  }
};

export default function () {
  // test logic
}
```

**Smell 3: Not checking requests**

- **Lines:** [7]
- **Snippet:**
```js
http.get('https://self-signed.badssl.com/');
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default function () {
  const res = http.get('https://self-signed.badssl.com/');
  check(res, {
    'status is 200': (r) => r.status === 200
  });
  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [7]
- **Snippet:**
```js
http.get('https://self-signed.badssl.com/');
```
- **Refactored:**
```js
export default function () {
  const res = http.get('https://self-signed.badssl.com/', {
    tags: {
      endpoint: 'home',
      flow: 'self_signed_badssl'
    }
  });
  sleep(1);
}
```

### `script_269.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [3]
- **Snippet:**
```js
// The script is missing an 'options' export with thresholds.
```
- **Refactored:**
```js
import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [7]
- **Snippet:**
```js
http.get('https://self-signed.badssl.com/');
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const res = http.get('https://self-signed.badssl.com/');
check(res, {
    'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [7]
- **Snippet:**
```js
http.get('https://self-signed.badssl.com/');
```
- **Refactored:**
```js
http.get('https://self-signed.badssl.com/', {
  tags: { name: 'BadSSL-SelfSigned' },
});
```

### `script_27.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '2m', target: 70 },
        { duration: '6m', target: 700 },
        { duration: '2m', target: 70 },
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '2m', target: 70 },
        { duration: '6m', target: 700 },
        { duration: '2m', target: 70 },
    ],
    thresholds: {
        http_req_duration: ['p(95)<1000'],
        http_req_failed: ['rate<0.1'],
        checks: ['rate>0.9'],
        total_failures: ['count<10'],
        check_slow_response: ['count<50'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [32, 33, 34, 35, 36, 42]
- **Snippet:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    }
};
...
res = http.get(url, params);
```
- **Refactored:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    },
    tags: {
        name: 'user_login',
        endpoint: '/v2/user/login',
        flow: 'authentication'
    }
};
...
res = http.get(url, params);
```

### `script_27.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '2m', target: 70 },
        { duration: '6m', target: 700 },
        { duration: '2m', target: 70 },
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '2m', target: 70 },
        { duration: '6m', target: 700 },
        { duration: '2m', target: 70 },
    ],
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<1000'],
        checks: ['rate>0.95'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [32, 33, 34, 35, 36, 42, 70]
- **Snippet:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    }
};

res = http.get(url, params);

check(res, { ... });
```
- **Refactored:**
```js
const tags = {
    endpoint: 'user_login',
    flow: 'login',
    method: 'GET'
};

const params = {
    headers: {
        'Content-Type': 'application/json'
    },
    tags
};

res = http.get(url, params);

check(res, {
    'Status is 200': (r) => r.status === 200,
    'Response time < 1000ms': (r) => r.timings.duration < 1000,
}, tags);
```

### `script_27.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '2m', target: 70 },  // Load normal
        { duration: '6m', target: 700 }, // Lonjakan (simulasi kegagalan)
        { duration: '2m', target: 70 },  // Pemulihan (cek kapan kembali ke normal)
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '2m', target: 70 },
        { duration: '6m', target: 700 },
        { duration: '2m', target: 70 },
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'], // Fail test if error rate > 1%
        'http_req_duration': ['p(95)<1500'], // 95% of requests must be below 1.5s
        'checks': ['rate>0.99'], // Over 99% of checks must pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [32, 33, 34, 35, 36, 42]
- **Snippet:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    }
};

// ...

res = http.get(url, params);
```
- **Refactored:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    },
    tags: {
        name: 'UserLogin',
    },
};

// ...

res = http.get(url, params);
```

### `script_270.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [7, 8, 9, 10]
- **Snippet:**
```js
export const options = {
    // vus: 5,
    duration: '2s',
};
```
- **Refactored:**
```js
export const options = {
    // vus: 5,
    duration: '2s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        'checks': ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [22]
- **Snippet:**
```js
const response = http.post(url, { cookies });
```
- **Refactored:**
```js
const response = http.post(url, { cookies }, {
    tags: { name: 'logout', endpoint: '/auth/cookie/logout/' },
});
```

### `script_270.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [7, 8, 9, 10]
- **Snippet:**
```js
export const options = {
    // vus: 5,
    duration: '2s',
};
```
- **Refactored:**
```js
export const options = {
    duration: '2s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [22, 25, 26, 27]
- **Snippet:**
```js
const response = http.post(url, { cookies });

check(response, {
    [`Status is 200 for ${url}`]: (r) => r.status === 200,
});
```
- **Refactored:**
```js
const tags = {
    endpoint: endpoint,
    flow: 'logout',
};

const params = {
    cookies,
    tags,
};

const response = http.post(url, null, params);

check(response, {
    'status is 200': (r) => r.status === 200,
}, tags);
```

### `script_270.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [7, 8, 9, 10]
- **Snippet:**
```js
export const options = {
    // vus: 5,
    duration: '2s',
};
```
- **Refactored:**
```js
export const options = {
    // vus: 5,
    duration: '2s',
    thresholds: {
        'http_req_failed': ['rate<0.01'], // <1% errors
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [22]
- **Snippet:**
```js
const response = http.post(url, { cookies });
```
- **Refactored:**
```js
const response = http.post(url, {
    cookies,
    tags: {
        name: 'Logout',
    },
});
```

### `script_271.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [6]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};

export default function () {
```

**Smell 3: Not checking requests**

- **Lines:** [7]
- **Snippet:**
```js
http.get('https://www.google.com');
```
- **Refactored:**
```js
import { check } from 'k6';

const res = http.get('https://www.google.com');
check(res, {
  'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [7]
- **Snippet:**
```js
http.get('https://www.google.com');
```
- **Refactored:**
```js
http.get('https://www.google.com', { tags: { name: 'google_homepage', endpoint: 'GET_/' } });
```

### `script_271.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [6]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};

export default function () {
  // test logic
}
```

**Smell 3: Not checking requests**

- **Lines:** [7]
- **Snippet:**
```js
http.get('https://www.google.com');
```
- **Refactored:**
```js
import { check, sleep } from 'k6';

export default function () {
  const res = http.get('https://www.google.com', {
    tags: { endpoint: 'google_homepage' },
  });

  check(res, {
    'GET google homepage returned 200': (r) => r.status === 200,
  });
}
```

**Smell 4: Not using tags**

- **Lines:** [7]
- **Snippet:**
```js
http.get('https://www.google.com');
```
- **Refactored:**
```js
http.get('https://www.google.com', {
  tags: {
    endpoint: 'google_homepage',
    flow: 'homepage_access'
  }
});
```

### `script_271.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5]
- **Snippet:**
```js
// No options object with thresholds is defined.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
  },
};

```

**Smell 3: Not checking requests**

- **Lines:** [7]
- **Snippet:**
```js
http.get('https://www.google.com');
```
- **Refactored:**
```js
const res = http.get('https://www.google.com');
    check(res, {
        'status is 200': (r) => r.status === 200,
    });
```

**Smell 4: Not using tags**

- **Lines:** [7]
- **Snippet:**
```js
http.get('https://www.google.com');
```
- **Refactored:**
```js
http.get('https://www.google.com', {
      tags: { name: 'GoogleHomepage' },
    });
```

### `script_272.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
export let options = Object.assign({}, test_options, {
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
  },
});
```

### `script_273.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
- **Snippet:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: __ENV.RPS,
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100,
            maxVUs: 200,
        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: __ENV.RPS,
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100,
            maxVUs: 200,
        },
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        'checks{scenario:constant_request_rate}': ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [19, 22, 23, 24]
- **Snippet:**
```js
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {headers: { 'Content-Type': 'application/json' }})
```
- **Refactored:**
```js
const httppost = (task, body) => http.post(
    `${hostprefix}/SYNC-${task}`,
    JSON.stringify(body),
    {
        headers: { 'Content-Type': 'application/json' },
        tags: { name: `POST /SYNC-${task}`, endpoint: `/SYNC-${task}` },
    }
);
```

### `script_273.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
- **Snippet:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: __ENV.RPS,
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100,
            maxVUs: 200,
        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: Number(__ENV.RPS),
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100,
            maxVUs: 200,
        },
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [19]
- **Snippet:**
```js
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {headers: { 'Content-Type': 'application/json' }})
```
- **Refactored:**
```js
const httppost = (task, body) => http.post(
    `${hostprefix}/SYNC-${task}`,
    JSON.stringify(body),
    {
        headers: { 'Content-Type': 'application/json' },
        tags: { endpoint: `SYNC-${task}`, operation: body.operation || 'unknown' },
    }
);
```

### `script_273.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 16]
- **Snippet:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: __ENV.RPS, // Equals to RPS
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100, // how large the initial pool of VUs would be
            maxVUs: 200, // if the preAllocatedVUs are not enough, we can initialize more
        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: __ENV.RPS, // Equals to RPS
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100, // how large the initial pool of VUs would be
            maxVUs: 200, // if the preAllocatedVUs are not enough, we can initialize more
        },
    },
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [19]
- **Snippet:**
```js
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {headers: { 'Content-Type': 'application/json' }})
```
- **Refactored:**
```js
const httppost = (task, body) => http.post(
    `${hostprefix}/SYNC-${task}`,
    JSON.stringify(body),
    {
        headers: { 'Content-Type': 'application/json' },
        tags: { name: `SYNC-${task}` },
    }
);
```

### `script_276.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
  stages: [
    { duration: '5m', target: 1 },
  ],
};
```
- **Refactored:**
```js
export let options = {
  stages: [
    { duration: '5m', target: 1 },
  ],
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
    'checks': ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
let response = http.get('https://gqfnc7ztrujstj3fyuzjdzjb2u0nqvus.lambda-url.us-east-2.on.aws');
```
- **Refactored:**
```js
let response = http.get('https://gqfnc7ztrujstj3fyuzjdzjb2u0nqvus.lambda-url.us-east-2.on.aws', {
  tags: { name: 'lambda-get', endpoint: 'root' },
});
```

### `script_276.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
  stages: [
    { duration: '5m', target: 1 },
  ],
};
```
- **Refactored:**
```js
export let options = {
  stages: [
    { duration: '5m', target: 1 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [12, 15, 16, 17]
- **Snippet:**
```js
let response = http.get('https://gqfnc7ztrujstj3fyuzjdzjb2u0nqvus.lambda-url.us-east-2.on.aws');

check(response, {
  'is status 200': (r) => r.status === 200,
});
```
- **Refactored:**
```js
let response = http.get(
  'https://gqfnc7ztrujstj3fyuzjdzjb2u0nqvus.lambda-url.us-east-2.on.aws',
  {
    tags: {
      endpoint: 'lambda_root',
      flow: 'default_flow',
      method: 'GET',
    },
  }
);

check(
  response,
  {
    'is status 200': (r) => r.status === 200,
  },
  {
    endpoint: 'lambda_root',
    flow: 'default_flow',
  }
);
```

### `script_276.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
  stages: [
    { duration: '5m', target: 1 },  // 1 virtual user arriving every second for 5 minutes
  ],
};
```
- **Refactored:**
```js
export let options = {
  stages: [
    { duration: '5m', target: 1 },
  ],
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
let response = http.get('https://gqfnc7ztrujstj3fyuzjdzjb2u0nqvus.lambda-url.us-east-2.on.aws');
```
- **Refactored:**
```js
let response = http.get('https://gqfnc7ztrujstj3fyuzjdzjb2u0nqvus.lambda-url.us-east-2.on.aws', {
    tags: { name: 'Homepage' },
  });
```

### `script_277.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
- **Snippet:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: __ENV.RPS,
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100,
            maxVUs: 200,
        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: __ENV.RPS,
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100,
            maxVUs: 200,
        },
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        'checks{check:A status was 200}': ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [22, 23, 24, 25]
- **Snippet:**
```js
const resCo = httppost("A-128", {
    operation: "test",
})
check(resCo, { 'A status was 200': (r) => r.status == 200 });
```
- **Refactored:**
```js
const resCo = http.post(`${hostprefix}/SYNC-A-128`, JSON.stringify({ operation: 'test' }), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'SYNC-A-128', endpoint: '/SYNC-A-128' },
});
check(resCo, { 'A status was 200': (r) => r.status == 200 }, { tags: { name: 'SYNC-A-128' } });
```

### `script_277.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
- **Snippet:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: __ENV.RPS,
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100,
            maxVUs: 200,
        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: Number(__ENV.RPS),
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100,
            maxVUs: 200,
        },
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [19, 25]
- **Snippet:**
```js
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {headers: { 'Content-Type': 'application/json' }})

check(resCo, { 'A status was 200': (r) => r.status == 200 });
```
- **Refactored:**
```js
const httppost = (task, body) => http.post(
    `${hostprefix}/SYNC-${task}`,
    JSON.stringify(body),
    {
        headers: { 'Content-Type': 'application/json' },
        tags: { endpoint: `SYNC-${task}`, task },
    }
);

export default function () {
    const task = 'A-128';
    const resCo = httppost(task, {
        operation: 'test',
    });
    check(resCo, { 'A status was 200': (r) => r.status === 200 }, { endpoint: `SYNC-${task}`, task });
}
```

### `script_277.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 16]
- **Snippet:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: __ENV.RPS, // Equals to RPS
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100, // how large the initial pool of VUs would be
            maxVUs: 200, // if the preAllocatedVUs are not enough, we can initialize more
        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        constant_request_rate: {
            executor: 'constant-arrival-rate',
            rate: __ENV.RPS, // Equals to RPS
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100, // how large the initial pool of VUs would be
            maxVUs: 200, // if the preAllocatedVUs are not enough, we can initialize more
        },
    },
    thresholds: {
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [19]
- **Snippet:**
```js
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {headers: { 'Content-Type': 'application/json' }})
```
- **Refactored:**
```js
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {headers: { 'Content-Type': 'application/json' }, tags: { name: `SYNC-${task}` }})
```

### `script_278.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [45]
- **Snippet:**
```js
const db = sql.open('postgres', pgConnectionString)
```
- **Refactored:**
```js
// Move the database connection opening inside the default function or setup,
// so it is not executed in the init context for every VU at startup.
// Option 1: open connection per VU inside the default function
export default () => {
  const db = sql.open('postgres', pgConnectionString)
  // ... rest of the function
  db.close()
}

// Option 2: use setup() to open a shared connection if the extension supports it
export function setup() {
  const db = sql.open('postgres', pgConnectionString)
  return { db }
}
export default (data) => {
  const db = data.db
  // ... rest of the function
}
```

**Smell 4: Not using tags**

- **Lines:** [58, 59, 60, 61]
- **Snippet:**
```js
db.exec(
  'insert into positions (stud_id,first_name,last_name,title,reports_to,timestamp,location,email) ' +
    `values(${name}, 'Virtual ${name}', 'User ${name}', 'Load Tester', 1, ${Date.now()}, st_point(-73.946${x}, 40.807${y}), 'vu${name}@chinookcorp.com');`
)
```
- **Refactored:**
```js
// Add tags to the trend and counter metrics to allow filtering by operation type
insertTrend.add(exFinish - exStart, { operation: 'insert', table: 'positions' })
counterInserts.add(1, { operation: 'insert', table: 'positions' })
myFailRate.add(false, { operation: 'insert', table: 'positions' })
// In the catch block:
myFailRate.add(true, { operation: 'insert', table: 'positions' })
counterFailed.add(1, { operation: 'insert', table: 'positions' })
```

### `script_278.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [45]
- **Snippet:**
```js
const db = sql.open('postgres', pgConnectionString)
```
- **Refactored:**
```js
let db

export function setup() {
  return { pgConnectionString }
}

export default (data) => {
  if (!db) {
    db = sql.open('postgres', data.pgConnectionString)
  }
  // test logic using db
}

export function teardown() {
  if (db) {
    db.exec("delete from public.positions where title='Load Tester'")
    db.close()
  }
}
```

**Smell 4: Not using tags**

- **Lines:** [62, 65, 66, 69, 70]
- **Snippet:**
```js
myFailRate.add(false)
myFailRate.add(true)
counterFailed.add(1)
counterInserts.add(1)
insertTrend.add(exFinish - exStart)
```
- **Refactored:**
```js
const tags = { operation: 'insert_position', scenario: 'pg_single_insert' }

myFailRate.add(false, tags)
myFailRate.add(true, tags)
counterFailed.add(1, tags)
counterInserts.add(1, tags)
insertTrend.add(exFinish - exStart, tags)
```

### `script_278.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [62, 65, 66, 69, 70]
- **Snippet:**
```js
myFailRate.add(false)
//...
myFailRate.add(true)
counterFailed.add(1)
//...
counterInserts.add(1)
insertTrend.add(exFinish - exStart)
```
- **Refactored:**
```js
const tags = { query: 'insert_positions' };
myFailRate.add(false, tags);
//...
myFailRate.add(true, tags);
counterFailed.add(1, tags);
//...
counterInserts.add(1, tags);
insertTrend.add(exFinish - exStart, tags);
```

### `script_279.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
- **Snippet:**
```js
export const options = {
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '90s',
      preAllocatedVUs: 50,
      rate: 50,
      timeUnit: '1s',
    },
  },
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '90s',
      preAllocatedVUs: 50,
      rate: 50,
      timeUnit: '1s',
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    'checks': ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [25]
- **Snippet:**
```js
const res = http.get('http://localhost:3000/products', { headers });
```
- **Refactored:**
```js
const res = http.get('http://localhost:3000/products', { headers, tags: { name: 'GetProducts', endpoint: '/products' } });
```

### `script_279.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
- **Snippet:**
```js
export const options = {
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '90s',
      preAllocatedVUs: 50,
      rate: 50,
      timeUnit: '1s',
    },
  },
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '90s',
      preAllocatedVUs: 50,
      rate: 50,
      timeUnit: '1s',
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [25, 28]
- **Snippet:**
```js
const res = http.get('http://localhost:3000/products', { headers });

check(res, {
  'Get status is 200': (r) => res.status === 200,
});
```
- **Refactored:**
```js
const requestTags = { endpoint: 'products', flow: 'list_products', method: 'GET' };
const res = http.get('http://localhost:3000/products', {
  headers,
  tags: requestTags,
});

check(res, {
  'Get status is 200': (r) => r.status === 200,
}, requestTags);
```

### `script_279.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
- **Snippet:**
```js
export const options = {
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '90s', // total duration
      preAllocatedVUs: 50, // to allocate runtime resources

      rate: 50, // number of constant iterations given `timeUnit`
      timeUnit: '1s',
    },
  },
};
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
  },
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '90s', // total duration
      preAllocatedVUs: 50, // to allocate runtime resources

      rate: 50, // number of constant iterations given `timeUnit`
      timeUnit: '1s',
    },
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [25]
- **Snippet:**
```js
const res = http.get('http://localhost:3000/products', { headers });
```
- **Refactored:**
```js
const res = http.get('http://localhost:3000/products', {
    headers,
    tags: {
      name: 'GetProducts',
    },
  });
```

### `script_28.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 81, 82, 83, 84, 85, 86, 87]
- **Snippet:**
```js
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = usersRaw.map(line => {
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    ...
}).filter(...);

for (let panelId = 1; panelId <= MAX_PANEL_ID; panelId++) {
    panelMetrics[panelId] = {
        responseTime: new Trend(`panel_response_time_${panelId}`, true),
        successRate: new Rate(`panel_success_rate_${panelId}`, true),
        failureRate: new Rate(`panel_failure_rate_${panelId}`, true)
    };
}
```
- **Refactored:**
```js
// Reading and parsing the file is acceptable in init context since open() is only allowed there,
// but the heavy map/filter/split chain and the creation of 150*3=450 custom metric objects
// in a loop are costly. Limit metric objects to what is actually needed, or defer panel
// metric creation to the default function using a lazy-init pattern, and keep file parsing minimal.

// Lighter init-context file parsing:
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n').filter(l => l.trim().length > 0);
const users = usersRaw.map(line => {
    const parts = line.split(',');
    return {
        username: parts[0],
        password: parts[1],
        vunetSession: parts[2],
        xVuNetHTTPInfo: parts[3],
        grafanaSessionExpiry: parseInt(parts[4], 10)
    };
}).filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);

// Instead of pre-creating 450 metric objects for all possible panel IDs,
// use a smaller fixed set of aggregate metrics and tag them with panelId:
const panelResponseTime = new Trend('panel_response_time', true);
const panelSuccessRate = new Rate('panel_success_rate', true);
const panelFailureRate = new Rate('panel_failure_rate', true);
// Then in the default function, add with panelId tag instead of per-panel metric objects.
```

**Smell 2: Do not use thresholds**

- **Lines:** [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
- **Snippet:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    }
};
```
- **Refactored:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    },
    thresholds: {
        'dashboard_success_rate': ['rate>0.95'],
        'dashboard_response_time': ['p(95)<2000'],
        'panel_success_rate': ['rate>0.95'],
        'panel_response_time': ['p(95)<3000'],
        'http_req_duration_custom': ['p(99)<5000'],
        'checks': ['rate>0.95']
    }
};
```

### `script_28.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
- **Snippet:**
```js
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = usersRaw.map(line => {
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    return {
        username,
        password,
        vunetSession,
        xVuNetHTTPInfo,
        grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10)
    };
}).filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

const users = new SharedArray('users', function () {
    return open('/home/vunet/user_creation_k6/user_cookies.txt')
        .split('\n')
        .map(line => {
            const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
            return {
                username,
                password,
                vunetSession,
                xVuNetHTTPInfo,
                grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10)
            };
        })
        .filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
});
```

**Smell 2: Do not use thresholds**

- **Lines:** [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
- **Snippet:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
   // iterations: 5,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    }
};
```
- **Refactored:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<2000'],
        checks: ['rate>0.95'],
        dashboard_success_rate: ['rate>0.95'],
        dashboard_response_time: ['p(95)<2000']
    }
};
```

### `script_28.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
- **Snippet:**
```js
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = usersRaw.map(line => {
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    return {
        username,
        password,
        vunetSession,
        xVuNetHTTPInfo,
        grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10)
    };
}).filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

const users = new SharedArray('users', function () {
  const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
  return usersRaw.map(line => {
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    return {
        username,
        password,
        vunetSession,
        xVuNetHTTPInfo,
        grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10)
    };
  }).filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
});
```

**Smell 2: Do not use thresholds**

- **Lines:** [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
- **Snippet:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
   // iterations: 5,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    }
};
```
- **Refactored:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    },
    thresholds: {
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<1000'],  // 95% of requests must complete below 1s
        'checks': ['rate>0.99'],             // 99% of checks must pass
        'dashboard_response_time{endpoint:dashboard}': ['p(90)<400'] // 90% of dashboard metadata loads must be below 400ms
    }
};
```

### `script_280.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
    vus: 1000,
    duration: '100s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 1000,
    duration: '100s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        'checks{scenario:default}': ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [27]
- **Snippet:**
```js
let authResponse = http.post(`${BASE_URL}${AUTH_ENDPOINT}`, authPayload, authHeaders);
```
- **Refactored:**
```js
let authHeaders = {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'authenticateUser', endpoint: AUTH_ENDPOINT },
};
let authResponse = http.post(`${BASE_URL}${AUTH_ENDPOINT}`, authPayload, authHeaders);
```

### `script_280.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
    vus: 1000,
    duration: '100s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 1000,
    duration: '100s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [22, 23, 24, 27, 30, 31, 32, 33]
- **Snippet:**
```js
let authHeaders = {
    headers: { 'Content-Type': 'application/json' },
};

let authResponse = http.post(`${BASE_URL}${AUTH_ENDPOINT}`, authPayload, authHeaders);

check(authResponse, {
    'authentication response status is 200': (r) => r.status === 200,
    'authentication successful': (r) => r.json('token') !== '',
});
```
- **Refactored:**
```js
let authParams = {
    headers: { 'Content-Type': 'application/json' },
    tags: { endpoint: 'authenticateUser', flow: 'authentication' },
};

let authResponse = http.post(`${BASE_URL}${AUTH_ENDPOINT}`, authPayload, authParams);

check(authResponse, {
    'authentication response status is 200': (r) => r.status === 200,
    'authentication successful': (r) => r.json('token') !== '',
}, { endpoint: 'authenticateUser', flow: 'authentication' });
```

### `script_280.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
    vus: 1000, // Number of virtual users
    duration: '100s', // Duration of the test
};
```
- **Refactored:**
```js
export let options = {
    vus: 1000,
    duration: '100s',
    thresholds: {
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [27]
- **Snippet:**
```js
let authResponse = http.post(`${BASE_URL}${AUTH_ENDPOINT}`, authPayload, authHeaders);
```
- **Refactored:**
```js
let params = {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'Authentication' },
};

let authResponse = http.post(`${BASE_URL}${AUTH_ENDPOINT}`, authPayload, params);
```

### `script_281.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [20]
- **Snippet:**
```js
let response = http.get('https://test-api.k6.io/public/crocodiles/')
```
- **Refactored:**
```js
import { check, sleep } from 'k6'
import http from 'k6/http'

export const options = {
    stages: [
        { duration: '1m', target: 20 },
        { duration: '3m', target: 20 },
        { duration: '1m', target: 0 },
    ],
    thresholds: {
        http_req_failed: ['rate<0.02'],
        http_req_duration: ['p(95)<2000'],
    }
}

export default function main() {
    let response = http.get('https://test-api.k6.io/public/crocodiles/')
    check(response, {
        'status is 200': (r) => r.status === 200,
        'response body is not empty': (r) => r.body && r.body.length > 0,
    })
    sleep(1)
}
```

**Smell 4: Not using tags**

- **Lines:** [20]
- **Snippet:**
```js
let response = http.get('https://test-api.k6.io/public/crocodiles/')
```
- **Refactored:**
```js
let response = http.get('https://test-api.k6.io/public/crocodiles/', { tags: { name: 'GetCrocodiles', endpoint: 'public/crocodiles' } })
```

### `script_281.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [20]
- **Snippet:**
```js
let response = http.get('https://test-api.k6.io/public/crocodiles/')
```
- **Refactored:**
```js
import { sleep, check } from 'k6'
import http from 'k6/http'

export default function main() {
    const response = http.get('https://test-api.k6.io/public/crocodiles/')
    check(response, {
        'GET /public/crocodiles/ status is 200': (res) => res.status === 200,
        'GET /public/crocodiles/ response is not empty': (res) => res.body && res.body.length > 0,
    })
    sleep(1)
}
```

**Smell 4: Not using tags**

- **Lines:** [20]
- **Snippet:**
```js
let response = http.get('https://test-api.k6.io/public/crocodiles/')
```
- **Refactored:**
```js
export default function main() {
    const response = http.get('https://test-api.k6.io/public/crocodiles/', {
        tags: {
            endpoint: 'public_crocodiles',
            flow: 'list_crocodiles',
            method: 'GET'
        }
    })
    sleep(1)
}
```

### `script_281.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [20]
- **Snippet:**
```js
let response = http.get('https://test-api.k6.io/public/crocodiles/')
```
- **Refactored:**
```js
import { sleep, check } from 'k6'
import http from 'k6/http'

// ...

export default function main() {
    let response = http.get('https://test-api.k6.io/public/crocodiles/')
    check(response, { 'status is 200': (r) => r.status === 200 });
    sleep(1)
}
```

**Smell 4: Not using tags**

- **Lines:** [20]
- **Snippet:**
```js
let response = http.get('https://test-api.k6.io/public/crocodiles/')
```
- **Refactored:**
```js
export default function main() {
    let response = http.get('https://test-api.k6.io/public/crocodiles/', {
        tags: { name: 'PublicCrocodiles' },
    });
    sleep(1);
}
```

### `script_282.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [14, 15, 16, 17, 18]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '30s', target: 10 }
    ]
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '30s', target: 10 }
    ],
    thresholds: {
        'http_req_duration': ['p(95)<500'],
        'http_req_failed': ['rate<0.01'],
        'checks': ['rate>0.99']
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [24]
- **Snippet:**
```js
const response = storeOrderGetService.execute();
```
- **Refactored:**
```js
const response = storeOrderGetService.execute({ tags: { name: 'getStoreOrderById', endpoint: '/store/order' } });
```

### `script_282.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [14, 15, 16, 17, 18]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '30s', target: 10 }
    ]
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '30s', target: 10 }
    ],
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99']
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [24, 25, 26, 27]
- **Snippet:**
```js
const response = storeOrderGetService.execute();
check(response, {
    'Get store order by Id Status is 200': (r) => r.status === 200,
});
```
- **Refactored:**
```js
export default function () {
    const tags = { endpoint: 'get_store_order_by_id', flow: 'store_order' };
    const response = storeOrderGetService.execute({ tags });
    check(response, {
        'Get store order by Id Status is 200': (r) => r.status === 200,
    }, tags);
}
```

### `script_282.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [14, 15, 16, 17, 18]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '30s', target: 10 }
    ]
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '30s', target: 10 }
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [24]
- **Snippet:**
```js
const response = storeOrderGetService.execute();
```
- **Refactored:**
```js
// The service function should be modified to accept and apply tags to the HTTP request.
// For example, by passing a params object.
const response = storeOrderGetService.execute({
    tags: {
        name: 'GetStoreOrder',
    },
});
```

### `script_285.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [47, 49]
- **Snippet:**
```js
const response = cartsResource.get(idCart, ['items']);

    metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
import { check } from 'k6';

// inside the group:
const response = cartsResource.get(idCart, ['items']);

check(response, {
  'get cart by id status is 200': (r) => r.status === 200,
  'get cart by id has body': (r) => r.body && r.body.length > 0,
});

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```

**Smell 4: Not using tags**

- **Lines:** [47]
- **Snippet:**
```js
const response = cartsResource.get(idCart, ['items']);
```
- **Refactored:**
```js
const response = cartsResource.get(idCart, ['items'], {
  tags: { endpoint: 'get_cart_by_id', group: testConfiguration.group, testId: testConfiguration.id },
});
```

### `script_285.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [47]
- **Snippet:**
```js
const response = cartsResource.get(idCart, ['items']);
```
- **Refactored:**
```js
import { group, check } from 'k6';

...

group(testConfiguration.group, () => {
  const cartsResource = new CartsResource(bearerToken);
  const tags = { endpoint: 'get_carts_by_id', group: testConfiguration.group };
  const response = cartsResource.get(idCart, ['items'], { tags });

  check(response, {
    'GET cart by id returned 200': (r) => r.status === 200,
    'GET cart by id returned a body': (r) => !!r.body,
  }, tags);

  metrics[testConfiguration.metrics[0]].add(response.timings.duration, tags);
});
```

**Smell 4: Not using tags**

- **Lines:** [47, 49]
- **Snippet:**
```js
const response = cartsResource.get(idCart, ['items']);
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
group(testConfiguration.group, () => {
  const cartsResource = new CartsResource(bearerToken);
  const tags = { endpoint: 'get_carts_by_id', group: testConfiguration.group };
  const response = cartsResource.get(idCart, ['items'], { tags });

  metrics[testConfiguration.metrics[0]].add(response.timings.duration, tags);
});
```

### `script_285.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [27, 28, 29, 30, 31]
- **Snippet:**
```js
const fixture = new CartFixture({
  customerCount: testConfiguration.vus ?? EnvironmentUtil.getRampVus(),
  cartCount: 1,
  itemCount: 70,
});
```
- **Refactored:**
```js
// The fixture instantiation should be moved from the init context to the setup function.
// The default function must be updated to not depend on the fixture instance.
export function setup() {
  const fixture = new CartFixture({
    customerCount: testConfiguration.vus ?? EnvironmentUtil.getRampVus(),
    cartCount: 1,
    itemCount: 70,
  });
  return fixture.getData(); // Returns all data needed by VUs
}

export default function (data) {
  // Replace instance method with logic that uses the data from setup
  const vuData = data.customers[exec.vu.idInTest - 1];
  const { customerEmail, idCart } = { customerEmail: vuData.email, idCart: vuData.carts[0].id };
  // ... rest of the script
}
```

**Smell 3: Not checking requests**

- **Lines:** [47]
- **Snippet:**
```js
const response = cartsResource.get(idCart, ['items']);
```
- **Refactored:**
```js
import { check } from 'k6';
// ...

// inside the default function
const response = cartsResource.get(idCart, ['items']);

check(response, {
  'GET Cart by ID status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [47]
- **Snippet:**
```js
const response = cartsResource.get(idCart, ['items']);
```
- **Refactored:**
```js
// The underlying resource method should be updated to accept and use tags.
const response = cartsResource.get(idCart, ['items'], {
  tags: {
    name: 'SAPI32_GetCartByID',
  },
});
```

### `script_286.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [39, 40, 41, 42]
- **Snippet:**
```js
export const options = {
  duration: `${baseDuration}s`,
  vus: virtualUsers,
}
```
- **Refactored:**
```js
export const options = {
  duration: `${baseDuration}s`,
  vus: virtualUsers,
  thresholds: {
    'inserts': ['count>0'],
    'iteration_duration': ['p(95)<2000'],
  },
}
```

**Smell 3: Not checking requests**

- **Lines:** [59, 60, 61, 62, 63]
- **Snippet:**
```js
db.exec(
  `insert into rls_messages_authenticated (domain) values ('${
    domains[getRandomInt(0, 5)]
  }');`
)
```
- **Refactored:**
```js
import { check } from 'k6';

// inside the default function:
let result;
try {
  result = db.exec(
    `insert into rls_messages_authenticated (domain) values ('${
      domains[getRandomInt(0, 5)]
    }');`
  );
  check(result, {
    'insert succeeded': (r) => r !== null && r !== undefined,
  });
} catch (e) {
  check(null, { 'insert succeeded': () => false });
  console.error(`DB exec failed: ${e}`);
}
```

**Smell 4: Not using tags**

- **Lines:** [59, 60, 61, 62, 63]
- **Snippet:**
```js
db.exec(
  `insert into rls_messages_authenticated (domain) values ('${
    domains[getRandomInt(0, 5)]
  }');`
)
```
- **Refactored:**
```js
import { tagWithCurrentStageIndex } from 'k6/execution';

// Apply tags to the metric tracking the insert operation:
counterInserts.add(1, { operation: 'insert', table: 'rls_messages_authenticated' });

// And annotate the exec call context with tags via k6 group or custom metric tags:
// group('insert rls_messages_authenticated', () => {
//   db.exec(`insert into rls_messages_authenticated (domain) values ('...');`);
// });
```

### `script_286.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [39, 40, 41, 42]
- **Snippet:**
```js
export const options = {
  duration: `${baseDuration}s`,
  vus: virtualUsers,
}
```
- **Refactored:**
```js
export const options = {
  duration: `${baseDuration}s`,
  vus: virtualUsers,
  thresholds: {
    inserts: ['count>0'],
    iteration_duration: ['p(95)<1000'],
  },
}
```

**Smell 4: Not using tags**

- **Lines:** [65]
- **Snippet:**
```js
counterInserts.add(1)
```
- **Refactored:**
```js
const domain = domains[getRandomInt(0, 5)]
db.exec(`insert into rls_messages_authenticated (domain) values ('${domain}');`)
counterInserts.add(1, { operation: 'insert', table: 'rls_messages_authenticated', domain })
```

### `script_286.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [39, 40, 41, 42]
- **Snippet:**
```js
export const options = {
  duration: `${baseDuration}s`,
  vus: virtualUsers,
}
```
- **Refactored:**
```js
export const options = {
  duration: `${baseDuration}s`,
  vus: virtualUsers,
  thresholds: {
    'iteration_duration': ['p(95)<500'], // e.g., 95% of iterations must be below 500ms
    'inserts': ['count>0'], // e.g., ensure at least one insert succeeded
  },
}
```

**Smell 3: Not checking requests**

- **Lines:** [59, 65]
- **Snippet:**
```js
db.exec(
  `insert into rls_messages_authenticated (domain) values ('${
    domains[getRandomInt(0, 5)]
  }');`
)
const finish = new Date()
counterInserts.add(1)
```
- **Refactored:**
```js
try {
  db.exec(
    `insert into rls_messages_authenticated (domain) values ('${domains[getRandomInt(0, 5)]}');`
  );
  // Only increment the counter on a successful operation
  counterInserts.add(1);
} catch (e) {
  console.error(`DB insert failed: ${e}`);
}
const finish = new Date();
```

**Smell 4: Not using tags**

- **Lines:** [60, 61, 62, 65]
- **Snippet:**
```js
`insert into rls_messages_authenticated (domain) values ('${
  domains[getRandomInt(0, 5)]
}');`
//...
counterInserts.add(1)
```
- **Refactored:**
```js
const domain = domains[getRandomInt(0, 5)];
db.exec(
  `insert into rls_messages_authenticated (domain) values ('${domain}');`
);
//...
counterInserts.add(1, { domain: domain });
```

### `script_287.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
  vus: 10,
  duration: '30s',
};
```
- **Refactored:**
```js
export const options = {
  vus: 10,
  duration: '30s',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    'checks': ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [10]
- **Snippet:**
```js
let res = http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
let res = http.get('https://quickpizza.grafana.com', { tags: { name: 'QuickPizzaHomePage', endpoint: 'homepage' } });
```

### `script_287.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
  vus: 10,
  duration: '30s',
};
```
- **Refactored:**
```js
export const options = {
  vus: 10,
  duration: '30s',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [10, 11]
- **Snippet:**
```js
let res = http.get('https://quickpizza.grafana.com');
check(res, { 'status is 200': (res) => res.status === 200 });
```
- **Refactored:**
```js
const tags = { endpoint: 'home', flow: 'browse' };
let res = http.get('https://quickpizza.grafana.com', { tags });
check(res, { 'status is 200': (res) => res.status === 200 }, tags);
```

### `script_287.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
  vus: 10,
  duration: '30s',
};
```
- **Refactored:**
```js
export const options = {
  vus: 10,
  duration: '30s',
  thresholds: {
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests must complete below 500ms
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [10]
- **Snippet:**
```js
let res = http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
let res = http.get('https://quickpizza.grafana.com', { tags: { name: 'Homepage' } });
```

### `script_288.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [73, 74, 75]
- **Snippet:**
```js
const response = checkoutResource.checkout();
const responseJson = JSON.parse(response.body);
orderReference = responseJson.data.attributes.orderReference;
```
- **Refactored:**
```js
const response = checkoutResource.checkout();
if (check(response, { 'Checkout succeeded': (r) => r.status === 200 })) {
  const responseJson = JSON.parse(response.body);
  orderReference = responseJson.data.attributes.orderReference;
}
```

**Smell 3: Not checking requests**

- **Lines:** [80, 81, 82, 83]
- **Snippet:**
```js
const response = orderAmendmentResource.amendOrder();
const responseJson = JSON.parse(response.body);
metrics['SAPI20_post_cart_reorder'].add(response.timings.duration);
reorderedIdCart = responseJson.data.id;
```
- **Refactored:**
```js
const response = orderAmendmentResource.amendOrder();
metrics['SAPI20_post_cart_reorder'].add(response.timings.duration);
if (check(response, { 'Start Order Amendment succeeded': (r) => r.status === 200 })) {
  const responseJson = JSON.parse(response.body);
  reorderedIdCart = responseJson.data.id;
}
```

**Smell 3: Not checking requests**

- **Lines:** [88, 89]
- **Snippet:**
```js
const response = cartsResource.delete(reorderedIdCart);
metrics['SAPI21_delete_carts'].add(response.timings.duration);
```
- **Refactored:**
```js
const response = cartsResource.delete(reorderedIdCart);
check(response, { 'Cancel Order Amendment succeeded': (r) => r.status === 204 });
metrics['SAPI21_delete_carts'].add(response.timings.duration);
```

**Smell 3: Not checking requests**

- **Lines:** [93, 94, 95]
- **Snippet:**
```js
const response = orderAmendmentResource.amendOrder();
const responseJson = JSON.parse(response.body);
reorderedIdCart = responseJson.data.id;
```
- **Refactored:**
```js
const response = orderAmendmentResource.amendOrder();
if (check(response, { 'Start Order Amendment (2nd time) succeeded': (r) => r.status === 200 })) {
  const responseJson = JSON.parse(response.body);
  reorderedIdCart = responseJson.data.id;
}
```

**Smell 3: Not checking requests**

- **Lines:** [100, 101]
- **Snippet:**
```js
const response = checkoutResource.checkout();
metrics['SAPI22_post_checkout'].add(response.timings.duration);
```
- **Refactored:**
```js
const response = checkoutResource.checkout();
check(response, { 'Finish Order Amendment (Checkout) succeeded': (r) => r.status === 200 });
metrics['SAPI22_post_checkout'].add(response.timings.duration);
```

### `script_289.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 31]
- **Snippet:**
```js
export default function () { ... }
```
- **Refactored:**
```js
export const options = {
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
    },
};

export default function () { ... }
```

**Smell 3: Not checking requests**

- **Lines:** [24, 28, 29, 30, 31]
- **Snippet:**
```js
const responses = http.batch(request);
// check(responses[2], {
//     'form data OK': (res) => JSON.parse(res.body)['form']['hello'] == 'world!',
// });
```
- **Refactored:**
```js
const responses = http.batch(request);
responses.forEach((res, index) => {
    check(res, {
        [`response ${index} status is 200`]: (r) => r.status === 200,
    });
});
```

**Smell 4: Not using tags**

- **Lines:** [16, 17, 18, 19, 20]
- **Snippet:**
```js
request.push({
    method: 'GET',
    url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
    params: params
});
```
- **Refactored:**
```js
request.push({
    method: 'GET',
    url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
    params: {
        ...params,
        tags: { name: 'user_search', endpoint: '/user/search' },
    },
});
```

### `script_289.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [1, 31]
- **Snippet:**
```js
No export const options with thresholds is defined anywhere in the script.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [24, 28, 29, 30]
- **Snippet:**
```js
const responses = http.batch(request);

// check(responses[2], {
//     'form data OK': (res) => JSON.parse(res.body)['form']['hello'] == 'world!',
// });
```
- **Refactored:**
```js
const responses = http.batch(request);

responses.forEach((res) => {
  check(res, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
  });
});
```

**Smell 4: Not using tags**

- **Lines:** [4, 8, 16, 20]
- **Snippet:**
```js
const params = {
    headers: {
        'Authorization': 'Bearer ...',
    },
};

request.push({
    method: 'GET',
    url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
    params: params
});
```
- **Refactored:**
```js
const params = {
  headers: {
    'Authorization': 'Bearer ...',
  },
  tags: {
    endpoint: 'user_search',
    flow: 'search_user',
  },
};

request.push({
  method: 'GET',
  url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
  params,
});
```

### `script_289.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [10]
- **Snippet:**
```js
// No options or thresholds are defined in the script.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [24, 25, 26, 27, 28, 29, 30]
- **Snippet:**
```js
const responses = http.batch(request);

    // httpbin.test.k6.io should return our POST data in the response body, so
    // we check the third response object to see that the POST worked.
    // check(responses[2], {
    //     'form data OK': (res) => JSON.parse(res.body)['form']['hello'] == 'world!',
    // });
```
- **Refactored:**
```js
const responses = http.batch(request);

    responses.forEach((res) => {
      check(res, {
        'status is 200': (r) => r.status === 200,
      });
    });
```

**Smell 4: Not using tags**

- **Lines:** [15, 16, 17, 18, 19, 20, 21]
- **Snippet:**
```js
for (let req = 0; req < countRequest; req++) {
        request.push({
            method: 'GET',
            url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
            params: params
        });
    }
```
- **Refactored:**
```js
for (let req = 0; req < countRequest; req++) {
        request.push({
            method: 'GET',
            url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
            params: {
                ...params,
                tags: { name: 'UserSearch' }
            }
        });
    }
```

### `script_29.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
- **Snippet:**
```js
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = usersRaw.map(line => {
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    return {
        username,
        password,
        vunetSession,
        xVuNetHTTPInfo,
        grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10)
    };
}).filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
```
- **Refactored:**
```js
// Reading the file is unavoidable in init context, but parsing and filtering
// should be as lightweight as possible. Pre-parse only what is strictly needed
// and avoid chaining heavy map+filter in the global scope for large files.
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = [];
for (let i = 0; i < usersRaw.length; i++) {
    const parts = usersRaw[i].split(',');
    if (parts.length < 5) continue;
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiryRaw] = parts;
    const grafanaSessionExpiry = parseInt(grafanaSessionExpiryRaw, 10);
    if (vunetSession && xVuNetHTTPInfo && grafanaSessionExpiry) {
        users.push({ username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry });
    }
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [28, 29, 30, 31, 32, 33, 34, 35, 36]
- **Snippet:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance'
    }
};
```
- **Refactored:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance'
    },
    thresholds: {
        'dashboard_response_time': ['p(95)<2000'],
        'dashboard_success_rate': ['rate>0.95'],
        'http_req_duration_custom': ['p(95)<3000'],
        'http_req_failed': ['rate<0.05']
    }
};
```

### `script_29.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [28, 29, 30, 31, 32, 33, 34, 35, 36]
- **Snippet:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance'
    }
};
```
- **Refactored:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance'
    },
    thresholds: {
        'http_req_failed': ['rate<0.01'],      // http errors should be less than 1%
        'http_req_duration': ['p(95)<1500'],   // 95% of requests must complete below 1.5s
        'dashboard_success_rate': ['rate>0.99'], // custom success rate metric > 99%
        'checks': ['rate>0.99']                // the rate of successful checks should be > 99%
    }
};
```

### `script_290.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [54, 55, 56, 57, 61, 63]
- **Snippet:**
```js
group('Gets customer cart info', () => {
    const response = cartsResource.get(idCart, ['items']);
    const bodyJson = JSON.parse(response.body);
    skuForRemove = bodyJson.included[0].attributes.sku;
  });

  group(testConfiguration.group, () => {
    const response = cartsResource.removeItem(idCart, skuForRemove);
    metrics[testConfiguration.metrics[0]].add(response.timings.duration);
  });
```
- **Refactored:**
```js
import { check } from 'k6';

group('Gets customer cart info', () => {
    const response = cartsResource.get(idCart, ['items']);
    const checkResult = check(response, {
      'get cart status is 200': (r) => r.status === 200,
      'get cart body has included items': (r) => {
        try {
          const body = JSON.parse(r.body);
          return Array.isArray(body.included) && body.included.length > 0;
        } catch (e) {
          return false;
        }
      },
    });
    if (checkResult) {
      const bodyJson = JSON.parse(response.body);
      skuForRemove = bodyJson.included[0].attributes.sku;
    }
  });

  group(testConfiguration.group, () => {
    const response = cartsResource.removeItem(idCart, skuForRemove);
    check(response, {
      'remove cart item status is 204': (r) => r.status === 204,
    });
    metrics[testConfiguration.metrics[0]].add(response.timings.duration);
  });
```

**Smell 4: Not using tags**

- **Lines:** [54, 61]
- **Snippet:**
```js
const response = cartsResource.get(idCart, ['items']);
...
const response = cartsResource.removeItem(idCart, skuForRemove);
```
- **Refactored:**
```js
// Pass tags through the resource methods or add them via params
// Example assuming cartsResource methods accept a params argument:
group('Gets customer cart info', () => {
    const response = cartsResource.get(idCart, ['items'], { tags: { name: 'GetCartInfo', endpoint: 'GET /carts/{idCart}', group: 'Cart' } });
    const checkResult = check(response, {
      'get cart status is 200': (r) => r.status === 200,
    });
    if (checkResult) {
      const bodyJson = JSON.parse(response.body);
      skuForRemove = bodyJson.included[0].attributes.sku;
    }
  });

  group(testConfiguration.group, () => {
    const response = cartsResource.removeItem(idCart, skuForRemove, { tags: { name: 'DeleteCartItem', endpoint: 'DELETE /carts/{idCart}/items/{sku}', group: 'Cart' } });
    check(response, {
      'remove cart item status is 204': (r) => r.status === 204,
    });
    metrics[testConfiguration.metrics[0]].add(response.timings.duration);
  });
```

### `script_290.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [54, 61]
- **Snippet:**
```js
const response = cartsResource.get(idCart, ['items']);
const bodyJson = JSON.parse(response.body);
skuForRemove = bodyJson.included[0].attributes.sku;
...
const response = cartsResource.removeItem(idCart, skuForRemove);
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
import { check } from 'k6';
//...
const getResponse = cartsResource.get(idCart, ['items']);
check(getResponse, {
  'Get Cart Details - Status is 200': (r) => r.status === 200,
});
const bodyJson = getResponse.json(); // Safely parse JSON
skuForRemove = bodyJson.included?.[0]?.attributes?.sku;
//...
const removeResponse = cartsResource.removeItem(idCart, skuForRemove);
check(removeResponse, {
  'Remove Cart Item - Status is 204': (r) => r.status === 204, // Assuming 204 No Content
});
metrics[testConfiguration.metrics[0]].add(removeResponse.timings.duration);
```

**Smell 4: Not using tags**

- **Lines:** [54, 61, 63]
- **Snippet:**
```js
const response = cartsResource.get(idCart, ['items']);
//...
const response = cartsResource.removeItem(idCart, skuForRemove);
//...
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
// Assumes CartsResource methods accept a params object for tags
const getResponse = cartsResource.get(idCart, ['items'], {
  tags: { name: 'GetCartDetails' },
});
//...
const removeResponse = cartsResource.removeItem(idCart, skuForRemove, {
  tags: { name: 'RemoveCartItem' },
});
//...
metrics[testConfiguration.metrics[0]].add(removeResponse.timings.duration, {
  name: 'RemoveCartItem',
});
```

### `script_291.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [22, 23, 24, 25]
- **Snippet:**
```js
export const options = {
  vus: 10,
  duration: "30s",
};
```
- **Refactored:**
```js
export const options = {
  vus: 10,
  duration: "30s",
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [28]
- **Snippet:**
```js
const res = http.post("http://localhost:3000/api", payload, { headers });
```
- **Refactored:**
```js
const res = http.post("http://localhost:3000/api", payload, { headers, tags: { name: 'post_api', endpoint: '/api' } });
```

### `script_291.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [22, 23, 24, 25]
- **Snippet:**
```js
export const options = {
  vus: 10,
  duration: "30s",
};
```
- **Refactored:**
```js
export const options = {
  vus: 10,
  duration: "30s",
  thresholds: {
    http_req_failed: ["rate<0.01"],
    http_req_duration: ["p(95)<500"],
    checks: ["rate>0.99"],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [28]
- **Snippet:**
```js
const res = http.post("http://localhost:3000/api", payload, { headers });
```
- **Refactored:**
```js
const params = {
  headers,
  tags: {
    endpoint: "api",
    method: "POST",
    flow: "webhook",
  },
};

const res = http.post("http://localhost:3000/api", payload, params);
```

### `script_291.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [22, 23, 24, 25]
- **Snippet:**
```js
export const options = {
  vus: 10,
  duration: "30s",
};
```
- **Refactored:**
```js
export const options = {
  vus: 10,
  duration: "30s",
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [28]
- **Snippet:**
```js
const res = http.post("http://localhost:3000/api", payload, { headers });
```
- **Refactored:**
```js
const res = http.post("http://localhost:3000/api", payload, { 
    headers,
    tags: { name: 'CreateAPIResource' } 
  });
```

### `script_292.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [29, 30, 31, 32, 33, 34, 35, 36, 37, 38]
- **Snippet:**
```js
export let options = {
	stages: [
		{ duration: "1s", target: 5000 },
	],
};
```
- **Refactored:**
```js
export let options = {
	stages: [
		{ duration: "1s", target: 5000 },
	],
	thresholds: {
		http_req_failed: ['rate<0.01'],
		http_req_duration: ['p(95)<200'],
		'checks': ['rate>0.99'],
	},
};
```

**Smell 4: Not using tags**

- **Lines:** [58, 59, 60]
- **Snippet:**
```js
let commentRes = http.get(`${baseUrl}`, {
	headers: headers
});
```
- **Refactored:**
```js
let commentRes = http.get(`${baseUrl}`, {
	headers: headers,
	tags: { name: 'GetRoutine', endpoint: 'k12-course-service-routine' },
});
```

### `script_292.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [29, 34, 36, 38]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: "1s", target: 5000 },
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: "1s", target: 5000 },
    ],
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<200'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [58, 59, 60, 62, 63, 64, 65]
- **Snippet:**
```js
let commentRes = http.get(`${baseUrl}`, {
    headers: headers
});

check(commentRes, {
    'status is 200': (r) => r.status === 200,
    'response time < 200ms': (r) => r.timings.duration < 200
});
```
- **Refactored:**
```js
const tags = {
    endpoint: 'routine',
    service: 'k12-course-service',
    flow: 'get-routine'
};

let commentRes = http.get(`${baseUrl}`, {
    headers: headers,
    tags: tags
});

check(commentRes, {
    'status is 200': (r) => r.status === 200,
    'response time < 200ms': (r) => r.timings.duration < 200
}, tags);
```

### `script_292.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [29, 30, 31, 32, 33, 34, 35, 36, 37, 38]
- **Snippet:**
```js
export let options = {
	//executor: 'shared-iterations',
	// iterations: 1,
	// vus: 1,
    // duration: '20s',
    stages: [
        // Ramp up to 1 VUs for 5 second
        { duration: "1s", target: 5000 },
      ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: "1s", target: 5000 },
      ],
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
        'checks{status is 200}': ['rate>0.99'], // 99% of checks for 200 status must pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [58, 59, 60]
- **Snippet:**
```js
let commentRes = http.get(`${baseUrl}`, {
        headers: headers
    });
```
- **Refactored:**
```js
let commentRes = http.get(`${baseUrl}`, {
        headers: headers,
        tags: {
            name: 'GetRoutineAPI',
        },
    });
```

### `script_295.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 100,
  duration: '5m',
};
```
- **Refactored:**
```js
export const options = {
  vus: 100,
  duration: '5m',
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
    'checks': ['rate>0.95'],
    'response_time': ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [32]
- **Snippet:**
```js
const res = http.put(url, payload, { headers });
```
- **Refactored:**
```js
const res = http.put(url, payload, { headers, tags: { name: 'UpdateUser', endpoint: 'PUT /user/:username' } });
```

### `script_295.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 100,
  duration: '5m',
};
```
- **Refactored:**
```js
export const options = {
  vus: 100,
  duration: '5m',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500', 'p(99)<1000'],
    checks: ['rate>0.95'],
    response_time: ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [32, 35, 41]
- **Snippet:**
```js
const res = http.put(url, payload, { headers });
responseTime.add(res.timings.duration);
check(res, { ... });
```
- **Refactored:**
```js
const tags = {
  endpoint: 'update_user',
  flow: 'user_update',
  method: 'PUT',
};

const res = http.put(url, payload, { headers, tags });
responseTime.add(res.timings.duration, tags);
check(res, {
  'Status is 200': (r) => r.status === 200,
  'Response time < 500ms': (r) => r.timings.duration < 500,
}, tags);
```

### `script_295.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 100, // Jumlah VUs
  duration: '5m', // Durasi pengujian
};
```
- **Refactored:**
```js
export const options = {
  vus: 100,
  duration: '5m',
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'response_time': ['p(95)<500'], // 95th percentile of our custom metric should be below 500ms
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [32, 35]
- **Snippet:**
```js
const res = http.put(url, payload, { headers });

  // Menyimpan metrik tambahan
  responseTime.add(res.timings.duration);
```
- **Refactored:**
```js
const params = {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'UpdateUser' },
  };

  // Kirim request ke API
  const res = http.put(url, payload, params);

  // Menyimpan metrik tambahan
  responseTime.add(res.timings.duration, { name: 'UpdateUser' });
```

### `script_296.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8]
- **Snippet:**
```js
export const options = {
  stages: [
    { duration: '10m', target: 1000000 }, 
  ],
};
```
- **Refactored:**
```js
export const options = {
  stages: [
    { duration: '10m', target: 1000000 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [11, 14, 17]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
http.get('https://quickpizza.grafana.com/contacts.php');
http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
import { check } from 'k6';

const res1 = http.get('https://quickpizza.grafana.com/test.k6.io/');
check(res1, { 'homepage status is 200': (r) => r.status === 200 });

const res2 = http.get('https://quickpizza.grafana.com/contacts.php');
check(res2, { 'contacts status is 200': (r) => r.status === 200 });

const res3 = http.get('https://quickpizza.grafana.com/news.php');
check(res3, { 'news status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [11, 14, 17]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
http.get('https://quickpizza.grafana.com/contacts.php');
http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/', { tags: { name: 'homepage' } });
http.get('https://quickpizza.grafana.com/contacts.php', { tags: { name: 'contacts' } });
http.get('https://quickpizza.grafana.com/news.php', { tags: { name: 'news' } });
```

### `script_296.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8]
- **Snippet:**
```js
export const options = {
  stages: [
    { duration: '10m', target: 1000000 }, 
  ],
};
```
- **Refactored:**
```js
export const options = {
  stages: [
    { duration: '10m', target: 1000000 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [11, 14, 17]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
http.get('https://quickpizza.grafana.com/contacts.php');
http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default () => {
  const homeRes = http.get('https://quickpizza.grafana.com/test.k6.io/', { tags: { endpoint: 'home' } });
  check(homeRes, { 'home status is 200': (r) => r.status === 200 });
  sleep(1);

  const contactsRes = http.get('https://quickpizza.grafana.com/contacts.php', { tags: { endpoint: 'contacts' } });
  check(contactsRes, { 'contacts status is 200': (r) => r.status === 200 });
  sleep(2);

  const newsRes = http.get('https://quickpizza.grafana.com/news.php', { tags: { endpoint: 'news' } });
  check(newsRes, { 'news status is 200': (r) => r.status === 200 });
  sleep(2);
};
```

**Smell 4: Not using tags**

- **Lines:** [11, 14, 17]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
http.get('https://quickpizza.grafana.com/contacts.php');
http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
export default () => {
  http.get('https://quickpizza.grafana.com/test.k6.io/', {
    tags: { endpoint: 'home', flow: 'main' },
  });
  sleep(1);

  http.get('https://quickpizza.grafana.com/contacts.php', {
    tags: { endpoint: 'contacts', flow: 'main' },
  });
  sleep(2);

  http.get('https://quickpizza.grafana.com/news.php', {
    tags: { endpoint: 'news', flow: 'main' },
  });
  sleep(2);
};
```

### `script_296.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8]
- **Snippet:**
```js
export const options = {
  stages: [
    { duration: '10m', target: 1000000 }, 
  ],
};
```
- **Refactored:**
```js
export const options = {
  stages: [
    { duration: '10m', target: 1000000 }, 
  ],
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [11, 14, 17]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const res = http.get('https://quickpizza.grafana.com/test.k6.io/');
check(res, { 'status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [11, 14, 17]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/contacts.php');
```
- **Refactored:**
```js
http.get('https://quickpizza.grafana.com/contacts.php', {
  tags: { name: 'Contacts' },
});
```

### `script_30.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 360 },
        { duration: '30s', target: 3600 },
        { duration: '20s', target: 360 },
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 360 },
        { duration: '30s', target: 3600 },
        { duration: '20s', target: 360 },
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<1000'],
        'check_success': ['count>0'],
        'check_fail_500': ['count<10'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [30, 31, 32, 33, 34, 40]
- **Snippet:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    }
};
...
res = http.get(url, params);
```
- **Refactored:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    },
    tags: {
        name: 'user_logout',
        endpoint: '/v2/user/logout',
        method: 'GET'
    }
};
...
res = http.get(url, params);
```

### `script_30.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 360 },
        { duration: '30s', target: 3600 },
        { duration: '20s', target: 360 },
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 360 },
        { duration: '30s', target: 3600 },
        { duration: '20s', target: 360 },
    ],
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<1000'],
        'http_req_duration{endpoint:logout}': ['p(95)<1000'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [30, 31, 32, 33, 34, 40, 68]
- **Snippet:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    }
};

res = http.get(url, params);

check(res, { ... });
```
- **Refactored:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    },
    tags: {
        endpoint: 'logout',
        flow: 'user_session',
        method: 'GET'
    }
};

res = http.get(url, params);

check(res, {
    'Status is 200': (r) => r.status === 200,
    'Response time < 1000ms': (r) => r.timings.duration < 1000,
}, {
    endpoint: 'logout',
    flow: 'user_session'
});
```

### `script_30.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 360 },  // Load normal
        { duration: '30s', target: 3600 }, // Lonjakan (simulasi kegagalan)
        { duration: '20s', target: 360 },  // Pemulihan (cek kapan kembali ke normal)
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 360 },
        { duration: '30s', target: 3600 },
        { duration: '20s', target: 360 },
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<1500'], // 95% of requests must complete below 1.5s
        'checks': ['rate>0.99'],             // >99% of checks must pass
        'check_slow_response': ['count==0'],  // No slow responses allowed
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [40]
- **Snippet:**
```js
res = http.get(url, params);
```
- **Refactored:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    },
    tags: {
        name: 'UserLogout',
    },
};

res = http.get(url, params);
```

### `script_31.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [14]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
export let options = {
  ...test_options,
  thresholds: {
    'http_req_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
    'checks': ['rate>0.99']
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [50]
- **Snippet:**
```js
const res = http.del(`${url}/${store.id}`);
```
- **Refactored:**
```js
const res = http.del(`${url}/${store.id}`, null, {
  tags: { name: 'delete_store', endpoint: 'store', operation: 'delete' }
});
```

### `script_31.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [14]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
export let options = {
  ...test_options,
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99']
  }
};
```

**Smell 3: Not checking requests**

- **Lines:** [28, 29, 30, 62]
- **Snippet:**
```js
const res = http.post(`${url}`, JSON.stringify(store), {
    headers: { 'Content-Type': 'application/json' },
});
...
const res = http.del(`${url}/${store.id}`);
```
- **Refactored:**
```js
const res = http.post(`${url}`, JSON.stringify(store), {
  headers: { 'Content-Type': 'application/json' },
  tags: { endpoint: 'stores', operation: 'setup-create-store' }
});
check(res, {
  'setup create store status is 200': (r) => r.status === 200
});

// teardown
const res = http.del(`${url}/${store.id}`, {
  tags: { endpoint: 'stores/:id', operation: 'teardown-delete-store' }
});
check(res, {
  'teardown delete store status is 200': (r) => r.status === 200 || r.status === 404
});
```

**Smell 4: Not using tags**

- **Lines:** [28, 29, 30, 50, 62]
- **Snippet:**
```js
http.post(`${url}`, JSON.stringify(store), {
    headers: { 'Content-Type': 'application/json' },
});
...
const res = http.del(`${url}/${store.id}`);
...
const res = http.del(`${url}/${store.id}`);
```
- **Refactored:**
```js
const createParams = {
  headers: { 'Content-Type': 'application/json' },
  tags: { endpoint: 'stores', operation: 'create-store' }
};
const createRes = http.post(`${url}`, JSON.stringify(store), createParams);

const deleteParams = {
  tags: { endpoint: 'stores/:id', operation: 'delete-store' }
};
const deleteRes = http.del(`${url}/${store.id}`, null, deleteParams);
```

### `script_31.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [14]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
export let options = {
  ...test_options, // Assuming test_options contains VUs, duration, etc.
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<200'], // 95% of requests should be below 200ms
    'checks': ['rate>0.99']            // 99% of checks should pass
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [62]
- **Snippet:**
```js
const res = http.del(`${url}/${store.id}`);
```
- **Refactored:**
```js
for (const store in stores) {
    const res = http.del(`${url}/${store.id}`);
    check(res, {
        'teardown: status is 200': (r) => r.status === 200,
    });
}
```

**Smell 4: Not using tags**

- **Lines:** [50]
- **Snippet:**
```js
const res = http.del(`${url}/${store.id}`);
```
- **Refactored:**
```js
const res = http.del(`${url}/${store.id}`, null, {
  tags: {
    name: 'DeleteStore',
  },
});
```

### `script_32.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 81, 82, 83, 84, 85, 86, 87]
- **Snippet:**
```js
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = usersRaw.map(line => {
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    return { ... }
}).filter(...);

for (let panelId = 1; panelId <= MAX_PANEL_ID; panelId++) {
    panelMetrics[panelId] = {
        responseTime: new Trend(`panel_response_time_${panelId}`, true),
        successRate: new Rate(`panel_success_rate_${panelId}`, true),
        failureRate: new Rate(`panel_failure_rate_${panelId}`, true)
    };
}
```
- **Refactored:**
```js
// Reading and parsing the file is acceptable in init context since open() is only allowed there,
// but the heavy string splitting and map/filter chain can be kept minimal.
// The loop creating 150 Trend/Rate metric objects is costly — consider reducing MAX_PANEL_ID
// or lazily initializing metrics only for panels actually encountered at runtime.

// Instead of pre-creating 150*3=450 metric objects, initialize on demand:
const panelMetrics = {};

function getOrCreatePanelMetrics(panelId) {
    if (!panelMetrics[panelId]) {
        panelMetrics[panelId] = {
            responseTime: new Trend(`panel_response_time_${panelId}`, true),
            successRate: new Rate(`panel_success_rate_${panelId}`, true),
            failureRate: new Rate(`panel_failure_rate_${panelId}`, true)
        };
    }
    return panelMetrics[panelId];
}
// Then in the default function, replace panelMetrics[panelId] with getOrCreatePanelMetrics(panelId)
```

**Smell 2: Do not use thresholds**

- **Lines:** [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
- **Snippet:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    }
};
```
- **Refactored:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    },
    thresholds: {
        'dashboard_response_time': ['p(95)<2000'],
        'dashboard_success_rate': ['rate>0.95'],
        'http_req_duration_custom': ['p(95)<3000'],
        'checks': ['rate>0.95']
    }
};
```

### `script_32.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
- **Snippet:**
```js
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = usersRaw.map(line => {
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    return {
        username,
        password,
        vunetSession,
        xVuNetHTTPInfo,
        grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10)
    };
}).filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

const users = new SharedArray('users', function () {
    return open('/home/vunet/user_creation_k6/user_cookies.txt')
        .split('\n')
        .map(line => {
            const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
            return {
                username,
                password,
                vunetSession,
                xVuNetHTTPInfo,
                grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10)
            };
        })
        .filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
});
```

**Smell 2: Do not use thresholds**

- **Lines:** [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
- **Snippet:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
   // iterations: 5,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    }
};
```
- **Refactored:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<2000', 'p(99)<5000'],
        checks: ['rate>0.99'],
        dashboard_success_rate: ['rate>0.99'],
        dashboard_response_time: ['p(95)<2000']
    },
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    }
};
```

### `script_32.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
- **Snippet:**
```js
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = usersRaw.map(line => {
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    return {
        username,
        password,
        vunetSession,
        xVuNetHTTPInfo,
        grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10)
    };
}).filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

const users = new SharedArray('users', function () {
  // This function is executed only once for the entire test run.
  const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
  return usersRaw.map(line => {
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    return {
        username,
        password,
        vunetSession,
        xVuNetHTTPInfo,
        grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10)
    };
  }).filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
});
```

**Smell 2: Do not use thresholds**

- **Lines:** [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
- **Snippet:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
   // iterations: 5,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    }
};
```
- **Refactored:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    },
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration_custom': ['p(95)<2000'], // 95% of custom http requests must be below 2s
        'dashboard_success_rate': ['rate>0.99'], // success rate for dashboard metadata must be >99%
        'checks': ['rate>0.99'] // check success rate must be >99%
    }
};
```

### `script_33.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 365 },
        { duration: '30s', target: 3650 },
        { duration: '20s', target: 365 },
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 365 },
        { duration: '30s', target: 3650 },
        { duration: '20s', target: 365 },
    ],
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<1000'],
        'checks{check:✅ Status is 200 (Success)}': ['rate>0.95'],
        total_failures: ['count<10'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [42, 43, 44, 45, 46]
- **Snippet:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    }
};
```
- **Refactored:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    },
    tags: {
        name: 'update_user',
        endpoint: '/v2/user/:username',
        flow: 'user_update'
    }
};
```

### `script_33.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 365 },
        { duration: '30s', target: 3650 },
        { duration: '20s', target: 365 },
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 365 },
        { duration: '30s', target: 3650 },
        { duration: '20s', target: 365 },
    ],
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<1000'],
        total_failures: ['count==0'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [42, 43, 44, 45, 46, 52, 80]
- **Snippet:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    }
};

res = http.put(url, payload, params);

check(res, { ... });
```
- **Refactored:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    },
    tags: {
        endpoint: 'put_user',
        name: 'PUT /v2/user/{username}',
        user_flow: 'user_update'
    }
};

res = http.put(url, payload, params);

check(res, {
    'Status is 200': (r) => r.status === 200,
    'Response time < 1000ms': (r) => r.timings.duration < 1000,
}, {
    endpoint: 'put_user',
    user_flow: 'user_update'
});
```

### `script_33.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 365 },  // Load normal
        { duration: '30s', target: 3650 }, // Lonjakan (simulasi kegagalan)
        { duration: '20s', target: 365 },  // Pemulihan (cek kapan kembali ke normal)
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 365 },
        { duration: '30s', target: 3650 },
        { duration: '20s', target: 365 },
    ],
    thresholds: {
        'http_req_failed': ['rate<0.05'], // Fail if error rate is > 5%
        'http_req_duration': ['p(95)<1500'], // 95% of requests must complete below 1.5s
        'checks': ['rate>0.98'] // Over 98% of checks must pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [42, 43, 44, 45, 46, 52]
- **Snippet:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    }
};

...

res = http.put(url, payload, params);
```
- **Refactored:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    },
    tags: {
        name: 'UpdateUser',
    },
};

res = http.put(url, payload, params);
```

### `script_34.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '2m', target: 70 },
        { duration: '6m', target: 700 },
        { duration: '2m', target: 70 },
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '2m', target: 70 },
        { duration: '6m', target: 700 },
        { duration: '2m', target: 70 },
    ],
    thresholds: {
        http_req_failed: ['rate<0.05'],           // Error rate must be below 5%
        http_req_duration: ['p(95)<1000'],         // 95th percentile response time under 1s
        'check_success': ['count>0'],              // At least some successful requests
        'check_fail_500': ['count<10'],            // Fewer than 10 server errors
        'check_slow_response': ['count<50'],       // Fewer than 50 slow responses
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [36]
- **Snippet:**
```js
res = http.get(url);
```
- **Refactored:**
```js
res = http.get(url, {
    tags: {
        name: 'GetStoreOrder',
        endpoint: '/v2/store/order',
        flow: 'order-lookup',
    },
});
```

### `script_34.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '2m', target: 70 },
        { duration: '6m', target: 700 },
        { duration: '2m', target: 70 },
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '2m', target: 70 },
        { duration: '6m', target: 700 },
        { duration: '2m', target: 70 },
    ],
    thresholds: {
        http_req_failed: ['rate<0.05'],
        http_req_duration: ['p(95)<1000'],
        'http_req_duration{endpoint:GET /store/order/{orderId}}': ['p(95)<1000'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [36, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96]
- **Snippet:**
```js
res = http.get(url);
...
check(res, {
    '✅ Status is 200 (Success)': (r) => {
        let result = r.status === 200;
        if (result) checkSuccess.add(1);
        return result;
    },
    ...
});
```
- **Refactored:**
```js
const requestTags = {
    endpoint: 'GET /store/order/{orderId}',
    flow: 'get_order',
};

res = http.get(url, { tags: requestTags });

check(res, {
    'status is acceptable': (r) => [200, 404].includes(r.status),
    'response time below 1000ms': (r) => r.timings.duration < 1000,
}, requestTags);
```

### `script_34.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '2m', target: 70 },  // Load normal
        { duration: '6m', target: 700 }, // Lonjakan (simulasi kegagalan)
        { duration: '2m', target: 70 },  // Pemulihan (cek kapan kembali ke normal)
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '2m', target: 70 },  // Load normal
        { duration: '6m', target: 700 }, // Lonjakan (simulasi kegagalan)
        { duration: '2m', target: 70 },  // Pemulihan (cek kapan kembali ke normal)
    ],
    thresholds: {
        'http_req_failed': ['rate<0.05'], // HTTP errors should be less than 5%
        'http_req_duration': ['p(95)<1000'], // 95% of requests must complete below 1s
        'checks': ['rate>0.99'], // 99% of checks must pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [36]
- **Snippet:**
```js
res = http.get(url);
```
- **Refactored:**
```js
res = http.get(url, { tags: { name: 'GetOrder' } });
```

### `script_35.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
  iterations: 100,
  duration: '30s',
};
```
- **Refactored:**
```js
export const options = {
  iterations: 100,
  duration: '30s',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    'checks': ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [14, 23]
- **Snippet:**
```js
const res = http.get(videoPath + String(i).padStart(5, '0') + '.ts');
```
- **Refactored:**
```js
const res = http.get(videoPath + String(i).padStart(5, '0') + '.ts', {
  tags: { name: 'video_chunk', segment: String(i) },
});
```

### `script_35.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
  iterations: 100,
  duration: '30s',
};
```
- **Refactored:**
```js
export const options = {
  iterations: 100,
  duration: '30s',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [14, 15, 23, 24]
- **Snippet:**
```js
const res = http.get(videoPath + String(i).padStart(5, '0') + '.ts');
check(res, {
  'is status 200': (r) => r.status === 200,
  'is video chunk loaded': (r) => r.body.length > 0,
  'is video chunk cached': (r) => r.headers['X-Cache'] === 'Hit from cloudfront',
});
```
- **Refactored:**
```js
function loadVideoChunk(i, phase) {
  const url = videoPath + String(i).padStart(5, '0') + '.ts';
  const tags = { endpoint: 'video_chunk', phase };
  const res = http.get(url, { tags });
  check(res, {
    'is status 200': (r) => r.status === 200,
    'is video chunk loaded': (r) => r.body.length > 0,
    'is video chunk cached': (r) => r.headers['X-Cache'] === 'Hit from cloudfront',
  }, tags);
}

export default function() {
  for (let i = 1; i <= 5; i++) {
    loadVideoChunk(i, 'initial_buffer');
  }
  for (let i = 6; i <= 11; i++) {
    sleep(3);
    loadVideoChunk(i, 'playback');
  }
}
```

### `script_35.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
  iterations: 100,
  duration: '30s',
};
```
- **Refactored:**
```js
export const options = {
  iterations: 100,
  duration: '30s',
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks': ['rate>0.99'], // 99% of checks should pass
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [14, 23]
- **Snippet:**
```js
const res = http.get(videoPath + String(i).padStart(5, '0') + '.ts');
```
- **Refactored:**
```js
const res = http.get(videoPath + String(i).padStart(5, '0') + '.ts', { tags: { name: 'VideoChunk' } });
```

### `script_36.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 81, 82, 83, 84, 85, 86, 87]
- **Snippet:**
```js
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = usersRaw.map(line => {
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    return { ... }
}).filter(...);

for (let panelId = 1; panelId <= MAX_PANEL_ID; panelId++) {
    panelMetrics[panelId] = {
        responseTime: new Trend(`panel_response_time_${panelId}`, true),
        successRate: new Rate(`panel_success_rate_${panelId}`, true),
        failureRate: new Rate(`panel_failure_rate_${panelId}`, true)
    };
}
```
- **Refactored:**
```js
// Reading and parsing the file is unavoidable in init, but the mapping/filtering
// should be kept minimal. The panel metrics loop creates 150*3=450 custom metric
// objects eagerly; consider creating them lazily inside the default function only
// for panels actually encountered, reducing unnecessary object allocation.

// Lazy panel metrics example:
function getPanelMetrics(panelId) {
    if (!panelMetrics[panelId]) {
        panelMetrics[panelId] = {
            responseTime: new Trend(`panel_response_time_${panelId}`, true),
            successRate: new Rate(`panel_success_rate_${panelId}`, true),
            failureRate: new Rate(`panel_failure_rate_${panelId}`, true)
        };
    }
    return panelMetrics[panelId];
}
// NOTE: In k6, custom metrics must be created in the init context, so
// the lazy approach above is not directly applicable. The recommended fix
// is to reduce MAX_PANEL_ID to the actual number of panels or load only
// the panel IDs from a pre-generated file, avoiding over-allocation.
```

**Smell 2: Do not use thresholds**

- **Lines:** [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
- **Snippet:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    }
};
```
- **Refactored:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    },
    thresholds: {
        'dashboard_response_time': ['p(95)<2000'],
        'dashboard_success_rate': ['rate>0.95'],
        'http_req_duration_custom': ['p(95)<3000'],
        'checks': ['rate>0.95']
    }
};
```

### `script_36.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
- **Snippet:**
```js
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = usersRaw.map(line => {
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    return {
        username,
        password,
        vunetSession,
        xVuNetHTTPInfo,
        grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10)
    };
}).filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

const users = new SharedArray('users', function () {
    return open('/home/vunet/user_creation_k6/user_cookies.txt')
        .split('\n')
        .map(line => {
            const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
            return {
                username,
                password,
                vunetSession,
                xVuNetHTTPInfo,
                grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10)
            };
        })
        .filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
});
```

**Smell 2: Do not use thresholds**

- **Lines:** [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
- **Snippet:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
   // iterations: 5,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    }
};
```
- **Refactored:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<2000'],
        checks: ['rate>0.99'],
        dashboard_success_rate: ['rate>0.99'],
        dashboard_response_time: ['p(95)<2000']
    }
};
```

### `script_36.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
- **Snippet:**
```js
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = usersRaw.map(line => {
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    return {
        username,
        password,
        vunetSession,
        xVuNetHTTPInfo,
        grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10)
    };
}).filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
```
- **Refactored:**
```js
/* Move data loading and processing to the setup function, which runs only once. */
export function setup() {
    const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
    const users = usersRaw.map(line => {
        const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
        return {
            username,
            password,
            vunetSession,
            xVuNetHTTPInfo,
            grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10)
        };
    }).filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);

    if (users.length === 0) {
        throw new Error('No valid users found in user_cookies.txt!');
    }
    return users; // Return the processed data
}

/* The default function receives the data from setup(). The VU number can be used to select a unique user. */
export default function (users) {
    let user = users[__VU - 1];
    if (!user) { return; } // Exit if no user is available for this VU
    // ... rest of the VU code
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
- **Snippet:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
   // iterations: 5,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    }
};
```
- **Refactored:**
```js
export let options = {
    vus: users.length,
    iterations: users.length,
    tags: {
        dashboardName: DASHBOARD_CONFIG.name,
        dashboardId: DASHBOARD_CONFIG.id,
        test_type: 'dashboard_performance',
        timeFrom: TIME_RANGE.from,
        timeTo: TIME_RANGE.to
    },
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<1000'], // 95% of requests must complete below 1s
        'checks': ['rate>0.99'], // 99% of checks must pass
        'dashboard_success_rate': ['rate>0.95'] // dashboard success rate must be > 95%
    }
};
```

### `script_37.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11, 12, 13, 14]
- **Snippet:**
```js
export let options = {
  stages: [
      { duration: "10s", target: `${__ENV.USERS}` },
      { duration: "100s", target: `${__ENV.USERS}` },
      { duration: "10s", target: 0 }
  ]
};
```
- **Refactored:**
```js
export let options = {
  stages: [
      { duration: "10s", target: `${__ENV.USERS}` },
      { duration: "100s", target: `${__ENV.USERS}` },
      { duration: "10s", target: 0 }
  ],
  thresholds: {
    'http_req_duration': ['p(95)<500'],
    'Get_books': ['p(95)<500'],
    'Get_books error': ['rate<0.01'],
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [25, 26, 27, 28, 29, 30, 31]
- **Snippet:**
```js
const requests = {
    'Get_books': {
      method: 'GET',
      url: url +'books/simple',
      params: params,
    }
  };
```
- **Refactored:**
```js
const params = {
  headers: {
    'Content-Type': 'application/json',
  },
  tags: { name: 'Get_books', endpoint: 'books/simple' },
};

const requests = {
    'Get_books': {
      method: 'GET',
      url: url + 'books/simple',
      params: params,
    }
  };
```

### `script_37.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11, 12, 13, 14]
- **Snippet:**
```js
export let options = {
  stages: [
      { duration: "10s", target: `${__ENV.USERS}` },
      { duration: "100s", target: `${__ENV.USERS}` },
      { duration: "10s", target: 0 }
  ]
};
```
- **Refactored:**
```js
export let options = {
  stages: [
    { duration: "10s", target: `${__ENV.USERS}` },
    { duration: "100s", target: `${__ENV.USERS}` },
    { duration: "10s", target: 0 }
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
    'Get_books': ['p(95)<500'],
    'Get_books error': ['rate<0.01']
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [19, 20, 21, 22, 23, 29, 38, 40]
- **Snippet:**
```js
const params = {
  headers: {
    'Content-Type': 'application/json',
  },
};
...
params: params,
...
getErrorRate.add(1);
getTrend.add(getResp.timings.duration);
```
- **Refactored:**
```js
const params = {
  headers: {
    'Content-Type': 'application/json',
  },
  tags: {
    name: 'Get_books',
    endpoint: '/books/simple',
    flow: 'books'
  }
};

const requests = {
  'Get_books': {
    method: 'GET',
    url: url + 'books/simple',
    params: params,
  }
};

const responses = http.batch(requests);
const getResp = responses['Get_books'];

const tags = { endpoint: '/books/simple', flow: 'books' };
check(getResp, {
  'status is 200': (r) => r.status === 200,
}, tags) || getErrorRate.add(1, tags);

getTrend.add(getResp.timings.duration, tags);
```

### `script_37.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11, 12, 13, 14]
- **Snippet:**
```js
export let options = {
  stages: [
      { duration: "10s", target: `${__ENV.USERS}` },
      { duration: "100s", target: `${__ENV.USERS}` },
      { duration: "10s", target: 0 }
  ]
};
```
- **Refactored:**
```js
export let options = {
  stages: [
      { duration: "10s", target: `${__ENV.USERS}` },
      { duration: "100s", target: `${__ENV.USERS}` },
      { duration: "10s", target: 0 }
  ],
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'Get_books': ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [19, 36, 38, 40]
- **Snippet:**
```js
  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  // ...

  check(getResp, {
    'status is 200': (r) => r.status === 200,
  }) || getErrorRate.add(1);

  getTrend.add(getResp.timings.duration);
```
- **Refactored:**
```js
  const requestTags = { name: 'GetBooksSimple' };
  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
    tags: requestTags,
  };

  // ...

  check(getResp, {
    'status is 200': (r) => r.status === 200,
  }, requestTags) || getErrorRate.add(1, requestTags);

  getTrend.add(getResp.timings.duration, requestTags);
```

### `script_38.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11, 12, 13, 14]
- **Snippet:**
```js
export let options = {
  stages: [
      { duration: "10s", target: `${__ENV.USERS}` },
      { duration: "100s", target: `${__ENV.USERS}` },
      { duration: "10s", target: 0 }
  ]
};
```
- **Refactored:**
```js
export let options = {
  stages: [
      { duration: "10s", target: `${__ENV.USERS}` },
      { duration: "100s", target: `${__ENV.USERS}` },
      { duration: "10s", target: 0 }
  ],
  thresholds: {
    'http_req_duration': ['p(95)<500'],
    'Get_Orders_Async': ['p(95)<500'],
    'Get_Orders_Async_error': ['rate<0.01'],
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [19, 20, 21, 22, 23]
- **Snippet:**
```js
const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };
```
- **Refactored:**
```js
const params = {
    headers: {
      'Content-Type': 'application/json',
    },
    tags: {
      name: 'Get_Orders_Async',
      endpoint: 'api/orders/async',
    },
  };
```

### `script_38.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11, 12, 13, 14]
- **Snippet:**
```js
export let options = {
  stages: [
      { duration: "10s", target: `${__ENV.USERS}` },
      { duration: "100s", target: `${__ENV.USERS}` },
      { duration: "10s", target: 0 }
  ]
};
```
- **Refactored:**
```js
export let options = {
  stages: [
    { duration: '10s', target: Number(__ENV.USERS) },
    { duration: '100s', target: Number(__ENV.USERS) },
    { duration: '10s', target: 0 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    Get_Orders_Async: ['p(95)<500'],
    Get_Orders_Async_error: ['rate<0.01'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [19, 20, 21, 22, 23, 29, 36, 37, 38, 40]
- **Snippet:**
```js
const params = {
  headers: {
    'Content-Type': 'application/json',
  },
};

params: params,

check(getResp, {
  'status is 200': (r) => r.status === 200,
}) || getErrorRate.add(1);

getTrend.add(getResp.timings.duration);
```
- **Refactored:**
```js
const tags = {
  endpoint: 'get_orders_async',
  flow: 'orders',
};

const params = {
  headers: {
    'Content-Type': 'application/json',
  },
  tags,
};

const requests = {
  Get_Orders_Async: {
    method: 'GET',
    url: `${url}api/orders/async/1`,
    params,
  },
};

const responses = http.batch(requests);
const getResp = responses.Get_Orders_Async;

check(getResp, {
  'status is 200': (r) => r.status === 200,
}, tags) || getErrorRate.add(1, tags);

getTrend.add(getResp.timings.duration, tags);
```

### `script_38.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11, 12, 13, 14]
- **Snippet:**
```js
export let options = {
  stages: [
      { duration: "10s", target: `${__ENV.USERS}` },
      { duration: "100s", target: `${__ENV.USERS}` },
      { duration: "10s", target: 0 }
  ]
};
```
- **Refactored:**
```js
export let options = {
  stages: [
      { duration: "10s", target: `${__ENV.USERS}` },
      { duration: "100s", target: `${__ENV.USERS}` },
      { duration: "10s", target: 0 }
  ],
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'Get_Orders_Async_error': ['rate<0.01'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [25, 38, 40]
- **Snippet:**
```js
  const requests = {
      'Get_Orders_Async': {
        method: 'GET',
        url: url +'api/orders/async/1',
        params: params,
      }
    };
...
  }) || getErrorRate.add(1);
...
  getTrend.add(getResp.timings.duration);
```
- **Refactored:**
```js
  const requestTags = { name: 'GetOrdersAsync' };
  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
    tags: requestTags
  };

  const requests = {
      'Get_Orders_Async': {
        method: 'GET',
        url: url +'api/orders/async/1',
        params: params,
      }
    };
...
  }) || getErrorRate.add(1, requestTags);
...
  getTrend.add(getResp.timings.duration, requestTags);
```

### `script_39.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [29, 30, 31, 32, 39]
- **Snippet:**
```js
const auth_resp = http.post('https://test-api.k6.io/auth/token/login/', {
    username: 'test-user',
    password: 'supersecure',
  });
...
  const other_resp = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
import { check } from 'k6';

// Inside default function:
const auth_resp = http.post('https://test-api.k6.io/auth/token/login/', {
  username: 'test-user',
  password: 'supersecure',
});
check(auth_resp, {
  'auth status is 200': (r) => r.status === 200,
  'auth response has token': (r) => r.json('access') !== undefined,
});
if (auth_resp.status >= 400) {
  allErrors.add(1, { errorType: 'authError' });
}

const other_resp = http.get('https://test-api.k6.io/public/crocodiles/1/');
check(other_resp, {
  'crocodiles status is 200': (r) => r.status === 200,
  'crocodiles response has body': (r) => r.body && r.body.length > 0,
});
if (other_resp.status >= 400) {
  allErrors.add(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [29, 39]
- **Snippet:**
```js
const auth_resp = http.post('https://test-api.k6.io/auth/token/login/', {
    username: 'test-user',
    password: 'supersecure',
  });
...
  const other_resp = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
const auth_resp = http.post(
  'https://test-api.k6.io/auth/token/login/',
  { username: 'test-user', password: 'supersecure' },
  { tags: { name: 'auth_login', endpoint: 'login' } }
);

const other_resp = http.get(
  'https://test-api.k6.io/public/crocodiles/1/',
  { tags: { name: 'get_crocodile', endpoint: 'crocodiles' } }
);
```

### `script_39.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [29, 39]
- **Snippet:**
```js
const auth_resp = http.post('https://test-api.k6.io/auth/token/login/', {
  username: 'test-user',
  password: 'supersecure',
});
...
const other_resp = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
import { sleep, check } from 'k6';
import http from 'k6/http';

export default function () {
  const auth_resp = http.post('https://test-api.k6.io/auth/token/login/', {
    username: 'test-user',
    password: 'supersecure',
  });

  check(auth_resp, {
    'auth request succeeded': (r) => r.status < 400,
    'auth token returned': (r) => r.json('access') !== undefined,
  });

  if (auth_resp.status >= 400) {
    allErrors.add(1, { errorType: 'authError' });
  }

  const other_resp = http.get('https://test-api.k6.io/public/crocodiles/1/');

  check(other_resp, {
    'crocodile request succeeded': (r) => r.status === 200,
  });

  if (other_resp.status >= 400) {
    allErrors.add(1, { errorType: 'otherError' });
  }

  sleep(1);
}
```

### `script_40.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [18, 22]
- **Snippet:**
```js
let res = http.get('https://quickpizza.grafana.com/test.k6.io/');
    myCounter.add(1);
    sleep(1);
    
    res = http.get('https://quickpizza.grafana.com/news.php');
    newsPageResponseTrend.add(res.timings.duration);
```
- **Refactored:**
```js
import { check } from 'k6';

// Inside default function:
let res = http.get('https://quickpizza.grafana.com/test.k6.io/');
check(res, {
    'home page status is 200': (r) => r.status === 200,
});
myCounter.add(1);
sleep(1);

res = http.get('https://quickpizza.grafana.com/news.php');
check(res, {
    'news page status is 200': (r) => r.status === 200,
});
newsPageResponseTrend.add(res.timings.duration);
sleep(1);
```

**Smell 4: Not using tags**

- **Lines:** [18, 22]
- **Snippet:**
```js
let res = http.get('https://quickpizza.grafana.com/test.k6.io/');
    ...
    res = http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
let res = http.get('https://quickpizza.grafana.com/test.k6.io/', { tags: { name: 'home_page' } });
myCounter.add(1);
sleep(1);

res = http.get('https://quickpizza.grafana.com/news.php', { tags: { name: 'news_page' } });
newsPageResponseTrend.add(res.timings.duration);
sleep(1);
```

### `script_40.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [18, 22]
- **Snippet:**
```js
let res = http.get('https://quickpizza.grafana.com/test.k6.io/');
...
res = http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default function () {
    let res = http.get('https://quickpizza.grafana.com/test.k6.io/');
    check(res, {
        'home page status is 200': (r) => r.status === 200,
        'home page body is not empty': (r) => r.body && r.body.length > 0
    });
    myCounter.add(1);
    sleep(1);

    res = http.get('https://quickpizza.grafana.com/news.php');
    check(res, {
        'news page status is 200': (r) => r.status === 200,
        'news page body is not empty': (r) => r.body && r.body.length > 0
    });
    newsPageResponseTrend.add(res.timings.duration);
    sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [18, 19, 22, 23]
- **Snippet:**
```js
let res = http.get('https://quickpizza.grafana.com/test.k6.io/');
myCounter.add(1);
...
res = http.get('https://quickpizza.grafana.com/news.php');
newsPageResponseTrend.add(res.timings.duration);
```
- **Refactored:**
```js
export default function () {
    let res = http.get('https://quickpizza.grafana.com/test.k6.io/', {
        tags: { endpoint: 'home', flow: 'browse' }
    });
    myCounter.add(1, { endpoint: 'home', flow: 'browse' });
    sleep(1);

    res = http.get('https://quickpizza.grafana.com/news.php', {
        tags: { endpoint: 'news', flow: 'browse' }
    });
    newsPageResponseTrend.add(res.timings.duration, { endpoint: 'news', flow: 'browse' });
    sleep(1);
}
```

### `script_40.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [18, 22]
- **Snippet:**
```js
let res = http.get('https://quickpizza.grafana.com/test.k6.io/');
// ...
res = http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
import http from 'k6/http';
import { sleep, check } from 'k6';
// ...
export default function () {
    let res = http.get('https://quickpizza.grafana.com/test.k6.io/');
    check(res, { 'main page status is 200': (r) => r.status === 200 });
    myCounter.add(1);
    sleep(1);
    
    res = http.get('https://quickpizza.grafana.com/news.php');
    check(res, { 'news page status is 200': (r) => r.status === 200 });
    newsPageResponseTrend.add(res.timings.duration);
    sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [18, 19, 22, 23]
- **Snippet:**
```js
let res = http.get('https://quickpizza.grafana.com/test.k6.io/');
myCounter.add(1);
// ...
res = http.get('https://quickpizza.grafana.com/news.php');
newsPageResponseTrend.add(res.timings.duration);
```
- **Refactored:**
```js
export default function () {
    let res = http.get('https://quickpizza.grafana.com/test.k6.io/', {
        tags: { name: 'MainPage' },
    });
    myCounter.add(1, { page: 'main' });
    sleep(1);
    
    res = http.get('https://quickpizza.grafana.com/news.php', {
        tags: { name: 'NewsPage' },
    });
    newsPageResponseTrend.add(res.timings.duration, { page: 'news' });
    sleep(1);
}
```

### `script_41.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4010, 4011, 4012, 4013, 4014, 4015, 4016, 4017, 4018, 4019]
- **Snippet:**
```js
export let options = {
    scenarios: {
        scenario2: {
            executor: 'per-vu-iterations',
            vus: users.length,
            iterations: 1,
            exec: 'scenario2',
        },
    },
};
```
- **Refactored:**
```js
export let options = {
    scenarios: {
        scenario2: {
            executor: 'per-vu-iterations',
            vus: users.length,
            iterations: 1,
            exec: 'scenario2',
        },
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<2000'],
        'participation_400': ['count<10'],
        'participation_500': ['count<5'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [4026, 4027, 4028, 4029, 4030, 4031, 4052, 4053, 4054]
- **Snippet:**
```js
const loginRes = http.post('http://localhost:3000/guestUser/logIn', JSON.stringify({...}), {
    headers: { 'Content-Type': 'application/json' },
});
...
const eventRes = http.post('http://localhost:3000/user/organizer/createEvent', JSON.stringify(payload), {
    headers: { 'Content-Type': 'application/json' },
});
```
- **Refactored:**
```js
const loginRes = http.post('http://localhost:3000/guestUser/logIn', JSON.stringify({
    email: user.email,
    password: password,
}), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'login', endpoint: '/guestUser/logIn' },
});
...
const eventRes = http.post('http://localhost:3000/user/organizer/createEvent', JSON.stringify(payload), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'createEvent', endpoint: '/user/organizer/createEvent' },
});
```

### `script_41.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [5, 4006]
- **Snippet:**
```js
const users = [ ... large inline user dataset ... ]
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

const users = new SharedArray('users', () => JSON.parse(open('./users.json')));
```

**Smell 2: Do not use thresholds**

- **Lines:** [4010, 4019]
- **Snippet:**
```js
export let options = {
    scenarios: {
        scenario2: {
            executor: 'per-vu-iterations',
            vus: users.length,
            iterations: 1,
            exec: 'scenario2',
        },
    },
};
```
- **Refactored:**
```js
export let options = {
    scenarios: {
        scenario2: {
            executor: 'per-vu-iterations',
            vus: users.length,
            iterations: 1,
            exec: 'scenario2',
        },
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99'],
        participation_400: ['count==0'],
        participation_500: ['count==0'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [4026, 4031, 4052, 4054]
- **Snippet:**
```js
const loginRes = http.post('http://localhost:3000/guestUser/logIn', JSON.stringify({...}), {
    headers: { 'Content-Type': 'application/json' },
});

const eventRes = http.post('http://localhost:3000/user/organizer/createEvent', JSON.stringify(payload), {
    headers: { 'Content-Type': 'application/json' },
});
```
- **Refactored:**
```js
const loginRes = http.post('http://localhost:3000/guestUser/logIn', JSON.stringify({
    email: user.email,
    password: password,
}), {
    headers: { 'Content-Type': 'application/json' },
    tags: { endpoint: 'login', flow: 'create_event' },
});

check(loginRes, { 'login successful': (r) => r.status === 200 }, { endpoint: 'login', flow: 'create_event' });

const eventRes = http.post('http://localhost:3000/user/organizer/createEvent', JSON.stringify(payload), {
    headers: { 'Content-Type': 'application/json' },
    tags: { endpoint: 'create_event', flow: 'create_event' },
});

check(eventRes, {
    'event created': (r) => r.status === 200,
}, { endpoint: 'create_event', flow: 'create_event' });
```

### `script_41.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [5, 4006]
- **Snippet:**
```js
const users = [
    {
        "_id": "660edbc4219f87ec22e8e7d2",
        "email": "user0@example.com"
    },
    // ... more users
]
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

const users = new SharedArray('users', function () {
  // Load user data from an external file (e.g., users.json)
  // This ensures the data is read only once from disk and shared in memory by all VUs.
  return JSON.parse(open('./users.json'));
});
```

**Smell 2: Do not use thresholds**

- **Lines:** [4010, 4019]
- **Snippet:**
```js
export let options = {
    scenarios: {
        scenario2: {
            executor: 'per-vu-iterations',
            vus: users.length,
            iterations: 1,
            exec: 'scenario2',
        },
    },
};
```
- **Refactored:**
```js
export let options = {
    scenarios: {
        scenario2: {
            executor: 'per-vu-iterations',
            vus: users.length,
            iterations: 1,
            exec: 'scenario2',
        },
    },
    thresholds: {
        'http_req_failed': ['rate<0.01'], // Fail if more than 1% of requests fail
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
        'checks': ['rate>0.99'], // Over 99% of checks must pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [4026, 4052]
- **Snippet:**
```js
const loginRes = http.post('http://localhost:3000/guestUser/logIn', ...);
// ...
const eventRes = http.post('http://localhost:3000/user/organizer/createEvent', ...);
```
- **Refactored:**
```js
const loginRes = http.post('http://localhost:3000/guestUser/logIn', JSON.stringify({
    email: user.email,
    password: password,
}), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'Login' }, // Add tag for login request
});

// ...

const eventRes = http.post('http://localhost:3000/user/organizer/createEvent', JSON.stringify(payload), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'CreateEvent' }, // Add tag for event creation request
});
```

### `script_42.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 350 },
        { duration: '30s', target: 3500 },
        { duration: '20s', target: 350 },
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 350 },
        { duration: '30s', target: 3500 },
        { duration: '20s', target: 350 },
    ],
    thresholds: {
        'http_req_failed': ['rate<0.05'],
        'http_req_duration': ['p(95)<1000'],
        'check_success': ['count>0'],
        'check_fail_500': ['count<10'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [45, 46, 47, 48, 49, 54]
- **Snippet:**
```js
let params = {
    headers: {
        'Content-Type': 'application/json',
    },
};
...
res = http.post(url, payload, params);
```
- **Refactored:**
```js
let params = {
    headers: {
        'Content-Type': 'application/json',
    },
    tags: {
        name: 'post_pet',
        endpoint: '/v2/pet',
        method: 'POST',
    },
};
...
res = http.post(url, payload, params);
```

### `script_42.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 350 },
        { duration: '30s', target: 3500 },
        { duration: '20s', target: 350 },
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 350 },
        { duration: '30s', target: 3500 },
        { duration: '20s', target: 350 },
    ],
    thresholds: {
        http_req_failed: ['rate<0.05'],
        http_req_duration: ['p(95)<1000'],
        'checks{check:✅ Status is 200 (Success)}': ['rate>0.95'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [45, 46, 47, 48, 49, 54, 82, 113]
- **Snippet:**
```js
let params = {
    headers: {
        'Content-Type': 'application/json',
    },
};

res = http.post(url, payload, params);

check(res, { ... });
```
- **Refactored:**
```js
let params = {
    headers: {
        'Content-Type': 'application/json',
    },
    tags: {
        endpoint: 'create_pet',
        method: 'POST',
        flow: 'pet_creation',
    },
};

res = http.post(url, payload, params);

check(res, {
    '✅ Status is 200 (Success)': (r) => r.status === 200,
    '⏱️ Response time < 1000ms': (r) => r.timings.duration < 1000,
}, {
    endpoint: 'create_pet',
    flow: 'pet_creation',
});
```

### `script_42.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 11]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 350 },  // Load normal
        { duration: '30s', target: 3500 }, // Lonjakan (simulasi kegagalan)
        { duration: '20s', target: 350 },  // Pemulihan (cek kapan kembali ke normal)
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '10s', target: 350 },
        { duration: '30s', target: 3500 },
        { duration: '20s', target: 350 },
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'], // Fail test if error rate > 1%
        'http_req_duration': ['p(95)<2000'], // 95th percentile response time must be < 2000ms
        'checks': ['rate>0.99'] // Over 99% of checks must pass
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [54]
- **Snippet:**
```js
res = http.post(url, payload, params);
```
- **Refactored:**
```js
let params = {
    headers: {
        'Content-Type': 'application/json',
    },
    tags: {
        name: 'CreatePet',
    },
};

res = http.post(url, payload, params);
```

### `script_45.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [22, 23]
- **Snippet:**
```js
const csvData = open('../loginSuccess.csv');
const userTokenData = papaparse.parse(csvData).data;
```
- **Refactored:**
```js
// These lines are already in the init context (top-level), which is acceptable for open().
// However, papaparse.parse() is a heavy CPU-bound operation executed once per VU during init.
// To mitigate cost, ensure the CSV is as small as necessary and consider pre-processing it
// outside k6. If the file is large, this will significantly slow VU initialization.
// If SharedArray is available (k6 >= 0.32.0), use it to parse only once across all VUs:
import { SharedArray } from 'k6/data';
const userTokenData = new SharedArray('userTokenData', function () {
    const csvData = open('../loginSuccess.csv');
    return papaparse.parse(csvData, { header: false }).data;
});
```

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: "20s", target: 1000 },
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: "20s", target: 1000 },
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'],          // Less than 1% of requests should fail
        'http_req_duration': ['p(95)<200'],         // 95% of requests must complete below 200ms
        'checks': ['rate>0.99'],                    // More than 99% of checks should pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [41, 42, 43]
- **Snippet:**
```js
let tokenValidateRes = http.post(`${baseUrl}/auth/v1/token/validate`, tokenJSON, {
    headers: headers
});
```
- **Refactored:**
```js
let tokenValidateRes = http.post(`${baseUrl}/auth/v1/token/validate`, tokenJSON, {
    headers: headers,
    tags: {
        name: 'TokenValidate',
        endpoint: '/auth/v1/token/validate',
        flow: 'token_validation'
    }
});
```

### `script_45.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [22, 23]
- **Snippet:**
```js
const csvData = open('../loginSuccess.csv');
const userTokenData = papaparse.parse(csvData).data;
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

const userTokenData = new SharedArray('user token data', function () {
  const csvData = open('../loginSuccess.csv');
  return papaparse.parse(csvData).data;
});
```

**Smell 2: Do not use thresholds**

- **Lines:** [6, 15]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: "20s", target: 1000 },
      ],
};
```
- **Refactored:**
```js
export let options = {
  stages: [
    { duration: '20s', target: 1000 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<200'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [41, 42, 43, 45, 46, 47, 48]
- **Snippet:**
```js
let tokenValidateRes = http.post(`${baseUrl}/auth/v1/token/validate`, tokenJSON, {
    headers: headers
});

check(tokenValidateRes, {
    'status is 200': (r) => r.status === 200,
    'response time < 200ms': (r) => r.timings.duration < 200
});
```
- **Refactored:**
```js
let tokenValidateRes = http.post(`${baseUrl}/auth/v1/token/validate`, tokenJSON, {
  headers: headers,
  tags: { endpoint: 'token_validate', flow: 'auth' },
});

check(tokenValidateRes, {
  'status is 200': (r) => r.status === 200,
  'response time < 200ms': (r) => r.timings.duration < 200,
}, { endpoint: 'token_validate', flow: 'auth' });
```

### `script_45.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [22, 23]
- **Snippet:**
```js
const csvData = open('../loginSuccess.csv');
const userTokenData = papaparse.parse(csvData).data;
```
- **Refactored:**
```js
// In init context:
const csvData = open('../loginSuccess.csv');

// Add a setup function to parse data once for all VUs:
export function setup() {
  return papaparse.parse(csvData).data;
}

// Modify the default function to receive the parsed data:
export default function(userTokenData) {
  //...rest of the script uses the userTokenData parameter
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [6, 15]
- **Snippet:**
```js
export let options = {
	//executor: 'shared-iterations',
	// iterations: 15000,
	// vus: 10,
    // duration : '20s',
    stages: [
        // Ramp up to 1 VUs for 5 second
        { duration: "20s", target: 1000 },
      ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: "20s", target: 1000 },
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<200'], // 95% of requests must complete below 200ms
        'checks': ['rate>0.95'], // 95% of checks must pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [41, 43]
- **Snippet:**
```js
let tokenValidateRes = http.post(`${baseUrl}/auth/v1/token/validate`, tokenJSON, {
        headers: headers
    });
```
- **Refactored:**
```js
let tokenValidateRes = http.post(`${baseUrl}/auth/v1/token/validate`, tokenJSON, {
    headers: headers,
    tags: {
        name: 'TokenValidation',
    },
});
```

### `script_47.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
  executor: 'ramping-arrival-rate',
  stages: [
    { duration: '2h', target: 20000 },
  ],
};
```
- **Refactored:**
```js
export const options = {
  executor: 'ramping-arrival-rate',
  stages: [
    { duration: '2h', target: 20000 },
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [12]
- **Snippet:**
```js
const urlRes = http.get('https://test-api.k6.io');
```
- **Refactored:**
```js
import { check } from 'k6';

// inside default function:
const urlRes = http.get('https://test-api.k6.io');
check(urlRes, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
const urlRes = http.get('https://test-api.k6.io');
```
- **Refactored:**
```js
const urlRes = http.get('https://test-api.k6.io', {
  tags: { name: 'homepage', endpoint: 'GET /' },
});
```

### `script_47.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
  executor: 'ramping-arrival-rate',
  stages: [
    { duration: '2h', target: 20000 },
  ],
};
```
- **Refactored:**
```js
export const options = {
  executor: 'ramping-arrival-rate',
  stages: [
    { duration: '2h', target: 20000 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [12]
- **Snippet:**
```js
const urlRes = http.get('https://test-api.k6.io');
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default () => {
  const urlRes = http.get('https://test-api.k6.io');
  check(urlRes, {
    'GET / returns status 200': (r) => r.status === 200,
  });
  sleep(1);
};
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
const urlRes = http.get('https://test-api.k6.io');
```
- **Refactored:**
```js
export default () => {
  const urlRes = http.get('https://test-api.k6.io', {
    tags: {
      endpoint: 'home',
      flow: 'default',
    },
  });
  sleep(1);
};
```

### `script_47.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
  executor: 'ramping-arrival-rate',
  stages: [
    { duration: '2h', target: 20000 },
  ],
};
```
- **Refactored:**
```js
export const options = {
  executor: 'ramping-arrival-rate',
  stages: [
    { duration: '2h', target: 20000 },
  ],
  thresholds: {
    'http_req_failed': ['rate<0.01'], // fail if more than 1% of requests fail
    'http_req_duration': ['p(95)<500'], // 95th percentile response time must be below 500ms
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [12]
- **Snippet:**
```js
const urlRes = http.get('https://test-api.k6.io');
```
- **Refactored:**
```js
import { check } from 'k6';
// ... in default function ...
const urlRes = http.get('https://test-api.k6.io');
check(urlRes, {
  'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
const urlRes = http.get('https://test-api.k6.io');
```
- **Refactored:**
```js
const urlRes = http.get('https://test-api.k6.io', {
  tags: { name: 'PublicHomepage' },
});
```

### `script_51.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9]
- **Snippet:**
```js
export let options = {
  vus: 10,
  duration: '1m',
};
```
- **Refactored:**
```js
export let options = {
  vus: 10,
  duration: '1m',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [18]
- **Snippet:**
```js
http.put(url+`/29145037094`,JSON.stringify(data), { headers: headers } );
```
- **Refactored:**
```js
import { check } from 'k6';

const res = http.put(url+`/29145037094`, JSON.stringify(data), { headers: headers });
check(res, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [18]
- **Snippet:**
```js
http.put(url+`/29145037094`,JSON.stringify(data), { headers: headers } );
```
- **Refactored:**
```js
http.put(url+`/29145037094`, JSON.stringify(data), { headers: headers, tags: { name: 'update_user', endpoint: '/v1/user/:id' } });
```

### `script_51.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9]
- **Snippet:**
```js
export let options = {
  vus: 10,
  duration: '1m',
};
```
- **Refactored:**
```js
export let options = {
  vus: 10,
  duration: '1m',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [18]
- **Snippet:**
```js
http.put(url+`/29145037094`,JSON.stringify(data), { headers: headers } );
```
- **Refactored:**
```js
import { check } from 'k6';

export default function () {
  var url = 'http://localhost:8081/v1/user';
  const data = {
    first_name: 'Jefferson',
    last_name: 'Otoni',
    birthday: '1980-08-20',
  };

  const res = http.put(`${url}/29145037094`, JSON.stringify(data), { headers: headers });

  check(res, {
    'PUT /v1/user/{id} status is 200': (r) => r.status === 200,
    'PUT /v1/user/{id} response is not empty': (r) => r.body && r.body.length > 0,
  });
}
```

**Smell 4: Not using tags**

- **Lines:** [18]
- **Snippet:**
```js
http.put(url+`/29145037094`,JSON.stringify(data), { headers: headers } );
```
- **Refactored:**
```js
http.put(`${url}/29145037094`, JSON.stringify(data), {
  headers: headers,
  tags: {
    endpoint: 'update_user',
    method: 'PUT',
    resource: 'user',
  },
});
```

### `script_51.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9]
- **Snippet:**
```js
export let options = {
  vus: 10,
  duration: '1m',
};
```
- **Refactored:**
```js
export let options = {
  vus: 10,
  duration: '1m',
  thresholds: {
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [18]
- **Snippet:**
```js
http.put(url+`/29145037094`,JSON.stringify(data), { headers: headers } );
```
- **Refactored:**
```js
import { check } from 'k6';
// ... in default function
const res = http.put(url+`/29145037094`,JSON.stringify(data), { headers: headers });
check(res, {
  'update user request status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [18]
- **Snippet:**
```js
http.put(url+`/29145037094`,JSON.stringify(data), { headers: headers } );
```
- **Refactored:**
```js
http.put(url+`/29145037094`, JSON.stringify(data), {
  headers: headers,
  tags: {
    name: 'UpdateUser',
  },
});
```

### `script_52.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
- **Snippet:**
```js
export const options = {
    stages: [
        {
            duration: '2m',
            target: 40,
        },
        {
            duration: '1m',
            target: 0,
        }
    ]
}
```
- **Refactored:**
```js
export const options = {
    stages: [
        {
            duration: '2m',
            target: 40,
        },
        {
            duration: '1m',
            target: 0,
        }
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
    }
}
```

**Smell 3: Not checking requests**

- **Lines:** [18]
- **Snippet:**
```js
http.get('https://test.k6.io');
```
- **Refactored:**
```js
import { check } from 'k6';

// inside default function:
const res = http.get('https://test.k6.io');
check(res, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [18]
- **Snippet:**
```js
http.get('https://test.k6.io');
```
- **Refactored:**
```js
const res = http.get('https://test.k6.io', {
    tags: { name: 'homepage', endpoint: 'test.k6.io' }
});
```

### `script_52.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
- **Snippet:**
```js
export const options = {
    stages: [
        {
            duration: '2m',
            target: 40,
        },
        {
            duration: '1m',
            target: 0,
        }
    ]
}
```
- **Refactored:**
```js
export const options = {
    stages: [
        { duration: '2m', target: 40 },
        { duration: '1m', target: 0 }
    ],
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500']
    }
};
```

**Smell 3: Not checking requests**

- **Lines:** [18]
- **Snippet:**
```js
http.get('https://test.k6.io');
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default function () {
    const res = http.get('https://test.k6.io');
    check(res, {
        'GET / status is 200': (r) => r.status === 200,
        'GET / body is not empty': (r) => r.body && r.body.length > 0
    });
    sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [18]
- **Snippet:**
```js
http.get('https://test.k6.io');
```
- **Refactored:**
```js
export default function () {
    const params = {
        tags: {
            endpoint: 'home',
            flow: 'landing_page'
        }
    };
    http.get('https://test.k6.io', params);
    sleep(1);
}
```

### `script_52.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
- **Snippet:**
```js
export const options = {
    stages: [
        {
            duration: '2m',
            target: 40,
        },
        {
            duration: '1m',
            target: 0,
        }
    ]
}
```
- **Refactored:**
```js
export const options = {
    stages: [
        {
            duration: '2m',
            target: 40,
        },
        {
            duration: '1m',
            target: 0,
        }
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<200'],
    }
}
```

**Smell 3: Not checking requests**

- **Lines:** [18]
- **Snippet:**
```js
http.get('https://test.k6.io');
```
- **Refactored:**
```js
const res = http.get('https://test.k6.io');
check(res, {
    'is status 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [18]
- **Snippet:**
```js
http.get('https://test.k6.io');
```
- **Refactored:**
```js
http.get('https://test.k6.io', {
    tags: {
        name: 'Homepage',
    },
});
```

### `script_53.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
- **Snippet:**
```js
export const options = {
  stages: [
    { duration: '2m', target: 100 },
    { duration: '5m', target: 100 },
    ...
  ],
};
```
- **Refactored:**
```js
export const options = {
  stages: [
    { duration: '2m', target: 100 },
    { duration: '5m', target: 100 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [22, 23, 24, 25, 26, 27, 28]
- **Snippet:**
```js
const responses = http.batch([
    ['GET', `${BASE_URL}/...`, null, { tags: { name: 'PublicCrocs' } }],
    ...
  ]);
```
- **Refactored:**
```js
import { check } from 'k6';

// inside default function:
const responses = http.batch([
    ['GET', `${BASE_URL}/departaments/Informatica/Segur01.nsf/xsp/.ibmmodres/domino/OpenAttachment/departaments/Informatica/Segur01.nsf/4B4D663F2463B917C12580DC002D0EC0/Body/doc%20web%20incidencias%20mbi.v3.pdf`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/departaments/Informatica/Segur01.nsf/xsp/.ibmmodres/domino/OpenAttachment/departaments/Informatica/Segur01.nsf/959624B092DFBEECC12580E3003AA2DF/Body/lnvgy_fod_0001_8869J311Y9K_anyos_noarch.key`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/departaments/Informatica/Segur01.nsf/xsp/.ibmmodres/domino/OpenAttachment/departaments/Informatica/Segur01.nsf/959624B092DFBEECC12580E3003AA2DF/Body/lnvgy_fod_0001_8869J311YA6_anyos_noarch.key`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/departaments/Informatica/Segur01.nsf/xsp/.ibmmodres/domino/OpenAttachment/departaments/Informatica/Segur01.nsf/959624B092DFBEECC12580E3003AA2DF/Body/lnvgy_fod_0001_8869J311YA9_anyos_noarch.key`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/departaments/Informatica/Segur01.nsf/xsp/.ibmmodres/domino/OpenAttachment/departaments/Informatica/Segur01.nsf/E18FD095EE09D072C12581F7003DC744/Body/estructura%2busuarisbasics.ldif`, null, { tags: { name: 'PublicCrocs' } }],
  ]);

  responses.forEach((res) => {
    check(res, {
      'status is 200': (r) => r.status === 200,
    });
  });
```

### `script_53.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
- **Snippet:**
```js
export const options = {
  stages: [
    { duration: '2m', target: 100 },
    { duration: '5m', target: 100 },
  ],
};
```
- **Refactored:**
```js
export const options = {
  stages: [
    { duration: '2m', target: 100 },
    { duration: '5m', target: 100 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [22, 23, 24, 25, 26, 27, 28]
- **Snippet:**
```js
const responses = http.batch([
  ['GET', `${BASE_URL}/departaments/Informatica/Segur01.nsf/xsp/.ibmmodres/domino/OpenAttachment/departaments/Informatica/Segur01.nsf/4B4D663F2463B917C12580DC002D0EC0/Body/doc%20web%20incidencias%20mbi.v3.pdf`, null, { tags: { name: 'PublicCrocs' } }],
  ['GET', `${BASE_URL}/departaments/Informatica/Segur01.nsf/xsp/.ibmmodres/domino/OpenAttachment/departaments/Informatica/Segur01.nsf/959624B092DFBEECC12580E3003AA2DF/Body/lnvgy_fod_0001_8869J311Y9K_anyos_noarch.key`, null, { tags: { name: 'PublicCrocs' } }],
]);
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

const responses = http.batch([
  ['GET', `${BASE_URL}/departaments/Informatica/Segur01.nsf/xsp/.ibmmodres/domino/OpenAttachment/departaments/Informatica/Segur01.nsf/4B4D663F2463B917C12580DC002D0EC0/Body/doc%20web%20incidencias%20mbi.v3.pdf`, null, { tags: { name: 'PublicCrocs' } }],
  ['GET', `${BASE_URL}/departaments/Informatica/Segur01.nsf/xsp/.ibmmodres/domino/OpenAttachment/departaments/Informatica/Segur01.nsf/959624B092DFBEECC12580E3003AA2DF/Body/lnvgy_fod_0001_8869J311Y9K_anyos_noarch.key`, null, { tags: { name: 'PublicCrocs' } }],
]);

responses.forEach((res) => {
  check(res, {
    'status is 200': (r) => r.status === 200,
  });
});
```

### `script_53.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 16]
- **Snippet:**
```js
export const options = {
  stages: [
    { duration: '2m', target: 100 }, // below normal load
    { duration: '5m', target: 100 },
    //{ duration: '2m', target: 200 }, // normal load
    //{ duration: '5m', target: 200 },
    //{ duration: '2m', target: 300 }, // around the breaking point
    //{ duration: '5m', target: 300 },
    //{ duration: '2m', target: 400 }, // beyond the breaking point
    //{ duration: '5m', target: 400 },
    //{ duration: '10m', target: 0 }, // scale down. Recovery stage.
  ],
};
```
- **Refactored:**
```js
export const options = {
  stages: [
    { duration: '2m', target: 100 }, // below normal load
    { duration: '5m', target: 100 },
    //{ duration: '2m', target: 200 }, // normal load
    //{ duration: '5m', target: 200 },
    //{ duration: '2m', target: 300 }, // around the breaking point
    //{ duration: '5m', target: 300 },
    //{ duration: '2m', target: 400 }, // beyond the breaking point
    //{ duration: '5m', target: 400 },
    //{ duration: '10m', target: 0 }, // scale down. Recovery stage.
  ],
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<2000'], // 95% of requests should be below 2000ms
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [22, 28]
- **Snippet:**
```js
const responses = http.batch([
    ['GET', `${BASE_URL}/departaments/Informatica/Segur01.nsf/xsp/.ibmmodres/domino/OpenAttachment/departaments/Informatica/Segur01.nsf/4B4D663F2463B917C12580DC002D0EC0/Body/doc%20web%20incidencias%20mbi.v3.pdf`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/departaments/Informatica/Segur01.nsf/xsp/.ibmmodres/domino/OpenAttachment/departaments/Informatica/Segur01.nsf/959624B092DFBEECC12580E3003AA2DF/Body/lnvgy_fod_0001_8869J311Y9K_anyos_noarch.key`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/departaments/Informatica/Segur01.nsf/xsp/.ibmmodres/domino/OpenAttachment/departaments/Informatica/Segur01.nsf/959624B092DFBEECC12580E3003AA2DF/Body/lnvgy_fod_0001_8869J311YA6_anyos_noarch.key`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/departaments/Informatica/Segur01.nsf/xsp/.ibmmodres/domino/OpenAttachment/departaments/Informatica/Segur01.nsf/959624B092DFBEECC12580E3003AA2DF/Body/lnvgy_fod_0001_8869J311YA9_anyos_noarch.key`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/departaments/Informatica/Segur01.nsf/xsp/.ibmmodres/domino/OpenAttachment/departaments/Informatica/Segur01.nsf/E18FD095EE09D072C12581F7003DC744/Body/estructura%2busuarisbasics.ldif`, null, { tags: { name: 'PublicCrocs' } }],
  ]);
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
export default function () {
  // ...
  const responses = http.batch([
    // ... batch requests
  ]);

  check(responses, {
    'all responses were successful': (res) => res.every(r => r.status === 200),
  });

  sleep(1);
}
```

### `script_55.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
- **Snippet:**
```js
const image = open('car.jpg', 'b');
const fd = new FormData();
fd.append('payload', http.file(image, 'image.png', 'image/png'));
let resnet = {
        method: 'POST',
        url: 'http://localhost:5000/predict',
        body: fd.body(), 
        params: {
            headers: {
	            'Content-Type': 'multipart/form-data; boundary=' + fd.boundary 
	          },
        },
};
```
- **Refactored:**
```js
// Keep open() in init context (it is allowed), but move FormData construction and fd.body() call inside the default function to avoid sharing mutable state across VUs
const image = open('car.jpg', 'b');

export default function () {
  const fd = new FormData();
  fd.append('payload', http.file(image, 'image.png', 'image/png'));
  const params = {
    headers: {
      'Content-Type': 'multipart/form-data; boundary=' + fd.boundary
    },
  };
  const res = http.post('http://localhost:5000/predict', fd.body(), params);
  check(res, {
    'is status 200': (r) => r.status === 200,
  });
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
- **Snippet:**
```js
export const options = {
   scenarios: {
    contacts: {
      executor: 'constant-vus',
      startTime: '0s',
      vus: 5,
      duration: '1m',
   },
  },
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'constant-vus',
      startTime: '0s',
      vus: 5,
      duration: '1m',
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    'checks': ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [34]
- **Snippet:**
```js
const res = http.post(resnet.url, resnet.body, resnet.params)
```
- **Refactored:**
```js
const res = http.post(resnet.url, resnet.body, {
  ...resnet.params,
  tags: { name: 'resnet_predict', endpoint: '/predict' },
});
```

### `script_55.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [19]
- **Snippet:**
```js
const image = open('car.jpg', 'b');
```
- **Refactored:**
```js
export function setup() {
  // Read the file only once for all VUs and pass its content to them.
  const image = open('car.jpg', 'b');
  return image;
}

export default function (image) {
  // The FormData object is now created per iteration, which is safer.
  const fd = new FormData();
  fd.append('payload', http.file(image, 'image.png', 'image/png'));
  
  const resnet = {
    body: fd.body(), 
    params: {
      headers: {
        'Content-Type': 'multipart/form-data; boundary=' + fd.boundary 
      },
    },
  };

  const res = http.post('http://localhost:5000/predict', resnet.body, resnet.params)
  check(res, {
    'is status 200': (r) => r.status === 200,
  });
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [8, 17]
- **Snippet:**
```js
export const options = {
   scenarios: {
    contacts: {
      executor: 'constant-vus',
      startTime: '0s',
      vus: 5,
      duration: '1m',
   },
  },
};
```
- **Refactored:**
```js
export const options = {
   scenarios: {
    contacts: {
      executor: 'constant-vus',
      startTime: '0s',
      vus: 5,
      duration: '1m',
   },
  },
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks': ['rate>0.99']            // Over 99% of checks should pass
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [27, 31]
- **Snippet:**
```js
params: {
    headers: {
	            'Content-Type': 'multipart/form-data; boundary=' + fd.boundary 
	          },
        },
```
- **Refactored:**
```js
params: {
    headers: {
	            'Content-Type': 'multipart/form-data; boundary=' + fd.boundary 
	          },
    tags: {
      name: 'ResNetPrediction', // Add a tag to categorize metrics
    },
},
```

### `script_56.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
- **Snippet:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'shared-iterations',
      vus: 10,
      iterations: 200,
      maxDuration: '30s',
    },
  },
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'shared-iterations',
      vus: 10,
      iterations: 200,
      maxDuration: '30s',
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
import { check } from 'k6';

const res = http.get('https://test.k6.io/contacts.php');
check(res, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
http.get('https://test.k6.io/contacts.php', {
  tags: { name: 'contacts_page', endpoint: '/contacts.php' },
});
```

### `script_56.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
- **Snippet:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'shared-iterations',
      vus: 10,
      iterations: 200,
      maxDuration: '30s',
    },
  },
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'shared-iterations',
      vus: 10,
      iterations: 200,
      maxDuration: '30s',
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default function () {
  const res = http.get('https://test.k6.io/contacts.php');
  check(res, {
    'contacts page status is 200': (r) => r.status === 200,
  });
  sleep(0.5);
}
```

**Smell 4: Not using tags**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
export default function () {
  http.get('https://test.k6.io/contacts.php', {
    tags: {
      endpoint: 'contacts',
      flow: 'contacts_page',
    },
  });
  sleep(0.5);
}
```

### `script_56.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
- **Snippet:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'shared-iterations',
      vus: 10,
      iterations: 200,
      maxDuration: '30s',
    },
  },
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'shared-iterations',
      vus: 10,
      iterations: 200,
      maxDuration: '30s',
    },
  },
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<200'], // 95% of requests should be below 200ms
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
const res = http.get('https://test.k6.io/contacts.php');
check(res, { 'status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
http.get('https://test.k6.io/contacts.php', {
  tags: { name: 'ContactsPage' },
});
```

### `script_59.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [16, 17]
- **Snippet:**
```js
const csvData = open('../logsCSV/exam/accessToken.csv');
const userTokenData = papaparse.parse(csvData).data;
```
- **Refactored:**
```js
// open() is acceptable in init context, but papaparse.parse() is a heavy computation
// that runs once per VU. For large CSV files, consider pre-processing the data
// outside of k6 and loading a simpler format, or cache the result at the module level
// so it is computed only once (which it already is at module scope, but be aware
// that for large files this still runs per-VU init phase).
// If the file is large, pre-convert to JSON externally and load with JSON.parse via open():
const csvData = open('../logsCSV/exam/accessToken.csv');
// Parsing is unavoidable here, but ensure the CSV file is as small as possible
// and consider using a pre-parsed JSON file instead:
// const userTokenData = JSON.parse(open('../logsCSV/exam/accessToken.json'));
const userTokenData = papaparse.parse(csvData).data;
```

**Smell 2: Do not use thresholds**

- **Lines:** [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: "1s", target: 4000 },
    ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: "1s", target: 4000 },
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'],          // less than 1% of requests should fail
        'http_req_duration': ['p(95)<500'],        // 95% of requests should complete within 500ms
        'checks': ['rate>0.99'],                   // more than 99% of checks should pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [46, 47, 48]
- **Snippet:**
```js
let orderRes = http.get(`${baseUrl}/exam-service/v1/group-exams`, {
    headers: headers
});
```
- **Refactored:**
```js
let orderRes = http.get(`${baseUrl}/exam-service/v1/group-exams`, {
    headers: headers,
    tags: { name: 'GetGroupExams', endpoint: '/exam-service/v1/group-exams', flow: 'exam' }
});
```

### `script_59.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [16, 17]
- **Snippet:**
```js
const csvData = open('../logsCSV/exam/accessToken.csv');
const userTokenData = papaparse.parse(csvData).data;
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

const userTokenData = new SharedArray('user tokens', function () {
  const csvData = open('../logsCSV/exam/accessToken.csv');
  return papaparse.parse(csvData).data;
});
```

**Smell 2: Do not use thresholds**

- **Lines:** [20, 29]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: "1s", target: 4000 },
      ],
};
```
- **Refactored:**
```js
export let options = {
  stages: [
    { duration: '1s', target: 4000 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<200'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [46, 48]
- **Snippet:**
```js
let orderRes = http.get(`${baseUrl}/exam-service/v1/group-exams`, {
    headers: headers
});
```
- **Refactored:**
```js
let orderRes = http.get(`${baseUrl}/exam-service/v1/group-exams`, {
  headers: headers,
  tags: {
    endpoint: 'group-exams',
    service: 'exam-service',
    flow: 'get-group-exams'
  }
});
```

### `script_59.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [16, 17]
- **Snippet:**
```js
const csvData = open('../logsCSV/exam/accessToken.csv');
const userTokenData = papaparse.parse(csvData).data;
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

const userTokenData = new SharedArray('user data', function () {
  // All VUs will share the same data array
  return papaparse.parse(open('../logsCSV/exam/accessToken.csv'), { header: false }).data;
});
```

**Smell 2: Do not use thresholds**

- **Lines:** [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
- **Snippet:**
```js
export let options = {
	//executor: 'shared-iterations',
	// iterations: 2,
	// vus: 1,
    // duration: '2s',
    stages: [
        // Ramp up to 1 VUs for 5 second
        { duration: "1s", target: 4000 },
      ],
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: "1s", target: 4000 },
      ],
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
        'checks': ['rate>0.99'], // 99% of checks must pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [46, 47, 48]
- **Snippet:**
```js
let orderRes = http.get(`${baseUrl}/exam-service/v1/group-exams`, {
    headers: headers
});
```
- **Refactored:**
```js
let orderRes = http.get(`${baseUrl}/exam-service/v1/group-exams`, {
    headers: headers,
    tags: {
        name: 'GetGroupExamsAPI'
    }
});
```

### `script_60.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
- **Snippet:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'per-vu-iterations',
            vus: 10,
            iterations: 20,
            maxDuration: '30s'
        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'per-vu-iterations',
            vus: 10,
            iterations: 20,
            maxDuration: '30s'
        },
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php')
```
- **Refactored:**
```js
import { check } from 'k6';

const res = http.get('https://test.k6.io/contacts.php');
check(res, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php')
```
- **Refactored:**
```js
http.get('https://test.k6.io/contacts.php', {
    tags: { name: 'contacts', endpoint: '/contacts.php' },
});
```

### `script_60.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
- **Snippet:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'per-vu-iterations',
            vus: 10,
            iterations: 20,
            maxDuration: '30s'
        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'per-vu-iterations',
            vus: 10,
            iterations: 20,
            maxDuration: '30s'
        },
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php')
```
- **Refactored:**
```js
import { sleep, check } from 'k6'

export default function () {
    const res = http.get('https://test.k6.io/contacts.php')
    check(res, {
        'contacts page status is 200': (r) => r.status === 200,
    })
    sleep(0.5)
}
```

**Smell 4: Not using tags**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php')
```
- **Refactored:**
```js
export default function () {
    http.get('https://test.k6.io/contacts.php', {
        tags: { endpoint: 'contacts' }
    })
    sleep(0.5)
}
```

### `script_60.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
- **Snippet:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'per-vu-iterations',
            vus: 10,
            iterations: 20,
            maxDuration: '30s'
        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'per-vu-iterations',
            vus: 10,
            iterations: 20,
            maxDuration: '30s'
        },
    },
    thresholds: {
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<200'], // 95% of requests should be below 200ms
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php')
```
- **Refactored:**
```js
import { check } from 'k6';
// ...

const res = http.get('https://test.k6.io/contacts.php');
check(res, {
  'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php')
```
- **Refactored:**
```js
http.get('https://test.k6.io/contacts.php', {
  tags: { name: 'ContactsPage' },
});
```

### `script_61.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
- **Snippet:**
```js
const image = open('car.jpg', 'b');
const fd = new FormData();
fd.append('payload', http.file(image, 'image.png', 'image/png'));
let resnet = {
        method: 'POST',
	url: 'http://localhost:5000/predict',
        body: fd.body(), 
        params: {
            headers: {
	      'Content-Type': 'multipart/form-data; boundary=' + fd.boundary 
	    },
        },
};
```
- **Refactored:**
```js
// Keep only the file read in init context (it must stay there)
const image = open('car.jpg', 'b');
const gateway = 'http://10.103.51.65:8080';

export default function () {
  // Build FormData and request body inside the VU function to avoid heavy init-context work
  const fd = new FormData();
  fd.append('payload', http.file(image, 'image.png', 'image/png'));
  const params = {
    headers: {
      'Content-Type': 'multipart/form-data; boundary=' + fd.boundary
    },
    tags: { endpoint: 'resnet-predict' }
  };
  const res = http.post('http://localhost:5000/predict', fd.body(), params);
  check(res, {
    'is status 200': (r) => r.status === 200,
  });
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
- **Snippet:**
```js
export const options = {
   scenarios: {
    contacts: {
      executor: 'constant-vus',
      startTime: '0s',
      vus: 10,
      duration: '2m',
   },
  },
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'constant-vus',
      startTime: '0s',
      vus: 10,
      duration: '2m',
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],       // less than 1% of requests should fail
    http_req_duration: ['p(95)<500'],     // 95% of requests must complete within 500ms
    checks: ['rate>0.99'],                // more than 99% of checks must pass
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [34]
- **Snippet:**
```js
const res = http.post(resnet.url, resnet.body, resnet.params)
```
- **Refactored:**
```js
const params = {
  headers: {
    'Content-Type': 'multipart/form-data; boundary=' + fd.boundary
  },
  tags: { endpoint: 'resnet-predict', method: 'POST' }
};
const res = http.post(resnet.url, resnet.body, params);
```

### `script_61.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [19, 20, 21]
- **Snippet:**
```js
const image = open('car.jpg', 'b');
const fd = new FormData();
fd.append('payload', http.file(image, 'image.png', 'image/png'));
```
- **Refactored:**
```js
// Move file reading and data preparation to the setup function, which runs only once.
export function setup() {
  const image = open('car.jpg', 'b');
  const fd = new FormData();
  fd.append('payload', http.file(image, 'image.png', 'image/png'));
  
  const requestData = {
    body: fd.body(),
    params: {
      headers: { 'Content-Type': 'multipart/form-data; boundary=' + fd.boundary },
    }
  };
  return requestData;
}

// The default function receives the data prepared by setup() and reuses it for each iteration.
export default function (data) {
  const res = http.post('http://localhost:5000/predict', data.body, data.params);
  // ...
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
- **Snippet:**
```js
export const options = {
   scenarios: {
    contacts: {
      executor: 'constant-vus',
      startTime: '0s',
      vus: 10,
      duration: '2m',
   },
  },
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'constant-vus',
      startTime: '0s',
      vus: 10,
      duration: '2m',
    },
  },
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [27, 28, 29, 30, 31]
- **Snippet:**
```js
params: {
    headers: {
	      'Content-Type': 'multipart/form-data; boundary=' + fd.boundary 
	    },
},
```
- **Refactored:**
```js
params: {
    headers: {
        'Content-Type': 'multipart/form-data; boundary=' + fd.boundary
    },
    tags: {
        name: 'ImagePredictionAPI',
    },
},
```

### `script_62.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
- **Snippet:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'per-vu-iterations',
      vus: 10,
      iterations: 20,
      maxDuration: '30s',
    },
  },
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'per-vu-iterations',
      vus: 10,
      iterations: 20,
      maxDuration: '30s',
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
import { check } from 'k6';

// inside default function:
const res = http.get('https://test.k6.io/contacts.php');
check(res, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
http.get('https://test.k6.io/contacts.php', {
  tags: { name: 'contacts_page', endpoint: '/contacts.php' },
});
```

### `script_62.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
- **Snippet:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'per-vu-iterations',
      vus: 10,
      iterations: 20,
      maxDuration: '30s',
    },
  },
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'per-vu-iterations',
      vus: 10,
      iterations: 20,
      maxDuration: '30s',
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default function () {
  const res = http.get('https://test.k6.io/contacts.php');
  check(res, {
    'contacts status is 200': (r) => r.status === 200,
  });
  sleep(0.5);
}
```

**Smell 4: Not using tags**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
export default function () {
  const res = http.get('https://test.k6.io/contacts.php', {
    tags: { endpoint: 'contacts', flow: 'contacts' },
  });
  sleep(0.5);
}
```

### `script_62.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
- **Snippet:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'per-vu-iterations',
      vus: 10,
      iterations: 20,
      maxDuration: '30s',
    },
  },
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    contacts: {
      executor: 'per-vu-iterations',
      vus: 10,
      iterations: 20,
      maxDuration: '30s',
    },
  },
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
import { check } from 'k6';
// ... in default function
const res = http.get('https://test.k6.io/contacts.php');
check(res, { 'status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
http.get('https://test.k6.io/contacts.php', {
  tags: { name: 'GetContacts' },
});
```

### `script_63.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '30s',
    cloud: {
        projectID: 3771795
    }
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '30s',
    cloud: {
        projectID: 3771795
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500']
    }
}
```

**Smell 3: Not checking requests**

- **Lines:** [13]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
```
- **Refactored:**
```js
import { check } from 'k6';

// inside default function:
const res = http.get('https://quickpizza.grafana.com/test.k6.io/');
check(res, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0
});
```

**Smell 4: Not using tags**

- **Lines:** [13]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
```
- **Refactored:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/', {
    tags: { name: 'homepage', endpoint: 'test.k6.io' }
});
```

### `script_63.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '30s',
    cloud: {
        projectID: 3771795
    }
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '30s',
    cloud: {
        projectID: 3771795
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500']
    }
};
```

**Smell 3: Not checking requests**

- **Lines:** [13]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default function () {
    const res = http.get('https://quickpizza.grafana.com/test.k6.io/');
    check(res, {
        'status is 200': (r) => r.status === 200
    });
    sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [13]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
```
- **Refactored:**
```js
export default function () {
    http.get('https://quickpizza.grafana.com/test.k6.io/', {
        tags: {
            endpoint: 'home',
            flow: 'quickpizza_test'
        }
    });
    sleep(1);
}
```

### `script_63.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '30s',
    cloud: {
        projectID: 3771795
    }
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '30s',
    cloud: {
        projectID: 3771795
    },
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    }
}
```

**Smell 3: Not checking requests**

- **Lines:** [13]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const res = http.get('https://quickpizza.grafana.com/test.k6.io/');
check(res, { 'status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [13]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
```
- **Refactored:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/', {
    tags: { name: 'Homepage' },
});
```

### `script_69.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
- **Snippet:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'per-vu-iterations',
            vus:10,
            iterations: 20,
            maxDuration: '30s',
        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'per-vu-iterations',
            vus: 10,
            iterations: 20,
            maxDuration: '30s',
        },
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [17]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
import { check } from 'k6';

// inside default function:
const res = http.get('https://test.k6.io/contacts.php');
check(res, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [17]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
const res = http.get('https://test.k6.io/contacts.php', {
    tags: { name: 'contacts', endpoint: '/contacts.php' },
});
```

### `script_69.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
- **Snippet:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'per-vu-iterations',
            vus:10,
            iterations: 20,
            maxDuration: '30s',
        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'per-vu-iterations',
            vus: 10,
            iterations: 20,
            maxDuration: '30s',
        },
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [17]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default function() {
    const res = http.get('https://test.k6.io/contacts.php');
    check(res, {
        'contacts page status is 200': (r) => r.status === 200,
    });
    sleep(0.5);
}
```

**Smell 4: Not using tags**

- **Lines:** [17]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
export default function() {
    http.get('https://test.k6.io/contacts.php', {
        tags: {
            endpoint: 'contacts',
            flow: 'contacts',
        },
    });
    sleep(0.5);
}
```

### `script_69.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4]
- **Snippet:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'per-vu-iterations',
            vus:10,
            iterations: 20,
            maxDuration: '30s',

        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'per-vu-iterations',
            vus: 10,
            iterations: 20,
            maxDuration: '30s',
        },
    },
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [17]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
import http from 'k6/http';
import { sleep, check } from 'k6';
// ... inside default function
const res = http.get('https://test.k6.io/contacts.php');
check(res, {
    'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [17]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php');
```
- **Refactored:**
```js
http.get('https://test.k6.io/contacts.php', {
    tags: { name: 'GetContacts' },
});
```

### `script_70.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export const options = {
    vus: 5,
    duration: '20s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 5,
    duration: '20s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500']
    }
}
```

**Smell 3: Not checking requests**

- **Lines:** [11]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
import { check } from 'k6';

// inside default function:
const res = http.get('https://quickpizza.grafana.com');
check(res, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0
});
```

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
http.get('https://quickpizza.grafana.com', {
    tags: { name: 'homepage', endpoint: 'quickpizza-home' }
});
```

### `script_70.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export const options = {
    vus: 5,
    duration: '20s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 5,
    duration: '20s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500']
    }
};
```

**Smell 3: Not checking requests**

- **Lines:** [11]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

const res = http.get('https://quickpizza.grafana.com');
check(res, {
    'homepage status is 200': (r) => r.status === 200
});
```

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
const res = http.get('https://quickpizza.grafana.com', {
    tags: {
        endpoint: 'homepage',
        flow: 'browse'
    }
});
```

### `script_70.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export const options = {
    vus: 5,
    duration: '20s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 5,
    duration: '20s',
    thresholds: {
        http_req_failed: ['rate<0.01'],   // http errors should be less than 1%
        http_req_duration: ['p(95)<500'], // 95% of requests must complete below 500ms
    },
}
```

**Smell 3: Not checking requests**

- **Lines:** [11]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
const res = http.get('https://quickpizza.grafana.com');
check(res, {
    'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
http.get('https://quickpizza.grafana.com', {
    tags: { 
        name: 'Homepage' 
    },
});
```

### `script_71.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
- **Snippet:**
```js
export const options = {
  vus: 100,
  duration: '10s',
  ext: { ... }
};
```
- **Refactored:**
```js
export const options = {
  vus: 100,
  duration: '10s',
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
  ext: {
    loadimpact: {
      projectID: 3671346,
      name: 'Test (27/11/2023-12:13:48)'
    }
  }
};
```

**Smell 3: Not checking requests**

- **Lines:** [18]
- **Snippet:**
```js
http.get('http://test.k6.io');
```
- **Refactored:**
```js
import { check } from 'k6';

// inside default function:
const res = http.get('http://test.k6.io');
check(res, {
  'status is 200': (r) => r.status === 200,
  'response time < 500ms': (r) => r.timings.duration < 500,
});
```

**Smell 4: Not using tags**

- **Lines:** [18]
- **Snippet:**
```js
http.get('http://test.k6.io');
```
- **Refactored:**
```js
const res = http.get('http://test.k6.io', {
  tags: { name: 'homepage', endpoint: 'test.k6.io' },
});
```

### `script_71.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
- **Snippet:**
```js
export const options = {
  vus: 100,
  duration: '10s',
  ext: { ... }
};
```
- **Refactored:**
```js
export const options = {
  vus: 100,
  duration: '10s',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500']
  },
  ext: {
    loadimpact: {
      projectID: 3671346,
      name: 'Test (27/11/2023-12:13:48)'
    }
  }
};
```

**Smell 3: Not checking requests**

- **Lines:** [18]
- **Snippet:**
```js
http.get('http://test.k6.io');
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default function() {
  const res = http.get('http://test.k6.io');
  check(res, {
    'GET / status is 200': (r) => r.status === 200
  });
  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [18]
- **Snippet:**
```js
http.get('http://test.k6.io');
```
- **Refactored:**
```js
export default function() {
  const res = http.get('http://test.k6.io', {
    tags: {
      endpoint: 'home',
      flow: 'homepage'
    }
  });
  sleep(1);
}
```

### `script_71.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
- **Snippet:**
```js
export const options = {
  vus: 100,
  duration: '10s',
  ext: {
    loadimpact: {
      // Project: apresentação_Tech
      projectID: 3671346,
      // Test runs with the same name groups test runs together.
      name: 'Test (27/11/2023-12:13:48)'
    }
  }
};
```
- **Refactored:**
```js
export const options = {
  vus: 100,
  duration: '10s',
  thresholds: {
    http_req_failed: ['rate<0.01'],   // http errors should be less than 1%
    http_req_duration: ['p(95)<200'], // 95% of requests should be below 200ms
  },
  ext: {
    loadimpact: {
      // Project: apresentação_Tech
      projectID: 3671346,
      // Test runs with the same name groups test runs together.
      name: 'Test (27/11/2023-12:13:48)'
    }
  }
};
```

**Smell 3: Not checking requests**

- **Lines:** [18]
- **Snippet:**
```js
http.get('http://test.k6.io');
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const res = http.get('http://test.k6.io');
check(res, {
  'status was 200': (r) => r.status == 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [18]
- **Snippet:**
```js
http.get('http://test.k6.io');
```
- **Refactored:**
```js
http.get('http://test.k6.io', {
  tags: {
    name: 'PublicHomepage',
  },
});
```

### `script_76.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11, 12]
- **Snippet:**
```js
export const options = {
  stages: [
     { duration: '2s', target: 10 },
  ],
};
```
- **Refactored:**
```js
export const options = {
  stages: [
     { duration: '2s', target: 10 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    shufflenet_http_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [21, 22]
- **Snippet:**
```js
let res = http.batch([paddle])
```
- **Refactored:**
```js
let res = http.batch([paddle]);
check(res[0], {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [16, 17, 18, 19]
- **Snippet:**
```js
let paddle = {
        method: 'GET',
        url: 'http://10.109.232.51:8080/function/shufflenet/',
};
```
- **Refactored:**
```js
let paddle = {
        method: 'GET',
        url: 'http://10.109.232.51:8080/function/shufflenet/',
        params: {
          tags: { name: 'shufflenet', endpoint: '/function/shufflenet/' },
        },
};
```

### `script_76.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11, 12]
- **Snippet:**
```js
export const options = {
  stages: [
     { duration: '2s', target: 10 },
  ],
};
```
- **Refactored:**
```js
export const options = {
  stages: [
    { duration: '2s', target: 10 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [21]
- **Snippet:**
```js
let res = http.batch([paddle])
```
- **Refactored:**
```js
let res = http.batch([paddle]);

check(res[0], {
  'shufflenet status is 200': (r) => r.status === 200,
  'shufflenet response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [16, 17, 18, 19]
- **Snippet:**
```js
let paddle = {
        method: 'GET',
        url: 'http://10.109.232.51:8080/function/shufflenet/',
};
```
- **Refactored:**
```js
let paddle = {
  method: 'GET',
  url: 'http://10.109.232.51:8080/function/shufflenet/',
  params: {
    tags: {
      endpoint: 'shufflenet',
      flow: 'inference',
    },
  },
};
```

### `script_76.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11, 12]
- **Snippet:**
```js
export const options = {
  stages: [
     { duration: '2s', target: 10 },
  ],
};
```
- **Refactored:**
```js
export const options = {
  stages: [
     { duration: '2s', target: 10 },
  ],
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [21]
- **Snippet:**
```js
let res = http.batch([paddle])
```
- **Refactored:**
```js
let res = http.batch([paddle]);
check(res[0], {
  'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [16, 17, 18, 19, 21]
- **Snippet:**
```js
let paddle = {
        method: 'GET',
        url: 'http://10.109.232.51:8080/function/shufflenet/',
};

let res = http.batch([paddle])
```
- **Refactored:**
```js
let paddle = {
        method: 'GET',
        url: 'http://10.109.232.51:8080/function/shufflenet/',
        params: {
          tags: { name: 'ShuffleNetRequest' }, // Tag the request
        },
};

let res = http.batch([paddle]);
// Add the response time to the custom Trend metric, with tags
shufflenet_http_duration.add(res[0].timings.duration, { name: 'ShuffleNetRequest' });
```

### `script_77.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12]
- **Snippet:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'constant-vus',
            vus: 10,
            duration: '30s'
        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'constant-vus',
            vus: 10,
            duration: '30s'
        },
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [15]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php')
```
- **Refactored:**
```js
import { check } from 'k6';

const res = http.get('https://test.k6.io/contacts.php');
check(res, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [15]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php')
```
- **Refactored:**
```js
http.get('https://test.k6.io/contacts.php', { tags: { name: 'contacts', endpoint: '/contacts.php' } });
```

### `script_77.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12]
- **Snippet:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'constant-vus',
            vus: 10,
            duration: '30s'
        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'constant-vus',
            vus: 10,
            duration: '30s'
        },
    },
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [15]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php')
```
- **Refactored:**
```js
import { sleep, check } from 'k6'

export default function () {
    const res = http.get('https://test.k6.io/contacts.php')
    check(res, {
        'contacts page returned 200': (r) => r.status === 200,
        'contacts page is not empty': (r) => r.body && r.body.length > 0,
    })
    sleep(0.5)
}
```

**Smell 4: Not using tags**

- **Lines:** [15]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php')
```
- **Refactored:**
```js
export default function () {
    const res = http.get('https://test.k6.io/contacts.php', {
        tags: {
            endpoint: 'contacts',
            flow: 'contacts',
        },
    })
    sleep(0.5)
}
```

### `script_77.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12]
- **Snippet:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'constant-vus',
            vus: 10,
            duration: '30s'
        },
    },
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
        contacts: {
            executor: 'constant-vus',
            vus: 10,
            duration: '30s'
        },
    },
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [15]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php')
```
- **Refactored:**
```js
import { check } from 'k6';
...
const res = http.get('https://test.k6.io/contacts.php');
check(res, {
    'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [15]
- **Snippet:**
```js
http.get('https://test.k6.io/contacts.php')
```
- **Refactored:**
```js
http.get('https://test.k6.io/contacts.php', {
    tags: { name: 'Contacts' },
});
```

### `script_78.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 20,
  duration: '60s',
}
```
- **Refactored:**
```js
export const options = {
  vus: 20,
  duration: '60s',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
}
```

**Smell 3: Not checking requests**

- **Lines:** [14]
- **Snippet:**
```js
http.get('https://test.k6.io')
```
- **Refactored:**
```js
import { check } from 'k6';

// inside default function:
const res = http.get('https://test.k6.io');
check(res, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [14]
- **Snippet:**
```js
http.get('https://test.k6.io')
```
- **Refactored:**
```js
http.get('https://test.k6.io', {
  tags: { name: 'homepage', endpoint: 'test.k6.io' },
});
```

### `script_78.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 20,
  duration: '60s',
}
```
- **Refactored:**
```js
export const options = {
  vus: 20,
  duration: '60s',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [14]
- **Snippet:**
```js
http.get('https://test.k6.io')
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default function () {
  const res = http.get('https://test.k6.io');
  check(res, {
    'GET / status is 200': (r) => r.status === 200,
  });
  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [14]
- **Snippet:**
```js
http.get('https://test.k6.io')
```
- **Refactored:**
```js
export default function () {
  const res = http.get('https://test.k6.io', {
    tags: { endpoint: 'home', flow: 'landing' },
  });
  sleep(1);
}
```

### `script_78.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 20,
  duration: '60s',
}
```
- **Refactored:**
```js
export const options = {
  vus: 20,
  duration: '60s',
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<200'], // 95% of requests must complete below 200ms
  },
}
```

**Smell 3: Not checking requests**

- **Lines:** [14]
- **Snippet:**
```js
http.get('https://test.k6.io')
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const res = http.get('https://test.k6.io');
check(res, { 'status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [14]
- **Snippet:**
```js
http.get('https://test.k6.io')
```
- **Refactored:**
```js
http.get('https://test.k6.io', {
  tags: { name: 'Homepage' },
});
```

### `script_80.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [10, 11, 12, 13, 14, 15, 16]
- **Snippet:**
```js
export const options = {
    stages: [
        { duration: "4m", target: 400 },
        { duration: "3h56m", target: 400 },
        { duration: "4m", target: 0 },
    ]
};
```
- **Refactored:**
```js
export const options = {
    stages: [
        { duration: "4m", target: 400 },
        { duration: "3h56m", target: 400 },
        { duration: "4m", target: 0 },
    ],
    thresholds: {
        'http_req_duration': ['p(95)<500'],
        'success_rate': ['rate>0.95'],
        'http_req_failed': ['rate<0.05'],
    }
};
```

**Smell 3: Not checking requests**

- **Lines:** [20, 29, 30, 31, 32, 33]
- **Snippet:**
```js
const response = http.get('http://test.k6.io');

    if (response.status === 200) {
        successRate.add(true);
    } else {
        successRate.add(false);
    }
```
- **Refactored:**
```js
import { check } from 'k6';

// inside default function:
const response = http.get('http://test.k6.io');

const success = check(response, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
});

requestCounter.add(1);
requestTrend.add(response.timings.duration);
successRate.add(success);
```

**Smell 4: Not using tags**

- **Lines:** [20]
- **Snippet:**
```js
const response = http.get('http://test.k6.io');
```
- **Refactored:**
```js
const response = http.get('http://test.k6.io', {
    tags: {
        name: 'homepage',
        endpoint: 'GET /'
    }
});
```

### `script_80.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [10, 11, 12, 13, 14, 15, 16]
- **Snippet:**
```js
export const options = {
    stages: [
        { duration: "4m", target: 400 },
        { duration: "3h56m", target: 400 },
        { duration: "4m", target: 0 },
    ]
};
```
- **Refactored:**
```js
export const options = {
    stages: [
        { duration: "4m", target: 400 },
        { duration: "3h56m", target: 400 },
        { duration: "4m", target: 0 },
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
        checks: ['rate>0.99'],
        success_rate: ['rate>0.99']
    }
};
```

**Smell 3: Not checking requests**

- **Lines:** [20, 29, 30, 31, 32, 33]
- **Snippet:**
```js
const response = http.get('http://test.k6.io');

if (response.status === 200) {
    successRate.add(true);
} else {
    successRate.add(false);
}
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default function () {
    const response = http.get('http://test.k6.io');

    const ok = check(response, {
        'GET / returns 200': (r) => r.status === 200,
        'GET / response body is not empty': (r) => r.body && r.body.length > 0
    });

    successRate.add(ok);
    sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [20, 23, 26, 30, 32]
- **Snippet:**
```js
const response = http.get('http://test.k6.io');
requestCounter.add(1);
requestTrend.add(response.timings.duration);
successRate.add(true);
```
- **Refactored:**
```js
export default function () {
    const tags = { endpoint: 'home', flow: 'smoke_test' };
    const response = http.get('http://test.k6.io', { tags });

    requestCounter.add(1, tags);
    requestTrend.add(response.timings.duration, tags);
    successRate.add(response.status === 200, tags);

    sleep(1);
}
```

### `script_80.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [10, 11, 12, 13, 14, 15, 16]
- **Snippet:**
```js
export const options = {
    stages: [
        { duration: "4m", target: 400 }, // ramp up to 400 users
        { duration: "3h56m", target: 400 }, // stay at 400 for ~4 hours
        { duration: "4m", target: 0 }, // scale down. (optional)
    ]
};
```
- **Refactored:**
```js
export const options = {
    stages: [
        { duration: "4m", target: 400 },
        { duration: "3h56m", target: 400 },
        { duration: "4m", target: 0 },
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    }
};
```

**Smell 3: Not checking requests**

- **Lines:** [29, 30, 31, 32, 33]
- **Snippet:**
```js
if (response.status === 200) {
    successRate.add(true);
} else {
    successRate.add(false);
}
```
- **Refactored:**
```js
import { check } from 'k6';
// ... inside the default function:
check(response, {
    'status is 200': (r) => r.status === 200,
});
// Note: The custom 'successRate' metric and its usage (lines 8, 29-33) can now be removed.
```

**Smell 4: Not using tags**

- **Lines:** [20]
- **Snippet:**
```js
const response = http.get('http://test.k6.io');
```
- **Refactored:**
```js
const response = http.get('http://test.k6.io', {
  tags: { name: 'Homepage' },
});
```

### `script_82.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [7, 8, 9]
- **Snippet:**
```js
export const options = {
    iterations: 10,
}
```
- **Refactored:**
```js
export const options = {
    iterations: 10,
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
    },
}
```

**Smell 3: Not checking requests**

- **Lines:** [12]
- **Snippet:**
```js
http.get('https://test-api.k6.io')
```
- **Refactored:**
```js
import { check } from 'k6';

const res = http.get('https://test-api.k6.io');
check(res, {
    'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
http.get('https://test-api.k6.io')
```
- **Refactored:**
```js
http.get('https://test-api.k6.io', { tags: { name: 'homepage', endpoint: 'root' } });
```

### `script_82.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [7, 8, 9]
- **Snippet:**
```js
export const options = {
    iterations: 10,
}
```
- **Refactored:**
```js
export const options = {
    iterations: 10,
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
    },
}
```

**Smell 3: Not checking requests**

- **Lines:** [12]
- **Snippet:**
```js
http.get('https://test-api.k6.io')
```
- **Refactored:**
```js
import { sleep, check } from 'k6'

export default function () {
    const res = http.get('https://test-api.k6.io')
    check(res, {
        'status is 200': (r) => r.status === 200,
    })
    sleep(1)
}
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
http.get('https://test-api.k6.io')
```
- **Refactored:**
```js
export default function () {
    const res = http.get('https://test-api.k6.io', {
        tags: {
            endpoint: 'home',
            flow: 'main',
        },
    })
    sleep(1)
}
```

### `script_82.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [7, 8, 9]
- **Snippet:**
```js
export const options = {
    iterations: 10,
}
```
- **Refactored:**
```js
export const options = {
    iterations: 10,
    thresholds: {
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
    },
}
```

**Smell 3: Not checking requests**

- **Lines:** [12]
- **Snippet:**
```js
http.get('https://test-api.k6.io')
```
- **Refactored:**
```js
// Add 'check' to imports: import { check } from 'k6'
const res = http.get('https://test-api.k6.io');
check(res, { 'status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
http.get('https://test-api.k6.io')
```
- **Refactored:**
```js
http.get('https://test-api.k6.io', {
  tags: { name: 'TestAPIHomepage' },
});
```

### `script_83.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
vus: 1,
duration: '1s',
};
```
- **Refactored:**
```js
export const options = {
  vus: 1,
  duration: '1s',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [24]
- **Snippet:**
```js
const response = http.get(endpoint, {headers: headers});
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const response = http.get(endpoint, { headers: headers });
check(response, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [24]
- **Snippet:**
```js
const response = http.get(endpoint, {headers: headers});
```
- **Refactored:**
```js
const response = http.get(endpoint, {
  headers: headers,
  tags: { name: 'get_test_table', endpoint: '/rest/v1/test' },
});
```

### `script_83.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
vus: 1,
duration: '1s',
};
```
- **Refactored:**
```js
export const options = {
  vus: 1,
  duration: '1s',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [24]
- **Snippet:**
```js
const response = http.get(endpoint, {headers:  headers});
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

const response = http.get(endpoint, { headers: headers });
check(response, {
  'GET /rest/v1/test returned 200': (r) => r.status === 200,
  'GET /rest/v1/test returned body': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [24]
- **Snippet:**
```js
const response = http.get(endpoint, {headers:  headers});
```
- **Refactored:**
```js
const response = http.get(endpoint, {
  headers: headers,
  tags: {
    endpoint: 'test_select',
    method: 'GET',
    flow: 'read_test_records',
  },
});
```

### `script_83.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
vus: 1,
duration: '1s',
};
```
- **Refactored:**
```js
export const options = {
  vus: 1,
  duration: '1s',
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should complete below 500ms
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [24, 25, 26]
- **Snippet:**
```js
const response = http.get(endpoint, {headers:  headers});

    console.log(response)
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const response = http.get(endpoint, {headers:  headers});
check(response, {
    'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [24]
- **Snippet:**
```js
const response = http.get(endpoint, {headers:  headers});
```
- **Refactored:**
```js
const response = http.get(endpoint, {
    headers:  headers,
    tags: {
        name: 'GetTestData',
    },
});
```

### `script_85.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
- **Snippet:**
```js
const allUsers = open('/home/vunet/user_creation_k6/user_cookies_module.txt')
  .split('\n')
  .map(line => { ... })
  .filter(user => user.accessToken && user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

const allUsers = new SharedArray('users', function () {
  return open('/home/vunet/user_creation_k6/user_cookies_module.txt')
    .split('\n')
    .map(line => {
      const [username, password, accessToken, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
      return {
        username,
        password,
        accessToken,
        vunetSession,
        xVuNetHTTPInfo,
        grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10),
        dashboardName: 'Linux%20-%20CPU%20Utilization'
      };
    })
    .filter(user => user.accessToken && user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
});
```

**Smell 2: Do not use thresholds**

- **Lines:** [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]
- **Snippet:**
```js
export let options = {
  vus: selectedUsers.length,
  iterations: CONFIG.iterationsPerUser * selectedUsers.length,
  tags: { ... }
};
```
- **Refactored:**
```js
export let options = {
  vus: selectedUsers.length,
  iterations: CONFIG.iterationsPerUser * selectedUsers.length,
  tags: {
    test_type: 'alert_execution',
    timeFrom: CONFIG.timeRange.from,
    timeTo: CONFIG.timeRange.to,
    userCount: CONFIG.userCount.toString(),
    iterationsPerUser: CONFIG.iterationsPerUser.toString()
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<2000'],
    checks: ['rate>0.99'],
    alert_execution_success_rate: ['rate>0.99'],
    alert_execution_response_time: ['p(95)<2000']
  }
};
```

### `script_85.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
- **Snippet:**
```js
const allUsers = open('/home/vunet/user_creation_k6/user_cookies_module.txt')
  .split('\n')
  .map(line => {
    const [username, password, accessToken, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    return {
      username,
      password,
      accessToken,
      vunetSession,
      xVuNetHTTPInfo,
      grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10),
      dashboardName: "Linux%20-%20CPU%20Utilization"
    };
  })
  .filter(user => user.accessToken && user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
```
- **Refactored:**
```js
export function setup() {
  const allUsers = open('/home/vunet/user_creation_k6/user_cookies_module.txt')
    .split('\n')
    .map(line => {
      const [username, password, accessToken, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
      return {
        username,
        password,
        accessToken,
        vunetSession,
        xVuNetHTTPInfo,
        grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10),
        dashboardName: "Linux%20-%20CPU%20Utilization"
      };
    })
    .filter(user => user.accessToken && user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);

  const selectedUsers = allUsers.slice(0, CONFIG.userCount);
  
  if (selectedUsers.length < CONFIG.userCount) {
    throw new Error(`Requested ${CONFIG.userCount} users but only found ${selectedUsers.length} valid users!`);
  }
  
  return { users: selectedUsers };
}

export default function (data) { // data is received from setup()
  const userIndex = (__VU - 1) % data.users.length;
  const user = data.users[userIndex];
  // ... rest of the VU code
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]
- **Snippet:**
```js
export let options = {
  vus: selectedUsers.length,                          // Dynamic VU count
  iterations: CONFIG.iterationsPerUser * selectedUsers.length, // Total iterations
  tags: {
    test_type: 'alert_execution',
    timeFrom: CONFIG.timeRange.from,
    timeTo: CONFIG.timeRange.to,
    userCount: CONFIG.userCount.toString(),
    iterationsPerUser: CONFIG.iterationsPerUser.toString()
  }
};
```
- **Refactored:**
```js
export let options = {
  vus: selectedUsers.length,                          
  iterations: CONFIG.iterationsPerUser * selectedUsers.length, 
  tags: {
    test_type: 'alert_execution',
    timeFrom: CONFIG.timeRange.from,
    timeTo: CONFIG.timeRange.to,
    userCount: CONFIG.userCount.toString(),
    iterationsPerUser: CONFIG.iterationsPerUser.toString()
  },
  thresholds: {
    // 99% of requests must succeed
    'checks{is status 200:true}': ['rate>0.99'], 
    // 95th percentile of response time must be below 2 seconds
    'alert_execution_response_time': ['p(95)<2000'],
    // Custom success rate metric must be above 99%
    'alert_execution_success_rate': ['rate>0.99']
  }
};
```

### `script_89.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [9, 10, 11]
- **Snippet:**
```js
export const options = {
  iterations: 5,
};
```
- **Refactored:**
```js
export const options = {
  iterations: 5,
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
import { check } from 'k6';

// Inside default function:
const res = http.get('https://quickpizza.grafana.com');
check(res, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
http.get('https://quickpizza.grafana.com', {
  tags: { name: 'QuickPizzaHome', endpoint: '/' },
});
```

### `script_89.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [9, 10, 11]
- **Snippet:**
```js
export const options = {
  iterations: 5,
};
```
- **Refactored:**
```js
export const options = {
  iterations: 5,
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default function () {
  const res = http.get('https://quickpizza.grafana.com');

  check(res, {
    'status is 200': (r) => r.status === 200,
  });

  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
export default function () {
  const res = http.get('https://quickpizza.grafana.com', {
    tags: {
      endpoint: 'home',
      flow: 'browse_pizza',
    },
  });

  sleep(1);
}
```

### `script_89.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [9, 10, 11]
- **Snippet:**
```js
export const options = {
  iterations: 5,
};
```
- **Refactored:**
```js
export const options = {
  iterations: 5,
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
import { check } from 'k6';
// ... in the default function ...
const res = http.get('https://quickpizza.grafana.com');
check(res, { 'status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [16]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
http.get('https://quickpizza.grafana.com', {
  tags: { name: 'Homepage' },
});
```

### `script_90.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
    vus: 10,
    duration: '10s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 10,
    duration: '10s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500']
    }
}
```

**Smell 3: Not checking requests**

- **Lines:** [10]
- **Snippet:**
```js
http.get('https://test.k6.io');
```
- **Refactored:**
```js
import { check } from 'k6';

const res = http.get('https://test.k6.io');
check(res, {
    'status is 200': (r) => r.status === 200
});
```

**Smell 4: Not using tags**

- **Lines:** [10]
- **Snippet:**
```js
http.get('https://test.k6.io');
```
- **Refactored:**
```js
http.get('https://test.k6.io', { tags: { name: 'homepage', endpoint: 'test.k6.io' } });
```

### `script_90.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
    vus: 10,
    duration: '10s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 10,
    duration: '10s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500']
    }
};
```

**Smell 3: Not checking requests**

- **Lines:** [10]
- **Snippet:**
```js
http.get('https://test.k6.io');
```
- **Refactored:**
```js
import { check, sleep } from 'k6';

export default function () {
    const res = http.get('https://test.k6.io');
    check(res, {
        'status is 200': (r) => r.status === 200
    });
    sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [10]
- **Snippet:**
```js
http.get('https://test.k6.io');
```
- **Refactored:**
```js
export default function () {
    const res = http.get('https://test.k6.io', {
        tags: {
            endpoint: 'home',
            flow: 'homepage'
        }
    });
    sleep(1);
}
```

### `script_90.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
    vus: 10,
    duration: '10s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 10,
    duration: '10s',
    thresholds: {
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [10]
- **Snippet:**
```js
http.get('https://test.k6.io');
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const res = http.get('https://test.k6.io');
check(res, {
    'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [10]
- **Snippet:**
```js
http.get('https://test.k6.io');
```
- **Refactored:**
```js
http.get('https://test.k6.io', {
    tags: { name: 'PublicMainPage' },
});
```

### `script_92.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [45, 63, 87, 104, 131, 150, 167, 230]
- **Snippet:**
```js
const res_login = http.post(url, login, params);
...
const res_abvenda = http.post(abrirVenda, ab_venda, params);
...
let res_pgentidade = http.get(`${pesquisaGeralEntidade}?${searchParams.toString()}`, params);
```
- **Refactored:**
```js
const params_login = {
  headers: { 'Content-Type': 'application/json' },
  Timeout: '600s',
  tags: { name: 'login', endpoint: '/Home/Login' }
};
const res_login = http.post(url, login, params_login);

const params_abvenda = {
  headers: { 'Content-Type': 'application/json' },
  Timeout: '600s',
  tags: { name: 'abrir-venda', endpoint: '/operacoes/faturamento/api/abrir-venda' }
};
const res_abvenda = http.post(abrirVenda, ab_venda, params_abvenda);

const params_pgentidade = {
  headers: { 'Content-Type': 'application/json' },
  Timeout: '600s',
  tags: { name: 'pesquisa-geral-entidade', endpoint: '/operacoes/faturamento/api/pesquisa-geral' }
};
let res_pgentidade = http.get(`${pesquisaGeralEntidade}?${searchParams.toString()}`, params_pgentidade);

// Apply similarly to all other requests:
// definir-entidade, lancar-rapido, pag-dinheiro, get-dados-emissao-doc-fiscal, gerar-nota-fiscal
```

### `script_92.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [38, 39, 40, 41, 42, 43, 45, 63, 87, 104, 131, 150, 167, 230]
- **Snippet:**
```js
const params = {
  headers: {
    'Content-Type': 'application/json',
  },
  'Timeout': '600s'
};

const res_login = http.post(url, login, params);
const res_abvenda = http.post(abrirVenda, ab_venda, params);
let res_pgentidade = http.get(`${pesquisaGeralEntidade}?${searchParams.toString()}`, params);
```
- **Refactored:**
```js
const baseParams = {
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: '600s',
};

const taggedParams = (endpoint, flow = 'faturamento') => ({
  ...baseParams,
  tags: {
    endpoint,
    flow,
  },
});

const res_login = http.post(url, login, taggedParams('login', 'auth'));
const res_abvenda = http.post(abrirVenda, ab_venda, taggedParams('abrir-venda'));
let res_pgentidade = http.get(`${pesquisaGeralEntidade}?${searchParams.toString()}`, taggedParams('pesquisa-geral'));
const res_dentidade = http.post(definirEntidade, d_entidade, taggedParams('definir-entidade'));
const res_lrapido = http.post(lancarRapido, l_rapido, taggedParams('lancar-rapido'));
const res_pagdinheiro = http.post(pagDinheiro, pag_dinheiro, taggedParams('pagamento-dinheiro'));
let res_gdemissaoDocFiscal = http.get(`${getDadosEmissaoDocFiscal}?${gd_emissaoDocFiscal.toString()}`, taggedParams('dados-emissao-documento-fiscal'));
const res_gnotaFiscal = http.post(gerarNotaFiscal, g_notaFiscal, taggedParams('gerar-nota-fiscal'));

check(res_login, {
  'login status should be 200': (r) => r.status === 200,
}, { endpoint: 'login', flow: 'auth' });
```

### `script_92.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [45, 63, 87, 104, 131, 150, 167, 230]
- **Snippet:**
```js
const res_login = http.post(url, login, params);
```
- **Refactored:**
```js
const res_login = http.post(url, login, {
  ...params,
  tags: {
    name: 'Login',
  },
});

// Apply the same pattern to subsequent requests:
const res_abvenda = http.post(abrirVenda, ab_venda, {
  ...params,
  tags: {
    name: 'AbrirVenda',
  },
});
```

### `script_93.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5]
- **Snippet:**
```js
import http from 'k6/http';
import { check } from 'k6';

const URL= 'http://localhost:8000';
export default function () {
```
- **Refactored:**
```js
import http from 'k6/http';
import { check } from 'k6';

const URL = 'http://localhost:8000';

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99']
  }
};

export default function () {
```

**Smell 3: Not checking requests**

- **Lines:** [12, 22, 40, 49, 81, 98, 113]
- **Snippet:**
```js
http.post(`${URL}/user/register/`, ...);
// no check on register response

let res = http.post(`${URL}/auth/token/login/`, ...);
// no check on login response

http.get(`${URL}/my/crocodiles/`, ...);
// no check

res = http.post(`${URL}/my/crocodiles/`, ...);
// no check

res = http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, ...);
// no check

res = http.patch(`${URL}o/my/crocodiles/${newCrocodileId}/`, ...);
// no check

res = http.del(`${URL}/my/crocodiles/${newCrocodileId}/`, ...);
// no check
```
- **Refactored:**
```js
let res = http.post(`${URL}/user/register/`, JSON.stringify(credentials), { headers: { 'Content-Type': 'application/json' } });
check(res, { 'register status is 201': (r) => r.status === 201 });

res = http.post(`${URL}/auth/token/login/`, JSON.stringify({ username: credentials.username, password: credentials.password }), { headers: { 'Content-Type': 'application/json' } });
check(res, { 'login status is 200': (r) => r.status === 200, 'has access token': (r) => r.json().access !== undefined });

res = http.get(`${URL}/my/crocodiles/`, { headers: { Authorization: 'Bearer ' + accessToken } });
check(res, { 'list crocs status is 200': (r) => r.status === 200 });

res = http.post(`${URL}/my/crocodiles/`, JSON.stringify({ name: 'Random croc', sex: 'M', date_of_birth: '1900-10-28' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' } });
check(res, { 'create croc status is 201': (r) => r.status === 201, 'create croc has id': (r) => r.json().id !== undefined });

res = http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ name: 'Updated Random croc', sex: 'M', date_of_birth: '1900-10-28' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' } });
check(res, { 'update croc status is 200': (r) => r.status === 200 });

res = http.patch(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ sex: 'F' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' } });
check(res, { 'patch croc status is 200': (r) => r.status === 200 });

res = http.del(`${URL}/my/crocodiles/${newCrocodileId}/`, null, { headers: { Authorization: 'Bearer ' + accessToken } });
check(res, { 'delete croc status is 204': (r) => r.status === 204 });
```

**Smell 4: Not using tags**

- **Lines:** [12, 22, 40, 49, 67, 81, 98, 113]
- **Snippet:**
```js
http.post(`${URL}/user/register/`, JSON.stringify(credentials), { headers: { 'Content-Type': 'application/json' } });

http.post(`${URL}/auth/token/login/`, ...);

http.get(`${URL}/my/crocodiles/`, ...);

http.post(`${URL}/my/crocodiles/`, ...);

http.get(`${URL}/my/crocodiles/${newCrocodileId}/`, ...);

http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, ...);

http.patch(`${URL}o/my/crocodiles/${newCrocodileId}/`, ...);

http.del(`${URL}/my/crocodiles/${newCrocodileId}/`, ...);
```
- **Refactored:**
```js
http.post(`${URL}/user/register/`, JSON.stringify(credentials), { headers: { 'Content-Type': 'application/json' }, tags: { name: 'register' } });

http.post(`${URL}/auth/token/login/`, JSON.stringify({ username: credentials.username, password: credentials.password }), { headers: { 'Content-Type': 'application/json' }, tags: { name: 'login' } });

http.get(`${URL}/my/crocodiles/`, { headers: { Authorization: 'Bearer ' + accessToken }, tags: { name: 'list_crocodiles' } });

http.post(`${URL}/my/crocodiles/`, JSON.stringify({ name: 'Random croc', sex: 'M', date_of_birth: '1900-10-28' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' }, tags: { name: 'create_crocodile' } });

http.get(`${URL}/my/crocodiles/${newCrocodileId}/`, { headers: { Authorization: 'Bearer ' + accessToken }, tags: { name: 'get_crocodile' } });

http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ name: 'Updated Random croc', sex: 'M', date_of_birth: '1900-10-28' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' }, tags: { name: 'update_crocodile' } });

http.patch(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ sex: 'F' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' }, tags: { name: 'patch_crocodile' } });

http.del(`${URL}/my/crocodiles/${newCrocodileId}/`, null, { headers: { Authorization: 'Bearer ' + accessToken }, tags: { name: 'delete_crocodile' } });
```

### `script_93.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 123]
- **Snippet:**
```js
The script does not define an `options` object with a `thresholds` configuration. Without performance goals, the test will always pass in a CI/CD pipeline, even if the system's response times or error rates are unacceptably high.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
    'checks': ['rate>0.99'], // 99% of checks should pass
  },
};

```

**Smell 3: Not checking requests**

- **Lines:** [12, 22, 40, 49, 81, 98, 113]
- **Snippet:**
```js
http.post(
    `${URL}/user/register/`,
    JSON.stringify(credentials),
    {
        headers: {
            'Content-Type': 'application/json'
        }
    }
);
```
- **Refactored:**
```js
const registerRes = http.post(
    `${URL}/user/register/`,
    JSON.stringify(credentials),
    {
        headers: {
            'Content-Type': 'application/json'
        }
    }
);

check(registerRes, {
    'User registration returns 201': (r) => r.status === 201,
});
```

**Smell 4: Not using tags**

- **Lines:** [12, 22, 40, 49, 67, 81, 98, 113]
- **Snippet:**
```js
http.post(
    `${URL}/auth/token/login/`,
    JSON.stringify(
        {
            username: credentials.username,
            password: credentials.password
        }
    ),
    {
        headers: {
            'Content-Type': 'application/json'
        }
    }
);
```
- **Refactored:**
```js
let res = http.post(
    `${URL}/auth/token/login/`,
    JSON.stringify(
        {
            username: credentials.username,
            password: credentials.password
        }
    ),
    {
        headers: {
            'Content-Type': 'application/json'
        },
        tags: {
            name: 'Login',
        },
    }
);
```

### `script_94.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112]
- **Snippet:**
```js
res = http.post(
    'https://test-api.k6.io/my/crocodiles/',
    JSON.stringify({ name: 'Random croc', sex: 'M', date_of_birth: '1900-10-28' }),
    { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' } }
);
const newCrocodileId = res.json().id;
```
- **Refactored:**
```js
res = http.post(
    'https://test-api.k6.io/my/crocodiles/',
    JSON.stringify({
        name: 'Random croc',
        sex: 'M',
        date_of_birth: '1900-10-28'
    }),
    {
        headers: {
            Authorization: 'Bearer ' + accessToken,
            'Content-Type': 'application/json'
        },
        tags: { endpoint: 'create_crocodile' }
    }
);

check(res, {
    'status is 201': (r) => r.status === 201,
    'created crocodile has id': (r) => r.json('id') !== undefined
});

const newCrocodileId = res.json('id');
```

**Smell 4: Not using tags**

- **Lines:** [39, 40, 41, 42, 43, 44, 45, 46, 47, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 80, 81, 82, 83, 84, 85, 86, 87, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 116, 117, 118, 119, 120, 121, 122, 123, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 178, 179, 180, 181, 182, 183, 184, 185, 186]
- **Snippet:**
```js
HTTP requests are made without tags, for example:
http.post('https://test-api.k6.io/user/register/', JSON.stringify(credentials), { headers: { 'Content-Type': 'application/json' } });
http.get('https://test-api.k6.io/my/crocodiles/', { headers: { Authorization: 'Bearer ' + accessToken } });
```
- **Refactored:**
```js
res = http.post(
    'https://test-api.k6.io/user/register/',
    JSON.stringify(credentials),
    {
        headers: { 'Content-Type': 'application/json' },
        tags: { endpoint: 'register_user', flow: 'crocodile_crud' }
    }
);

res = http.post(
    'https://test-api.k6.io/auth/token/login/',
    JSON.stringify({ username: credentials.username, password: credentials.password }),
    {
        headers: { 'Content-Type': 'application/json' },
        tags: { endpoint: 'login', flow: 'crocodile_crud' }
    }
);

res = http.get(
    'https://test-api.k6.io/my/crocodiles/',
    {
        headers: { Authorization: 'Bearer ' + accessToken },
        tags: { endpoint: 'list_crocodiles', flow: 'crocodile_crud' }
    }
);

res = http.post(
    'https://test-api.k6.io/my/crocodiles/',
    JSON.stringify({ name: 'Random croc', sex: 'M', date_of_birth: '1900-10-28' }),
    {
        headers: {
            Authorization: 'Bearer ' + accessToken,
            'Content-Type': 'application/json'
        },
        tags: { endpoint: 'create_crocodile', flow: 'crocodile_crud' }
    }
);

res = http.get(
    `https://test-api.k6.io/my/crocodiles/${newCrocodileId}/`,
    {
        headers: { Authorization: 'Bearer ' + accessToken },
        tags: { endpoint: 'get_crocodile', flow: 'crocodile_crud' }
    }
);

res = http.put(
    `https://test-api.k6.io/my/crocodiles/${newCrocodileId}/`,
    JSON.stringify({ name: 'Updated Random croc', sex: 'M', date_of_birth: '1900-10-28' }),
    {
        headers: {
            Authorization: 'Bearer ' + accessToken,
            'Content-Type': 'application/json'
        },
        tags: { endpoint: 'update_crocodile_put', flow: 'crocodile_crud' }
    }
);

res = http.patch(
    `https://test-api.k6.io/my/crocodiles/${newCrocodileId}/`,
    JSON.stringify({ sex: 'F' }),
    {
        headers: {
            Authorization: 'Bearer ' + accessToken,
            'Content-Type': 'application/json'
        },
        tags: { endpoint: 'update_crocodile_patch', flow: 'crocodile_crud' }
    }
);

res = http.del(
    `https://test-api.k6.io/my/crocodiles/${newCrocodileId}/`,
    null,
    {
        headers: { Authorization: 'Bearer ' + accessToken },
        tags: { endpoint: 'delete_crocodile', flow: 'crocodile_crud' }
    }
);
```

### `script_94.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111]
- **Snippet:**
```js
    res = http.post(
        'https://test-api.k6.io/my/crocodiles/',
        JSON.stringify(
            {
                name: 'Random croc',
                sex: 'M',
                date_of_birth: '1900-10-28'
            }
        ),
        {
            headers: {
                Authorization: 'Bearer ' + accessToken,
                'Content-Type': 'application/json'
            }
        }
    );
    const newCrocodileId = res.json().id;
```
- **Refactored:**
```js
    res = http.post(
        'https://test-api.k6.io/my/crocodiles/',
        JSON.stringify(
            {
                name: 'Random croc',
                sex: 'M',
                date_of_birth: '1900-10-28'
            }
        ),
        {
            headers: {
                Authorization: 'Bearer ' + accessToken,
                'Content-Type': 'application/json'
            }
        }
    );

    check(res, {
        'crocodile created successfully': (r) => r.status === 201,
    });
    
    const newCrocodileId = res.json().id;
```

**Smell 4: Not using tags**

- **Lines:** [39, 40, 41, 42, 43, 44, 45, 46, 47]
- **Snippet:**
```js
    let res = http.post(
        'https://test-api.k6.io/user/register/',
        JSON.stringify(credentials),
        {
            headers: {
                'Content-Type': 'application/json'
            }
        }
    );
```
- **Refactored:**
```js
    let res = http.post(
        'https://test-api.k6.io/user/register/',
        JSON.stringify(credentials),
        {
            headers: {
                'Content-Type': 'application/json'
            },
            tags: {
                name: 'RegisterUser',
            },
        }
    );
```

### `script_95.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [6]
- **Snippet:**
```js
export default function () {
    browser ();
}
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    browser_web_vital_lcp: ['p(75) < 2500'],
    browser_web_vital_fid: ['p(75) < 100'],
    checks: ['rate>=0.95'],
  },
};

export default function () {
    browser();
}
```

**Smell 4: Not using tags**

- **Lines:** [19, 28, 39, 40, 41, 47, 58, 70, 72, 76, 88, 99, 110, 111, 112, 116]
- **Snippet:**
```js
page.goto(domain);
...
element = page.$('//a[contains(.,"register")]');
element.click();
...
element = page.$('//a[contains(.,"Log in")]');
element.click();
```
- **Refactored:**
```js
page.goto(domain, { waitUntil: 'networkidle' });
// Tag page-level actions by setting tags on the browser context or using groups:
import { group } from 'k6';

group('01-Homepage', function () {
    page.goto(domain, { tags: { page: 'homepage' } });
    page.waitForLoadState('networkidle');
    // ...
});

group('02-Register', function () {
    let element = page.$('//a[contains(.,"register")]');
    element.click({ tags: { page: 'register' } });
    // ...
});

group('03-Login', function () {
    let element = page.$('//a[contains(.,"Log in")]');
    element.click({ tags: { page: 'login' } });
    // ...
});
```

### `script_95.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** []
- **Snippet:**
```js
No export const options with thresholds is defined in the script.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    checks: ['rate>=0.95']
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [22, 23, 24, 33, 34, 35, 51, 52, 53, 63, 64, 65, 82, 83, 84, 93, 94, 95, 104, 105, 106, 121, 122, 123]
- **Snippet:**
```js
check(page, {
  'browser-01a-Homepage': (p) => p.$('//p[@class="description"]').textContent().includes('Collection of HTTP and WebSocket APIs demonstrating the power of k6'),
});
```
- **Refactored:**
```js
check(page, {
  'browser-01a-Homepage': (p) => p.$('//p[@class="description"]').textContent().includes('Collection of HTTP and WebSocket APIs demonstrating the power of k6'),
}, { flow: 'homepage', page: 'home' });

check(page, {
  'browser-02a-Register page': (p) => p.$('//div[@class="response-info"]').textContent().includes('HTTP 405 Method Not Allowed'),
}, { flow: 'register', page: 'register' });

check(page, {
  'browser-02b-Register-submit': (p) => p.$('//div[@class="response-info"]').textContent().includes(accountUsername),
}, { flow: 'register', action: 'submit' });
```

### `script_95.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [6]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'checks': ['rate>0.99'], // e.g., 99% of checks must pass
    'browser_web_vital_lcp': ['p(95) < 2500'], // e.g., 95% of LCP measurements should be below 2.5s
  },
};

export default function () {
```

**Smell 4: Not using tags**

- **Lines:** [18, 27, 57, 87]
- **Snippet:**
```js
// 01-Homepage
page.goto(domain);
page.waitForLoadState('networkidle');
sleep(Math.random() * 5+3);
check(page, {
    'browser-01a-Homepage': (p) => p.$('//p[@class="description"]').textContent().includes("Collection of HTTP and WebSocket APIs demonstrating the power of k6"),
});
```
- **Refactored:**
```js
import { sleep, check, group } from 'k6';
// ... in the main function

group('01 - Homepage', function () {
  page.goto(domain);
  page.waitForLoadState('networkidle');
  sleep(Math.random() * 5+3);
  check(page, {
      'is homepage content correct': (p) => p.$('//p[@class="description"]').textContent().includes("Collection of HTTP and WebSocket APIs demonstrating the power of k6"),
  });
  page.screenshot({ path: `screenshots/01a-homepage.png` });
});

// Subsequent user actions should also be wrapped in group() blocks.
```

### `script_96.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6]
- **Snippet:**
```js
export default function () { ... }
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99']
  }
};
```

**Smell 3: Not checking requests**

- **Lines:** [13, 21, 23, 36, 41, 48, 50, 65, 82, 97, 99, 112]
- **Snippet:**
```js
http.post(`${URL}/user/register/`, ...);
http.post(`${URL}/auth/token/login/`, ...);
http.get(`${URL}/my/crocodiles/`, ...);
http.post(`${URL}/my/crocodiles/`, ...);
http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, ...);
http.patch(`${URL}/my/crocodiles/${newCrocodileId}/`, ...);
```
- **Refactored:**
```js
let res = http.post(`${URL}/user/register/`, JSON.stringify(credentials), { headers: { 'Content-Type': 'application/json' } });
check(res, { 'register status is 201': (r) => r.status === 201 });

res = http.post(`${URL}/auth/token/login/`, JSON.stringify({ username: credentials.username, password: credentials.password }), { headers: { 'Content-Type': 'application/json' } });
check(res, { 'login status is 200': (r) => r.status === 200, 'has access token': (r) => r.json().access !== undefined });

const accessToken = res.json().access;

res = http.get(`${URL}/my/crocodiles/`, { headers: { Authorization: 'Bearer ' + accessToken } });
check(res, { 'get crocodiles status is 200': (r) => r.status === 200 });

res = http.post(`${URL}/my/crocodiles/`, JSON.stringify({ name: 'Random croc', sex: 'M', date_of_birth: '1900-10-28' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' } });
check(res, { 'create crocodile status is 201': (r) => r.status === 201, 'has crocodile id': (r) => r.json().id !== undefined });

const newCrocodileId = res.json().id;

res = http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ name: 'Updated Random croc', sex: 'M', date_of_birth: '1900-10-28' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' } });
check(res, { 'update crocodile status is 200': (r) => r.status === 200 });

res = http.patch(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ sex: 'F' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' } });
check(res, { 'patch crocodile status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [13, 23, 41, 50, 68, 82, 99]
- **Snippet:**
```js
http.post(`${URL}/user/register/`, ...);
http.post(`${URL}/auth/token/login/`, ...);
http.get(`${URL}/my/crocodiles/`, ...);
http.post(`${URL}/my/crocodiles/`, ...);
http.get(`${URL}/my/crocodiles/${newCrocodileId}/`, ...);
http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, ...);
http.patch(`${URL}/my/crocodiles/${newCrocodileId}/`, ...);
```
- **Refactored:**
```js
http.post(`${URL}/user/register/`, JSON.stringify(credentials), { headers: { 'Content-Type': 'application/json' }, tags: { name: 'register' } });

http.post(`${URL}/auth/token/login/`, JSON.stringify({ username: credentials.username, password: credentials.password }), { headers: { 'Content-Type': 'application/json' }, tags: { name: 'login' } });

http.get(`${URL}/my/crocodiles/`, { headers: { Authorization: 'Bearer ' + accessToken }, tags: { name: 'list_crocodiles' } });

http.post(`${URL}/my/crocodiles/`, JSON.stringify({ name: 'Random croc', sex: 'M', date_of_birth: '1900-10-28' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' }, tags: { name: 'create_crocodile' } });

http.get(`${URL}/my/crocodiles/${newCrocodileId}/`, { headers: { Authorization: 'Bearer ' + accessToken }, tags: { name: 'get_crocodile' } });

http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ name: 'Updated Random croc', sex: 'M', date_of_birth: '1900-10-28' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' }, tags: { name: 'update_crocodile' } });

http.patch(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ sex: 'F' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' }, tags: { name: 'patch_crocodile' } });
```

### `script_96.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 6]
- **Snippet:**
```js
The script does not define an `options` object with a `thresholds` property, which is crucial for setting pass/fail criteria.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests must complete below 500ms
  },
};

export default function () { ... }
```

**Smell 3: Not checking requests**

- **Lines:** [13, 21]
- **Snippet:**
```js
http.post(
    `${URL}/user/register/`,
    JSON.stringify(credentials),
    {
        headers: {
            'Content-Type': 'application/json'
        }
    }
);
```
- **Refactored:**
```js
const registerRes = http.post(
    `${URL}/user/register/`,
    JSON.stringify(credentials),
    {
        headers: {
            'Content-Type': 'application/json'
        }
    }
);

check(registerRes, {
    'user registration status is 201': (r) => r.status === 201,
});
```

**Smell 4: Not using tags**

- **Lines:** [13, 21]
- **Snippet:**
```js
http.post(
    `${URL}/user/register/`,
    JSON.stringify(credentials),
    {
        headers: {
            'Content-Type': 'application/json'
        }
    }
);
```
- **Refactored:**
```js
http.post(
    `${URL}/user/register/`,
    JSON.stringify(credentials),
    {
        headers: {
            'Content-Type': 'application/json'
        },
        tags: {
            name: 'RegisterUser'
        }
    }
);
```

### `script_97.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 199]
- **Snippet:**
```js
export default function () {
	orders();
}
```
- **Refactored:**
```js
export const options = {
	thresholds: {
		http_req_failed: ['rate<0.01'],
		http_req_duration: ['p(95)<2000'],
		'checks': ['rate>0.99'],
	},
};

export default function () {
	orders();
}
```

### `script_97.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [197, 198, 199]
- **Snippet:**
```js
export default function () {
	orders();
}
```
- **Refactored:**
```js
export const options = {
	thresholds: {
		http_req_failed: ['rate<0.01'],
		http_req_duration: ['p(95)<500'],
		checks: ['rate>0.99'],
	},
};

export default function () {
	orders();
}
```

### `script_97.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [35]
- **Snippet:**
```js
// The script lacks an `options` object with a `thresholds` property to define pass/fail criteria.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    // Fail the test if more than 1% of requests return an error.
    'http_req_failed': ['rate<0.01'],
    // 95% of all requests must complete within 800ms.
    'http_req_duration': ['p(95)<800'],
    // 95% of requests tagged with 'Merchant - All Orders' must complete within 1000ms.
    'http_req_duration{name:Merchant - All Orders}': ['p(95)<1000'],
  },
};

export function orders( includeTests = {} ) {
```

### `script_98.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [203, 204, 205]
- **Snippet:**
```js
export default function () {
	homeWCAdmin();
}
```
- **Refactored:**
```js
export const options = {
	thresholds: {
		http_req_failed: ['rate<0.01'],
		http_req_duration: ['p(95)<2000'],
		'checks': ['rate>0.99'],
	},
};

export default function () {
	homeWCAdmin();
}
```

### `script_98.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [203, 204, 205]
- **Snippet:**
```js
export default function () {
	homeWCAdmin();
}
```
- **Refactored:**
```js
export const options = {
	thresholds: {
		http_req_failed: ['rate<0.01'],
		http_req_duration: ['p(95)<1000'],
		checks: ['rate>0.99'],
	},
};

export default function () {
	homeWCAdmin();
}
```

### `script_98.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [25]
- **Snippet:**
```js
export function homeWCAdmin( includeTests = {} ) {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
    checks: ['rate>0.99'], // 99% of checks should pass
  },
};

export function homeWCAdmin( includeTests = {} ) {
```

### `script_99.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [502, 503, 504]
- **Snippet:**
```js
export default function () {
	addOrder();
}
```
- **Refactored:**
```js
export const options = {
	thresholds: {
		http_req_failed: ['rate<0.01'],
		http_req_duration: ['p(95)<2000'],
		'checks': ['rate>0.99'],
	},
};

export default function () {
	addOrder();
}
```

### `script_99.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [502, 503, 504]
- **Snippet:**
```js
export default function () {
	addOrder();
}
```
- **Refactored:**
```js
export const options = {
	thresholds: {
		http_req_failed: ['rate<0.01'],
		http_req_duration: ['p(95)<1000'],
		checks: ['rate>0.99'],
	},
};

export default function () {
	addOrder();
}
```

### `script_99.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 504]
- **Snippet:**
```js
The script does not export an `options` object with a `thresholds` configuration, which is necessary to define pass/fail criteria for the test.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    // 99% of requests must complete within 2000ms.
    'http_req_duration': ['p(99)<2000'],
    // All checks must pass.
    'checks': ['rate==1.0'],
    // All HTTP requests should succeed (no 4xx or 5xx responses).
    'http_req_failed': ['rate==0'],
  },
};

/* eslint-disable import/no-unresolved */
/**
 * External dependencies
 */
import { sleep, check, group } from 'k6';
```
