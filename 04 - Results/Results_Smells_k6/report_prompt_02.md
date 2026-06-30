# k6 Performance Smell Analysis

Total de scripts: 228

S1 = Costly init | S2 = No thresholds | S3 = No checks | S4 = No tags

| File | LLM | S1 | S2 | S3 | S4 | Lines with smells |
|------|-----|:--:|:--:|:--:|:--:|-------------------|
| `script_01.js` | claude | x | x | x | x | S1:L22, S1:L23, S2:L26, S2:L27, S2:L28, S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S3:L52, S3:L53, S3:L54, S3:L82, S3:L83, S3:L84, S4:L52, S4:L53, S4:L54, S4:L82, S4:L83, S4:L84 |
|  | chatgpt | x | x | x | x | S1:L22, S1:L23, S2:L26, S2:L27, S2:L28, S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S3:L52, S3:L53, S3:L54, S3:L82, S3:L83, S3:L84, S4:L52, S4:L53, S4:L54, S4:L82, S4:L83, S4:L84 |
|  | gemini | x | x | x | x | S1:L22, S1:L23, S2:L26, S2:L35, S3:L56, S3:L86, S4:L52, S4:L82 |
| `script_02.js` | claude |  | x |  |  | S2:L32, S2:L33, S2:L34, S2:L35, S2:L36, S2:L37, S2:L38, S2:L39, S2:L40, S2:L41, S2:L42, S2:L43, S2:L44, S2:L45, S2:L46, S2:L47, S2:L48, S2:L49, S2:L50, S2:L51, S2:L52, S2:L53, S2:L54, S2:L55 |
|  | chatgpt |  | x |  | x | S2:L32, S2:L33, S2:L34, S2:L35, S2:L36, S2:L37, S2:L38, S2:L39, S2:L40, S2:L41, S2:L42, S2:L43, S2:L44, S2:L45, S2:L46, S2:L47, S2:L48, S2:L49, S2:L50, S2:L51, S2:L52, S2:L53, S2:L54, S2:L55, S4:L183, S4:L193, S4:L205, S4:L228, S4:L238, S4:L250 |
|  | gemini |  | x |  | x | S2:L32, S2:L33, S2:L54, S4:L183, S4:L193, S4:L205, S4:L228, S4:L238, S4:L250 |
| `script_03.js` | claude |  | x |  | x | S2:L27, S2:L31, S4:L60, S4:L85, S4:L103, S4:L128 |
|  | chatgpt | x | x |  | x | S1:L38, S2:L27, S2:L31, S4:L60, S4:L61, S4:L62, S4:L63, S4:L64, S4:L65, S4:L66, S4:L67, S4:L68, S4:L69, S4:L70, S4:L71, S4:L72, S4:L73, S4:L85, S4:L86, S4:L87, S4:L103, S4:L104, S4:L105, S4:L106, S4:L107, S4:L108, S4:L109, S4:L110, S4:L111, S4:L112, S4:L128, S4:L129, S4:L130, S4:L131, S4:L132, S4:L133, S4:L134, S4:L135, S4:L136, S4:L137, S4:L138, S4:L139, S4:L140 |
|  | gemini | x | x |  | x | S1:L38, S2:L27, S2:L31, S4:L60, S4:L85, S4:L103, S4:L128 |
| `script_04.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S3:L22, S3:L24, S3:L26, S4:L22, S4:L24, S4:L26 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S3:L22, S3:L24, S3:L26, S4:L22, S4:L24, S4:L26 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S3:L22, S3:L24, S3:L26, S4:L22, S4:L24, S4:L26 |
| `script_05.js` | claude |  | x | x | x | S2:L7, S2:L8, S2:L9, S3:L29, S3:L31, S3:L33, S4:L29, S4:L31, S4:L33 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L26, S3:L29, S3:L31, S3:L33, S4:L29, S4:L31, S4:L33 |
|  | gemini |  | x | x | x | S2:L7, S2:L8, S2:L9, S3:L29, S3:L31, S3:L33, S4:L29, S4:L31, S4:L33 |
| `script_06.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L16, S3:L18, S3:L20, S4:L16, S4:L18, S4:L20 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L16, S3:L18, S3:L20, S4:L16, S4:L18, S4:L20 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L16, S3:L18, S3:L20, S4:L16, S4:L18, S4:L20 |
| `script_07.js` | claude | x | x | x | x | S1:L22, S2:L7, S2:L8, S2:L9, S2:L10, S3:L13, S3:L48, S4:L13, S4:L48 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x | x | x | S1:L22, S2:L7, S2:L8, S2:L9, S2:L10, S3:L48, S4:L48 |
| `script_08.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S3:L11, S4:L11 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x | x | x | S1:L4, S2:L3, S3:L11, S4:L11 |
| `script_09.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  | x | x | S3:L70, S3:L71, S3:L72, S3:L74, S3:L88, S3:L89, S3:L90, S3:L91, S3:L92, S4:L70, S4:L71, S4:L72, S4:L88, S4:L89, S4:L90, S4:L91, S4:L92 |
|  | gemini |  |  | x | x | S3:L74, S4:L70, S4:L71, S4:L72 |
| `script_10.js` | claude |  | x |  | x | S2:L16, S4:L29, S4:L92, S4:L132, S4:L178, S4:L217, S4:L260, S4:L328, S4:L401, S4:L501, S4:L567, S4:L633, S4:L700, S4:L766, S4:L832, S4:L898, S4:L967, S4:L1035, S4:L1108, S4:L1176, S4:L1244, S4:L1328, S4:L1389, S4:L1450, S4:L1512, S4:L1573, S4:L1634, S4:L1695, S4:L1759, S4:L1827, S4:L1900, S4:L1968, S4:L2027, S4:L2077, S4:L2128, S4:L2179, S4:L2231, S4:L2282, S4:L2333, S4:L2384, S4:L2438, S4:L2506, S4:L2574, S4:L2633, S4:L2683, S4:L2734, S4:L2785, S4:L2837, S4:L2888, S4:L2939, S4:L2990, S4:L3044, S4:L3112, S4:L3185, S4:L3245, S4:L3304, S4:L3354, S4:L3405, S4:L3456, S4:L3508, S4:L3559, S4:L3610, S4:L3661, S4:L3715, S4:L3775, S4:L3825, S4:L3878, S4:L3931, S4:L3985, S4:L4038, S4:L4091, S4:L4144, S4:L4200, S4:L4268, S4:L4350, S4:L4411, S4:L4472, S4:L4534, S4:L4595, S4:L4656, S4:L4717 |
|  | chatgpt |  | x |  |  | S2:L16 |
|  | gemini |  | x |  |  | S2:L16 |
| `script_11.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  | x | x | S3:L99, S3:L132, S3:L138, S3:L146, S3:L196, S3:L204, S3:L213, S3:L229, S3:L262, S3:L269, S3:L302, S3:L319, S3:L334, S3:L348, S3:L376, S3:L390, S3:L404, S3:L419, S4:L99, S4:L132, S4:L138, S4:L146, S4:L196, S4:L204, S4:L213, S4:L229, S4:L262, S4:L269, S4:L302, S4:L319, S4:L334, S4:L348, S4:L376, S4:L390, S4:L404, S4:L419 |
|  | gemini |  |  | x | x | S3:L132, S3:L134, S4:L132, S4:L138, S4:L146, S4:L162, S4:L196 |
| `script_12.js` | claude | x |  |  | x | S1:L21, S1:L22, S1:L23, S1:L24, S1:L27, S1:L28, S1:L29, S1:L30, S1:L31, S1:L32, S1:L33, S1:L34, S1:L36, S4:L43, S4:L50, S4:L64, S4:L72, S4:L110, S4:L122, S4:L134, S4:L141, S4:L148, S4:L158, S4:L170, S4:L176, S4:L195, S4:L210 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x |  |  | x | S1:L36, S4:L43, S4:L50, S4:L64, S4:L72, S4:L110, S4:L122, S4:L134, S4:L141, S4:L148, S4:L158, S4:L170, S4:L176, S4:L195, S4:L210 |
| `script_13.js` | claude |  | x |  | x | S2:L15, S2:L16, S2:L17, S4:L30, S4:L93, S4:L140, S4:L200, S4:L250, S4:L303, S4:L356, S4:L410, S4:L463, S4:L516, S4:L569 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L15, S2:L16, S2:L17 |
| `script_15.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L161, S3:L162, S3:L163, S3:L164, S3:L165, S3:L166, S3:L167, S3:L248, S3:L249, S3:L250, S3:L251, S3:L252, S3:L253, S3:L254, S3:L255, S3:L256, S3:L257, S4:L121, S4:L122, S4:L123, S4:L124 |
| `script_16.js` | claude | x | x |  |  | S1:L18, S2:L5, S2:L6, S2:L7, S2:L8 |
|  | chatgpt |  | x | x | x | S2:L5, S2:L6, S2:L7, S2:L8, S3:L35, S3:L36, S3:L37, S3:L38, S3:L39, S3:L40, S3:L41, S3:L43, S3:L44, S4:L25, S4:L26, S4:L27, S4:L28, S4:L29, S4:L30, S4:L31, S4:L35, S4:L36, S4:L37, S4:L38, S4:L39, S4:L40, S4:L41 |
|  | gemini |  | x |  |  | S2:L5, S2:L6, S2:L7, S2:L8 |
| `script_17.js` | claude |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L13, S4:L16, S4:L24, S4:L27, S4:L30, S4:L35 |
|  | chatgpt |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L13, S4:L16, S4:L24, S4:L27, S4:L30, S4:L35 |
|  | gemini |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L13, S4:L16, S4:L24, S4:L27, S4:L30, S4:L35 |
| `script_19.js` | claude | x |  | x |  | S1:L110, S1:L111, S1:L112, S1:L113, S1:L114, S1:L115, S1:L116, S3:L128, S3:L132, S3:L136, S3:L140, S3:L144 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x |  | x |  | S1:L110, S1:L112, S1:L120, S3:L128, S3:L132, S3:L136, S3:L140, S3:L144 |
| `script_20.js` | claude |  | x |  |  | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20 |
|  | chatgpt |  | x |  | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S4:L25, S4:L26, S4:L27, S4:L28, S4:L29, S4:L38, S4:L39, S4:L40, S4:L41, S4:L42, S4:L43, S4:L44, S4:L45, S4:L46, S4:L47, S4:L48, S4:L49, S4:L50, S4:L51, S4:L52, S4:L53, S4:L54, S4:L55, S4:L56 |
|  | gemini |  | x |  |  | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20 |
| `script_21.js` | claude |  |  |  |  | - |
|  | chatgpt |  | x | x | x | S2:L1, S3:L10, S4:L10, S4:L14, S4:L31, S4:L45 |
|  | gemini |  | x |  | x | S2:L1, S4:L10, S4:L14, S4:L31, S4:L45 |
| `script_22.js` | claude |  | x |  |  | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20 |
|  | chatgpt |  | x |  | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S4:L25, S4:L26, S4:L27, S4:L28, S4:L29, S4:L38, S4:L39, S4:L40, S4:L41, S4:L42, S4:L43, S4:L44, S4:L45, S4:L46, S4:L47, S4:L48, S4:L49, S4:L50, S4:L51, S4:L52, S4:L53, S4:L54, S4:L55, S4:L56, S4:L58 |
|  | gemini |  | x |  |  | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20 |
| `script_23.js` | claude | x | x |  | x | S1:L37, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L44 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L44 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L44 |
| `script_24.js` | claude |  | x | x | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S2:L21, S2:L22, S2:L23, S3:L76, S3:L77, S3:L84, S3:L85, S4:L60, S4:L61, S4:L62, S4:L76, S4:L77, S4:L84, S4:L85 |
|  | chatgpt |  | x | x | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S2:L21, S2:L22, S2:L23, S3:L76, S3:L77, S3:L84, S3:L85, S4:L60, S4:L61, S4:L62, S4:L76, S4:L77, S4:L84, S4:L85 |
|  | gemini |  | x | x | x | S2:L14, S2:L23, S3:L76, S3:L84, S4:L60, S4:L76, S4:L84 |
| `script_25.js` | claude |  |  |  |  | - |
|  | chatgpt |  | x |  | x | S2:L26, S2:L28, S2:L30, S4:L38, S4:L126, S4:L144, S4:L145, S4:L147, S4:L163 |
|  | gemini |  | x |  |  | S2:L26, S2:L30 |
| `script_26.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L1, S4:L1003, S4:L1031 |
| `script_27.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L42 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L32, S4:L33, S4:L34, S4:L35, S4:L36, S4:L42 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L42 |
| `script_28.js` | claude | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L81, S1:L82, S1:L83, S1:L84, S1:L85, S1:L86, S1:L87, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
| `script_29.js` | claude | x | x |  |  | S1:L11, S1:L12, S1:L13, S1:L14, S1:L15, S1:L16, S1:L17, S1:L18, S1:L19, S1:L20, S1:L21, S1:L23, S1:L24, S1:L25, S1:L26, S1:L51, S1:L52, S1:L53, S1:L54, S1:L55, S1:L56, S1:L57, S2:L28, S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S2:L36 |
|  | chatgpt | x | x |  |  | S1:L11, S1:L12, S1:L13, S1:L14, S1:L15, S1:L16, S1:L17, S1:L18, S1:L19, S1:L20, S1:L21, S2:L28, S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S2:L36 |
|  | gemini | x | x |  |  | S1:L11, S1:L12, S1:L13, S1:L14, S1:L15, S1:L16, S1:L17, S1:L18, S1:L19, S1:L20, S1:L21, S2:L28, S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S2:L36 |
| `script_30.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L40 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L30, S4:L31, S4:L32, S4:L33, S4:L34, S4:L40 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L40 |
| `script_31.js` | claude |  |  |  |  | - |
|  | chatgpt |  | x | x | x | S2:L14, S3:L28, S3:L62, S4:L28, S4:L50, S4:L62 |
|  | gemini |  | x | x | x | S2:L14, S3:L62, S4:L28, S4:L50, S4:L62 |
| `script_32.js` | claude | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L81, S1:L82, S1:L83, S1:L84, S1:L85, S1:L86, S1:L87, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
|  | chatgpt | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L81, S1:L82, S1:L83, S1:L84, S1:L85, S1:L86, S1:L87, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
|  | gemini | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
| `script_33.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L52 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L42, S4:L43, S4:L44, S4:L45, S4:L46, S4:L52 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L52 |
| `script_34.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L36 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L36, S4:L65 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L36 |
| `script_35.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L14, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L14, S4:L23 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L14, S4:L23 |
| `script_36.js` | claude | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L81, S1:L82, S1:L83, S1:L84, S1:L85, S1:L86, S1:L87, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
|  | chatgpt | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L81, S1:L82, S1:L83, S1:L84, S1:L85, S1:L86, S1:L87, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
|  | gemini | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
| `script_37.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S4:L25, S4:L26, S4:L27, S4:L28, S4:L29, S4:L30, S4:L31, S4:L33 |
|  | chatgpt |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S4:L19, S4:L20, S4:L21, S4:L22, S4:L23, S4:L25, S4:L26, S4:L27, S4:L28, S4:L29, S4:L30, S4:L31, S4:L36, S4:L40 |
|  | gemini |  | x |  |  | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14 |
| `script_38.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S4:L25, S4:L26, S4:L27, S4:L28, S4:L29, S4:L30, S4:L31, S4:L33 |
|  | chatgpt |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S4:L19, S4:L20, S4:L21, S4:L22, S4:L23, S4:L25, S4:L26, S4:L27, S4:L28, S4:L29, S4:L30, S4:L31, S4:L33 |
|  | gemini |  | x |  |  | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14 |
| `script_39.js` | claude |  |  | x | x | S3:L29, S3:L39, S4:L29, S4:L39 |
|  | chatgpt |  |  |  | x | S4:L29, S4:L39, S4:L42 |
|  | gemini |  |  |  | x | S4:L29, S4:L39 |
| `script_40.js` | claude |  |  | x | x | S3:L18, S3:L22, S4:L18, S4:L22 |
|  | chatgpt |  |  | x | x | S3:L18, S3:L22, S4:L18, S4:L22 |
|  | gemini |  |  | x | x | S3:L18, S3:L22, S4:L18, S4:L22 |
| `script_41.js` | claude |  | x |  | x | S2:L4010, S2:L4011, S2:L4012, S2:L4013, S2:L4014, S2:L4015, S2:L4016, S2:L4017, S2:L4018, S2:L4019, S4:L4026, S4:L4027, S4:L4028, S4:L4029, S4:L4030, S4:L4031, S4:L4052, S4:L4053, S4:L4054 |
|  | chatgpt | x | x |  | x | S1:L5, S1:L4006, S2:L4010, S2:L4019, S4:L4026, S4:L4029, S4:L4030, S4:L4031, S4:L4052, S4:L4053, S4:L4054 |
|  | gemini | x | x |  | x | S1:L5, S1:L4006, S2:L4010, S2:L4019, S4:L4026, S4:L4052 |
| `script_42.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L54 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L45, S4:L46, S4:L47, S4:L48, S4:L49, S4:L54 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L54 |
| `script_45.js` | claude | x | x |  | x | S1:L22, S1:L23, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S4:L41, S4:L42, S4:L43 |
|  | chatgpt | x | x |  | x | S1:L22, S1:L23, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S4:L41, S4:L42, S4:L43 |
|  | gemini | x | x |  | x | S1:L22, S1:L23, S2:L6, S2:L15, S4:L41, S4:L42, S4:L43 |
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
|  | gemini |  | x | x |  | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S3:L22, S3:L23, S3:L24, S3:L25, S3:L26, S3:L27, S3:L28 |
| `script_55.js` | claude | x | x |  | x | S1:L19, S1:L20, S1:L21, S1:L22, S1:L23, S1:L24, S1:L25, S1:L26, S1:L27, S1:L28, S1:L29, S1:L30, S1:L31, S1:L32, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L34 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x |  | x | S1:L19, S1:L20, S1:L21, S1:L26, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L27, S4:L34 |
| `script_56.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
| `script_59.js` | claude | x | x |  | x | S1:L16, S1:L17, S2:L20, S2:L21, S2:L22, S2:L23, S2:L24, S2:L25, S2:L26, S2:L27, S2:L28, S2:L29, S4:L46, S4:L47, S4:L48 |
|  | chatgpt | x | x |  | x | S1:L16, S1:L17, S2:L20, S2:L21, S2:L22, S2:L23, S2:L24, S2:L25, S2:L26, S2:L27, S2:L28, S2:L29, S4:L46, S4:L47, S4:L48 |
|  | gemini | x | x |  | x | S1:L16, S1:L17, S2:L20, S2:L21, S2:L22, S2:L23, S2:L24, S2:L25, S2:L26, S2:L27, S2:L28, S2:L29, S4:L46, S4:L47, S4:L48 |
| `script_60.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
| `script_61.js` | claude | x | x |  | x | S1:L19, S1:L20, S1:L21, S1:L22, S1:L23, S1:L24, S1:L25, S1:L26, S1:L27, S1:L28, S1:L29, S1:L30, S1:L31, S1:L32, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L34 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x |  | x | S1:L19, S1:L20, S1:L21, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L34 |
| `script_62.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
| `script_63.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S3:L13, S4:L13 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S3:L13, S4:L13 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S3:L13, S4:L13 |
| `script_69.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S3:L17, S4:L17 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S3:L17, S4:L17 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S3:L17, S4:L17 |
| `script_70.js` | claude |  | x | x | x | S2:L5, S2:L6, S2:L7, S2:L8, S3:L11, S4:L11 |
|  | chatgpt |  | x | x | x | S2:L5, S2:L6, S2:L7, S2:L8, S3:L11, S4:L11 |
|  | gemini |  | x | x | x | S2:L5, S2:L6, S2:L7, S2:L8, S3:L11, S4:L11 |
| `script_71.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S3:L18, S4:L18 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S3:L18, S4:L18 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S3:L18, S4:L18 |
| `script_76.js` | claude |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L21, S3:L22, S4:L16, S4:L17, S4:L18, S4:L19, S4:L21 |
|  | chatgpt |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L21, S4:L16, S4:L17, S4:L18, S4:L19 |
|  | gemini |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L21, S4:L16, S4:L17, S4:L18, S4:L19 |
| `script_77.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L15, S4:L15 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L15, S4:L15 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L15, S4:L15 |
| `script_78.js` | claude |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S3:L14, S4:L14 |
|  | chatgpt |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S3:L14, S4:L14 |
|  | gemini |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S3:L14, S4:L14 |
| `script_80.js` | claude |  | x | x | x | S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S3:L20, S4:L20 |
|  | chatgpt |  | x | x | x | S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S3:L20, S3:L29, S3:L30, S3:L31, S3:L32, S3:L33, S4:L20 |
|  | gemini |  | x | x | x | S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S3:L29, S3:L30, S3:L31, S3:L32, S3:L33, S4:L20 |
| `script_82.js` | claude |  | x | x | x | S2:L7, S2:L8, S2:L9, S3:L12, S4:L12 |
|  | chatgpt |  | x | x | x | S2:L7, S2:L8, S2:L9, S3:L12, S4:L12 |
|  | gemini |  | x | x | x | S2:L7, S2:L8, S2:L9, S3:L12, S4:L12 |
| `script_83.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L24, S4:L24 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L24, S4:L24 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L24, S4:L24 |
| `script_85.js` | claude |  |  |  |  | - |
|  | chatgpt | x | x |  |  | S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L49, S1:L50, S1:L51, S1:L52, S1:L53, S1:L54, S1:L55, S1:L56, S1:L57, S2:L67, S2:L68, S2:L69, S2:L70, S2:L71, S2:L72, S2:L73, S2:L74, S2:L75, S2:L76, S2:L77 |
|  | gemini | x | x |  |  | S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L49, S1:L50, S1:L51, S1:L52, S1:L53, S1:L54, S1:L55, S1:L56, S1:L57, S1:L60, S2:L67, S2:L68, S2:L69, S2:L70, S2:L71, S2:L72, S2:L73, S2:L74, S2:L75, S2:L76, S2:L77 |
| `script_89.js` | claude |  | x | x | x | S2:L9, S2:L10, S2:L11, S3:L16, S4:L16 |
|  | chatgpt |  | x | x | x | S2:L9, S2:L10, S2:L11, S3:L16, S4:L16 |
|  | gemini |  | x | x | x | S2:L9, S2:L10, S2:L11, S3:L16, S4:L16 |
| `script_90.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L10, S4:L10 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L10, S4:L10 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L10, S4:L10 |
| `script_92.js` | claude |  |  |  | x | S4:L45, S4:L63, S4:L87, S4:L104, S4:L131, S4:L150, S4:L167, S4:L230 |
|  | chatgpt |  |  |  | x | S4:L45, S4:L63, S4:L87, S4:L104, S4:L131, S4:L150, S4:L167, S4:L230 |
|  | gemini |  |  |  | x | S4:L45, S4:L63, S4:L87, S4:L104, S4:L131, S4:L150, S4:L167, S4:L230 |
| `script_93.js` | claude |  | x | x | x | S2:L5, S3:L12, S3:L22, S3:L40, S3:L49, S3:L81, S3:L98, S3:L113, S4:L12, S4:L22, S4:L40, S4:L49, S4:L67, S4:L81, S4:L98, S4:L113 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L3, S3:L12, S3:L22, S3:L40, S3:L49, S3:L81, S3:L98, S3:L113, S4:L12, S4:L22, S4:L40, S4:L49, S4:L67, S4:L81, S4:L98, S4:L113 |
| `script_94.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  | x | x | S3:L96, S3:L97, S3:L98, S3:L105, S3:L111, S3:L112, S4:L39, S4:L56, S4:L80, S4:L96, S4:L116, S4:L132, S4:L156, S4:L178 |
|  | gemini |  |  | x | x | S3:L96, S3:L97, S3:L98, S3:L99, S3:L100, S3:L101, S3:L102, S3:L103, S3:L104, S3:L105, S3:L106, S3:L107, S3:L108, S3:L109, S3:L110, S3:L111, S4:L39, S4:L40, S4:L41, S4:L42, S4:L43, S4:L44, S4:L45, S4:L46, S4:L47 |
| `script_95.js` | claude |  | x |  | x | S2:L6, S4:L19, S4:L28, S4:L39, S4:L47, S4:L58, S4:L70, S4:L76, S4:L88, S4:L99, S4:L110, S4:L116 |
|  | chatgpt |  | x |  | x | S2:L6, S4:L22, S4:L33, S4:L51, S4:L63, S4:L82, S4:L93, S4:L104, S4:L121 |
|  | gemini |  | x |  | x | S2:L5, S4:L18, S4:L27, S4:L57, S4:L87, S4:L98, S4:L109 |
| `script_96.js` | claude |  | x | x | x | S2:L6, S3:L13, S3:L23, S3:L41, S3:L50, S3:L82, S3:L99, S4:L13, S4:L23, S4:L41, S4:L50, S4:L68, S4:L82, S4:L99 |
|  | chatgpt |  | x | x | x | S2:L1, S2:L114, S3:L13, S3:L23, S3:L41, S3:L50, S3:L82, S3:L99, S4:L13, S4:L23, S4:L41, S4:L50, S4:L68, S4:L82, S4:L99 |
|  | gemini |  | x | x | x | S2:L6, S3:L13, S3:L23, S3:L41, S3:L50, S3:L82, S3:L99, S4:L13, S4:L23, S4:L41, S4:L50, S4:L68, S4:L82, S4:L99 |
| `script_97.js` | claude |  | x |  |  | S2:L197, S2:L198, S2:L199 |
|  | chatgpt |  | x |  |  | S2:L197, S2:L198, S2:L199 |
|  | gemini |  | x |  |  | S2:L36 |
| `script_98.js` | claude |  | x |  |  | S2:L203, S2:L204, S2:L205 |
|  | chatgpt |  | x |  |  | S2:L203, S2:L204, S2:L205 |
|  | gemini |  | x |  |  | S2:L26 |
| `script_99.js` | claude |  | x |  |  | S2:L502, S2:L503, S2:L504 |
|  | chatgpt |  | x |  |  | S2:L502, S2:L503, S2:L504 |
|  | gemini |  | x |  |  | S2:L1, S2:L504 |
| `script_100.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  | x | S4:L15, S4:L30, S4:L43, S4:L58, S4:L71, S4:L85 |
|  | gemini |  |  |  | x | S4:L15, S4:L30, S4:L43, S4:L58, S4:L71, S4:L85 |
| `script_101.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  | x |  | S3:L107, S3:L108, S3:L109, S3:L110, S3:L111, S3:L112, S3:L113, S3:L114, S3:L115, S3:L116, S3:L117, S3:L118, S3:L119, S3:L120, S3:L121, S3:L122, S3:L123, S3:L124, S3:L125, S3:L126 |
|  | gemini |  |  | x |  | S3:L107, S3:L108, S3:L109, S3:L110, S3:L111, S3:L112, S3:L113, S3:L114, S3:L115, S3:L116, S3:L117, S3:L118, S3:L119, S3:L120, S3:L121, S3:L122, S3:L123, S3:L124, S3:L125 |
| `script_102.js` | claude |  |  |  |  | - |
|  | chatgpt |  | x | x | x | S3:L57, S3:L58, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S3:L64, S3:L65, S3:L66, S4:L19, S4:L32, S4:L41, S4:L50, S4:L58, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63, S4:L64, S4:L65, S4:L66 |
|  | gemini |  |  | x | x | S3:L57, S3:L58, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S3:L64, S3:L65, S3:L66, S3:L67, S4:L19, S4:L32, S4:L41, S4:L50, S4:L58 |
| `script_103.js` | claude |  |  | x | x | S3:L21, S3:L22, S3:L28, S4:L17, S4:L21, S4:L22, S4:L28 |
|  | chatgpt |  |  | x | x | S3:L21, S3:L22, S3:L28, S4:L17, S4:L21, S4:L22, S4:L28 |
|  | gemini |  |  | x |  | S3:L21, S3:L22, S3:L28 |
| `script_104.js` | claude |  |  |  | x | S4:L15, S4:L16, S4:L17, S4:L18 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  | x | S4:L15, S4:L20 |
| `script_105.js` | claude | x | x |  |  | S1:L22, S1:L23, S1:L24, S1:L25, S1:L26, S1:L27, S1:L28, S1:L29, S1:L30, S1:L31, S1:L32, S1:L33, S1:L34, S1:L35, S1:L36, S1:L37, S1:L38, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L51, S1:L52, S1:L53, S1:L54, S2:L13, S2:L14, S2:L15, S2:L16 |
|  | chatgpt |  |  |  | x | S4:L44, S4:L45, S4:L46, S4:L47, S4:L48, S4:L56, S4:L57, S4:L58, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63, S4:L64, S4:L65, S4:L66, S4:L67, S4:L68, S4:L69, S4:L70, S4:L71, S4:L72, S4:L73, S4:L75 |
|  | gemini |  | x |  | x | S2:L13, S2:L14, S2:L15, S2:L16, S4:L85, S4:L93, S4:L99 |
| `script_106.js` | claude |  |  |  | x | S4:L57, S4:L58, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63, S4:L64, S4:L65, S4:L66, S4:L67, S4:L68, S4:L69, S4:L70, S4:L71, S4:L72, S4:L73, S4:L74, S4:L76 |
|  | chatgpt |  |  |  | x | S4:L45, S4:L46, S4:L47, S4:L48, S4:L49, S4:L57, S4:L58, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63, S4:L64, S4:L65, S4:L66, S4:L67, S4:L68, S4:L69, S4:L70, S4:L71, S4:L72, S4:L73, S4:L74, S4:L76 |
|  | gemini |  | x |  | x | S2:L14, S2:L15, S2:L16, S2:L17, S4:L57, S4:L58, S4:L63, S4:L68 |
| `script_107.js` | claude |  |  | x | x | S3:L21, S3:L22, S3:L28, S4:L17, S4:L21, S4:L22, S4:L28 |
|  | chatgpt |  |  | x | x | S3:L21, S3:L22, S3:L28, S4:L17, S4:L21, S4:L22, S4:L28 |
|  | gemini |  |  | x | x | S3:L21, S3:L22, S3:L28, S4:L17, S4:L21, S4:L22, S4:L28 |
| `script_108.js` | claude |  |  | x |  | S3:L21, S3:L22, S3:L28 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L21, S3:L22, S3:L28, S4:L17, S4:L21, S4:L22, S4:L28 |
| `script_109.js` | claude |  | x |  |  | S2:L269, S2:L270, S2:L271 |
|  | chatgpt |  | x |  | x | S2:L269, S2:L270, S2:L271, S4:L254, S4:L255, S4:L256, S4:L257, S4:L258, S4:L259, S4:L260 |
|  | gemini |  | x |  |  | S2:L46 |
| `script_110.js` | claude |  |  | x | x | S3:L54, S4:L20, S4:L42, S4:L54, S4:L63 |
|  | chatgpt |  |  | x | x | S3:L54, S4:L20, S4:L42, S4:L54, S4:L63 |
|  | gemini |  |  | x | x | S3:L54, S4:L20, S4:L42, S4:L54, S4:L63 |
| `script_111.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  | x | S4:L19, S4:L20, S4:L27, S4:L28, S4:L34, S4:L35, S4:L41, S4:L44 |
|  | gemini |  |  |  | x | S4:L19, S4:L27, S4:L34, S4:L41 |
| `script_112.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x |  | x | x | S1:L22, S1:L23, S1:L24, S3:L57, S4:L57 |
| `script_113.js` | claude |  |  |  | x | S4:L66, S4:L87 |
|  | chatgpt |  |  |  | x | S4:L66, S4:L67, S4:L68, S4:L69, S4:L80, S4:L81, S4:L82, S4:L83, S4:L84, S4:L87 |
|  | gemini |  |  |  | x | S4:L66, S4:L87 |
| `script_114.js` | claude |  |  |  | x | S4:L46, S4:L67 |
|  | chatgpt |  |  |  | x | S4:L46, S4:L49, S4:L67 |
|  | gemini |  |  |  | x | S4:L46, S4:L67 |
| `script_115.js` | claude |  | x |  |  | S2:L93, S2:L94, S2:L95 |
|  | chatgpt |  | x |  |  | S2:L93, S2:L94, S2:L95 |
|  | gemini |  | x |  |  | S2:L26 |
| `script_116.js` | claude |  |  |  | x | S4:L43, S4:L55, S4:L71 |
|  | chatgpt |  |  |  | x | S4:L43, S4:L44, S4:L45, S4:L55, S4:L56, S4:L57, S4:L58, S4:L59, S4:L60, S4:L71, S4:L72, S4:L73, S4:L74, S4:L75, S4:L76, S4:L77 |
|  | gemini |  |  |  | x | S4:L43, S4:L55, S4:L71 |
| `script_117.js` | claude |  |  |  |  | - |
|  | chatgpt |  | x |  |  | - |
|  | gemini |  |  |  |  | - |
| `script_118.js` | claude | x |  |  |  | S1:L14 |
|  | chatgpt | x |  |  | x | S1:L13, S1:L14, S4:L63 |
|  | gemini | x |  |  |  | S1:L14 |
| `script_119.js` | claude |  | x |  |  | S2:L152, S2:L153, S2:L154 |
|  | chatgpt |  | x |  |  | S2:L152, S2:L153, S2:L154 |
|  | gemini |  | x |  |  | S2:L1, S2:L154 |
| `script_120.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  | x | S4:L51, S4:L52, S4:L53 |
|  | gemini |  |  | x |  | S3:L166, S3:L167, S3:L168, S3:L169, S3:L170 |
| `script_121.js` | claude |  | x |  |  | S2:L117, S2:L118, S2:L119 |
|  | chatgpt |  | x |  |  | S2:L117, S2:L118, S2:L119 |
|  | gemini |  | x |  |  | S2:L30 |
| `script_122.js` | claude |  |  |  | x | S4:L36, S4:L74, S4:L101 |
|  | chatgpt |  |  |  | x | S4:L36, S4:L37, S4:L38, S4:L39, S4:L74, S4:L75, S4:L76, S4:L77, S4:L101, S4:L102, S4:L103, S4:L104 |
|  | gemini |  |  |  |  | - |
| `script_123.js` | claude |  |  |  | x | S4:L64, S4:L65, S4:L66, S4:L67, S4:L68, S4:L87, S4:L88, S4:L89, S4:L90, S4:L91 |
|  | chatgpt |  |  |  | x | S4:L64, S4:L65, S4:L66, S4:L67, S4:L87, S4:L88, S4:L89, S4:L90 |
|  | gemini |  |  |  | x | S4:L64, S4:L87 |
| `script_124.js` | claude |  | x |  | x | S2:L7, S4:L12 |
|  | chatgpt |  | x |  | x | S2:L7, S4:L12 |
|  | gemini |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S3:L12, S3:L13, S3:L15, S4:L12 |
| `script_125.js` | claude |  | x |  | x | S2:L4, S4:L12 |
|  | chatgpt |  | x |  | x | S2:L4, S4:L12, S4:L14 |
|  | gemini |  | x |  | x | S2:L3, S4:L12 |
| `script_126.js` | claude |  | x | x | x | S2:L7, S3:L10, S3:L15, S4:L10, S4:L15 |
|  | chatgpt |  | x | x | x | S2:L1, S2:L20, S3:L10, S3:L15, S4:L10, S4:L12, S4:L15, S4:L17 |
|  | gemini |  | x | x | x | S2:L1, S2:L20, S3:L10, S3:L15, S4:L10, S4:L12, S4:L15, S4:L17 |
| `script_127.js` | claude |  |  |  | x | S4:L10, S4:L24 |
|  | chatgpt |  |  |  | x | S4:L10, S4:L11, S4:L12, S4:L24 |
|  | gemini |  |  |  | x | S4:L10, S4:L24 |
| `script_128.js` | claude |  |  |  | x | S4:L46, S4:L52 |
|  | chatgpt |  |  |  | x | S4:L46, S4:L52 |
|  | gemini |  |  |  | x | S4:L46, S4:L52 |
| `script_129.js` | claude |  |  |  | x | S4:L20, S4:L27 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  | x | S4:L20, S4:L27 |
| `script_130.js` | claude |  | x |  | x | S2:L7, S2:L8, S2:L9, S4:L14, S4:L22 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  |  | - |
| `script_131.js` | claude |  |  |  | x | S4:L66, S4:L81 |
|  | chatgpt |  |  |  | x | S4:L66, S4:L81, S4:L82, S4:L83, S4:L84, S4:L85 |
|  | gemini |  |  |  | x | S4:L66, S4:L81 |
| `script_133.js` | claude |  | x | x | x | S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S3:L10, S3:L15, S4:L10, S4:L15 |
|  | chatgpt |  | x | x | x | S2:L1, S2:L5, S3:L10, S3:L15, S4:L10, S4:L15 |
|  | gemini |  | x | x | x | S2:L7, S3:L10, S3:L15, S4:L10, S4:L15 |
| `script_134.js` | claude |  |  |  | x | S4:L14, S4:L22 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  |  | - |
| `script_136.js` | claude |  | x |  | x | S2:L7, S4:L9, S4:L22 |
|  | chatgpt |  | x |  | x | S2:L7, S4:L9, S4:L22 |
|  | gemini |  | x |  | x | S2:L3, S4:L9, S4:L22 |
| `script_137.js` | claude |  | x |  |  | S2:L4 |
|  | chatgpt |  | x |  | x | S2:L4, S4:L5, S4:L6, S4:L7 |
|  | gemini |  | x |  | x | S2:L1, S2:L2, S2:L3, S2:L4, S4:L5, S4:L6, S4:L7 |
| `script_138.js` | claude |  | x |  |  | S2:L1 |
|  | chatgpt |  | x |  |  | S2:L1, S2:L63 |
|  | gemini |  | x |  |  | S2:L1 |
| `script_140.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  | x | x | S3:L50, S4:L34, S4:L50 |
|  | gemini |  |  | x | x | S4:L34, S4:L50, S3:L50 |
| `script_143.js` | claude |  | x |  | x | S2:L4, S4:L6, S4:L15 |
|  | chatgpt |  | x |  | x | S2:L4, S4:L6, S4:L15 |
|  | gemini |  | x |  | x | S2:L3, S4:L6, S4:L15 |
| `script_144.js` | claude |  |  |  | x | S4:L16, S4:L38 |
|  | chatgpt |  |  |  | x | S4:L16, S4:L30, S4:L38 |
|  | gemini |  |  |  | x | S4:L16, S4:L38 |
| `script_145.js` | claude |  | x |  | x | S2:L67, S2:L79, S2:L83, S2:L91, S2:L106, S4:L233, S4:L263, S4:L297, S4:L344, S4:L399, S4:L434, S4:L445, S4:L475 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L67, S2:L79, S2:L83, S2:L91, S2:L106, S3:L233, S3:L263, S4:L233, S4:L263, S4:L297, S4:L344 |
| `script_146.js` | claude |  |  | x | x | S3:L34, S4:L34 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L34, S4:L25, S4:L34 |
| `script_148.js` | claude |  |  | x | x | S3:L23, S4:L23 |
|  | chatgpt |  |  | x | x | S3:L23, S4:L23 |
|  | gemini |  |  | x | x | S3:L23, S4:L23 |
| `script_149.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L9 |
| `script_150.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L22, S4:L23, S4:L24 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19 |
|  | gemini |  | x |  | x | S2:L5, S2:L16, S4:L19 |
| `script_151.js` | claude |  |  |  | x | S4:L59 |
|  | chatgpt |  |  | x | x | S3:L14, S3:L18, S3:L19, S4:L14, S4:L59 |
|  | gemini |  |  |  | x | S4:L14, S4:L59 |
| `script_152.js` | claude |  | x | x | x | S2:L6, S3:L10, S4:L10 |
|  | chatgpt |  | x | x | x | S2:L6, S3:L10, S4:L10 |
|  | gemini |  | x | x | x | S2:L5, S3:L10, S4:L10 |
| `script_153.js` | claude |  | x |  |  | S2:L4, S2:L5, S2:L6, S2:L7 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
| `script_154.js` | claude |  | x |  | x | S2:L33, S2:L34, S2:L35, S2:L36, S2:L37, S2:L38, S4:L42 |
|  | chatgpt |  | x |  | x | S2:L33, S2:L34, S2:L35, S2:L36, S2:L37, S2:L38, S4:L42 |
|  | gemini |  | x |  | x | S2:L33, S2:L34, S2:L35, S2:L36, S2:L37, S2:L38, S4:L42 |
| `script_155.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
| `script_156.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
| `script_158.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x |  | S3:L53, S3:L58 |
| `script_160.js` | claude |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L14 |
|  | chatgpt |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L14 |
|  | gemini |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L14 |
| `script_161.js` | claude |  | x | x | x | S2:L6, S3:L7, S4:L7 |
|  | chatgpt |  | x | x | x | S2:L6, S3:L7, S4:L7 |
|  | gemini |  | x | x | x | S3:L7, S4:L7 |
| `script_162.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  | x | S4:L33, S4:L62, S4:L65, S4:L66, S4:L69, S4:L70 |
| `script_163.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L21 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L21 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L21 |
| `script_165.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  | x | x | S3:L43, S3:L44, S3:L45, S3:L46, S3:L47, S3:L48, S4:L43, S4:L50 |
|  | gemini |  |  | x | x | S3:L43, S3:L50, S4:L43 |
| `script_166.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L12, S3:L13, S3:L14, S3:L15, S3:L16, S3:L17, S4:L12, S4:L13, S4:L14, S4:L15, S4:L16, S4:L17 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L12, S3:L13, S3:L14, S3:L15, S3:L16, S3:L17, S3:L24, S3:L25, S3:L26, S4:L12, S4:L13, S4:L14, S4:L15, S4:L16, S4:L17 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L12, S3:L13, S3:L14, S3:L15, S3:L16, S3:L17, S4:L12, S4:L13, S4:L14, S4:L15, S4:L16, S4:L17 |
| `script_167.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L22, S4:L23, S4:L24 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19 |
| `script_168.js` | claude |  | x | x |  | S2:L4, S2:L5, S2:L6, S2:L7, S3:L11, S3:L12, S3:L13, S3:L14, S3:L15 |
|  | chatgpt |  | x |  |  | S2:L4, S2:L5, S2:L6, S2:L7 |
|  | gemini |  | x |  |  | S2:L4, S2:L5, S2:L6, S2:L7 |
| `script_170.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L11 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L11 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L11 |
| `script_172.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L12 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L12 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L12 |
| `script_173.js` | claude |  | x |  | x | S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L26 |
|  | chatgpt |  | x |  | x | S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L26 |
|  | gemini |  | x |  | x | S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L26 |
| `script_174.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  | x | S4:L11 |
|  | gemini |  |  |  | x | S4:L11 |
| `script_175.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S4:L13 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S4:L13 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S4:L13 |
| `script_176.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  |  | - |
| `script_177.js` | claude |  |  |  | x | S4:L11 |
|  | chatgpt |  |  |  | x | S4:L11 |
|  | gemini |  |  |  | x | S4:L11 |
| `script_178.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L22, S4:L23, S4:L24 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19, S4:L22 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19, S4:L22 |
| `script_180.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L9 |
| `script_183.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L73, S3:L74, S3:L75, S4:L82 |
| `script_186.js` | claude |  |  | x | x | S3:L30, S4:L30 |
|  | chatgpt |  |  | x | x | S3:L30, S4:L30, S4:L33 |
|  | gemini |  |  | x | x | S3:L30, S4:L30 |
| `script_188.js` | claude |  | x | x | x | S2:L22, S3:L46, S4:L46 |
|  | chatgpt | x | x | x | x | S1:L18, S1:L19, S1:L20, S2:L22, S3:L46, S4:L39, S4:L40, S4:L41, S4:L42, S4:L43, S4:L44, S4:L46 |
|  | gemini |  | x | x | x | S2:L21, S3:L46, S4:L46 |
| `script_190.js` | claude |  | x | x |  | S2:L4, S2:L5, S2:L6, S2:L7, S3:L11, S3:L12, S3:L13, S3:L14, S3:L15 |
|  | chatgpt |  | x |  |  | S2:L4, S2:L5, S2:L6, S2:L7 |
|  | gemini |  | x |  |  | S2:L4, S2:L5, S2:L6, S2:L7 |
| `script_192.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L31, S4:L32, S4:L33, S4:L34, S4:L35 |
|  | chatgpt |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L31, S4:L32, S4:L33, S4:L34, S4:L35 |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L31, S4:L32, S4:L33, S4:L34, S4:L35 |
| `script_194.js` | claude |  | x |  |  | S2:L33, S2:L34, S2:L35, S2:L36 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L33, S2:L34, S2:L35, S2:L36, S3:L66, S3:L67, S3:L68, S3:L69, S3:L70, S3:L71, S3:L73, S4:L66, S4:L67, S4:L68, S4:L69, S4:L70, S4:L71, S4:L73 |
| `script_195.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
| `script_196.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L29 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L29 |
| `script_197.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
| `script_198.js` | claude |  | x |  | x | S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L35, S4:L36, S4:L37 |
|  | chatgpt |  | x |  | x | S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L35, S4:L36, S4:L37 |
|  | gemini |  | x |  | x | S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L35, S4:L36, S4:L37 |
| `script_201.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L9 |
| `script_202.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  |  | - |
| `script_203.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  | x | S4:L25, S4:L26, S4:L27 |
|  | gemini |  |  | x | x | S3:L29, S3:L30, S3:L31, S4:L25, S4:L26, S4:L27 |
| `script_204.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
| `script_205.js` | claude |  | x | x | x | S2:L39, S2:L40, S2:L41, S2:L42, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L39, S2:L40, S2:L41, S2:L42, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S4:L65 |
| `script_206.js` | claude |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L21 |
|  | chatgpt |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L14, S4:L15, S4:L16, S4:L17, S4:L18, S4:L19, S4:L21 |
|  | gemini |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L21 |
| `script_207.js` | claude |  |  |  | x | S4:L11 |
|  | chatgpt |  |  |  | x | S4:L11 |
|  | gemini |  |  |  | x | S4:L11 |
| `script_208.js` | claude |  | x |  | x | S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L24 |
|  | chatgpt |  | x |  | x | S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L24, S4:L25, S4:L26, S4:L27 |
|  | gemini |  | x |  | x | S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L24 |
| `script_209.js` | claude |  | x |  |  | S2:L5, S2:L6, S2:L7, S2:L8 |
|  | chatgpt |  | x |  |  | S2:L5, S2:L6, S2:L7, S2:L8 |
|  | gemini |  | x |  |  | S2:L5, S2:L6, S2:L7, S2:L8 |
| `script_210.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  |  | - |
| `script_212.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
| `script_213.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L9 |
| `script_214.js` | claude |  |  | x | x | S3:L26, S3:L28, S4:L26 |
|  | chatgpt |  |  | x | x | S3:L26, S3:L28, S4:L26 |
|  | gemini |  |  | x | x | S3:L26, S3:L28, S4:L26 |
| `script_215.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20, S4:L21 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20, S4:L21, S4:L23 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20, S4:L21 |
| `script_216.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L35 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L35 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L35 |
| `script_217.js` | claude |  |  |  | x | S4:L58 |
|  | chatgpt |  |  | x | x | S3:L14, S3:L18, S3:L19, S3:L20, S4:L14, S4:L58 |
|  | gemini |  |  |  | x | S4:L14, S4:L58 |
| `script_218.js` | claude |  | x |  | x | S2:L9, S4:L20, S4:L21, S4:L22 |
|  | chatgpt |  | x |  | x | S2:L9, S4:L20, S4:L21, S4:L22 |
|  | gemini |  | x |  | x | S2:L9, S4:L20, S4:L21, S4:L22 |
| `script_219.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
| `script_221.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
| `script_223.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L25 |
|  | chatgpt |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L25 |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L25, S4:L28 |
| `script_224.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  | x | x | S3:L36, S3:L38, S4:L36, S4:L38 |
|  | gemini |  |  | x | x | S3:L36, S3:L38, S4:L36 |
| `script_227.js` | claude |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L12 |
|  | chatgpt |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L12 |
|  | gemini |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L12 |
| `script_229.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
| `script_230.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  |  | - |
| `script_231.js` | claude |  |  | x |  | S3:L14, S3:L15 |
|  | chatgpt |  |  | x | x | S3:L14, S4:L14 |
|  | gemini |  |  | x | x | S3:L14, S4:L14 |
| `script_232.js` | claude |  | x |  |  | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S4:L13 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S4:L13 |
| `script_233.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L9 |
| `script_234.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S3:L25, S3:L29, S3:L30, S3:L31, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20 |
|  | chatgpt |  | x | x | x | S2:L1, S2:L11, S3:L25, S3:L29, S3:L30, S3:L31, S4:L4, S4:L19 |
|  | gemini |  | x | x | x | S2:L3, S3:L25, S3:L29, S3:L30, S3:L31, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20 |
| `script_235.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S4:L23, S4:L25, S4:L26, S4:L27, S4:L28, S4:L29 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S4:L23 |
| `script_236.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L33 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L26, S4:L27, S4:L28, S4:L29, S4:L30, S4:L33 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L33 |
| `script_237.js` | claude |  | x | x | x | S2:L4, S3:L6, S4:L6 |
|  | chatgpt |  | x | x | x | S2:L4, S3:L6, S4:L6 |
|  | gemini |  | x | x | x | S2:L3, S3:L6, S4:L6 |
| `script_238.js` | claude |  |  | x | x | S3:L39, S3:L41, S4:L39 |
|  | chatgpt | x |  | x | x | S1:L26, S1:L27, S1:L28, S3:L39, S4:L39, S4:L41 |
|  | gemini |  |  | x |  | S3:L39, S3:L41 |
| `script_239.js` | claude |  | x | x | x | S2:L5, S3:L7, S4:L7 |
|  | chatgpt |  | x | x | x | S2:L1, S2:L10, S3:L7, S4:L7 |
|  | gemini |  | x | x | x | S2:L1, S2:L10, S3:L7, S4:L7 |
| `script_240.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
| `script_241.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L19 |
|  | chatgpt |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L19, S4:L22, S4:L28 |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L19, S4:L22 |
| `script_242.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L26 |
|  | chatgpt |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L26, S4:L29, S4:L35, S4:L36, S4:L37, S4:L38, S4:L39, S4:L40, S4:L41, S4:L42, S4:L43, S4:L44, S4:L45, S4:L46 |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L26, S4:L29 |
| `script_245.js` | claude |  |  | x | x | S3:L43, S3:L44, S3:L45, S4:L43 |
|  | chatgpt |  |  | x | x | S3:L43, S4:L43, S4:L45 |
|  | gemini |  |  | x |  | S3:L43, S3:L45 |
| `script_247.js` | claude |  | x | x | x | S2:L6, S3:L14, S4:L14 |
|  | chatgpt |  | x | x | x | S2:L6, S3:L14, S4:L7, S4:L8, S4:L9, S4:L10, S4:L11, S4:L12, S4:L14 |
|  | gemini |  | x | x | x | S2:L1, S2:L21, S3:L14, S4:L14 |
| `script_248.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L22, S4:L23, S4:L24, S4:L25 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19 |
| `script_249.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L20 |
|  | chatgpt |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L20 |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L20, S4:L23 |
| `script_250.js` | claude |  |  | x | x | S3:L23, S4:L23 |
|  | chatgpt |  |  |  | x | S4:L23 |
|  | gemini |  |  | x | x | S3:L23, S3:L32, S3:L33, S3:L34, S3:L35, S3:L36, S4:L23 |
| `script_251.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  | x | x | S3:L57, S4:L57, S4:L58 |
|  | gemini |  |  | x |  | S3:L57, S3:L58 |
| `script_252.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L22 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L22 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L22 |
| `script_253.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S3:L25, S3:L29, S3:L30, S3:L31, S4:L15, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20, S4:L21 |
|  | chatgpt |  | x | x | x | S2:L11, S3:L25, S3:L29, S3:L30, S3:L31, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20 |
|  | gemini |  | x | x | x | S3:L25, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20 |
| `script_254.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L20, S4:L21, S4:L22, S4:L23 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L23 |
| `script_255.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L29 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L27, S4:L29 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L29 |
| `script_257.js` | claude |  |  |  |  | - |
|  | chatgpt | x |  | x | x | S1:L26, S1:L27, S1:L28, S3:L39, S4:L39, S4:L41 |
|  | gemini | x |  | x | x | S1:L26, S1:L27, S1:L28, S3:L39, S3:L41, S4:L39 |
| `script_259.js` | claude |  | x | x | x | S2:L7, S3:L8, S4:L8 |
|  | chatgpt |  | x | x | x | S2:L7, S3:L8, S4:L8 |
|  | gemini |  | x | x | x | S2:L1, S2:L18, S3:L8, S4:L8 |
| `script_260.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L9 |
| `script_262.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
| `script_264.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x | x | x | S1:L15, S2:L39, S2:L40, S2:L41, S2:L42, S3:L73, S3:L74, S3:L75, S4:L77 |
| `script_265.js` | claude |  | x | x | x | S2:L6, S3:L7, S4:L7 |
|  | chatgpt |  | x | x | x | S2:L1, S2:L2, S2:L6, S2:L7, S2:L8, S2:L9, S3:L7, S4:L7 |
|  | gemini |  | x | x | x | S2:L1, S2:L2, S2:L6, S2:L7, S2:L8, S2:L9, S3:L7, S4:L7 |
| `script_266.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x |  | S3:L62, S3:L64, S3:L70 |
| `script_267.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
| `script_268.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
| `script_269.js` | claude |  | x | x | x | S2:L6, S3:L7, S4:L7 |
|  | chatgpt |  | x | x | x | S2:L1, S2:L6, S3:L7, S4:L7 |
|  | gemini |  | x | x | x | S2:L1, S2:L2, S2:L6, S2:L7, S2:L8, S2:L9, S3:L7, S4:L7 |
| `script_270.js` | claude |  | x |  | x | S2:L7, S2:L8, S2:L9, S2:L10, S4:L22 |
|  | chatgpt |  | x |  | x | S2:L7, S2:L8, S2:L9, S2:L10, S4:L22 |
|  | gemini |  | x |  | x | S2:L7, S2:L8, S2:L9, S2:L10, S4:L22 |
| `script_271.js` | claude |  | x | x | x | S2:L6, S3:L7, S4:L7 |
|  | chatgpt |  | x | x | x | S2:L6, S3:L7, S4:L7 |
|  | gemini |  | x | x | x | S2:L6, S3:L7, S4:L7 |
| `script_272.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  |  | - |
| `script_273.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L22, S4:L23, S4:L24 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19 |
|  | gemini |  | x |  | x | S2:L5, S2:L16, S4:L19 |
| `script_276.js` | claude |  | x |  |  | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S4:L12 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S4:L12 |
| `script_277.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19, S4:L22, S4:L23, S4:L24 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19 |
|  | gemini |  | x |  | x | S2:L5, S2:L16, S4:L19 |
| `script_278.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  | x | S4:L62, S4:L65, S4:L66, S4:L69, S4:L70 |
| `script_279.js` | claude |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L25 |
|  | chatgpt |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L25 |
|  | gemini |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L25 |
| `script_280.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L27 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L22, S4:L23, S4:L24, S4:L27 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L27 |
| `script_281.js` | claude |  |  | x | x | S3:L20, S4:L20 |
|  | chatgpt |  |  | x | x | S3:L20, S4:L20 |
|  | gemini |  |  | x | x | S3:L20, S4:L20 |
| `script_282.js` | claude |  | x |  | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L24 |
|  | chatgpt |  | x |  | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L24, S4:L25, S4:L26, S4:L27 |
|  | gemini |  | x |  | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L23, S4:L24, S4:L25, S4:L26, S4:L27, S4:L28 |
| `script_285.js` | claude |  |  | x | x | S3:L47, S3:L49, S4:L47 |
|  | chatgpt |  |  | x | x | S3:L47, S4:L47, S4:L49 |
|  | gemini |  |  | x | x | S3:L47, S3:L49, S4:L47 |
| `script_286.js` | claude | x | x | x | x | S1:L22, S2:L39, S2:L40, S2:L41, S2:L42, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63 |
|  | chatgpt |  | x |  |  | S2:L39, S2:L40, S2:L41, S2:L42 |
|  | gemini |  | x | x | x | S2:L39, S2:L40, S2:L41, S2:L42, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S4:L65 |
| `script_287.js` | claude |  | x |  |  | S2:L4, S2:L5, S2:L6, S2:L7 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
| `script_288.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  | x | x | S3:L68, S3:L73, S3:L80, S3:L88, S3:L93, S3:L100, S4:L68, S4:L73, S4:L80, S4:L82, S4:L88, S4:L89, S4:L93, S4:L100, S4:L101 |
|  | gemini |  |  | x | x | S3:L73, S3:L80, S3:L88, S3:L93, S3:L100, S4:L80, S4:L82, S4:L88, S4:L89, S4:L100, S4:L101 |
| `script_289.js` | claude |  | x | x | x | S2:L11, S3:L24, S3:L28, S3:L29, S3:L30, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20 |
|  | chatgpt |  | x | x | x | S2:L11, S3:L24, S3:L28, S3:L29, S3:L30, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20 |
|  | gemini |  | x | x | x | S2:L3, S3:L24, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20 |
| `script_290.js` | claude |  |  | x |  | S3:L54, S3:L61 |
|  | chatgpt |  |  | x | x | S3:L54, S3:L61, S4:L54, S4:L61, S4:L63 |
|  | gemini |  |  | x | x | S3:L54, S3:L61, S4:L54, S4:L61 |
| `script_291.js` | claude | x | x |  | x | S1:L4, S1:L5, S1:L6, S1:L7, S1:L8, S1:L9, S1:L10, S1:L11, S1:L12, S1:L13, S1:L14, S1:L15, S1:L16, S2:L22, S2:L23, S2:L24, S2:L25, S4:L28 |
|  | chatgpt |  | x |  | x | S2:L22, S2:L23, S2:L24, S2:L25, S4:L28 |
|  | gemini |  | x |  | x | S2:L22, S2:L23, S2:L24, S2:L25, S4:L28 |
| `script_292.js` | claude |  | x |  | x | S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S2:L36, S2:L37, S2:L38, S4:L58, S4:L59, S4:L60 |
|  | chatgpt |  | x |  | x | S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S2:L36, S2:L37, S2:L38, S4:L58, S4:L59, S4:L60 |
|  | gemini |  | x |  | x | S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S2:L36, S2:L37, S2:L38, S4:L58, S4:L59, S4:L60 |
| `script_295.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L32 |
|  | chatgpt |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L32 |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L32 |
| `script_296.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S3:L11, S3:L14, S3:L17, S4:L11, S4:L14, S4:L17 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S3:L11, S3:L14, S3:L17, S4:L11, S4:L14, S4:L17 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S3:L11, S3:L14, S3:L17, S4:L11, S4:L14, S4:L17 |

---

## Detalhamento por Script

## `script_01.js`

### `script_01.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [22, 23]
- **Snippet:**
```js
const csvData = open('../loginSuccess.csv');
const userTokenData = papaparse.parse(csvData).data;
```
- **Refactored:**
```js
// These lines are acceptable in init context as open() is k6's built-in for init-phase file reading.
// However, if the CSV is very large, consider reducing its size or caching parsed results.
// The parse operation runs once per VU — ensure the file is reasonably sized.
const csvData = open('../loginSuccess.csv');
const userTokenData = papaparse.parse(csvData).data;
```

**Smell 2: Do not use thresholds**

- **Lines:** [26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
- **Snippet:**
```js
export let options = {
	iterations: 10,
	vus: 1,
};
```
- **Refactored:**
```js
export let options = {
	iterations: 10,
	vus: 1,
	thresholds: {
		http_req_duration: ['p(95)<500'],
		http_req_failed: ['rate<0.01'],
		'http_req_duration{name:OrderAPI}': ['p(95)<500'],
		'http_req_duration{name:OrderIPNAPI}': ['p(95)<500'],
	},
};
```

**Smell 3: Not checking requests**

- **Lines:** [52, 53, 54, 82, 83, 84]
- **Snippet:**
```js
let orderRes = http.post(`${baseUrl}/api/v1/orders`, orderJSON, {
    headers: headers
});
...
let orderIPNRes = http.post(`${baseUrl}/api/v1/orders/ipn`, orderipnJSON, {
    headers: headersIPN
});
```
- **Refactored:**
```js
let orderRes = http.post(`${baseUrl}/api/v1/orders`, orderJSON, {
    headers: headers
});
check(orderRes, {
    'order API status is 201': (r) => r.json().status_code === 201,
    'order API response time < 500ms': (r) => r.timings.duration < 500,
});
...
let orderIPNRes = http.post(`${baseUrl}/api/v1/orders/ipn`, orderipnJSON, {
    headers: headersIPN
});
check(orderIPNRes, {
    'order IPN API status is 201': (r) => r.status === 201,
    'order IPN API response time < 500ms': (r) => r.timings.duration < 500,
});
```

**Smell 4: Not using tags**

- **Lines:** [52, 53, 54, 82, 83, 84]
- **Snippet:**
```js
let orderRes = http.post(`${baseUrl}/api/v1/orders`, orderJSON, {
    headers: headers
});
...
let orderIPNRes = http.post(`${baseUrl}/api/v1/orders/ipn`, orderipnJSON, {
    headers: headersIPN
});
```
- **Refactored:**
```js
let orderRes = http.post(`${baseUrl}/api/v1/orders`, orderJSON, {
    headers: headers,
    tags: { name: 'OrderAPI' }
});
...
let orderIPNRes = http.post(`${baseUrl}/api/v1/orders/ipn`, orderipnJSON, {
    headers: headersIPN,
    tags: { name: 'OrderIPNAPI' }
});
```

### `script_01.js` — CHATGPT

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

const userTokenData = new SharedArray('user tokens', function () {
  const csvData = open('../loginSuccess.csv');
  return papaparse.parse(csvData, { header: false }).data;
});
```

**Smell 2: Do not use thresholds**

- **Lines:** [26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
- **Snippet:**
```js
export let options = {
	//executor: 'shared-iterations',
	iterations: 10,
	vus: 1,
    // duration: '20s',
};
```
- **Refactored:**
```js
export let options = {
  iterations: 10,
  vus: 1,
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
    'http_req_duration{name:CreateOrder}': ['p(95)<500'],
    'http_req_duration{name:OrderIPN}': ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [52, 53, 54, 82, 83, 84]
- **Snippet:**
```js
let orderRes = http.post(`${baseUrl}/api/v1/orders`, orderJSON, {
    headers: headers
});
...
let orderIPNRes = http.post(`${baseUrl}/api/v1/orders/ipn`, orderipnJSON, {
    headers: headersIPN
});
```
- **Refactored:**
```js
let orderRes = http.post(`${baseUrl}/api/v1/orders`, orderJSON, {
  headers: headers,
  tags: { name: 'CreateOrder' },
});

check(orderRes, {
  'create order HTTP status is 201': (r) => r.status === 201,
  'create order business status_code is 201': (r) => r.json('status_code') === 201,
});

let orderIPNRes = http.post(`${baseUrl}/api/v1/orders/ipn`, orderipnJSON, {
  headers: headersIPN,
  tags: { name: 'OrderIPN' },
});

check(orderIPNRes, {
  'order IPN HTTP status is 201': (r) => r.status === 201,
});
```

**Smell 4: Not using tags**

- **Lines:** [52, 53, 54, 82, 83, 84]
- **Snippet:**
```js
let orderRes = http.post(`${baseUrl}/api/v1/orders`, orderJSON, {
    headers: headers
});
...
let orderIPNRes = http.post(`${baseUrl}/api/v1/orders/ipn`, orderipnJSON, {
    headers: headersIPN
});
```
- **Refactored:**
```js
let orderRes = http.post(`${baseUrl}/api/v1/orders`, orderJSON, {
  headers: headers,
  tags: { name: 'CreateOrder', endpoint: '/api/v1/orders', flow: 'order-purchase' },
});

let orderIPNRes = http.post(`${baseUrl}/api/v1/orders/ipn`, orderipnJSON, {
  headers: headersIPN,
  tags: { name: 'OrderIPN', endpoint: '/api/v1/orders/ipn', flow: 'order-purchase' },
});
```

### `script_01.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [22, 23]
- **Snippet:**
```js
const csvData = open('../loginSuccess.csv');
const userTokenData = papaparse.parse(csvData).data;
```
- **Refactored:**
```js
export function setup() {
  const csvData = open('../loginSuccess.csv');
  const userTokenData = papaparse.parse(csvData).data;
  return { users: userTokenData }; // Pass parsed data to VUs
}

export default function(data) {
  // Access the pre-processed data passed from setup
  let i = Math.floor(Math.random() * 1000) + 1;
  let auth_id = data.users[i][2];
  let userToken = data.users[i][3];
  // ... rest of the script
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [26, 35]
- **Snippet:**
```js
export let options = {
	//executor: 'shared-iterations',
	iterations: 10,
	vus: 1,
    // duration: '20s',
    // stages: [
    //     // Ramp up to 1 VUs for 5 second
    //     { duration: "30s", target: 700 },
    //   ],
};
```
- **Refactored:**
```js
export let options = {
    iterations: 10,
    vus: 1,
    thresholds: {
      'http_req_duration': ['p(95)<1000'], // 95% of requests must be below 1000ms
      'http_req_failed': ['rate<0.01'],   // Error rate should be less than 1%
      'checks': ['rate>0.99']             // Over 99% of checks must pass
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [56, 86]
- **Snippet:**
```js
if(orderRes.json().status_code !== 201){ ... }
// ...
if(orderIPNRes.status !== 201){ ... }
```
- **Refactored:**
```js
// After the first request at line 54
check(orderRes, {
    'POST /api/v1/orders - status is 201': (r) => r.status === 201,
});

if(orderRes.status === 201) {
    // ... existing success logic and second request

    // After the second request at line 84
    check(orderIPNRes, {
        'POST /api/v1/orders/ipn - status is 201': (r) => r.status === 201,
    });
    // ... existing success/fail logic for second request
}
```

**Smell 4: Not using tags**

- **Lines:** [52, 82]
- **Snippet:**
```js
let orderRes = http.post(`${baseUrl}/api/v1/orders`, orderJSON, {
    headers: headers
});
// ...
let orderIPNRes = http.post(`${baseUrl}/api/v1/orders/ipn`, orderipnJSON, {
    headers: headersIPN
});
```
- **Refactored:**
```js
let orderRes = http.post(`${baseUrl}/api/v1/orders`, orderJSON, {
    headers: headers,
    tags: { name: 'CreateOrder' },
});

// ...

let orderIPNRes = http.post(`${baseUrl}/api/v1/orders/ipn`, orderipnJSON, {
    headers: headersIPN,
    tags: { name: 'OrderIPN' },
});
```

---

## `script_02.js`

### `script_02.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
- **Snippet:**
```js
export const options = {
    scenarios: {
      registration_scenario: { ... },
      authentication_scenario: { ... }
    }
};
```
- **Refactored:**
```js
export const options = {
    scenarios: {
      registration_scenario: {
        exec: 'registration',
        executor: 'ramping-vus',
        startVUs: 0,
        stages: [
            { duration: '2m', target: 1 },
            { duration: '15m', target: 1 },
            { duration: '2m', target: 0 }
        ]
      },
      authentication_scenario: {
        exec: 'authentication',
        executor: 'ramping-vus',
        startVUs: 0,
        stages: [
            { duration: '2m', target: 6 },
            { duration: '15m', target: 6 },
            { duration: '2m', target: 0 }
        ]
      }
    },
    thresholds: {
      'http_req_duration{group:::fullRegistration::regContext}': ['p(95)<3000'],
      'http_req_duration{group:::fullRegistration::regOptions}': ['p(95)<3000'],
      'http_req_duration{group:::fullRegistration::register}': ['p(95)<3000'],
      'http_req_duration{group:::fullAuthentication::authContext}': ['p(95)<3000'],
      'http_req_duration{group:::fullAuthentication::authOptions}': ['p(95)<3000'],
      'http_req_duration{group:::fullAuthentication::authenticate}': ['p(95)<3000'],
      'http_req_failed': ['rate<0.01']
    }
};
```

### `script_02.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
- **Snippet:**
```js
export const options = {
    scenarios: {
      registration_scenario: { ... },
      authentication_scenario: { ... }
    }
};
```
- **Refactored:**
```js
export const options = {
  scenarios: {
    registration_scenario: {
      exec: 'registration',
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '2m', target: 1 },
        { duration: '15m', target: 1 },
        { duration: '2m', target: 0 }
      ]
    },
    authentication_scenario: {
      exec: 'authentication',
      executor: 'ramping-vus',
      startVUs: 0,
      stages: [
        { duration: '2m', target: 6 },
        { duration: '15m', target: 6 },
        { duration: '2m', target: 0 }
      ]
    }
  },
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<3000'],
    checks: ['rate>0.99']
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [183, 193, 205, 228, 238, 250]
- **Snippet:**
```js
let res = http.get(`https://${url}/trumfid/biometri/registration/context?returnUrl=`+returnUrl);
let res = http.get(`https://${url}/trumfid/biometri/registration/options?returnUrl=`+returnUrl);
let res = http.post(registerUrl,fakeAttestation, params);
let res = http.get('https://test.id.trumf.no/trumfid/login/context?returnUrl=' + returnUrl);
let res = http.get('https://test.id.trumf.no/trumfid/biometri/login/options');
let res = http.post(url,fakeAssertionLogin);
```
- **Refactored:**
```js
const jsonParams = (name) => ({
  headers: { 'Content-Type': 'application/json' },
  tags: { name }
});

const requestParams = (name) => ({
  tags: { name }
});

let res = http.get(`https://${url}/trumfid/biometri/registration/context?returnUrl=${returnUrl}`, requestParams('RegistrationContext'));
let res = http.get(`https://${url}/trumfid/biometri/registration/options?returnUrl=${returnUrl}`, requestParams('RegistrationOptions'));
let res = http.post(registerUrl, fakeAttestation, jsonParams('RegisterBiometric'));
let res = http.get(`https://test.id.trumf.no/trumfid/login/context?returnUrl=${returnUrl}`, requestParams('AuthenticationContext'));
let res = http.get('https://test.id.trumf.no/trumfid/biometri/login/options', requestParams('AuthenticationOptions'));
let res = http.post(url, fakeAssertionLogin, jsonParams('AuthenticateBiometric'));
```

### `script_02.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [32, 33, 54]
- **Snippet:**
```js
export const options = {
    scenarios: {
      registration_scenario: {
        // ...
      },
      authentication_scenario: {
        // ...
      }
    }
};
```
- **Refactored:**
```js
export const options = {
    thresholds: {
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<3000'],
        'checks{group:::fullRegistration}': ['rate>0.99'],
        'checks{group:::fullAuthentication}': ['rate>0.99']
    },
    scenarios: {
      registration_scenario: {
        exec: 'registration',
        executor: 'ramping-vus',
        startVUs: 0,
        stages: [
                { duration: '2m', target: 6 }, 
                { duration: '15m', target: 6 }, 
                { duration: '2m', target: 0 } 
        ]
      },
      authentication_scenario: {
        exec: 'authentication',
        executor: 'ramping-vus',
        startVUs: 0,
        stages: [
                { duration: '2m', target: 6 }, 
                { duration: '15m', target: 6 }, 
                { duration: '2m', target: 0 } 
        ]
      }
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [183, 193, 205, 228, 238, 250]
- **Snippet:**
```js
let res = http.get(`https://${url}/trumfid/biometri/registration/context?returnUrl=`+returnUrl);
// ...
let res = http.post(registerUrl,fakeAttestation, params);
```
- **Refactored:**
```js
group('fullRegistration', function () {
    group('regContext', function () {
        let res = http.get(`https://${url}/trumfid/biometri/registration/context?returnUrl=`+returnUrl, {
            tags: { name: 'Registration-Context-GET' },
        });

        let checkRes = check(res, {
            'Status 200': (r) => r.status === 200,
            'Response time': (r) => r.timings.duration < 3000
        });
    });
    sleep(3);

    group('regOptions', function () {
        let res = http.get(`https://${url}/trumfid/biometri/registration/options?returnUrl=`+returnUrl, {
            tags: { name: 'Registration-Options-GET' },
        });

        let checkRes = check(res, {
            'Status 200': (r) => r.status === 200,
            'Response time': (r) => r.timings.duration < 3000
        });
    });

    sleep(6);

    group('register', function () {
        const registerUrl = `https://${url}/trumfid/registerbiometric?returnUrl=`+returnUrl;
        const postParams = Object.assign({}, params, { tags: { name: 'Registration-Register-POST' } });
        let res = http.post(registerUrl, fakeAttestation, postParams);

        let checkRes = check(res, {
            'Status 200': (r) => r.status === 200,
            'Response time': (r) => r.timings.duration < 3000
        });
    });
});
```

---

## `script_03.js`

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
    'http_req_duration': ['p(95)<2000'],
    'http_req_failed': ['rate<0.01'],
    'errors_chunked_upload': ['count<5'],
    'upload_duration': ['p(95)<10000'],
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
http.post(`${storageMultipartUri}`, null, { headers: ... })
http.head(location, { headers })
http.patch(location, chunk, { headers: ... })
http.del(`${storageObjectUri}/tus`, ..., { headers: ... })
```
- **Refactored:**
```js
// Add a 'name' tag to each request for proper metric grouping
http.post(`${storageMultipartUri}`, null, {
  headers: Object.assign({ ... }, headers),
  tags: { name: 'CreateUpload' },
})

http.head(location, {
  headers,
  tags: { name: 'CheckOffset' },
})

http.patch(location, chunk, {
  headers: Object.assign({ ... }, headers),
  tags: { name: 'UploadChunk' },
})

http.del(`${storageObjectUri}/tus`, JSON.stringify({ prefixes: [path] }), {
  headers: { ... },
  tags: { name: 'DeleteObject' },
})
```

### `script_03.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [38]
- **Snippet:**
```js
const binFile = open('./large_file.png', 'b')
```
- **Refactored:**
```js
// Avoid loading a large binary file in the init context for every VU when possible.
// Prefer a smaller fixture for load tests, or use the experimental filesystem API to read only needed chunks.
import { open as fsOpen } from 'k6/experimental/fs'

const binFile = fsOpen('./large_file.png')

export default async function () {
  // Read only the required chunk inside the scenario instead of materializing the whole file in init.
  // Example pattern:
  // const chunk = new Uint8Array(chunkSize)
  // await binFile.read(chunk, offset)
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [27, 31]
- **Snippet:**
```js
const to = {}

export const options = {
  thresholds: to,
}
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<1000'],
    checks: ['rate>0.99'],
    errors_chunked_upload: ['count==0'],
    upload_duration: ['p(95)<5000'],
  },
  summaryTrendStats: trends,
  scenarios: {
    storage_multipart: sc(rampingDuration, consecutiveDuration, conns),
  },
}
```

**Smell 4: Not using tags**

- **Lines:** [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 85, 86, 87, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140]
- **Snippet:**
```js
http.post(`${storageMultipartUri}`, null, { headers: ... })
http.head(location, { headers })
http.patch(location, chunk, { headers: ... })
http.del(`${storageObjectUri}/tus`, JSON.stringify(...), { headers: ... })
```
- **Refactored:**
```js
const uploadRes = http.post(`${storageMultipartUri}`, null, {
  headers: Object.assign(
    {
      'Upload-Length': length,
      'Content-Length': 0,
      'Upload-Metadata': `bucketName ${b64encode(metadata.bucketName)},objectName ${b64encode(metadata.objectName)},contentType ${b64encode(metadata.contentType)}`,
    },
    headers
  ),
  tags: { name: 'CreateMultipartUpload', flow: 'storage_multipart' },
})

const offsetRes = http.head(location, {
  headers,
  tags: { name: 'GetUploadOffset', flow: 'storage_multipart' },
})

const uploadChunkRes = http.patch(location, chunk, {
  headers: Object.assign(
    {
      'Content-Type': 'application/offset+octet-stream',
      'Upload-Offset': offset,
      'Content-Length': chunk.byteLength,
    },
    headers
  ),
  tags: { name: 'UploadChunk', flow: 'storage_multipart' },
})

const removeRes = http.del(
  `${storageObjectUri}/tus`,
  JSON.stringify({ prefixes: [path] }),
  {
    headers: {
      authorization: `Bearer ${serviceToken}`,
      apikey: serviceToken,
      'Content-Type': 'application/json',
    },
    tags: { name: 'DeleteUploadedObject', flow: 'storage_multipart' },
  }
)
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
/*
 The file should be loaded only once in the setup function and then passed to the VUs.
 This avoids each VU opening and loading the same file into memory, which is resource-intensive.
*/

export function setup() {
  const binFile = open('./large_file.png', 'b');
  return { fileData: binFile };
}

export default (data) => {
  const binFile = data.fileData; // Use the file data passed from setup()
  // ... rest of the default function logic
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [27, 31]
- **Snippet:**
```js
const to = {}
// ...
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
    'http_req_failed': ['rate<0.01'], // Fail if more than 1% of requests fail
    'http_req_duration': ['p(95)<5000'], // 95% of requests must complete below 5s
    'upload_duration': ['p(95)<15000'], // 95% of full file uploads must be below 15s
    'errors_chunked_upload': ['count==0'], // No chunked upload errors should occur
  },
  // ...
};
```

**Smell 4: Not using tags**

- **Lines:** [60, 85, 103, 128]
- **Snippet:**
```js
const uploadRes = http.post(`${storageMultipartUri}`, null, {
    headers: Object.assign(
    // ...
    ),
});
// ...and other http requests without tags
```
- **Refactored:**
```js
const uploadRes = http.post(`${storageMultipartUri}`, null, {
    tags: { name: 'tus-create' },
    headers: Object.assign(
      // ...
    ),
});

const offsetRes = http.head(location, {
    tags: { name: 'tus-offset' },
    headers,
});

const uploadChunkRes = http.patch(location, chunk, {
    tags: { name: 'tus-upload-chunk' },
    headers: Object.assign(
      // ...
    ),
});

const removeRes = http.del(
    `${storageObjectUri}/tus`,
    // ...
    {
      tags: { name: 'tus-delete' },
      headers: {
        // ...
      },
    }
);
```

---

## `script_04.js`

### `script_04.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
- **Snippet:**
```js
export const options = {
    stages: [
        { duration: '10s', target: 100 },
        { duration: '30s', target: 100 },
        { duration: '10s', target: 0 },
    ]
}
```
- **Refactored:**
```js
export const options = {
    stages: [
        { duration: '10s', target: 100 },
        { duration: '30s', target: 100 },
        { duration: '10s', target: 0 },
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [22, 24, 26]
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
check(res1, { 'home status is 200': (r) => r.status === 200 });
sleep(1);
const res2 = http.get('https://quickpizza.grafana.com/contacts.php');
check(res2, { 'contacts status is 200': (r) => r.status === 200 });
sleep(1);
const res3 = http.get('https://quickpizza.grafana.com/news.php');
check(res3, { 'news status is 200': (r) => r.status === 200 });
sleep(1);
```

**Smell 4: Not using tags**

- **Lines:** [22, 24, 26]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
http.get('https://quickpizza.grafana.com/contacts.php');
http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/', { tags: { name: 'Home' } });
http.get('https://quickpizza.grafana.com/contacts.php', { tags: { name: 'Contacts' } });
http.get('https://quickpizza.grafana.com/news.php', { tags: { name: 'News' } });
```

### `script_04.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
- **Snippet:**
```js
export const options = {
    stages: [
        ...
    ]
}
```
- **Refactored:**
```js
export const options = {
    stages: [
        { duration: '10s', target: 100 },
        { duration: '30s', target: 100 },
        { duration: '10s', target: 0 },
    ],
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [22, 24, 26]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
http.get('https://quickpizza.grafana.com/contacts.php');
http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default function() {
    const homeRes = http.get('https://quickpizza.grafana.com/test.k6.io/');
    check(homeRes, { 'home status is 200': (r) => r.status === 200 });
    sleep(1);

    const contactsRes = http.get('https://quickpizza.grafana.com/contacts.php');
    check(contactsRes, { 'contacts status is 200': (r) => r.status === 200 });
    sleep(1);

    const newsRes = http.get('https://quickpizza.grafana.com/news.php');
    check(newsRes, { 'news status is 200': (r) => r.status === 200 });
    sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [22, 24, 26]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
http.get('https://quickpizza.grafana.com/contacts.php');
http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
export default function() {
    http.get('https://quickpizza.grafana.com/test.k6.io/', {
        tags: { name: 'Home' },
    });
    sleep(1);

    http.get('https://quickpizza.grafana.com/contacts.php', {
        tags: { name: 'Contacts' },
    });
    sleep(1);

    http.get('https://quickpizza.grafana.com/news.php', {
        tags: { name: 'News' },
    });
    sleep(1);
}
```

### `script_04.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
- **Snippet:**
```js
export const options = {
    stages: [
        // ...
    ]
}
```
- **Refactored:**
```js
export const options = {
    stages: [
        {
            duration: '10s',
            target: 100, // Ramp up to 100 users
        },
        {
            duration: '30s',
            target: 100, // Stay at 100 users
        },
        {
            duration: '10s',
            target: 0, // Ramp down to 0 users
        },
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [22, 24, 26]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
sleep(1);
http.get('https://quickpizza.grafana.com/contacts.php');
sleep(1);
http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
import { check } from 'k6';
// ...

export default function() {
    const res1 = http.get('https://quickpizza.grafana.com/test.k6.io/');
    check(res1, { 'Homepage status is 200': (r) => r.status === 200 });
    sleep(1);

    const res2 = http.get('https://quickpizza.grafana.com/contacts.php');
    check(res2, { 'Contacts page status is 200': (r) => r.status === 200 });
    sleep(1);

    const res3 = http.get('https://quickpizza.grafana.com/news.php');
    check(res3, { 'News page status is 200': (r) => r.status === 200 });
    sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [22, 24, 26]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
sleep(1);
http.get('https://quickpizza.grafana.com/contacts.php');
sleep(1);
http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
export default function() {
    http.get('https://quickpizza.grafana.com/test.k6.io/', {
        tags: { name: 'Homepage' },
    });
    sleep(1);

    http.get('https://quickpizza.grafana.com/contacts.php', {
        tags: { name: 'Contacts' },
    });
    sleep(1);

    http.get('https://quickpizza.grafana.com/news.php', {
        tags: { name: 'News' },
    });
    sleep(1);
}
```

---

## `script_05.js`

### `script_05.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [7, 8, 9]
- **Snippet:**
```js
// thresholds: {
//     http_req_duration: ['p(95)<200'], // 95% of requests should complete below 200ms
// },
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '30s',
    thresholds: {
        http_req_duration: ['p(95)<200'], // 95% of requests should complete below 200ms
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [29, 31, 33]
- **Snippet:**
```js
http.get('https://test.k6.io');
http.get('https://test.k6.io/contact.php');
http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
import { check } from 'k6';

export default function () {
    let res1 = http.get('https://test.k6.io');
    check(res1, { 'homepage status 200': (r) => r.status === 200 });
    sleep(1);

    let res2 = http.get('https://test.k6.io/contact.php');
    check(res2, { 'contact status 200': (r) => r.status === 200 });
    sleep(2);

    let res3 = http.get('https://test.k6.io/news.php');
    check(res3, { 'news status 200': (r) => r.status === 200 });
    sleep(2);
}
```

**Smell 4: Not using tags**

- **Lines:** [29, 31, 33]
- **Snippet:**
```js
http.get('https://test.k6.io');
http.get('https://test.k6.io/contact.php');
http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
export default function () {
    let res1 = http.get('https://test.k6.io', { tags: { name: 'Homepage' } });
    check(res1, { 'homepage status 200': (r) => r.status === 200 });
    sleep(1);

    let res2 = http.get('https://test.k6.io/contact.php', { tags: { name: 'Contact' } });
    check(res2, { 'contact status 200': (r) => r.status === 200 });
    sleep(2);

    let res3 = http.get('https://test.k6.io/news.php', { tags: { name: 'News' } });
    check(res3, { 'news status 200': (r) => r.status === 200 });
    sleep(2);
}
```

### `script_05.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 26]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '30s',
    // thresholds: {
    //     http_req_duration: ['p(95)<200'],
    // },
};
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '30s',
    thresholds: {
        http_req_duration: ['p(95)<200'],
        http_req_failed: ['rate<0.01'],
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [29, 31, 33]
- **Snippet:**
```js
http.get('https://test.k6.io');
http.get('https://test.k6.io/contact.php');
http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
import { check, sleep } from 'k6';

export default function () {
    const homeRes = http.get('https://test.k6.io');
    check(homeRes, {
        'home status is 200': (r) => r.status === 200,
    });
    sleep(1);

    const contactRes = http.get('https://test.k6.io/contact.php');
    check(contactRes, {
        'contact status is 200': (r) => r.status === 200,
    });
    sleep(2);

    const newsRes = http.get('https://test.k6.io/news.php');
    check(newsRes, {
        'news status is 200': (r) => r.status === 200,
    });
    sleep(2);
}
```

**Smell 4: Not using tags**

- **Lines:** [29, 31, 33]
- **Snippet:**
```js
http.get('https://test.k6.io');
http.get('https://test.k6.io/contact.php');
http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '30s',
    thresholds: {
        'http_req_duration{name:Home}': ['p(95)<200'],
        'http_req_duration{name:Contact}': ['p(95)<200'],
        'http_req_duration{name:News}': ['p(95)<200'],
    },
};

export default function () {
    http.get('https://test.k6.io', { tags: { name: 'Home' } });
    sleep(1);
    http.get('https://test.k6.io/contact.php', { tags: { name: 'Contact' } });
    sleep(2);
    http.get('https://test.k6.io/news.php', { tags: { name: 'News' } });
    sleep(2);
}
```

### `script_05.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [7, 8, 9]
- **Snippet:**
```js
// thresholds: {
//     http_req_duration: ['p(95)<200'], // 95% of requests should complete below 200ms
// },
```
- **Refactored:**
```js
thresholds: {
    http_req_duration: ['p(95)<200'], // 95% of requests should complete below 200ms
},
```

**Smell 3: Not checking requests**

- **Lines:** [29, 31, 33]
- **Snippet:**
```js
http.get('https://test.k6.io');
http.get('https://test.k6.io/contact.php');
http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
import { check } from 'k6';

// In the default function
const res = http.get('https://test.k6.io');
check(res, { 'status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [29, 31, 33]
- **Snippet:**
```js
http.get('https://test.k6.io');
http.get('https://test.k6.io/contact.php');
http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
http.get('https://test.k6.io', { tags: { name: 'Homepage' } });
sleep(1);
http.get('https://test.k6.io/contact.php', { tags: { name: 'Contact' } });
sleep(2);
http.get('https://test.k6.io/news.php', { tags: { name: 'News' } });
```

---

## `script_06.js`

### `script_06.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '60s',
    ext: {
        loadimpact: {
            projectID: 3679087
        }
    }
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '60s',
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01']
    },
    ext: {
        loadimpact: {
            projectID: 3679087
        }
    }
}
```

**Smell 3: Not checking requests**

- **Lines:** [16, 18, 20]
- **Snippet:**
```js
http.get('https://test.k6.io');
http.get('https://test.k6.io/contacts.php')
http.get('https://test.k6.io/news.php')
```
- **Refactored:**
```js
import { check } from 'k6';

const res1 = http.get('https://test.k6.io');
check(res1, { 'home status is 200': (r) => r.status === 200 });
const res2 = http.get('https://test.k6.io/contacts.php');
check(res2, { 'contacts status is 200': (r) => r.status === 200 });
const res3 = http.get('https://test.k6.io/news.php');
check(res3, { 'news status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [16, 18, 20]
- **Snippet:**
```js
http.get('https://test.k6.io');
http.get('https://test.k6.io/contacts.php')
http.get('https://test.k6.io/news.php')
```
- **Refactored:**
```js
http.get('https://test.k6.io', { tags: { name: 'Home' } });
http.get('https://test.k6.io/contacts.php', { tags: { name: 'Contacts' } });
http.get('https://test.k6.io/news.php', { tags: { name: 'News' } });
```

### `script_06.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '60s',
    ext: {
        loadimpact: {
            projectID: 3679087
        }
    }
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '60s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99']
    },
    ext: {
        loadimpact: {
            projectID: 3679087
        }
    }
};
```

**Smell 3: Not checking requests**

- **Lines:** [16, 18, 20]
- **Snippet:**
```js
http.get('https://test.k6.io');
http.get('https://test.k6.io/contacts.php')
http.get('https://test.k6.io/news.php')
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default function() {
    const homeRes = http.get('https://test.k6.io', { tags: { name: 'Home' } });
    check(homeRes, {
        'Home status is 200': (r) => r.status === 200
    });
    sleep(1);

    const contactsRes = http.get('https://test.k6.io/contacts.php', { tags: { name: 'Contacts' } });
    check(contactsRes, {
        'Contacts status is 200': (r) => r.status === 200
    });
    sleep(2);

    const newsRes = http.get('https://test.k6.io/news.php', { tags: { name: 'News' } });
    check(newsRes, {
        'News status is 200': (r) => r.status === 200
    });
    sleep(2);
}
```

**Smell 4: Not using tags**

- **Lines:** [16, 18, 20]
- **Snippet:**
```js
http.get('https://test.k6.io');
http.get('https://test.k6.io/contacts.php')
http.get('https://test.k6.io/news.php')
```
- **Refactored:**
```js
export default function() {
    http.get('https://test.k6.io', {
        tags: { name: 'Home', endpoint: 'home' }
    });
    sleep(1);

    http.get('https://test.k6.io/contacts.php', {
        tags: { name: 'Contacts', endpoint: 'contacts' }
    });
    sleep(2);

    http.get('https://test.k6.io/news.php', {
        tags: { name: 'News', endpoint: 'news' }
    });
    sleep(2);
}
```

### `script_06.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '60s',
    ext: {
        loadimpact: {
            projectID: 3679087
        }
    }
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '60s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
    },
    ext: {
        loadimpact: {
            projectID: 3679087
        }
    }
}
```

**Smell 3: Not checking requests**

- **Lines:** [16, 18, 20]
- **Snippet:**
```js
http.get('https://test.k6.io');
// ...
http.get('https://test.k6.io/contacts.php')
// ...
http.get('https://test.k6.io/news.php')
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
export default function() {
    const res1 = http.get('https://test.k6.io');
    check(res1, { 'Homepage status is 200': (r) => r.status === 200 });
    sleep(1);

    const res2 = http.get('https://test.k6.io/contacts.php');
    check(res2, { 'Contacts status is 200': (r) => r.status === 200 });
    sleep(2);

    const res3 = http.get('https://test.k6.io/news.php');
    check(res3, { 'News status is 200': (r) => r.status === 200 });
    sleep(2);
}
```

**Smell 4: Not using tags**

- **Lines:** [16, 18, 20]
- **Snippet:**
```js
http.get('https://test.k6.io');
// ...
http.get('https://test.k6.io/contacts.php')
// ...
http.get('https://test.k6.io/news.php')
```
- **Refactored:**
```js
export default function() {
    http.get('https://test.k6.io', {
      tags: { name: 'Homepage' },
    });
    sleep(1);

    http.get('https://test.k6.io/contacts.php', {
      tags: { name: 'Contacts' },
    });
    sleep(2);

    http.get('https://test.k6.io/news.php', {
      tags: { name: 'News' },
    });
    sleep(2);
}
```

---

## `script_07.js`

### `script_07.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [22]
- **Snippet:**
```js
let payload = JSON.parse(open('./testdata_v1.json'));
```
- **Refactored:**
```js
// Use SharedArray to perform the JSON parsing only once and share it across VUs
import { SharedArray } from 'k6/data';
const payloadArray = new SharedArray('testdata', function() {
  return [JSON.parse(open('./testdata_v1.json'))];
});
// Then in the default function, access it as:
// let user = Object.assign({}, payloadArray[0]);
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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [13, 48]
- **Snippet:**
```js
const onlyonce = http.get(`https://example.com`);
...
const res = http.post(`https://echo.hoppscotch.io`, f);
```
- **Refactored:**
```js
import { check } from 'k6';

// In setup():
const onlyonce = http.get('https://example.com');
check(onlyonce, {
  'setup GET status is 200': (r) => r.status === 200,
});

// In default function:
const res = http.post('https://echo.hoppscotch.io', f);
check(res, {
  'POST status is 200': (r) => r.status === 200,
  'POST response has body': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [13, 48]
- **Snippet:**
```js
const onlyonce = http.get(`https://example.com`);
...
const res = http.post(`https://echo.hoppscotch.io`, f);
```
- **Refactored:**
```js
// In setup():
const onlyonce = http.get('https://example.com', { tags: { name: 'ExampleGet' } });

// In default function:
const res = http.post('https://echo.hoppscotch.io', f, { tags: { name: 'EchoPost' } });

// And update thresholds to leverage tags:
// thresholds: {
//   'http_req_duration{name:ExampleGet}': ['p(95)<300'],
//   'http_req_duration{name:EchoPost}': ['p(95)<500'],
// }
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
import { SharedArray } from 'k6/data';

const payloadData = new SharedArray('test-data', function () {
  return JSON.parse(open('./testdata_v1.json'));
});
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
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
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
//...
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
  tags: { name: 'EchoRequest' },
};
const res = http.post(`https://echo.hoppscotch.io`, f, params);
```

---

## `script_08.js`

### `script_08.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [11]
- **Snippet:**
```js
http.post('https://example.com/upload', data);
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const res = http.post('https://example.com/upload', data);
check(res, {
  'status is 200': (r) => r.status === 200,
  'upload successful': (r) => r.status >= 200 && r.status < 300,
});
```

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
http.post('https://example.com/upload', data);
```
- **Refactored:**
```js
http.post('https://example.com/upload', data, {
  tags: { name: 'FileUpload' },
});
```

### `script_08.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [4]
- **Snippet:**
```js
const binFile = open('./file.bin', 'b');
```
- **Refactored:**
```js
import { open } from 'k6';
import http from 'k6/http';

// Use the setup lifecycle function to read the file once.
export function setup() {
  const binFile = open('./file.bin', 'b');
  return { fileData: binFile };
}

// The data from setup is passed to the default function.
export default function (data) {
  const postData = {
    field: 'this is a standard form field',
    file: http.file(data.fileData, 'test.bin'),
  };
  // ... rest of the code
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [3]
- **Snippet:**
```js
// The options object with thresholds is missing from the script.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<1000'], // 95% of requests should be below 1000ms
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [11]
- **Snippet:**
```js
http.post('https://example.com/upload', data);
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const res = http.post('https://example.com/upload', data);
check(res, {
  'upload was successful (status 201)': (r) => r.status === 201,
});
```

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
http.post('https://example.com/upload', data);
```
- **Refactored:**
```js
http.post('https://example.com/upload', data, {
  tags: { name: 'FileUpload' },
});
```

---

## `script_09.js`

### `script_09.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [70, 71, 72, 74, 88, 89, 90, 91, 92]
- **Snippet:**
```js
const res = http.post(restURI + '/insert_positions', body, {
  headers: headers,
})

myFailRate.add(res.status !== 204)
...
http.del(
  restURI + '/positions?title=eq.Load%20Tester',
  {},
  { headers: Object.assign(headers, { Prefer: 'count=exact' }) }
)
```
- **Refactored:**
```js
const res = http.post(restURI + '/insert_positions', body, {
  headers: headers,
})

const insertOk = check(res, {
  'insert_positions returns 204': (r) => r.status === 204,
})
myFailRate.add(!insertOk)

export function teardown(data) {
  const cleanupRes = http.del(
    restURI + '/positions?title=eq.Load%20Tester',
    {},
    { headers: Object.assign({}, headers, { Prefer: 'count=exact' }) }
  )

  check(cleanupRes, {
    'cleanup request succeeds': (r) => r.status >= 200 && r.status < 300,
  })
}
```

**Smell 4: Not using tags**

- **Lines:** [70, 71, 72, 88, 89, 90, 91, 92]
- **Snippet:**
```js
const res = http.post(restURI + '/insert_positions', body, {
  headers: headers,
})
...
http.del(
  restURI + '/positions?title=eq.Load%20Tester',
  {},
  { headers: Object.assign(headers, { Prefer: 'count=exact' }) }
)
```
- **Refactored:**
```js
const res = http.post(restURI + '/insert_positions', body, {
  headers: headers,
  tags: { name: 'InsertPositions', endpoint: 'insert_positions', flow: 'load_test' },
})

export function teardown(data) {
  const cleanupRes = http.del(
    restURI + '/positions?title=eq.Load%20Tester',
    {},
    {
      headers: Object.assign({}, headers, { Prefer: 'count=exact' }),
      tags: { name: 'CleanupPositions', endpoint: 'positions_cleanup', flow: 'teardown' },
    }
  )
}
```

### `script_09.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [74]
- **Snippet:**
```js
myFailRate.add(res.status !== 204)
```
- **Refactored:**
```js
const checkRes = check(res, {
  'status is 204': (r) => r.status === 204,
});
myFailRate.add(!checkRes);
```

**Smell 4: Not using tags**

- **Lines:** [70, 71, 72]
- **Snippet:**
```js
const res = http.post(restURI + '/insert_positions', body, {
  headers: headers,
})
```
- **Refactored:**
```js
const res = http.post(restURI + '/insert_positions', body, {
  headers: headers,
  tags: {
    name: 'InsertPosition',
  },
});
```

---

## `script_10.js`

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
  // no tags property defined
  ...
});
```
- **Refactored:**
```js
postman[Request]({
  name: "Registration",
  method: "POST",
  address: "{{APIURL}}/users",
  tags: { name: "Registration", group: "Registration and Authentication" },
  ...
});
// Apply similarly to every postman[Request] call, using a descriptive 'name' and 'group' tag matching the enclosing group().
```

### `script_10.js` — CHATGPT

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
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99']
  }
};
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
  // Add thresholds to define success criteria for the test.
  thresholds: {
    // Fail the test if more than 1% of requests fail.
    'http_req_failed': ['rate<0.01'],
    // Fail the test if the 95th percentile of request duration is > 800ms.
    'http_req_duration': ['p(95)<800'],
    // The 'name' property from postman[Request] is used as a tag,
    // allowing for specific endpoint thresholds.
    'http_req_duration{name:Login}': ['p(95)<400'],
    'http_req_duration{name:Registration}': ['p(95)<500']
  },
};
```

---

## `script_11.js`

### `script_11.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [99, 132, 138, 146, 196, 204, 213, 229, 262, 269, 302, 319, 334, 348, 376, 390, 404, 419]
- **Snippet:**
```js
const loginRes = http.post(...);
let res = http.get(`${BASE_URL}/api/v1/dashboard`, { headers });
actionSuccess.add(res.status === 200);
```
- **Refactored:**
```js
import { check } from 'k6';

function assertStatus(res, label, acceptedStatuses) {
  check(res, {
    [`${label}: expected status ${acceptedStatuses.join(' or ')}`]: (r) => acceptedStatuses.includes(r.status),
  });
}

function authenticate() {
  const loginRes = http.post(
    `${BASE_URL}/api/v1/auth/login`,
    JSON.stringify({
      email: `user${Math.floor(Math.random() * 1000)}@mams.local`,
      password: 'TestUser123!',
    }),
    { headers: { 'Content-Type': 'application/json' } }
  );
  assertStatus(loginRes, 'Auth login', [200]);
  return loginRes.status === 200 ? loginRes.json('data.accessToken') : null;
}

// Apply the same pattern after each request:
let res = http.get(`${BASE_URL}/api/v1/dashboard`, { headers });
assertStatus(res, 'Dashboard', [200]);
userActions.add(1);
actionSuccess.add(res.status === 200);
```

**Smell 4: Not using tags**

- **Lines:** [99, 132, 138, 146, 196, 204, 213, 229, 262, 269, 302, 319, 334, 348, 376, 390, 404, 419]
- **Snippet:**
```js
http.get(`${BASE_URL}/api/v1/dashboard`, { headers });
http.get(`${BASE_URL}/api/v1/assets?sort=-created_at&limit=20`, { headers });
http.post(`${BASE_URL}/api/v1/assets`, payload, { headers });
```
- **Refactored:**
```js
function taggedParams(headers, name, flow, extra = {}) {
  return {
    ...extra,
    headers,
    tags: { name, flow },
  };
}

const authHeaders = { 'Content-Type': 'application/json' };
const loginRes = http.post(
  `${BASE_URL}/api/v1/auth/login`,
  JSON.stringify({ email, password }),
  taggedParams(authHeaders, 'AuthLogin', 'authentication')
);

let res = http.get(
  `${BASE_URL}/api/v1/dashboard`,
  taggedParams(headers, 'Dashboard', 'morning_user_behavior')
);

res = http.get(
  `${BASE_URL}/api/v1/assets?sort=-created_at&limit=20`,
  taggedParams(headers, 'RecentAssets', 'morning_user_behavior')
);

res = http.post(
  `${BASE_URL}/api/v1/assets`,
  JSON.stringify({ name: `morning-upload-${Date.now()}.mp4`, type: 'video', size }),
  taggedParams(headers, 'CreateAsset', 'morning_user_behavior')
);
```

### `script_11.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [132, 134]
- **Snippet:**
```js
let res = http.get(`${BASE_URL}/api/v1/dashboard`, { headers });
userActions.add(1);
actionSuccess.add(res.status === 200);
```
- **Refactored:**
```js
const res = http.get(`${BASE_URL}/api/v1/dashboard`, { headers });
check(res, {
  'dashboard response is 200': (r) => r.status === 200,
});
userActions.add(1);
actionSuccess.add(res.status === 200);
```

**Smell 4: Not using tags**

- **Lines:** [132, 138, 146, 162, 196]
- **Snippet:**
```js
res = http.get(`${BASE_URL}/api/v1/dashboard`, { headers });
...
res = http.get(`${BASE_URL}/api/v1/assets?sort=-created_at&limit=20`, { headers });
...
res = http.post(`${BASE_URL}/api/v1/assets`, ...);
```
- **Refactored:**
```js
res = http.get(`${BASE_URL}/api/v1/dashboard`, {
  headers,
  tags: { name: 'Dashboard' },
});
...
res = http.get(`${BASE_URL}/api/v1/assets?sort=-created_at&limit=20`, {
  headers,
  tags: { name: 'GetRecentAssets' },
});
...
res = http.post(`${BASE_URL}/api/v1/assets`, ..., {
  headers,
  tags: { name: 'UploadAsset' },
});
```

---

## `script_12.js`

### `script_12.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [21, 22, 23, 24, 27, 28, 29, 30, 31, 32, 33, 34, 36]
- **Snippet:**
```js
const mobileNumber = generateRandomMobileNumber();
const sentPayload = JSON.stringify({
    mobile: mobileNumber
})
...
const verifyPayload = JSON.stringify({
    "mobile": mobileNumber,
    ...
})
const fileData = open('./download.pdf', 'b');
```
- **Refactored:**
```js
// Move dynamic data generation and payload construction inside the default function
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
    // fileData is fine to keep in init since open() is only allowed there,
    // but JSON.stringify and generateRandomMobileNumber() should be inside default
    ...
}
```

**Smell 4: Not using tags**

- **Lines:** [43, 50, 64, 72, 110, 122, 134, 141, 148, 158, 170, 176, 195, 210]
- **Snippet:**
```js
const sendOtpResponse = http.post(`${baseUrl}/users/v1/public/send-otp`, sentPayload, { headers });
const verifyOtp = http.post(`${baseUrl}/users/v1/public/verify-otp`, verifyPayload, { headers });
const profileGet = http.get(`${baseUrl}/users/v1/profile`, { headers });
// ... all other requests have no tags
```
- **Refactored:**
```js
// Add tags to each request to enable metric filtering per endpoint
const sendOtpResponse = http.post(
    `${baseUrl}/users/v1/public/send-otp`,
    sentPayload,
    { headers, tags: { name: 'SendOTP' } }
);
const verifyOtp = http.post(
    `${baseUrl}/users/v1/public/verify-otp`,
    verifyPayload,
    { headers, tags: { name: 'VerifyOTP' } }
);
const profileGet = http.get(
    `${baseUrl}/users/v1/profile`,
    { headers, tags: { name: 'ProfileGet' } }
);
// Apply the same pattern to all remaining requests:
// uploadPost -> { headers, tags: { name: 'UploadDocument' } }
// healthRecordsGet -> { headers, tags: { name: 'HealthRecordsGet' } }
// getdownloadToken -> { headers, tags: { name: 'GetDownloadToken' } }
// downloadGetResponse -> { headers, tags: { name: 'DownloadDocument' } }
// deleteDocument -> { headers, tags: { name: 'DeleteDocument' } }
// notificationGet -> { headers, tags: { name: 'NotificationGet' } }
// allAddressesGet -> { headers, tags: { name: 'AllAddressesGet' } }
// postAddress -> { headers, tags: { name: 'PostAddress' } }
// patchAddress -> { headers, tags: { name: 'PatchAddress' } }
// deleteAddress -> { headers, tags: { name: 'DeleteAddress' } }
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
/* Move the file opening operation from the init context into the default function, just before it is used. This prevents each VU from holding the file in memory for the entire test duration, reducing overall memory consumption. */

    group('Health Records', function () {
        const fileData = open('./download.pdf', 'b');
        const fd = new FormData();
        fd.append("type", "health_records");
        fd.append("file", http.file(fileData, 'application/pdf'))
        // ... rest of the code that uses fd
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
/* Add a 'tags' object to each HTTP request's parameters. This allows for more granular metric filtering and the ability to set specific thresholds for individual endpoints, making it easier to pinpoint performance issues. */

const sendOtpResponse = http.post(`${baseUrl}/users/v1/public/send-otp`, sentPayload, {
    headers,
    tags: { name: 'SendOTP' }
});

const verifyOtp = http.post(`${baseUrl}/users/v1/public/verify-otp`, verifyPayload, {
    headers,
    tags: { name: 'VerifyOTP' }
});
```

---

## `script_13.js`

### `script_13.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [15, 16, 17]
- **Snippet:**
```js
export let options = {
  maxRedirects: 4
};
```
- **Refactored:**
```js
export let options = {
  maxRedirects: 4,
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [30, 93, 140, 200, 250, 303, 356, 410, 463, 516, 569]
- **Snippet:**
```js
postman[Request]({
  name: "Registration",
  ...
});

postman[Request]({
  name: "Login and Remember Token",
  ...
});

postman[Request]({
  name: "Create tags for create tags",
  ...
});
```
- **Refactored:**
```js
// Add a 'tags' property to each postman[Request] call to enable metric filtering per request.
// Example for the Registration request:
postman[Request]({
  name: "Registration",
  id: "2024-02-23-06-45-22-022",
  method: "POST",
  options: { timeout: timeout, tags: { name: 'Registration' } },
  address: "{{APIURL}}/users",
  ...
});

// Example for Login:
postman[Request]({
  name: "Login and Remember Token",
  id: "2024-02-23-06-45-22-022",
  method: "POST",
  options: { timeout: timeout, tags: { name: 'LoginAndRememberToken' } },
  address: "{{APIURL}}/users/login",
  ...
});

// Apply the same pattern to all other requests, e.g.:
// options: { timeout: timeout, tags: { name: 'CreateTags' } }
// options: { timeout: timeout, tags: { name: 'FindTagsByPrimaryKey' } }
// etc.
```

### `script_13.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [15, 16, 17]
- **Snippet:**
```js
export let options = {
  maxRedirects: 4
};
```
- **Refactored:**
```js
export let options = {
  maxRedirects: 4,
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks': ['rate>0.99'] // 99% of checks should pass
  }
};
```

---

## `script_15.js`

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
  check(res, {
    'GET /api/v1/assets status is 200': (r) => r.status === 200,
  });

  if (res.status === 0) {
    apiTimeouts.add(1);
  } else if (res.status >= 500) {
    apiErrors.add(1);
  }
});
```

**Smell 3: Not checking requests**

- **Lines:** [248, 249, 250, 251, 252, 253, 254, 255, 256, 257]
- **Snippet:**
```js
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
    { headers, timeout: '5s' }
  );
  check(patchRes, {
    'asset metadata updated successfully': (r) => r.status === 200,
  });
}
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
  tags: {
    name: 'GetAssets-RateLimit',
    scenario: 'rate_limit_test',
  },
});
```

---

## `script_16.js`

### `script_16.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [18]
- **Snippet:**
```js
const USERNAME = `${randomString(10)}@example.com`;
```
- **Refactored:**
```js
// Move random username generation inside the setup() function or default function, not at the init context level
// In setup():
export function setup() {
  const username = `${randomString(10)}@example.com`;
  const res = http.post(
    `${BASE_URL}/api/users`,
    JSON.stringify({
      username: username,
      password: PASSWORD,
    })
  );
  // ...
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export const options = {
  vus: 1,
  iterations: 1,
};
```
- **Refactored:**
```js
export const options = {
  vus: 1,
  iterations: 1,
  thresholds: {
    'http_req_duration{name:Create}': ['p(95)<500'],
    'http_req_duration{name:Fetch}': ['p(95)<500'],
    'http_req_duration{name:Update}': ['p(95)<500'],
    'http_req_duration{name:Delete}': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
  },
};
```

### `script_16.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export const options = {
  vus: 1,
  iterations: 1,
};
```
- **Refactored:**
```js
export const options = {
  vus: 1,
  iterations: 1,
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [35, 36, 37, 38, 39, 40, 41, 43, 44]
- **Snippet:**
```js
const loginRes = http.post(
  `${BASE_URL}/api/users/token/login`,
  JSON.stringify({
    username: USERNAME,
    password: PASSWORD,
  })
);

const authToken = loginRes.json('token');
check(authToken, { 'logged in successfully': () => authToken.length > 0 });
```
- **Refactored:**
```js
const loginRes = http.post(
  `${BASE_URL}/api/users/token/login`,
  JSON.stringify({
    username: USERNAME,
    password: PASSWORD,
  }),
  { tags: { name: 'Login' } }
);

check(loginRes, {
  'login status is 200': (r) => r.status === 200,
  'login returned token': (r) => Boolean(r.json('token')),
});

const authToken = loginRes.json('token');
```

**Smell 4: Not using tags**

- **Lines:** [25, 26, 27, 28, 29, 30, 31, 35, 36, 37, 38, 39, 40, 41]
- **Snippet:**
```js
const res = http.post(
  `${BASE_URL}/api/users`,
  JSON.stringify({
    username: USERNAME,
    password: PASSWORD,
  })
);

const loginRes = http.post(
  `${BASE_URL}/api/users/token/login`,
  JSON.stringify({
    username: USERNAME,
    password: PASSWORD,
  })
);
```
- **Refactored:**
```js
const res = http.post(
  `${BASE_URL}/api/users`,
  JSON.stringify({
    username: USERNAME,
    password: PASSWORD,
  }),
  { tags: { name: 'RegisterUser' } }
);

const loginRes = http.post(
  `${BASE_URL}/api/users/token/login`,
  JSON.stringify({
    username: USERNAME,
    password: PASSWORD,
  }),
  { tags: { name: 'Login' } }
);
```

### `script_16.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export const options = {
  vus: 1,
  iterations: 1,
};
```
- **Refactored:**
```js
export const options = {
  vus: 1,
  iterations: 1,
  thresholds: {
    http_req_failed: ['rate<0.01'],   // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests must complete below 500ms
    checks: ['rate>0.99']             // 99% of checks must pass
  },
};
```

---

## `script_17.js`

### `script_17.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
  vus: 500,
  duration: '300s',
};
```
- **Refactored:**
```js
export const options = {
  vus: 500,
  duration: '300s',
  thresholds: {
    'http_req_duration{group:::Login}': ['p(95)<500'],
    'http_req_duration{group:::Navigate}': ['p(95)<1000'],
    'http_req_duration{group:::Logout}': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [13, 16, 24, 27, 30, 35]
- **Snippet:**
```js
const loginPage = http.get(`${BASE_URL}/login`);
const loginAction = http.post(`${BASE_URL}/loginAction`, { ... });
const homePage = http.get(`${BASE_URL}/`);
const categoryPage = http.get(`${BASE_URL}/category`);
const productPage = http.get(`${BASE_URL}/product`);
const logoutAction = http.post(`${BASE_URL}/loginAction?logout=`);
```
- **Refactored:**
```js
const loginPage = http.get(`${BASE_URL}/login`, { tags: { name: 'LoginPage' } });
const loginAction = http.post(`${BASE_URL}/loginAction`, { username: 'user1', password: 'password' }, { tags: { name: 'LoginAction' } });
const homePage = http.get(`${BASE_URL}/`, { tags: { name: 'HomePage' } });
const categoryPage = http.get(`${BASE_URL}/category`, { tags: { name: 'CategoryPage' } });
const productPage = http.get(`${BASE_URL}/product`, { tags: { name: 'ProductPage' } });
const logoutAction = http.post(`${BASE_URL}/loginAction?logout=`, null, { tags: { name: 'LogoutAction' } });
```

### `script_17.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
  vus: 500,
  duration: '300s',
};
```
- **Refactored:**
```js
export const options = {
  vus: 500,
  duration: '300s',
  thresholds: {
    checks: ['rate>0.99'],
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<1000'],
    'http_req_duration{flow:Login}': ['p(95)<500'],
    'http_req_duration{flow:Navigate}': ['p(95)<800'],
    'http_req_duration{flow:Logout}': ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [13, 16, 24, 27, 30, 35]
- **Snippet:**
```js
const loginPage = http.get(`${BASE_URL}/login`);
const loginAction = http.post(`${BASE_URL}/loginAction`, {
  username: 'user1',
  password: 'password',
});
const homePage = http.get(`${BASE_URL}/`);
const categoryPage = http.get(`${BASE_URL}/category`);
const productPage = http.get(`${BASE_URL}/product`);
const logoutAction = http.post(`${BASE_URL}/loginAction?logout=`);
```
- **Refactored:**
```js
const loginPage = http.get(`${BASE_URL}/login`, {
  tags: { name: 'LoginPage', flow: 'Login' },
});

const loginAction = http.post(
  `${BASE_URL}/loginAction`,
  {
    username: 'user1',
    password: 'password',
  },
  {
    tags: { name: 'LoginAction', flow: 'Login' },
  }
);

const homePage = http.get(`${BASE_URL}/`, {
  tags: { name: 'HomePage', flow: 'Navigate' },
});

const categoryPage = http.get(`${BASE_URL}/category`, {
  tags: { name: 'CategoryPage', flow: 'Navigate' },
});

const productPage = http.get(`${BASE_URL}/product`, {
  tags: { name: 'ProductPage', flow: 'Navigate' },
});

const logoutAction = http.post(`${BASE_URL}/loginAction?logout=`, null, {
  tags: { name: 'LogoutAction', flow: 'Logout' },
});
```

### `script_17.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
  vus: 500,
  duration: '300s',
};
```
- **Refactored:**
```js
export const options = {
  vus: 500,
  duration: '300s',
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
    'checks': ['rate>0.99']
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [13, 16, 24, 27, 30, 35]
- **Snippet:**
```js
const loginPage = http.get(`${BASE_URL}/login`);
// ... other requests are also missing tags
```
- **Refactored:**
```js
const loginPage = http.get(`${BASE_URL}/login`, {
  tags: { name: 'GetLoginPage' },
});

// All other http requests should be similarly tagged, for example:
const loginAction = http.post(`${BASE_URL}/loginAction`, 
  {
    username: 'user1',
    password: 'password',
  },
  {
    tags: { name: 'PostLoginAction' },
  }
);
```

---

## `script_19.js`

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
// Keep file open and base64 encoding in init context (this is acceptable),
// but avoid heavy recomputation per VU by ensuring encoding is done once.
// If binFile is large, consider pre-encoding and storing as a static asset.
// The current pattern is borderline acceptable, but encoding.b64encode on a large
// binary file for every VU initialization is costly. Move heavy computation
// outside or cache the result at the module level (already done), which is correct.
// However, if zh.wav is large, consider pre-encoding it offline and loading
// the base64 string directly:
const paddledata = {
  audio: open('./zh_base64.txt'), // pre-encoded offline
  audio_format: "wav",
  sample_rate: 16000,
  lang: "zh_cn",
}
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
  http.post(paddle_model.url, paddle_model.body, paddle_model.params);
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

### `script_19.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [110, 112, 120]
- **Snippet:**
```js
const binFile = open('zh.wav', 'b');
const paddledata = {
  audio: encoding.b64encode(binFile),
  // ...
}
let paddle_model = {
        // ...
        body: JSON.stringify(paddledata),
        // ...
};
```
- **Refactored:**
```js
import { open } from 'k6';
import encoding from 'k6/encoding';

// Use the setup lifecycle function to prepare data once for the entire test.
export function setup() {
  const binFile = open('zh.wav', 'b');
  const paddledata = {
    audio: encoding.b64encode(binFile),
    audio_format: "wav",
    sample_rate: 16000,
    lang: "zh_cn",
  };
  // Pass the processed data to the VU functions.
  return { paddleBody: JSON.stringify(paddledata) }; 
}

// The VU function receives the data prepared in setup().
export function paddle(data) {
  http.post(paddle_model.url, data.paddleBody, paddle_model.params);
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
import { check } from 'k6';

// ... (other functions should also be refactored similarly)

export function shufflenet() {
  const res = http.get(shufflenet_model.url);
  check(res, {
    'shufflenet status is 200': (r) => r.status === 200,
  });
}

export function paddle() {
  const res = http.post(paddle_model.url, paddle_model.body, paddle_model.params);
  check(res, {
    'paddle status is 200': (r) => r.status === 200,
  });
}
```

---

## `script_20.js`

### `script_20.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [14, 15, 16, 17, 18, 19, 20]
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
    'Get_books': ['p(95)<500'],
    'Get_books error': ['rate<0.01'],
    'Add Book': ['p(95)<500'],
    'Add Book error': ['rate<0.01'],
    'Add Order': ['p(95)<500'],
    'Add Order error': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
  }
};
```

### `script_20.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [14, 15, 16, 17, 18, 19, 20]
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
    'http_req_duration{name:Get_books}': ['p(95)<300'],
    'http_req_duration{name:Add Book}': ['p(95)<500'],
    'http_req_duration{name:Add Order}': ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [25, 26, 27, 28, 29, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]
- **Snippet:**
```js
const params = {
  headers: {
    'Content-Type': 'application/json',
  },
};

const requests = {
  'Get_books': {
    method: 'GET',
    url: url +'books',
    params: params,
  },
  'Add Book': {
    method: 'POST',
    url: url+'books',
    params: params,
    body: addBookBody,
  },
  'Add Order': {
    method: 'POST',
    url: url + 'orders?bookIsbn=11111111&firstName=Gaetano',
    params: params,
    body: null
  }
};
```
- **Refactored:**
```js
const baseParams = {
  headers: {
    'Content-Type': 'application/json',
  },
};

const requests = {
  'Get_books': {
    method: 'GET',
    url: url + 'books',
    params: {
      ...baseParams,
      tags: { name: 'Get_books', endpoint: 'GET /books', flow: 'books' },
    },
  },
  'Add Book': {
    method: 'POST',
    url: url + 'books',
    params: {
      ...baseParams,
      tags: { name: 'Add Book', endpoint: 'POST /books', flow: 'books' },
    },
    body: addBookBody,
  },
  'Add Order': {
    method: 'POST',
    url: url + 'orders?bookIsbn=11111111&firstName=Gaetano',
    params: {
      ...baseParams,
      tags: { name: 'Add Order', endpoint: 'POST /orders', flow: 'orders' },
    },
    body: null,
  },
};
```

### `script_20.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [14, 15, 16, 17, 18, 19, 20]
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
    'http_req_duration{name:Get_books}': ['p(95)<200'],
    'http_req_duration{name:Add Book}': ['p(95)<300'],
    'http_req_duration{name:Add Order}': ['p(95)<500'],
    'Get_books error': ['rate<0.01'],
    'Add Book error': ['rate<0.01'],
    'Add Order error': ['rate<0.01']
  }
};
```

---

## `script_21.js`

### `script_21.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [1]
- **Snippet:**
```js
No export const options with thresholds is defined in the provided k6 code.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
    'http_req_duration{name:GetIndex}': ['p(95)<300'],
    'http_req_duration{name:DeleteIndex}': ['p(95)<300'],
    'http_req_duration{name:SaveMovie}': ['p(95)<500'],
    'http_req_duration{name:ListIndices}': ['p(95)<500']
  }
};
```

**Smell 3: Not checking requests**

- **Lines:** [10]
- **Snippet:**
```js
let res = http.get(`${host}/${index}`);
```
- **Refactored:**
```js
let res = http.get(`${host}/${index}`, { tags: { name: 'GetIndex' } });
check(res, {
  'get index status was 200 or 404': (r) => r.status === 200 || r.status === 404
});

if (res.status === 200) {
  res = http.del(`${host}/${index}`, null, { tags: { name: 'DeleteIndex' } });
  check(res, {
    'status was 200': (r) => r.status === 200,
    'Response message 200 OK': (r) => r.status_text === '200 OK'
  });
}
```

**Smell 4: Not using tags**

- **Lines:** [10, 14, 31, 45]
- **Snippet:**
```js
http.get(`${host}/${index}`);
http.del(`${host}/${index}`);
http.post(`${host}/${index}/_doc/${uuidv4()}`, JSON.stringify(movie), { headers: { 'Content-Type': 'application/json' } });
http.get(`${host}/_cat/indices?format=json&pretty=true`);
```
- **Refactored:**
```js
let res = http.get(`${host}/${index}`, { tags: { name: 'GetIndex', endpoint: '/{index}' } });

res = http.del(`${host}/${index}`, null, { tags: { name: 'DeleteIndex', endpoint: '/{index}' } });

let res = http.post(
  `${host}/${index}/_doc/${uuidv4()}`,
  JSON.stringify(movie),
  {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'SaveMovie', endpoint: '/{index}/_doc/{id}' }
  }
);

let res = http.get(`${host}/_cat/indices?format=json&pretty=true`, { tags: { name: 'ListIndices', endpoint: '/_cat/indices' } });
```

### `script_21.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1]
- **Snippet:**
```js
The script does not contain an `export const options` block, and therefore does not define any `thresholds`. Without thresholds, the test will always pass, regardless of the system's performance.
```
- **Refactored:**
```js
import http from 'k6/http';
import { check, fail, group } from 'k6';
import { uuidv4 } from 'https://jslib.k6.io/k6-utils/1.4.0/index.js';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks{group:::Save movies to Elasticsearch}': ['rate>0.99'], // 99% of checks in this group should pass
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [10, 14, 31, 45]
- **Snippet:**
```js
let res = http.get(`${host}/${index}`);
// ...
res = http.del(`${host}/${index}`);
// ...
let res = http.post(`${host}/${index}/_doc/${uuidv4()}`, ...);
// ...
let res = http.get(`${host}/_cat/indices?format=json&pretty=true`);
```
- **Refactored:**
```js
// Refactored deleteIndex function calls:
let res = http.get(`${host}/${index}`, { tags: { name: 'CheckIndexExists' } });
res = http.del(`${host}/${index}`, { tags: { name: 'DeleteIndex' } });

// Refactored saveMovies function call:
let res = http.post(`${host}/${index}/_doc/${uuidv4()}`, JSON.stringify(movie), { 
  headers: { 'Content-Type': 'application/json' },
  tags: { name: 'SaveMovie' } 
});

// Refactored existMovies function call:
let res = http.get(`${host}/_cat/indices?format=json&pretty=true`, { tags: { name: 'CheckIndicesCount' } });
```

---

## `script_22.js`

### `script_22.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [14, 15, 16, 17, 18, 19, 20]
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
    'Get_books': ['p(95)<500'],
    'Get_books error': ['rate<0.01'],
    'Add Book': ['p(95)<500'],
    'Add Book error': ['rate<0.01'],
    'Add Order': ['p(95)<500'],
    'Add Order error': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
  }
};
```

### `script_22.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [14, 15, 16, 17, 18, 19, 20]
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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
    checks: ['rate>0.95'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [25, 26, 27, 28, 29, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58]
- **Snippet:**
```js
const params = {
  headers: {
    'Content-Type': 'application/json',
  },
};

const requests = {
  'Get_books': {
    method: 'GET',
    url: url +'books',
    params: params,
  },
  'Add Book': {
    method: 'POST',
    url: url+'books',
    params: params,
    body: addBookBody,
  },
  'Add Order': {
    method: 'POST',
    url: url + 'orders?bookIsbn=11111111&firstName=Gaetano',
    params: params,
    body: null
  }
};

const responses = http.batch(requests);
```
- **Refactored:**
```js
const baseHeaders = {
  'Content-Type': 'application/json',
};

const requests = {
  'Get_books': {
    method: 'GET',
    url: url + 'books',
    params: {
      headers: baseHeaders,
      tags: { name: 'Get_books', endpoint: 'books', operation: 'get_books' },
    },
  },
  'Add Book': {
    method: 'POST',
    url: url + 'books',
    params: {
      headers: baseHeaders,
      tags: { name: 'Add Book', endpoint: 'books', operation: 'add_book' },
    },
    body: addBookBody,
  },
  'Add Order': {
    method: 'POST',
    url: url + 'orders?bookIsbn=11111111&firstName=Gaetano',
    params: {
      headers: baseHeaders,
      tags: { name: 'Add Order', endpoint: 'orders', operation: 'add_order' },
    },
    body: null,
  },
};

const responses = http.batch(requests);
```

### `script_22.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [14, 15, 16, 17, 18, 19, 20]
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
    'http_req_failed': ['rate<0.01'],             // http errors should be less than 1%
    'http_req_duration{name:Get_books}': ['p(95)<200'], // 95% of requests for Get_books must be below 200ms
    'http_req_duration{name:Add Book}': ['p(95)<300'],   // 95% of requests for Add Book must be below 300ms
    'http_req_duration{name:Add Order}': ['p(95)<300'],  // 95% of requests for Add Order must be below 300ms
    'Get_books error': ['rate<0.01'],
    'Add Book error': ['rate<0.01'],
    'Add Order error': ['rate<0.01']
  }
};
```

---

## `script_23.js`

### `script_23.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [37]
- **Snippet:**
```js
file: http.file('D:/Document/Semester 8/SQA/swagger-petstore-sqa/pet_s3/cat.jpeg'),
```
- **Refactored:**
```js
// In init context (outside default function), preload the file once:
const imageFile = open('D:/Document/Semester 8/SQA/swagger-petstore-sqa/pet_s3/cat.jpeg', 'b');

export default function () {
  let baseUrl = 'https://petstore.swagger.io/v2/pet';
  const petId = __VU;
  const url = `${baseUrl}/${petId}/uploadImage`;

  const payload = {
    file: http.file(imageFile, 'cat.jpeg', 'image/jpeg'),
    additionalMetadata: `Metadata for pet ${petId}`,
  };
  // ... rest of the function
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
    http_req_duration: ['p(95)<1000'],
    http_req_failed: ['rate<0.1'],
    'checks{check:✅ Status is 200 (Success)}': ['rate>0.9'],
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
  tags: { name: 'UploadPetImage', endpoint: 'uploadImage' },
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
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<1000'],
    'http_req_duration{name:UploadImage}': ['p(95)<1000'],
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
const params = {
  tags: {
    name: 'UploadImage',
    endpoint: '/pet/{petId}/uploadImage',
    flow: 'pet_image_upload',
  },
};

res = http.post(url, payload, params);

check(res, {
  'status is 200': (r) => r.status === 200,
  'response time < 1000ms': (r) => r.timings.duration < 1000,
}, params.tags);
```

### `script_23.js` — GEMINI

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
    'http_req_failed': ['rate<0.1'],   // http errors should be less than 10%
    'http_req_duration': ['p(95)<2000'], // 95% of requests should be below 2s
    'checks': ['rate>0.95'],             // 95% of checks must pass
    'total_failures': ['count<10']      // custom metric: total failures should be less than 10
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
const params = {
  tags: {
    name: 'UploadPetImage',
  },
};
res = http.post(url, payload, params);
```

---

## `script_24.js`

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
    'http_req_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
    'checks': ['rate>0.99'],
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
let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, { headers: headers });
check(verifyOTPres, {
  'verifyOTP status is 200': (r) => r.status === 200,
  'verifyOTP response time < 200ms': (r) => r.timings.duration < 200,
});
...
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
...
let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, { headers: headers });
...
let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, { headers: headers });
```
- **Refactored:**
```js
let userExistRes = http.post(`${baseUrl}/v1/userExists`, userExistsJSON, {
  headers: headers,
  tags: { name: 'UserExists' },
});
...
let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, {
  headers: headers,
  tags: { name: 'VerifyOTP' },
});
...
let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
  headers: headers,
  tags: { name: 'Signup' },
});
```

### `script_24.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
- **Snippet:**
```js
export let options = {
	//executor: 'shared-iterations',
	// iterations: 100,
	// vus: 100,
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
    checks: ['rate>0.99'],
    'http_req_duration{name:UserExists}': ['p(95)<200'],
    'http_req_duration{name:VerifyOTP}': ['p(95)<200'],
    'http_req_duration{name:Signup}': ['p(95)<500'],
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
  tags: { name: 'VerifyOTP' },
});

check(verifyOTPres, {
  'verify OTP status is 200': (r) => r.status === 200,
  'verify OTP response status is OK': (r) => r.json().status === 'OK',
});

let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
  headers: headers,
  tags: { name: 'Signup' },
});

check(signUpRes, {
  'signup status is 200': (r) => r.status === 200,
  'signup returns access token': (r) => Boolean(r.json().data.token.access_token),
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
  tags: { name: 'UserExists', flow: 'Signup' },
});

let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, {
  headers: headers,
  tags: { name: 'VerifyOTP', flow: 'Signup' },
});

let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
  headers: headers,
  tags: { name: 'Signup', flow: 'Signup' },
});
```

### `script_24.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [14, 23]
- **Snippet:**
```js
export let options = {
	//executor: 'shared-iterations',
	// iterations: 100,
	// vus: 100,
	stages: [
        // Ramp up to 1 VUs for 5 second
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
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [76, 84]
- **Snippet:**
```js
let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, {
    headers: headers});
// ...
let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
    headers: headers});
```
- **Refactored:**
```js
// ...
let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, {
    headers: headers});
check(verifyOTPres, { 'verify OTP status is 200': (r) => r.status === 200 });
// ...
let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
    headers: headers});
check(signUpRes, { 'signup status is 200': (r) => r.status === 200 });
// ...
```

**Smell 4: Not using tags**

- **Lines:** [60, 76, 84]
- **Snippet:**
```js
let userExistRes = http.post(`${baseUrl}/v1/userExists`, userExistsJSON, {
    headers: headers
});
// ...
let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, {
    headers: headers});
// ...
let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
    headers: headers});
```
- **Refactored:**
```js
let userExistRes = http.post(`${baseUrl}/v1/userExists`, userExistsJSON, {
    headers: headers,
    tags: { name: 'UserExists' },
});
// ...
let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, {
    headers: headers,
    tags: { name: 'VerifyOTP' },
});
// ...
let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
    headers: headers,
    tags: { name: 'Signup' },
});
```

---

## `script_25.js`

### `script_25.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [26, 28, 30]
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
    checks: ['rate>0.99'],
    latency_trend: ['p(95)<500'],
    received_updates: ['count>0'],
    ws_connecting: ['p(95)<1000'],
  },
  summaryTrendStats: trends,
  scenarios: {
    replication: scenario(baseDuration, conns),
  },
}
```

**Smell 4: Not using tags**

- **Lines:** [38, 126, 144, 145, 147, 163]
- **Snippet:**
```js
const res = ws.connect(URL, {}, (socket) => {
...
check(msg, {
  'subscribed to realtime': (msg) =>
    msg.topic === 'realtime:any' && msg.payload.status === 'ok',
})
...
latencyTrend.add(now - updated, { type: type })
counterReceived.add(1)
...
check(res, { 'status is 101': (r) => r && r.status === 101 })
```
- **Refactored:**
```js
const wsTags = { flow: 'replication', endpoint: 'realtime_websocket' }

const res = ws.connect(URL, { tags: wsTags }, (socket) => {
  socket.on('message', (msg) => {
    const now = Date.now()
    msg = JSON.parse(msg)

    if (msg.event === 'system') {
      check(
        msg,
        {
          'subscribed to realtime': (msg) =>
            msg.topic === 'realtime:any' && msg.payload.status === 'ok',
        },
        { ...wsTags, event: 'system' }
      )
    }

    if (msg.event !== 'postgres_changes') {
      return
    }

    const type = msg.payload.type
    const updated = msg.payload.data.record
      ? Date.parse(msg.payload.data.record.created_at)
      : new Date(msg.payload.data.commit_timestamp)

    latencyTrend.add(now - updated, { ...wsTags, type })
    counterReceived.add(1, { ...wsTags, type })

    check(
      msg,
      {
        'got realtime notification': (msg) => msg.topic === 'realtime:any',
      },
      { ...wsTags, event: 'postgres_changes', type }
    )
  })
})

check(res, { 'status is 101': (r) => r && r.status === 101 }, wsTags)
```

### `script_25.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [26, 30]
- **Snippet:**
```js
const to = {}

export const options = {
  ...
  thresholds: to,
```
- **Refactored:**
```js
export const options = {
  vus: 1,
  thresholds: {
    'latency_trend': ['p(95)<500'], // 95% of messages should have latency under 500ms
    'checks': ['rate>0.99'] // Over 99% of checks must pass
  },
  summaryTrendStats: trends,
  scenarios: {
    replication: scenario(baseDuration, conns),
  },
}
```

---

## `script_26.js`

### `script_26.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1]
- **Snippet:**
```js
// The 'export const options' block with thresholds is missing from the script.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
};

// ... rest of the script
```

**Smell 4: Not using tags**

- **Lines:** [1003, 1031]
- **Snippet:**
```js
function executeRequest({
  name,
  // ...
  tags,
  // ...
}) {
  try {
    // ...
    const config = makeRequestConfig(
      method,
      address,
      data,
      headers,
      options,
      tags // The 'name' is not automatically used as a tag
    );
    // ...
    const response = http.request(...args);
    // ...
  } finally {
    // ...
  }
}
```
- **Refactored:**
```js
function executeRequest({
  name,
  id = guid(),
  method,
  address,
  data,
  headers,
  options,
  tags,
  pre,
  auth,
  post,
}) {
  try {
    enterRequest(name, id, method, address, data, headers);
    executePrerequest(postman[Pre], pre);

    // Automatically add the request name as a tag for better metric filtering.
    const requestTags = Object.assign({ name: name }, tags);

    const config = makeRequestConfig(
      method,
      address,
      data,
      headers,
      options,
      requestTags // Pass the enhanced tags object
    );
    if (auth) {
      auth(config, Var);
    }
    const args = makeRequestArgs(config);
    const response = http.request(...args);
    if (post) {
      enterPost(response);
      executePostrequest(postman[Post], post, response);
      executeTests();
    }
    return response;
  } finally {
    exitRequest();
  }
}
```

---

## `script_27.js`

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
        http_req_duration: ['p(95)<1000', 'p(99)<2000'],
        http_req_failed: ['rate<0.05'],
        'check_success': ['count>0'],
        'check_fail_500': ['count<10'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [42]
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
        name: 'UserLogin',
        endpoint: '/v2/user/login'
    }
};

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
        'http_req_duration{name:UserLogin}': ['p(95)<1000'],
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
        endpoint: '/v2/user/login'
    }
};

res = http.get(url, params);
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
        'http_req_failed': ['rate<0.01'], // fail if more than 1% of requests fail
        'http_req_duration': ['p(95)<1500'], // 95% of requests must complete below 1.5s
        'checks': ['rate>0.99'], // over 99% of checks must pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [42]
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
        name: 'UserLogin',
    },
};

let res;

try {
    res = http.get(url, params);
} catch (error) {
    // ...
```

---

## `script_28.js`

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
// Reading and parsing the file is unavoidable in init, but the mapping/filtering
// can be made more efficient. Also, creating 150 custom metric objects in a loop
// is a heavy init-context operation. Consider reducing MAX_PANEL_ID or lazily
// initializing metrics only for panels actually encountered at runtime.

// Efficient file parsing (still in init, but keep it lean):
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n').filter(line => line.trim().length > 0);
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

// Instead of pre-creating 150 metric objects, create them lazily inside default():
// const panelMetrics = {}; // keep empty at init
// Then inside default function, when a panelId is encountered:
// if (!panelMetrics[panelId]) {
//     panelMetrics[panelId] = {
//         responseTime: new Trend(`panel_response_time_${panelId}`, true),
//         successRate: new Rate(`panel_success_rate_${panelId}`, true),
//         failureRate: new Rate(`panel_failure_rate_${panelId}`, true)
//     };
// }
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
    // no thresholds defined
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
        'dashboard_success_rate': ['rate>0.99'],
        'http_req_duration_custom': ['p(95)<2000'],
        'http_req_failed': ['rate<0.01']
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
export function setup() {
  const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
  const users = usersRaw.map(line => {
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    return { username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10) };
  }).filter(u => u.vunetSession && u.xVuNetHTTPInfo && u.grafanaSessionExpiry);
  
  if (users.length === 0) {
    throw new Error('No valid users found in user_cookies.txt!');
  }
  return { users: users };
}

// Note: `vus` and `iterations` in the options block must now be set explicitly, 
// as `users.length` is no longer available in the init context.

// In the default function, access users via the 'data' parameter:
export default function (data) {
  let user = data.users[__VU - 1];
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
        'http_req_failed': ['rate<0.01'], // less than 1% failed requests
        'http_req_duration': ['p(95)<2000'], // 95% of requests must complete below 2s
        'dashboard_response_time': ['p(95)<1000'], // 95% of dashboard requests < 1s
        'checks': ['rate>0.99'] // 99% of checks must pass
    }
};
```

---

## `script_29.js`

### `script_29.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 51, 52, 53, 54, 55, 56, 57]
- **Snippet:**
```js
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = usersRaw.map(line => {
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    return { ... };
}).filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);

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
// Keep open() in init context (it is allowed), but minimise heavy processing.
// Parse lazily inside default function or limit metric instantiation to actually
// discovered panel IDs rather than pre-creating 100 metric objects.

// Init context — lightweight
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
// Defer heavy map/filter to setup() so it runs only once for the whole test,
// not once per VU.
export function setup() {
    const users = usersRaw
        .filter(line => line.trim().length > 0)
        .map(line => {
            const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
            return { username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10) };
        })
        .filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
    if (users.length === 0) {
        throw new Error('No valid users found in user_cookies.txt!');
    }
    return { users };
}

// Remove the pre-created 100-metric loop from init context.
// Create panel metrics on-demand inside the default function instead,
// or use a single tagged Trend/Rate covering all panels.
const panelResponseTime = new Trend('panel_response_time', true);
const panelSuccessRate  = new Rate('panel_success_rate', true);
const panelFailureRate  = new Rate('panel_failure_rate', true);

export default function (data) {
    const user = data.users[__VU - 1];
    // ... rest of the test logic unchanged, using panelResponseTime etc.
    //     with panelId tag instead of per-panel metric objects.
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
    // no thresholds defined
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
        // Overall HTTP request duration
        'http_req_duration': ['p(95)<2000', 'p(99)<5000'],
        // Custom dashboard response time
        'dashboard_response_time': ['p(95)<2000'],
        // Dashboard must succeed at least 99 % of the time
        'dashboard_success_rate': ['rate>0.99'],
        // Per-panel success rate
        'panel_success_rate': ['rate>0.95'],
        // No more than 5 % failures across all panel requests
        'panel_failure_rate': ['rate<0.05']
    }
};
```

### `script_29.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
- **Snippet:**
```js
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = usersRaw.map(line => {
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    return { username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10) };
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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<1000'],
        dashboard_success_rate: ['rate>0.99'],
        dashboard_response_time: ['p(95)<1000'],
        http_req_duration_custom: ['p(95)<1000']
    }
};
```

### `script_29.js` — GEMINI

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
/* Move data loading to the setup function, which runs only once for the entire test. */
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
  return { users: users };
}

/* The default function now receives the data from setup() as an argument. */
export default function (data) {
    if (__VU > data.users.length) {
        // Avoids errors if vus > number of users in the file.
        return;
    }
    let user = data.users[__VU - 1];
    // ... rest of the VU code
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
        'http_req_failed': ['rate<0.01'], // Global HTTP error rate should be less than 1%
        'dashboard_success_rate': ['rate>0.99'], // Dashboard metadata success rate > 99%
        'dashboard_response_time': ['p(95)<800'], // 95% of dashboard metadata requests < 800ms
        'panel_response_time_*': ['p(95)<1500'] // 95% of all panel requests < 1500ms
    }
};
```

---

## `script_30.js`

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
        http_req_duration: ['p(95)<1000'],
        http_req_failed: ['rate<0.1'],
        'total_failures': ['count<10'],
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
    tags: { name: 'UserLogout' }
};
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
        checks: ['rate>0.95'],
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
        endpoint: '/v2/user/logout',
        flow: 'logout'
    }
};

res = http.get(url, params);
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
        'http_req_failed': ['rate<0.05'],   // 5% max error rate
        'http_req_duration': ['p(95)<1500'], // 95% of requests must complete below 1.5s
        'checks{name:"✅ Status is 200 (Success)"}': ['rate>0.95'], // 95% of checks for success must pass
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
        name: 'Logout',
    },
};

let res;
// ...
res = http.get(url, params);
```

---

## `script_31.js`

### `script_31.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [14]
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
    'http_req_duration{name:DeleteStore}': ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [28, 62]
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
  tags: { name: 'CreateStore', endpoint: 'stores', flow: 'setup' },
});

const created = check(res, {
  'store created successfully': (r) => r.status === 200,
});

if (created) {
  stores.push(store);
}

export function teardown(data) {
  for (const store of data.stores) {
    const res = http.del(`${url}/${store.id}`, null, {
      tags: { name: 'CleanupStore', endpoint: 'stores', flow: 'teardown' },
    });

    check(res, {
      'store cleanup status is 200 or 404': (r) => r.status === 200 || r.status === 404,
    });
  }
}
```

**Smell 4: Not using tags**

- **Lines:** [28, 50, 62]
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
const createStoreParams = {
  headers: { 'Content-Type': 'application/json' },
  tags: { name: 'CreateStore', endpoint: 'stores', flow: 'setup' },
};
const res = http.post(`${url}`, JSON.stringify(store), createStoreParams);

const deleteStoreParams = {
  tags: { name: 'DeleteStore', endpoint: 'stores', flow: 'delete-store' },
};
const res = http.del(`${url}/${store.id}`, null, deleteStoreParams);

const cleanupStoreParams = {
  tags: { name: 'CleanupStore', endpoint: 'stores', flow: 'teardown' },
};
const cleanupRes = http.del(`${url}/${store.id}`, null, cleanupStoreParams);
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
import { test_options } from './options.js';

export let options = {
  ...test_options, // Spread existing options from the import
  thresholds: {
    'http_req_failed': ['rate<0.01'],    // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'],  // 95% of requests must be below 500ms
    'checks': ['rate>0.99']             // 99% of checks must pass
  }
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
export function teardown(stores) {
    for (const store in stores) {
        const res = http.del(`${url}/${store.id}`);
        check(res, {
            'teardown: delete status is 200': (r) => r.status === 200,
        });
    }
}
```

**Smell 4: Not using tags**

- **Lines:** [28, 50, 62]
- **Snippet:**
```js
const res = http.del(`${url}/${store.id}`);
```
- **Refactored:**
```js
const params = {
  tags: {
    name: 'DeleteStore', // Descriptive name for the request
  },
};
const res = http.del(`${url}/${store.id}`, null, params);
```

---

## `script_32.js`

### `script_32.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 81, 82, 83, 84, 85, 86, 87]
- **Snippet:**
```js
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = usersRaw.map(line => {
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
// Reading and parsing the file is acceptable in init context (open() is init-only),
// but the heavy map/filter/split chain and the loop creating 150 metric objects
// should be kept minimal. Pre-parse only what is strictly necessary and consider
// lazily creating panel metrics inside the VU function only for panel IDs actually used.

// Optimised init context:
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n').filter(line => line.trim() !== '');
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

// Instead of pre-creating 150 Trend/Rate objects (heavy loop in init),
// create metrics lazily or limit to a known set of panel IDs:
const panelMetrics = {};
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
    // no thresholds defined
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
        // Overall dashboard metadata request must respond within 2s at p95
        'dashboard_response_time': ['p(95)<2000'],
        // At least 95% of dashboard requests must succeed
        'dashboard_success_rate': ['rate>0.95'],
        // Overall HTTP request duration p95 under 3s
        'http_req_duration': ['p(95)<3000'],
        // Custom combined duration metric
        'http_req_duration_custom': ['p(95)<3000'],
        // User success vs failure ratio
        'user_failure_count': ['count<10']
    }
};
```

### `script_32.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 81, 82, 83, 84, 85, 86, 87]
- **Snippet:**
```js
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = usersRaw.map(line => {
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    return { username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10) };
}).filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);

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

// Use generic panel metrics with tags instead of creating hundreds of metrics in init.
const panelResponseTime = new Trend('panel_response_time', true);
const panelSuccessRate = new Rate('panel_success_rate', true);
const panelFailureRate = new Rate('panel_failure_rate', true);

// Later inside the panel request loop:
panelResponseTime.add(panelRes.timings.duration, panelTags);
panelSuccessRate.add(panelRes.status === 200, panelTags);
panelFailureRate.add(panelRes.status !== 200, panelTags);
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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<1000'],
        dashboard_success_rate: ['rate>0.95'],
        dashboard_response_time: ['p(95)<2000'],
        panel_success_rate: ['rate>0.95'],
        panel_response_time: ['p(95)<3000']
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

const users = new SharedArray('all-users', function () {
    // This function is executed only once, and the result is shared among all VUs.
    return open('/home/vunet/user_creation_k6/user_cookies.txt')
        .split('\n')
        .map(line => {
            const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
            return { username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10) };
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
        'http_req_failed': ['rate<0.01'],      // http errors should be less than 1%
        'http_req_duration': ['p(95)<2000'],    // 95% of requests should be below 2s
        'checks': ['rate>0.99'],               // 99% of checks must pass
        'dashboard_response_time': ['p(95)<2500'], // 95% of main dashboard requests < 2.5s
    }
};
```

---

## `script_33.js`

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
        http_req_duration: ['p(95)<1000'],
        http_req_failed: ['rate<0.1'],
        'check_success': ['count>0'],
        'check_fail_500': ['count<10'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [52]
- **Snippet:**
```js
res = http.put(url, payload, params);
```
- **Refactored:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    },
    tags: { name: 'UpdateUser' },
};

res = http.put(url, payload, params);
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
        'http_req_duration{name:UpdateUser}': ['p(95)<1000'],
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
        endpoint: '/v2/user/{username}',
        method: 'PUT'
    }
};

res = http.put(url, payload, params);
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
        'http_req_failed': ['rate<0.01'],   // Fail if error rate is > 1%
        'http_req_duration': ['p(95)<1500'], // 95% of requests must be below 1.5s
        'checks': ['rate>0.99'],           // 99% of checks must pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [52]
- **Snippet:**
```js
res = http.put(url, payload, params);
```
- **Refactored:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    },
    tags: {
        name: 'UpdateUser', // Add a tag for better metric filtering
    },
};

let res;
// ...
    res = http.put(url, payload, params);
```

---

## `script_34.js`

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
        http_req_duration: ['p(95)<1000', 'p(99)<2000'],
        http_req_failed: ['rate<0.05'],
        'total_failures': ['count<10'],
        'check_slow_response': ['count<50'],
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
res = http.get(url, { tags: { name: 'GetStoreOrder', endpoint: 'store/order' } });
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
        http_req_duration: ['p(95)<1000'],
        total_failures: ['count<1'],
        check_slow_response: ['count<10'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [36, 65]
- **Snippet:**
```js
res = http.get(url);
...
check(res, {
    '✅ Status is 200 (Success)': (r) => { ... }
});
```
- **Refactored:**
```js
const requestTags = {
    name: 'GetOrder',
    endpoint: '/v2/store/order/:orderId',
    flow: 'order_lookup',
};

res = http.get(url, { tags: requestTags });

check(res, {
    '✅ Status is 200 (Success)': (r) => {
        let result = r.status === 200;
        if (result) checkSuccess.add(1, requestTags);
        return result;
    },
    '❌ Status is 400 (Bad Request)': (r) => {
        let result = r.status === 400;
        if (result) checkFail400.add(1, requestTags);
        return result;
    },
    '⚠️ Status is 429 (Rate Limit Exceeded)': (r) => {
        let result = r.status === 429;
        if (result) checkFail429.add(1, requestTags);
        return result;
    },
    '🔥 Status is 500 (Server Error)': (r) => {
        let result = r.status === 500;
        if (result) checkFail500.add(1, requestTags);
        return result;
    },
    '⚡ Unexpected Error (Other)': (r) => {
        let result = ![200, 400, 404, 429, 500].includes(r.status);
        if (result) checkUnexpectedError.add(1, requestTags);
        return result;
    },
    '⏱️ Response time > 1000ms (Slow)': (r) => {
        let result = r.timings.duration >= 1000;
        if (result) checkSlowResponse.add(1, requestTags);
        return result;
    },
}, requestTags);
```

### `script_34.js` — GEMINI

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
        'http_req_failed': ['rate<0.05'], // fail if more than 5% of requests error out
        'http_req_duration': ['p(95)<2000'], // 95% of requests must complete below 2s
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
        name: 'GetOrder',
    },
});
```

---

## `script_35.js`

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
    'http_req_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
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
// First loop (chunks 1-5, no sleep — initial burst)
const res = http.get(videoPath + String(i).padStart(5, '0') + '.ts', {
  tags: { name: 'VideoChunkInitial', chunk: String(i) },
});

// Second loop (chunks 6-11, with sleep — simulated playback)
const res = http.get(videoPath + String(i).padStart(5, '0') + '.ts', {
  tags: { name: 'VideoChunkPlayback', chunk: String(i) },
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
    http_req_duration: ['p(95)<1000'],
    checks: ['rate>0.95'],
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
const videoChunkParams = {
  tags: {
    name: 'VideoChunk',
    flow: 'video_stream',
    quality: '1080p',
  },
};

const res = http.get(videoPath + String(i).padStart(5, '0') + '.ts', videoChunkParams);
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
    'http_req_duration': ['p(95)<1000'], // 95% of requests should be below 1000ms
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
export default function() { // What the VU does:
  for (let i = 1; i <= 5; i++) {
    const res = http.get(videoPath + String(i).padStart(5, '0') + '.ts', {
      tags: { name: 'InitialChunks' },
    });
    check(res, {
      'is status 200': (r) => r.status === 200,
      'is video chunk loaded': (r) => r.body.length > 0,
      'is video chunk cached': (r) => r.headers['X-Cache'] === 'Hit from cloudfront',
    });
  }
  for (let i = 6; i <= 11; i++) {
    sleep(3);
    const res = http.get(videoPath + String(i).padStart(5, '0') + '.ts', {
      tags: { name: 'ChunksAfterPause' },
    });
    check(res, {
      'is status 200': (r) => r.status === 200,
      'is video chunk loaded': (r) => r.body.length > 0,
      'is video chunk cached': (r) => r.headers['X-Cache'] === 'Hit from cloudfront',
    });
  }
}
```

---

## `script_36.js`

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
// Reading and parsing the file is unavoidable in init, but the parsing logic
// should be kept minimal and the heavy metric creation loop should be deferred
// or reduced. For example, limit MAX_PANEL_ID or create metrics lazily:

const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = usersRaw
    .filter(line => line.trim().length > 0)
    .map(line => {
        const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
        return { username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10) };
    })
    .filter(user => user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);

// Instead of pre-creating 150 Trend/Rate objects unconditionally,
// create them lazily inside the default function only for panel IDs actually encountered:
const panelMetrics = {};

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
    // no thresholds defined
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

- **Lines:** [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 81, 82, 83, 84, 85, 86, 87]
- **Snippet:**
```js
const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = usersRaw.map(line => { ... }).filter(...);

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

// Use a small number of tagged metrics instead of creating one metric per panel.
const panelResponseTime = new Trend('panel_response_time', true);
const panelSuccessRate = new Rate('panel_success_rate', true);
const panelFailureRate = new Rate('panel_failure_rate', true);

// Later, inside the panel request loop:
panelResponseTime.add(panelRes.timings.duration, panelTags);
panelSuccessRate.add(panelRes.status === 200, panelTags);
panelFailureRate.add(panelRes.status !== 200, panelTags);
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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<1000'],
        dashboard_success_rate: ['rate>0.99'],
        dashboard_response_time: ['p(95)<1000'],
        panel_success_rate: ['rate>0.99'],
        panel_response_time: ['p(95)<2000']
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
// Move data loading and processing to the setup function, which runs only once for the entire test.
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
        throw new Error('🚨 No valid users found in user_cookies.txt!');
    }
    return { users }; // Pass the processed users data to the VUs
}

// The main function receives the data from setup.
export default function (data) {
    // Access the user data for the current VU from the data object passed by setup.
    let user = data.users[__VU - 1];

    // ... rest of the function remains the same
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
    // Add thresholds to define success criteria for the test.
    thresholds: {
        'http_req_failed': ['rate<0.01'],    // http errors should be less than 1%
        'http_req_duration': ['p(95)<2000'], // 95% of requests must complete below 2s
        'dashboard_success_rate': ['rate>0.95'], // custom metric: dashboard success rate > 95%
        'checks': ['rate>0.98']              // 98% of all checks must pass
    }
};
```

---

## `script_37.js`

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

- **Lines:** [25, 26, 27, 28, 29, 30, 31, 33]
- **Snippet:**
```js
const requests = {
      'Get_books': {
        method: 'GET',
        url: url +'books/simple',
        params: params,
      }
    };

  const responses = http.batch(requests);
```
- **Refactored:**
```js
const params = {
    headers: {
      'Content-Type': 'application/json',
    },
    tags: { name: 'Get_books' },
  };

  const requests = {
      'Get_books': {
        method: 'GET',
        url: url + 'books/simple',
        params: params,
      }
    };

  const responses = http.batch(requests);
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
    { duration: '10s', target: Number(__ENV.USERS) },
    { duration: '100s', target: Number(__ENV.USERS) },
    { duration: '10s', target: 0 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    'http_req_duration{name:Get_books}': ['p(95)<500'],
    'Get_books error': ['rate<0.01'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 36, 40]
- **Snippet:**
```js
const params = {
  headers: {
    'Content-Type': 'application/json',
  },
};

const requests = {
  'Get_books': {
    method: 'GET',
    url: url +'books/simple',
    params: params,
  }
};

check(getResp, {
  'status is 200': (r) => r.status === 200,
}) || getErrorRate.add(1);

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
    endpoint: 'books/simple',
    flow: 'books',
  },
};

const requests = {
  Get_books: {
    method: 'GET',
    url: `${url}books/simple`,
    params,
  },
};

const responses = http.batch(requests);
const getResp = responses.Get_books;

check(getResp, {
  'status is 200': (r) => r.status === 200,
}, { name: 'Get_books', endpoint: 'books/simple', flow: 'books' }) || getErrorRate.add(1, { name: 'Get_books', endpoint: 'books/simple', flow: 'books' });

getTrend.add(getResp.timings.duration, { name: 'Get_books', endpoint: 'books/simple', flow: 'books' });
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
    'Get_books error': ['rate<0.01'], // Error rate should be less than 1%
    'Get_books': ['p(95)<500'],      // 95th percentile of response time should be below 500ms
    'http_req_failed': ['rate<0.01'] // Global HTTP failure rate should be less than 1%
  }
};
```

---

## `script_38.js`

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
    'Get_Orders_Async': ['p(95)<500'],
    'Get_Orders_Async_error': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [25, 26, 27, 28, 29, 30, 31, 33]
- **Snippet:**
```js
const requests = {
    'Get_Orders_Async': {
      method: 'GET',
      url: url +'api/orders/async/1',
      params: params,
    }
  };
const responses = http.batch(requests);
```
- **Refactored:**
```js
const params = {
  headers: {
    'Content-Type': 'application/json',
  },
  tags: { name: 'Get_Orders_Async' },
};

const requests = {
    'Get_Orders_Async': {
      method: 'GET',
      url: url + 'api/orders/async/1',
      params: params,
    }
  };
const responses = http.batch(requests);
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
    checks: ['rate==1'],
    http_req_failed: ['rate<0.01'],
    'http_req_duration{name:Get_Orders_Async}': ['p(95)<500'],
    Get_Orders_Async_error: ['rate<0.01'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 33]
- **Snippet:**
```js
const params = {
  headers: {
    'Content-Type': 'application/json',
  },
};

const requests = {
  'Get_Orders_Async': {
    method: 'GET',
    url: url +'api/orders/async/1',
    params: params,
  }
};

const responses = http.batch(requests);
```
- **Refactored:**
```js
const params = {
  headers: {
    'Content-Type': 'application/json',
  },
  tags: {
    name: 'Get_Orders_Async',
    endpoint: 'orders_async',
    flow: 'orders',
  },
};

const requests = {
  Get_Orders_Async: {
    method: 'GET',
    url: `${url}api/orders/async/1`,
    params,
  },
};

const responses = http.batch(requests);
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
      'Get_Orders_Async_error': ['rate<0.01'], // Error rate should be less than 1%
      'Get_Orders_Async': ['p(95)<500'], // 95% of requests should be below 500ms
  }
};
```

---

## `script_39.js`

### `script_39.js` — CLAUDE

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
import { check } from 'k6';

const auth_resp = http.post('https://test-api.k6.io/auth/token/login/', {
  username: 'test-user',
  password: 'supersecure',
});
check(auth_resp, {
  'auth status is 200': (r) => r.status === 200,
});
if (auth_resp.status >= 400) {
  allErrors.add(1, { errorType: 'authError' });
}

const other_resp = http.get('https://test-api.k6.io/public/crocodiles/1/');
check(other_resp, {
  'crocodiles status is 200': (r) => r.status === 200,
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
  { tags: { name: 'AuthLogin' } }
);

const other_resp = http.get(
  'https://test-api.k6.io/public/crocodiles/1/',
  { tags: { name: 'GetCrocodile' } }
);
```

### `script_39.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [29, 39, 42]
- **Snippet:**
```js
const auth_resp = http.post('https://test-api.k6.io/auth/token/login/', {
  username: 'test-user',
  password: 'supersecure',
});

const other_resp = http.get('https://test-api.k6.io/public/crocodiles/1/');
...
allErrors.add(1); // untagged value
```
- **Refactored:**
```js
export default function () {
  const auth_resp = http.post(
    'https://test-api.k6.io/auth/token/login/',
    {
      username: 'test-user',
      password: 'supersecure',
    },
    { tags: { name: 'AuthLogin', endpoint: 'auth_token_login' } }
  );
  console.log('auth_resp', auth_resp.status);

  if (auth_resp.status >= 400) {
    allErrors.add(1, { errorType: 'authError', endpoint: 'auth_token_login' });
  }

  const other_resp = http.get(
    'https://test-api.k6.io/public/crocodiles/1/',
    { tags: { name: 'GetCrocodileById', endpoint: 'public_crocodiles_1' } }
  );
  console.log('other_resp', other_resp.status);

  if (other_resp.status >= 400) {
    allErrors.add(1, { errorType: 'publicApiError', endpoint: 'public_crocodiles_1' });
  }

  sleep(1);
}
```

### `script_39.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [29, 39]
- **Snippet:**
```js
const auth_resp = http.post('https://test-api.k6.io/auth/token/login/', {
  username: 'test-user',
  password: 'supersecure',
});
// ...
const other_resp = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
const auth_resp = http.post(
  'https://test-api.k6.io/auth/token/login/',
  {
    username: 'test-user',
    password: 'supersecure',
  },
  { tags: { name: 'Auth' } }
);

// ...

const other_resp = http.get('https://test-api.k6.io/public/crocodiles/1/', {
  tags: { name: 'GetCrocodile' },
});
```

---

## `script_40.js`

### `script_40.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [18, 22]
- **Snippet:**
```js
let res = http.get('https://quickpizza.grafana.com/test.k6.io/');
    res = http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
import { check } from 'k6';

export default function () {
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
}
```

**Smell 4: Not using tags**

- **Lines:** [18, 22]
- **Snippet:**
```js
let res = http.get('https://quickpizza.grafana.com/test.k6.io/');
    res = http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
export const options = {
    vus: 5,
    duration: '5s',
    thresholds: {
        'http_req_duration{name:HomePage}': ['p(95)<250'],
        'http_req_duration{name:NewsPage}': ['p(95)<250'],
        my_counter: ['count>10']
    }
};

export default function () {
    let res = http.get('https://quickpizza.grafana.com/test.k6.io/', { tags: { name: 'HomePage' } });
    check(res, { 'home page status is 200': (r) => r.status === 200 });
    myCounter.add(1);
    sleep(1);

    res = http.get('https://quickpizza.grafana.com/news.php', { tags: { name: 'NewsPage' } });
    check(res, { 'news page status is 200': (r) => r.status === 200 });
    newsPageResponseTrend.add(res.timings.duration);
    sleep(1);
}
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
    });
    myCounter.add(1);
    sleep(1);

    res = http.get('https://quickpizza.grafana.com/news.php');
    check(res, {
        'news page status is 200': (r) => r.status === 200,
    });
    newsPageResponseTrend.add(res.timings.duration);
    sleep(1);
}
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
export const options = {
    vus: 5,
    duration: '5s',
    thresholds: {
        'http_req_duration{name:HomePage}': ['p(95)<250'],
        'http_req_duration{name:NewsPage}': ['p(95)<250'],
        my_counter: ['count>10']
    }
};

export default function () {
    let res = http.get('https://quickpizza.grafana.com/test.k6.io/', {
        tags: { name: 'HomePage' }
    });
    myCounter.add(1);
    sleep(1);

    res = http.get('https://quickpizza.grafana.com/news.php', {
        tags: { name: 'NewsPage' }
    });
    newsPageResponseTrend.add(res.timings.duration);
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

//... other code

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

- **Lines:** [18, 22]
- **Snippet:**
```js
let res = http.get('https://quickpizza.grafana.com/test.k6.io/');
// ...
res = http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
export default function () {
    let res = http.get('https://quickpizza.grafana.com/test.k6.io/', {
        tags: { name: 'Homepage' },
    });
    myCounter.add(1);
    sleep(1);
    
    res = http.get('https://quickpizza.grafana.com/news.php', {
        tags: { name: 'NewsPage' },
    });
    newsPageResponseTrend.add(res.timings.duration);
    sleep(1);
}
```

---

## `script_41.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
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
    tags: { name: 'Login' },
});
...
const eventRes = http.post('http://localhost:3000/user/organizer/createEvent', JSON.stringify(payload), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'CreateEvent' },
});
```

### `script_41.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [5, 4006]
- **Snippet:**
```js
const users = [ ...large inline user dataset... ]
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

const users = new SharedArray('users', function () {
  return JSON.parse(open('./users.json'));
});

// Move the large user dataset to users.json so it is loaded once and shared across VUs instead of materializing a huge inline array per VU.
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
    'http_req_duration{name:Login}': ['p(95)<500'],
    'http_req_duration{name:CreateEvent}': ['p(95)<1000'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [4026, 4029, 4030, 4031, 4052, 4053, 4054]
- **Snippet:**
```js
const loginRes = http.post('http://localhost:3000/guestUser/logIn', JSON.stringify(...), {
    headers: { 'Content-Type': 'application/json' },
});

const eventRes = http.post('http://localhost:3000/user/organizer/createEvent', JSON.stringify(payload), {
    headers: { 'Content-Type': 'application/json' },
});
```
- **Refactored:**
```js
const loginRes = http.post(
  'http://localhost:3000/guestUser/logIn',
  JSON.stringify({
    email: user.email,
    password: password,
  }),
  {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'Login', endpoint: 'guestUser_logIn', flow: 'event_creation' },
  }
);

check(loginRes, { 'login successful': (r) => r.status === 200 }, { name: 'Login', flow: 'event_creation' });

const eventRes = http.post(
  'http://localhost:3000/user/organizer/createEvent',
  JSON.stringify(payload),
  {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'CreateEvent', endpoint: 'organizer_createEvent', flow: 'event_creation' },
  }
);

check(eventRes, { 'event created': (r) => r.status === 200 }, { name: 'CreateEvent', flow: 'event_creation' });
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
    // ... more than 1000 user objects
]
```
- **Refactored:**
```js
/* 1. Create a file named 'users.json' with the user data array. */

/* 2. Refactor the k6 script to load the data efficiently. */
import { SharedArray } from 'k6/data';

const users = new SharedArray('users', function () {
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
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration{name:Login}': ['p(95)<500'], // 95% of login requests should be below 500ms
        'http_req_duration{name:CreateEvent}': ['p(95)<800'], // 95% of event creation requests should be below 800ms
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [4026, 4052]
- **Snippet:**
```js
const loginRes = http.post('http://localhost:3000/guestUser/logIn', JSON.stringify({
    //... body
}), {
    headers: { 'Content-Type': 'application/json' },
});
//...
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
    tags: { name: 'Login' },
});
//...
const eventRes = http.post('http://localhost:3000/user/organizer/createEvent', JSON.stringify(payload), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'CreateEvent' },
});
```

---

## `script_42.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.1'],
        'total_failures': ['count<10'],
        'check_slow_response': ['count<50'],
    },
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
    tags: { name: 'AddPet', endpoint: '/v2/pet' },
};
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
        http_req_duration: ['p(95)<1000'],
        http_req_failed: ['rate<0.05'],
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
        endpoint: '/v2/pet',
        method: 'POST',
    },
};
res = http.post(url, payload, params);
```

### `script_42.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11]
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
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<2000'], // 95% of requests must complete below 2s
        'checks': ['rate>0.99'],             // over 99% of checks must pass
        'total_failures': ['count<10'],      // a maximum of 10 failures are allowed
    },
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
        name: 'CreatePet', // Add a tag to identify this request
    },
};

res = http.post(url, payload, params);
```

---

## `script_45.js`

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
// These lines are acceptable in the init context as `open()` is meant to be used there.
// However, papaparse.parse() is a heavy computation executed once per VU in init.
// To mitigate cost, ensure the CSV is reasonably sized and avoid any additional
// heavy transformations. If further processing is needed, defer it to the default function.
const csvData = open('../loginSuccess.csv');
const userTokenData = papaparse.parse(csvData, { header: false, skipEmptyLines: true }).data;
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
		'http_req_duration': ['p(95)<500'],
		'http_req_failed': ['rate<0.01'],
		'checks': ['rate>0.95'],
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
	tags: { name: 'TokenValidate', endpoint: '/auth/v1/token/validate' }
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

- **Lines:** [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
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
    { duration: '20s', target: 1000 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    'http_req_duration{name:TokenValidate}': ['p(95)<200'],
    checks: ['rate>0.99'],
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
  },
});
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
import { SharedArray } from 'k6/data';

// Use SharedArray to load and parse the data only once, sharing the memory across all VUs.
// This is more efficient than each VU reading and parsing the file independently.
const userTokenData = new SharedArray('users', function () {
  return papaparse.parse(open('../loginSuccess.csv'), { header: false }).data;
});
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
        'http_req_failed': ['rate<0.01'],      // Fail if the error rate is higher than 1%
        'http_req_duration': ['p(95)<200'],    // 95% of requests must complete below 200ms (based on check on line 47)
        'checks': ['rate>0.99'],               // 99% of all checks must pass
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
            name: 'TokenValidation',
        },
    });
```

---

## `script_47.js`

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
// ...
const urlRes = http.get('https://test-api.k6.io');
check(urlRes, {
  'status is 200': (r) => r.status === 200,
  'response time < 500ms': (r) => r.timings.duration < 500,
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
const urlRes = http.get('https://test-api.k6.io', null, { tags: { name: 'Homepage' } });
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
    'status is 200': (res) => res.status === 200,
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
    tags: { name: 'Home' },
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
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
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
// ...
const urlRes = http.get('https://test-api.k6.io');
check(urlRes, {
  'is status 200': (r) => r.status === 200,
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
  tags: { name: 'PublicCrocsAPI' },
});
```

---

## `script_51.js`

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
http.put(url+`/29145037094`, JSON.stringify(data), {
  headers: headers,
  tags: { name: 'UpdateUser' },
});
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
export const options = {
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

const res = http.put(`${url}/29145037094`, JSON.stringify(data), { headers });
check(res, {
  'PUT /v1/user/:id status is 200 or 204': (r) => r.status === 200 || r.status === 204,
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
const params = {
  headers,
  tags: {
    name: 'UpdateUser',
    endpoint: '/v1/user/:id',
    method: 'PUT',
  },
};

const res = http.put(`${url}/29145037094`, JSON.stringify(data), params);
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
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
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
// ...
const res = http.put(url+`/29145037094`,JSON.stringify(data), { headers: headers } );
check(res, {
  'update user status is 200': (r) => r.status === 200,
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
http.put(url+`/29145037094`,JSON.stringify(data), { 
  headers: headers, 
  tags: { name: 'UpdateUser' } 
} );
```

---

## `script_52.js`

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
    },
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
const res = http.get('https://test.k6.io', { tags: { name: 'Homepage' } });
```

### `script_52.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
- **Snippet:**
```js
export const options = {
    stages: [
        { duration: '2m', target: 40 },
        { duration: '1m', target: 0 }
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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01']
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
        'status is 200': (r) => r.status === 200
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
    const res = http.get('https://test.k6.io', {
        tags: { name: 'HomePage' }
    });
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
        'http_req_duration': ['p(95)<500'],
    },
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
check(res, { 'status is 200': (r) => r.status === 200 });
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
  tags: { name: 'Homepage' },
});
```

---

## `script_53.js`

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
    'http_req_duration{name:PublicCrocs}': ['p(95)<2000'],
    'http_req_failed{name:PublicCrocs}': ['rate<0.01'],
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
// ...
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
    'response body is not empty': (r) => r.body && r.body.length > 0,
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
    'http_req_duration{name:PublicCrocs}': ['p(95)<500'],
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

export default function () {
  const BASE_URL = 'http://$domain_ba_aplic';

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
      'body is not empty': (r) => r.body && r.body.length > 0,
    });
  });

  sleep(1);
}
```

### `script_53.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
- **Snippet:**
```js
export const options = {
  stages: [
    { duration: '2m', target: 100 }, // below normal load
    { duration: '5m', target: 100 },
    //{ duration: '2m', target: 200 }, // normal load
    // ... more stages
  ],
};
```
- **Refactored:**
```js
export const options = {
  stages: [
    { duration: '2m', target: 100 }, // below normal load
    { duration: '5m', target: 100 },
    // ... other stages
  ],
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration{name:PublicCrocs}': ['p(95)<500'], // 95% of requests for 'PublicCrocs' should be below 500ms
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [22, 23, 24, 25, 26, 27, 28]
- **Snippet:**
```js
const responses = http.batch([
    ['GET', `${BASE_URL}/...`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/...`, null, { tags: { name: 'PublicCrocs' } }],
    // ... more requests
  ]);
```
- **Refactored:**
```js
import http from 'k6/http';
import { sleep, check } from 'k6';
// ... options ...

export default function () {
  const BASE_URL = 'http://$domain_ba_aplic'; // make sure this is not production

  const responses = http.batch([
    ['GET', `${BASE_URL}/departaments/Informatica/Segur01.nsf/xsp/.ibmmodres/domino/OpenAttachment/departaments/Informatica/Segur01.nsf/4B4D663F2463B917C12580DC002D0EC0/Body/doc%20web%20incidencias%20mbi.v3.pdf`, null, { tags: { name: 'PublicCrocs' } }],
    // ... other requests
  ]);

  responses.forEach(res => {
    check(res, {
      'is status 200': (r) => r.status === 200,
    });
  });

  sleep(1);
}
```

---

## `script_55.js`

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
  params: { headers: { 'Content-Type': 'multipart/form-data; boundary=' + fd.boundary } },
};
```
- **Refactored:**
```js
// Keep open() in init (it is allowed), but build FormData and body inside the default function to avoid heavy object construction per VU at init time
const image = open('car.jpg', 'b');
const gateway = 'http://10.103.51.65:8080';

export default function () {
  const fd = new FormData();
  fd.append('payload', http.file(image, 'image.png', 'image/png'));
  const params = {
    headers: {
      'Content-Type': 'multipart/form-data; boundary=' + fd.boundary,
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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
const res = http.post(
  resnet.url,
  resnet.body,
  Object.assign({}, resnet.params, { tags: { name: 'ResnetPredict' } })
);
```

### `script_55.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [19, 20, 21, 26]
- **Snippet:**
```js
const image = open('car.jpg', 'b');
const fd = new FormData();
fd.append('payload', http.file(image, 'image.png', 'image/png'));
let resnet = {
        ...
        body: fd.body(), 
        ...
};
```
- **Refactored:**
```js
export function setup() {
  const image = open('car.jpg', 'b');
  const fd = new FormData();
  fd.append('payload', http.file(image, 'image.png', 'image/png'));
  return {
    body: fd.body(),
    params: {
      headers: {
        'Content-Type': 'multipart/form-data; boundary=' + fd.boundary,
      },
    },
  };
}

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
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [27, 34]
- **Snippet:**
```js
let resnet = {
        ...
        params: {
            headers: {
 	            'Content-Type': 'multipart/form-data; boundary=' + fd.boundary 
 	          },
        },
};
...
const res = http.post(resnet.url, resnet.body, resnet.params)
```
- **Refactored:**
```js
let resnet = {
        ...
        params: {
            headers: {
 	            'Content-Type': 'multipart/form-data; boundary=' + fd.boundary 
 	          },
            tags: { name: 'ResNetPrediction' },
        },
};
...
const res = http.post(resnet.url, resnet.body, resnet.params)
```

---

## `script_56.js`

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
  'response time < 500ms': (r) => r.timings.duration < 500,
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
const res = http.get('https://test.k6.io/contacts.php', {
  tags: { name: 'Contacts' },
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
  const res = http.get('https://test.k6.io/contacts.php', {
    tags: { name: 'Contacts', endpoint: 'contacts' },
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
check(res, {
  'status is 200': (r) => r.status === 200,
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
  tags: { name: 'Contacts' },
});
```

---

## `script_59.js`

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
// Reading the file with open() is acceptable in init context, but parsing with papaparse
// is a heavy operation that runs once per VU. If the file is large, consider pre-processing
// it outside k6 or minimizing parsing overhead. The current pattern is the best available
// in k6 for CSV loading, but be aware it runs per VU init.
const csvData = open('../logsCSV/exam/accessToken.csv');
const userTokenData = papaparse.parse(csvData, { header: false, skipEmptyLines: true }).data;
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
        'http_req_duration': ['p(95)<500'],
        'http_req_failed': ['rate<0.01'],
        'checks': ['rate>0.99'],
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
    tags: { name: 'GetGroupExams', endpoint: 'exam-service' }
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

- **Lines:** [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
- **Snippet:**
```js
export let options = {
	//executor: 'shared-iterations',
	// iterations: 2,
	// vus: 1,
    // duration: '2s',
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
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
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
    name: 'GroupExams',
    endpoint: '/exam-service/v1/group-exams',
    flow: 'exam'
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

// The file is read and parsed only once for the entire test run, 
// and the data is shared among all VUs.
const userTokenData = new SharedArray('userTokens', function () {
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
        // Define success criteria for the test
        'http_req_duration': ['p(95)<200'], // 95% of requests must complete below 200ms
        'http_req_failed': ['rate<0.01'],   // Error rate must be less than 1%
        'checks': ['rate>0.99'],           // More than 99% of checks must pass
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
        name: 'GetGroupExams', // Tag to identify this specific request in results
    },
});
```

---

## `script_60.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
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
http.get('https://test.k6.io/contacts.php')
```
- **Refactored:**
```js
const res = http.get('https://test.k6.io/contacts.php', { tags: { name: 'Contacts' } });
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
        http_req_duration: ['p(95)<500']
    }
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
        'contacts page status is 200': (r) => r.status === 200
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
        tags: { name: 'Contacts', endpoint: 'contacts' }
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
        http_req_failed: ['rate<0.01'],   // http errors should be less than 1%
        http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
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
// ... in default function ...
const res = http.get('https://test.k6.io/contacts.php');
check(res, { 'status is 200': (r) => r.status === 200 });
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
  tags: { name: 'GetContacts' },
});
```

---

## `script_61.js`

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
// Keep open() in init context (it is allowed and recommended),
// but build FormData and request body inside the default function
// to avoid sharing mutable state across VUs and avoid heavy construction once globally.
const image = open('car.jpg', 'b'); // open() is fine in init

export default function () {
  const fd = new FormData();
  fd.append('payload', http.file(image, 'image.png', 'image/png'));
  const params = {
    headers: {
      'Content-Type': 'multipart/form-data; boundary=' + fd.boundary,
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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
const res = http.post(
  resnet.url,
  resnet.body,
  Object.assign({}, resnet.params, { tags: { name: 'ResnetPredict' } })
);
// And update thresholds to filter by tag:
// 'http_req_duration{name:ResnetPredict}': ['p(95)<500']
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
export function setup() {
  const image = open('car.jpg', 'b');
  const fd = new FormData();
  fd.append('payload', http.file(image, 'image.png', 'image/png'));
  return {
    body: fd.body(),
    boundary: fd.boundary
  };
}

export default function (data) {
  const resnet = {
    url: 'http://localhost:5000/predict',
    body: data.body,
    params: {
      headers: {
        'Content-Type': 'multipart/form-data; boundary=' + data.boundary
      },
    },
  };
  const res = http.post(resnet.url, resnet.body, resnet.params);
  //... rest of the code
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
    'checks': ['rate>0.99'], // 99% of checks must pass
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
let resnet = {
        method: 'POST',
	url: 'http://localhost:5000/predict',
        body: fd.body(), 
        params: {
            headers: {
	      'Content-Type': 'multipart/form-data; boundary=' + fd.boundary 
	    },
            tags: {
              name: 'PredictImage',
            },
        },
};
// ...
export default function () {
  const res = http.post(resnet.url, resnet.body, resnet.params);
  //...
}
```

---

## `script_62.js`

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
// ...
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
http.get('https://test.k6.io/contacts.php', { tags: { name: 'Contacts' } });
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
    'http_req_duration{name:Contacts}': ['p(95)<500'],
    checks: ['rate>0.99'],
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
import { check, sleep } from 'k6';

export default function () {
  const res = http.get('https://test.k6.io/contacts.php', {
    tags: { name: 'Contacts' },
  });

  check(res, {
    'Contacts page returned status 200': (r) => r.status === 200,
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
    tags: { name: 'Contacts', endpoint: 'contacts' },
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
http.get('https://test.k6.io/contacts.php', { tags: { name: 'GetContacts' } });
```

---

## `script_63.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
    },
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
    'response body is not empty': (r) => r.body && r.body.length > 0,
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
    tags: { name: 'Homepage' },
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
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01']
    },
    cloud: {
        projectID: 3771795
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
import { check, sleep } from 'k6';

export default function () {
    const res = http.get('https://quickpizza.grafana.com/test.k6.io/', {
        tags: { name: 'QuickPizzaHome' }
    });

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
    const res = http.get('https://quickpizza.grafana.com/test.k6.io/', {
        tags: { name: 'QuickPizzaHome', endpoint: 'home' }
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
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
    },
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

export default function () {
    const res = http.get('https://quickpizza.grafana.com/test.k6.io/');
    check(res, { 'status is 200': (r) => r.status === 200 });
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
http.get('https://quickpizza.grafana.com/test.k6.io/', {
      tags: { name: 'Homepage' },
    });
```

---

## `script_69.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
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
// ...
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
    tags: { name: 'Contacts' },
});
// And update thresholds to use tag-based filtering:
// 'http_req_duration{name:Contacts}': ['p(95)<500']
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
import { check, sleep } from 'k6';

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
        'http_req_duration{name:Contacts}': ['p(95)<500'],
        'http_req_failed{name:Contacts}': ['rate<0.01'],
    },
};

export default function() {
    http.get('https://test.k6.io/contacts.php', {
        tags: { name: 'Contacts' },
    });
    sleep(0.5);
}
```

### `script_69.js` — GEMINI

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
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
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
// ... in default function
const res = http.get('https://test.k6.io/contacts.php');
check(res, { 'status is 200': (r) => r.status === 200 });
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

---

## `script_70.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01']
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
http.get('https://quickpizza.grafana.com', { tags: { name: 'HomePage' } });
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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01']
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
import { check, sleep } from 'k6';

export default function () {
    const res = http.get('https://quickpizza.grafana.com');

    check(res, {
        'status is 200': (r) => r.status === 200
    });

    console.log('- VU stage -');
    sleep(randomIntBetween(1, 5));
}
```

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
export default function () {
    const res = http.get('https://quickpizza.grafana.com', {
        tags: { name: 'Home' }
    });

    check(res, {
        'Home status is 200': (r) => r.status === 200
    });

    console.log('- VU stage -');
    sleep(randomIntBetween(1, 5));
}

export const options = {
    vus: 5,
    duration: '20s',
    thresholds: {
        'http_req_duration{name:Home}': ['p(95)<500'],
        'http_req_failed{name:Home}': ['rate<0.01']
    }
};
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
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
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
import { check } from 'k6';
// ...
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
  tags: { name: 'Homepage' },
});
```

---

## `script_71.js`

### `script_71.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
- **Snippet:**
```js
export const options = {
  vus: 100,
  duration: '10s',
  ext: {
    loadimpact: { ... }
  }
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
  'response body is not empty': (r) => r.body && r.body.length > 0,
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
const res = http.get('http://test.k6.io', { tags: { name: 'Homepage' } });
// Also update thresholds to leverage the tag:
// 'http_req_duration{name:Homepage}': ['p(95)<500']
```

### `script_71.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
- **Snippet:**
```js
export const options = {
  vus: 100,
  duration: '10s',
  ext: {
    loadimpact: {
      projectID: 3671346,
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
  const res = http.get('http://test.k6.io', { tags: { name: 'Home' } });
  check(res, {
    'Home status is 200': (r) => r.status === 200
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
    tags: { name: 'Home', endpoint: '/' }
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
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
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
// ...
export default function() {
  const res = http.get('http://test.k6.io');
  check(res, { 'status is 200': (r) => r.status === 200 });
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
http.get('http://test.k6.io', {
    tags: { name: 'PublicMainPage' },
});
```

---

## `script_76.js`

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
    'shufflenet_http_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
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
  'response time < 500ms': (r) => r.timings.duration < 500,
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
          tags: { name: 'ShuffleNet' },
        },
};
let res = http.batch([paddle]);
shufflenet_http_duration.add(res[0].timings.duration, { name: 'ShuffleNet' });
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
    'http_req_duration{name:ShuffleNet}': ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
let responses = http.batch([paddle]);
check(responses[0], {
  'ShuffleNet status is 200': (r) => r.status === 200,
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
      name: 'ShuffleNet',
      endpoint: 'shufflenet',
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
    'http_req_failed': ['rate<0.01'], // less than 1% failed requests
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
let responses = http.batch([paddle]);
check(responses[0], {
  'shufflenet status is 200': (r) => r.status === 200,
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
        params: { tags: { name: 'ShuffleNet' } },
};
```

---

## `script_77.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
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

// inside default function:
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
const res = http.get('https://test.k6.io/contacts.php', { tags: { name: 'Contacts' } });
// and update thresholds to use the tag:
// 'http_req_duration{name:Contacts}': ['p(95)<500']
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
        checks: ['rate>0.99']
    }
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
        'contacts status is 200': (r) => r.status === 200,
        'contacts response is not empty': (r) => r.body && r.body.length > 0
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
            name: 'Contacts',
            endpoint: 'contacts'
        }
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
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
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

---

## `script_78.js`

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
import { check } from 'k6';

// inside default function:
const res = http.get('https://test.k6.io');
check(res, {
  'status is 200': (r) => r.status === 200,
  'response time < 500ms': (r) => r.timings.duration < 500,
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
http.get('https://test.k6.io', { tags: { name: 'Homepage' } });
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
    'status is 200': (r) => r.status === 200,
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
    tags: { name: 'HomePage' },
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
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<200'],
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
const res = http.get('https://test.k6.io');
check(res, {
  'status is 200': (r) => r.status === 200,
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
  tags: { name: 'Homepage' },
});
```

---

## `script_80.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
        success_rate: ['rate>0.99'],
    }
};
```

**Smell 3: Not checking requests**

- **Lines:** [20]
- **Snippet:**
```js
const response = http.get('http://test.k6.io');
```
- **Refactored:**
```js
import { check, sleep } from 'k6';

// inside default function:
const response = http.get('http://test.k6.io');
check(response, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
});
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
    tags: { name: 'HomePage' },
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
        http_req_failed: ['rate<0.01'],
        'http_req_duration{name:Home}': ['p(95)<500'],
        checks: ['rate>0.99']
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
    const response = http.get('http://test.k6.io', {
        tags: { name: 'Home' }
    });

    const ok = check(response, {
        'Home status is 200': (r) => r.status === 200
    });

    successRate.add(ok);
    requestCounter.add(1);
    requestTrend.add(response.timings.duration);
    sleep(1);
}
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
    tags: { name: 'Home' }
});
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
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
        'success_rate': ['rate>0.99'],      // custom metric: success rate must be > 99%
    },
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

// inside default function:
const success = check(response, {
    'status is 200': (r) => r.status === 200,
});
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
  tags: { name: 'PublicHomepage' },
});
```

---

## `script_82.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
    },
};
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

// inside default function:
const res = http.get('https://test-api.k6.io');
check(res, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500,
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
const res = http.get('https://test-api.k6.io', {
    tags: { name: 'HomePage' },
});
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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
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
import { check, sleep } from 'k6'

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
export const options = {
    iterations: 10,
    thresholds: {
        'http_req_duration{name:Home}': ['p(95)<500'],
        'http_req_failed{name:Home}': ['rate<0.01'],
    },
}

export default function () {
    http.get('https://test-api.k6.io', { tags: { name: 'Home' } })
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
        http_req_failed: ['rate<0.01'], // http errors should be less than 1%
        http_req_duration: ['p(95)<500'], // 95% of requests must complete below 500ms
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

//... inside the default function
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
  tags: { name: 'PublicAPICheck' },
});
```

---

## `script_83.js`

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
  tags: { name: 'GetTestRecords', endpoint: '/rest/v1/test' },
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
  'status is 200': (r) => r.status === 200,
  'body is not empty': (r) => r.body && r.body.length > 0,
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
    name: 'SelectTestRecords',
    endpoint: 'rest_v1_test',
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
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
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
import { check } from 'k6';
// ...
const response = http.get(endpoint, { headers: headers });
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
  headers: headers,
  tags: {
    name: 'GetTestData',
  },
});
```

---

## `script_85.js`

### `script_85.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57]
- **Snippet:**
```js
const allUsers = open('/home/vunet/user_creation_k6/user_cookies_module.txt')
  .split('\n')
  .map(line => {
    const [username, password, accessToken, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    return { ... };
  })
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

- **Lines:** [43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 60]
- **Snippet:**
```js
const allUsers = open('/home/vunet/user_creation_k6/user_cookies_module.txt')
  .split('\n')
  .map(line => { ... })
  .filter(user => ...);

const selectedUsers = allUsers.slice(0, CONFIG.userCount);
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
    throw new Error(`Not enough valid users found in file.`);
  }
  return { users: selectedUsers };
}

// In default function, access users via the 'data' parameter
// export default function (data) {
//   const user = data.users[__VU - 1];
//   ...
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
    // ... same tags
  },
  thresholds: {
    'http_req_failed': ['rate<0.01'],       // http errors should be less than 1%
    'http_req_duration': ['p(95)<2000'],    // 95% of requests should be below 2000ms
    'checks': ['rate>0.99'],                // 99% of checks should pass
    'alert_execution_success_rate': ['rate>0.95'] // 95% of executions should be successful
  }
};
```

---

## `script_89.js`

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
// ...
const res = http.get('https://quickpizza.grafana.com');
check(res, {
  'status is 200': (r) => r.status === 200,
  'response time < 500ms': (r) => r.timings.duration < 500,
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
http.get('https://quickpizza.grafana.com', { tags: { name: 'HomePage' } });
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
  const res = http.get('https://quickpizza.grafana.com', {
    tags: { name: 'QuickPizzaHome' },
  });

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
http.get('https://quickpizza.grafana.com', {
  tags: { name: 'QuickPizzaHome' },
});
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
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
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
// ...
const res = http.get('https://quickpizza.grafana.com');
check(res, { 'status was 200': (r) => r.status == 200 });
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

---

## `script_90.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01']
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
// ...
const res = http.get('https://test.k6.io');
check(res, {
    'status is 200': (r) => r.status === 200,
    'response time < 500ms': (r) => r.timings.duration < 500
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
http.get('https://test.k6.io', { tags: { name: 'Homepage' } });
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
        'http_req_duration{name:Home}': ['p(95)<500']
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
import { sleep, check } from 'k6';

export default function () {
    const res = http.get('https://test.k6.io', { tags: { name: 'Home' } });
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
http.get('https://test.k6.io', {
    tags: {
        name: 'Home'
    }
});
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
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
    },
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
// ...
const res = http.get('https://test.k6.io');
check(res, { 'status was 200': (r) => r.status == 200 });
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
  tags: { name: 'Homepage' },
});
```

---

## `script_92.js`

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
...
const res_dentidade = http.post(definirEntidade, d_entidade, params)
...
const res_lrapido = http.post(lancarRapido, l_rapido, params);
...
const res_pagdinheiro = http.post(pagDinheiro, pag_dinheiro, params);
...
let res_gdemissaoDocFiscal = http.get(`${getDadosEmissaoDocFiscal}?${gd_emissaoDocFiscal.toString()}`, params);
...
const res_gnotaFiscal = http.post(gerarNotaFiscal, g_notaFiscal, params);
```
- **Refactored:**
```js
// Add tags to each request's params so metrics can be filtered per endpoint

// Login
const paramsLogin = { headers: { 'Content-Type': 'application/json' }, timeout: '600s', tags: { name: 'Login' } };
const res_login = http.post(url, login, paramsLogin);

// Abrir Venda
const paramsAbVenda = { headers: { 'Content-Type': 'application/json' }, timeout: '600s', tags: { name: 'AbrirVenda' } };
const res_abvenda = http.post(abrirVenda, ab_venda, paramsAbVenda);

// Pesquisa Geral Entidade
const paramsPGEntidade = { headers: { 'Content-Type': 'application/json' }, timeout: '600s', tags: { name: 'PesquisaGeralEntidade' } };
let res_pgentidade = http.get(`${pesquisaGeralEntidade}?${searchParams.toString()}`, paramsPGEntidade);

// Definir Entidade
const paramsDEntidade = { headers: { 'Content-Type': 'application/json' }, timeout: '600s', tags: { name: 'DefinirEntidade' } };
const res_dentidade = http.post(definirEntidade, d_entidade, paramsDEntidade);

// Lançar Rápido
const paramsLRapido = { headers: { 'Content-Type': 'application/json' }, timeout: '600s', tags: { name: 'LancarRapido' } };
const res_lrapido = http.post(lancarRapido, l_rapido, paramsLRapido);

// Pagamento Dinheiro
const paramsPagDinheiro = { headers: { 'Content-Type': 'application/json' }, timeout: '600s', tags: { name: 'PagamentoDinheiro' } };
const res_pagdinheiro = http.post(pagDinheiro, pag_dinheiro, paramsPagDinheiro);

// Consulta Dados Emissão Documento Fiscal
const paramsGDEmissao = { headers: { 'Content-Type': 'application/json' }, timeout: '600s', tags: { name: 'GetDadosEmissaoDocFiscal' } };
let res_gdemissaoDocFiscal = http.get(`${getDadosEmissaoDocFiscal}?${gd_emissaoDocFiscal.toString()}`, paramsGDEmissao);

// Gerar Nota Fiscal
const paramsGNotaFiscal = { headers: { 'Content-Type': 'application/json' }, timeout: '600s', tags: { name: 'GerarNotaFiscal' } };
const res_gnotaFiscal = http.post(gerarNotaFiscal, g_notaFiscal, paramsGNotaFiscal);

// Also update thresholds to leverage tags:
export const options = {
  vus: 1,
  duration: '2m',
  thresholds: {
    'http_req_duration{name:Login}': ['p(95)<2000'],
    'http_req_duration{name:AbrirVenda}': ['p(95)<2000'],
    'http_req_duration{name:PesquisaGeralEntidade}': ['p(95)<2000'],
    'http_req_duration{name:DefinirEntidade}': ['p(95)<2000'],
    'http_req_duration{name:LancarRapido}': ['p(95)<2000'],
    'http_req_duration{name:PagamentoDinheiro}': ['p(95)<2000'],
    'http_req_duration{name:GetDadosEmissaoDocFiscal}': ['p(95)<2000'],
    'http_req_duration{name:GerarNotaFiscal}': ['p(95)<2000'],
    http_req_failed: ['rate<0.01']
  }
};
```

### `script_92.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [45, 63, 87, 104, 131, 150, 167, 230]
- **Snippet:**
```js
const res_login = http.post(url, login, params);
const res_abvenda = http.post(abrirVenda, ab_venda, params);
let res_pgentidade = http.get(`${pesquisaGeralEntidade}?${searchParams.toString()}`, params);
const res_dentidade = http.post(definirEntidade, d_entidade, params)
const res_lrapido = http.post(lancarRapido, l_rapido, params);
const res_pagdinheiro = http.post(pagDinheiro, pag_dinheiro, params);
let res_gdemissaoDocFiscal = http.get(`${getDadosEmissaoDocFiscal}?${gd_emissaoDocFiscal.toString()}`, params);
const res_gnotaFiscal = http.post(gerarNotaFiscal, g_notaFiscal, params);
```
- **Refactored:**
```js
const baseParams = {
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: '600s',
};

const res_login = http.post(url, login, {
  ...baseParams,
  tags: { name: 'Login', endpoint: '/Home/Login', flow: 'Faturamento' },
});

const res_abvenda = http.post(abrirVenda, ab_venda, {
  ...baseParams,
  tags: { name: 'AbrirVenda', endpoint: '/operacoes/faturamento/api/abrir-venda', flow: 'Faturamento' },
});

let res_pgentidade = http.get(`${pesquisaGeralEntidade}?${searchParams.toString()}`, {
  ...baseParams,
  tags: { name: 'PesquisaGeralEntidade', endpoint: '/operacoes/faturamento/api/pesquisa-geral', flow: 'Faturamento' },
});

const res_dentidade = http.post(definirEntidade, d_entidade, {
  ...baseParams,
  tags: { name: 'DefinirEntidade', endpoint: '/operacoes/faturamento/api/:id/definir-entidade', flow: 'Faturamento' },
});

const res_lrapido = http.post(lancarRapido, l_rapido, {
  ...baseParams,
  tags: { name: 'LancarRapido', endpoint: '/operacoes/faturamento/api/:id/lancar-rapido', flow: 'Faturamento' },
});

const res_pagdinheiro = http.post(pagDinheiro, pag_dinheiro, {
  ...baseParams,
  tags: { name: 'PagamentoDinheiro', endpoint: '/operacoes/faturamento/api/:id/lancar-meio-de-pagamento/dinheiro', flow: 'Faturamento' },
});

let res_gdemissaoDocFiscal = http.get(`${getDadosEmissaoDocFiscal}?${gd_emissaoDocFiscal.toString()}`, {
  ...baseParams,
  tags: { name: 'GetDadosEmissaoDocumentoFiscal', endpoint: '/entidade/GetDadosParaEmissaoDeDocumentoFiscal', flow: 'Faturamento' },
});

const res_gnotaFiscal = http.post(gerarNotaFiscal, g_notaFiscal, {
  ...baseParams,
  tags: { name: 'GerarNotaFiscal', endpoint: '/operacoes/gerar-nota-fiscal', flow: 'Faturamento' },
});
```

### `script_92.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [45, 63, 87, 104, 131, 150, 167, 230]
- **Snippet:**
```js
const params = {
  headers: {
    'Content-Type': 'application/json',
  },
  'Timeout': '600s'
};

const res_login = http.post(url, login, params);
// ... and all subsequent http requests use the same untagged params object
```
- **Refactored:**
```js
// Refactor by adding tags to each request to differentiate metrics.
// This can be done by creating specific params for each request or by merging tags into the base params.

const res_login = http.post(url, login, {
  ...params,
  tags: { name: 'Login' },
});

//...

const res_abvenda = http.post(abrirVenda, ab_venda, {
  ...params,
  tags: { name: 'AbrirVenda' },
});

//...

let res_pgentidade = http.get(`${pesquisaGeralEntidade}?${searchParams.toString()}`, {
  ...params,
  tags: { name: 'PesquisaGeralEntidade' },
});

// Apply this pattern to all other http requests in the script.
```

---

## `script_93.js`

### `script_93.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
export default function () {
```

**Smell 3: Not checking requests**

- **Lines:** [12, 22, 40, 49, 81, 98, 113]
- **Snippet:**
```js
http.post(`${URL}/user/register/`, ...);
http.post(`${URL}/auth/token/login/`, ...);
http.get(`${URL}/my/crocodiles/`, ...);
http.post(`${URL}/my/crocodiles/`, ...);
http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, ...);
http.patch(`${URL}o/my/crocodiles/${newCrocodileId}/`, ...);
http.del(`${URL}/my/crocodiles/${newCrocodileId}/`, ...);
```
- **Refactored:**
```js
let res = http.post(`${URL}/user/register/`, JSON.stringify(credentials), { headers: { 'Content-Type': 'application/json' } });
check(res, { 'register status is 201': (r) => r.status === 201 });

res = http.post(`${URL}/auth/token/login/`, JSON.stringify({ username: credentials.username, password: credentials.password }), { headers: { 'Content-Type': 'application/json' } });
check(res, { 'login status is 200': (r) => r.status === 200, 'has access token': (r) => r.json().access !== undefined });

res = http.get(`${URL}/my/crocodiles/`, { headers: { Authorization: 'Bearer ' + accessToken } });
check(res, { 'get crocodiles status is 200': (r) => r.status === 200 });

res = http.post(`${URL}/my/crocodiles/`, JSON.stringify({ name: 'Random croc', sex: 'M', date_of_birth: '1900-10-28' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' } });
check(res, { 'create crocodile status is 201': (r) => r.status === 201, 'crocodile id exists': (r) => r.json().id !== undefined });

res = http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ name: 'Updated Random croc', sex: 'M', date_of_birth: '1900-10-28' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' } });
check(res, { 'update crocodile status is 200': (r) => r.status === 200 });

res = http.patch(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ sex: 'F' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' } });
check(res, { 'patch crocodile status is 200': (r) => r.status === 200 });

res = http.del(`${URL}/my/crocodiles/${newCrocodileId}/`, null, { headers: { Authorization: 'Bearer ' + accessToken } });
check(res, { 'delete crocodile status is 204': (r) => r.status === 204 });
```

**Smell 4: Not using tags**

- **Lines:** [12, 22, 40, 49, 67, 81, 98, 113]
- **Snippet:**
```js
http.post(`${URL}/user/register/`, ...);
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
http.post(`${URL}/user/register/`, JSON.stringify(credentials), { headers: { 'Content-Type': 'application/json' }, tags: { name: 'RegisterUser' } });

http.post(`${URL}/auth/token/login/`, JSON.stringify({ username: credentials.username, password: credentials.password }), { headers: { 'Content-Type': 'application/json' }, tags: { name: 'Login' } });

http.get(`${URL}/my/crocodiles/`, { headers: { Authorization: 'Bearer ' + accessToken }, tags: { name: 'ListCrocodiles' } });

http.post(`${URL}/my/crocodiles/`, JSON.stringify({ name: 'Random croc', sex: 'M', date_of_birth: '1900-10-28' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' }, tags: { name: 'CreateCrocodile' } });

http.get(`${URL}/my/crocodiles/${newCrocodileId}/`, { headers: { Authorization: 'Bearer ' + accessToken }, tags: { name: 'GetCrocodile' } });

http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ name: 'Updated Random croc', sex: 'M', date_of_birth: '1900-10-28' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' }, tags: { name: 'UpdateCrocodile' } });

http.patch(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ sex: 'F' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' }, tags: { name: 'PatchCrocodile' } });

http.del(`${URL}/my/crocodiles/${newCrocodileId}/`, null, { headers: { Authorization: 'Bearer ' + accessToken }, tags: { name: 'DeleteCrocodile' } });
```

### `script_93.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [3]
- **Snippet:**
```js
The script does not define an `export const options` block, and therefore, no `thresholds` are set to define success or failure criteria for the test.
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
        headers: { 'Content-Type': 'application/json' }
    }
);
check(registerRes, { 'user registration status is 201': (r) => r.status === 201 });
```

**Smell 4: Not using tags**

- **Lines:** [12, 22, 40, 49, 67, 81, 98, 113]
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
            name: 'User-Register',
        },
    }
);
```

---

## `script_94.js`

### `script_94.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [96, 97, 98, 105, 111, 112]
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
        }
    }
);

check(res, {
    'status is 201': (r) => r.status === 201,
    'has crocodile id': (r) => r.json().id !== undefined
});

const newCrocodileId = res.json().id;
```

**Smell 4: Not using tags**

- **Lines:** [39, 56, 80, 96, 116, 132, 156, 178]
- **Snippet:**
```js
http.post('https://test-api.k6.io/user/register/', ...);
http.post('https://test-api.k6.io/auth/token/login/', ...);
http.get('https://test-api.k6.io/my/crocodiles/', ...);
http.post('https://test-api.k6.io/my/crocodiles/', ...);
http.get(`https://test-api.k6.io/my/crocodiles/${newCrocodileId}/`, ...);
http.put(`https://test-api.k6.io/my/crocodiles/${newCrocodileId}/`, ...);
http.patch(`https://test-api.k6.io/my/crocodiles/${newCrocodileId}/`, ...);
http.del(`https://test-api.k6.io/my/crocodiles/${newCrocodileId}/`, ...);
```
- **Refactored:**
```js
res = http.post(
    'https://test-api.k6.io/user/register/',
    JSON.stringify(credentials),
    {
        headers: { 'Content-Type': 'application/json' },
        tags: { name: 'RegisterUser', endpoint: 'user_register' }
    }
);

res = http.post(
    'https://test-api.k6.io/auth/token/login/',
    JSON.stringify({ username: credentials.username, password: credentials.password }),
    {
        headers: { 'Content-Type': 'application/json' },
        tags: { name: 'Login', endpoint: 'auth_login' }
    }
);

res = http.get(
    'https://test-api.k6.io/my/crocodiles/',
    {
        headers: { Authorization: 'Bearer ' + accessToken },
        tags: { name: 'ListCrocodiles', endpoint: 'crocodiles_list' }
    }
);

res = http.post(
    'https://test-api.k6.io/my/crocodiles/',
    JSON.stringify({ name: 'Random croc', sex: 'M', date_of_birth: '1900-10-28' }),
    {
        headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' },
        tags: { name: 'CreateCrocodile', endpoint: 'crocodiles_create' }
    }
);

res = http.get(
    `https://test-api.k6.io/my/crocodiles/${newCrocodileId}/`,
    {
        headers: { Authorization: 'Bearer ' + accessToken },
        tags: { name: 'GetCrocodile', endpoint: 'crocodiles_get' }
    }
);

res = http.put(
    `https://test-api.k6.io/my/crocodiles/${newCrocodileId}/`,
    JSON.stringify({ name: 'Updated Random croc', sex: 'M', date_of_birth: '1900-10-28' }),
    {
        headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' },
        tags: { name: 'UpdateCrocodile', endpoint: 'crocodiles_update' }
    }
);

res = http.patch(
    `https://test-api.k6.io/my/crocodiles/${newCrocodileId}/`,
    JSON.stringify({ sex: 'F' }),
    {
        headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' },
        tags: { name: 'PatchCrocodile', endpoint: 'crocodiles_patch' }
    }
);

res = http.del(
    `https://test-api.k6.io/my/crocodiles/${newCrocodileId}/`,
    null,
    {
        headers: { Authorization: 'Bearer ' + accessToken },
        tags: { name: 'DeleteCrocodile', endpoint: 'crocodiles_delete' }
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
            name: 'UserRegistration'
        }
    }
);
```

---

## `script_95.js`

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
    'browser_http_req_duration{name:Homepage}': ['p(95)<3000'],
    'browser_http_req_duration{name:Register}': ['p(95)<3000'],
    'browser_http_req_duration{name:Login}': ['p(95)<3000'],
    'checks': ['rate>0.95'],
  },
};

export default function () {
    browser();
}
```

**Smell 4: Not using tags**

- **Lines:** [19, 28, 39, 47, 58, 70, 76, 88, 99, 110, 116]
- **Snippet:**
```js
page.goto(domain);
...
element = page.$('//a[contains(.,"register")]');
element.click();
...
element = page.$('//a[contains(.,"Log in")]');
element.click();
...
element = page.$('//a[contains(.,"k6 Test Api")]');
element.click();
```
- **Refactored:**
```js
// Tag navigation actions to enable filtering by step in metrics
page.goto(domain, { waitUntil: 'networkidle' }, { tags: { name: 'Homepage' } });
...
// For browser actions that support params, pass tags in params object
// e.g., use page.goto with tags where supported
// For clicks and interactions, set tags via k6 group() to logically group steps:
import { group } from 'k6';

group('01-Homepage', function () {
    page.goto(domain);
    page.waitForLoadState('networkidle');
    // ...
});

group('02-Register', function () {
    element = page.$('//a[contains(.,"register")]');
    element.click();
    // ...
});

group('03-Login', function () {
    element = page.$('//a[contains(.,"Log in")]');
    element.click();
    // ...
});
```

### `script_95.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [6]
- **Snippet:**
```js
export default function () {
    browser ();
}
// No export const options with thresholds is defined in the script.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    checks: ['rate>0.95'],
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<1000'],
  },
};

export default function () {
  browser();
}
```

**Smell 4: Not using tags**

- **Lines:** [22, 33, 51, 63, 82, 93, 104, 121]
- **Snippet:**
```js
check(page, {
    'browser-01a-Homepage': (p) => p.$('//p[@class="description"]').textContent().includes("Collection of HTTP and WebSocket APIs demonstrating the power of k6"),
});

check(page, {
    'browser-02a-Register page': (p) => p.$('//div[@class="response-info"]').textContent().includes("HTTP 405 Method Not Allowed"),
});

// Other check() calls also omit the optional tags parameter.
```
- **Refactored:**
```js
check(page, {
  'browser-01a-Homepage': (p) => p.$('//p[@class="description"]').textContent().includes('Collection of HTTP and WebSocket APIs demonstrating the power of k6'),
}, { flow: 'browser', step: 'homepage' });

check(page, {
  'browser-02a-Register page': (p) => p.$('//div[@class="response-info"]').textContent().includes('HTTP 405 Method Not Allowed'),
}, { flow: 'browser', step: 'register-page' });

check(page, {
  'browser-02b-Register-submit': (p) => p.$('//div[@class="response-info"]').textContent().includes(accountUsername),
}, { flow: 'browser', step: 'register-submit' });

check(page, {
  'browser-03a-Login page': (p) => p.$('//div[@id="div_id_username"]').textContent().includes('Username'),
}, { flow: 'browser', step: 'login-page' });

check(page, {
  'browser-03b-Login-submit': (p) => p.$('//li[@class="dropdown"]').textContent().includes(accountUsername),
}, { flow: 'browser', step: 'login-submit' });

check(page, {
  'browser-01-Homepage': (p) => p.$('//p[@class="description"]').textContent().includes('Collection of HTTP and WebSocket APIs demonstrating the power of k6'),
}, { flow: 'browser', step: 'back-homepage' });

check(page, {
  'browser-04a-My Crocodiles page': (p) => p.$('//div[@id="content"]').textContent().includes('Crocs belonging to the authenticated user'),
}, { flow: 'browser', step: 'my-crocodiles-page' });

check(page, {
  'browser-05a-New croc submitted': (p) => p.$('//div[@class="response-info"]').textContent().includes('2012-06-02'),
}, { flow: 'browser', step: 'new-croc-submit' });
```

### `script_95.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5]
- **Snippet:**
```js
The script does not contain an `export const options` block, and therefore, no performance thresholds are defined. Without thresholds, the test will always be reported as successful, regardless of the system's actual performance.
```
- **Refactored:**
```js
import { sleep, check } from 'k6';
import launcher from "k6/x/browser";
import { vu } from 'k6/execution';
import { randomIntBetween } from "https://jslib.k6.io/k6-utils/1.0.0/index.js";

export const options = {
  vus: 5,
  duration: '5m',
  thresholds: {
    'checks': ['rate>0.99'], // Over 99% of checks must pass
    'browser_web_vital_lcp': ['p(95)<2500'], // LCP for 95% of VUs must be below 2.5s
    'browser_web_vital_inp': ['p(95)<200'],   // INP for 95% of VUs must be below 200ms
    'browser_web_vital_cls': ['p(95)<0.1'],   // CLS for 95% of VUs must be below 0.1
  },
};

// The rest of the script follows
```

**Smell 4: Not using tags**

- **Lines:** [18, 27, 57, 87, 98, 109]
- **Snippet:**
```js
Logical sections of the user journey, such as 'Homepage', 'Register', and 'Login', are commented but are not wrapped in `group()` blocks. This prevents metrics from being tagged and aggregated by user flow, making it difficult to analyze the performance of individual steps.

// 01-Homepage
page.goto(domain);
page.waitForLoadState('networkidle');
// ...
```
- **Refactored:**
```js
import { sleep, check, group } from 'k6';
// ... other imports

export function browser () {
    // ... setup code ...

    group('01-Homepage', () => {
        page.goto(domain);
        page.waitForLoadState('networkidle');
        sleep(Math.random() * 5+3);
        check(page, {
            'browser-01a-Homepage': (p) => p.$('//p[@class="description"]').textContent().includes("Collection of HTTP and WebSocket APIs demonstrating the power of k6"),
        });
        page.screenshot({ path: `screenshots/01a-homepage.png` });
    });

    group('02-Register', () => {
        // ... all actions related to registration go here
    });

    // ... other groups for Login, My Crocodiles, etc. ...

    // ... teardown code ...
}
```

---

## `script_96.js`

### `script_96.js` — CLAUDE

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
    'http_req_duration{name:Register}': ['p(95)<500'],
    'http_req_duration{name:Login}': ['p(95)<500'],
    'http_req_duration{name:GetCrocodiles}': ['p(95)<1000'],
    'http_req_duration{name:CreateCrocodile}': ['p(95)<1000'],
    'http_req_duration{name:GetCrocodile}': ['p(95)<500'],
    'http_req_duration{name:UpdateCrocodile}': ['p(95)<500'],
    'http_req_duration{name:PatchCrocodile}': ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [13, 23, 41, 50, 82, 99]
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
check(res, { 'create crocodile status is 201': (r) => r.status === 201 });
const newCrocodileId = res.json().id;

res = http.get(`${URL}/my/crocodiles/${newCrocodileId}/`, { headers: { Authorization: 'Bearer ' + accessToken } });
check(res, { 'status is 200': (r) => r.status === 200, 'crocodile id': (r) => r.json().id === newCrocodileId });

res = http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ name: 'Updated Random croc', sex: 'M', date_of_birth: '1900-10-28' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' } });
check(res, { 'put status is 200': (r) => r.status === 200 });

res = http.patch(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ sex: 'F' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' } });
check(res, { 'patch status is 200': (r) => r.status === 200 });
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
http.post(`${URL}/user/register/`, JSON.stringify(credentials), { headers: { 'Content-Type': 'application/json' }, tags: { name: 'Register' } });

http.post(`${URL}/auth/token/login/`, JSON.stringify({ username: credentials.username, password: credentials.password }), { headers: { 'Content-Type': 'application/json' }, tags: { name: 'Login' } });

http.get(`${URL}/my/crocodiles/`, { headers: { Authorization: 'Bearer ' + accessToken }, tags: { name: 'GetCrocodiles' } });

http.post(`${URL}/my/crocodiles/`, JSON.stringify({ name: 'Random croc', sex: 'M', date_of_birth: '1900-10-28' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' }, tags: { name: 'CreateCrocodile' } });

http.get(`${URL}/my/crocodiles/${newCrocodileId}/`, { headers: { Authorization: 'Bearer ' + accessToken }, tags: { name: 'GetCrocodile' } });

http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ name: 'Updated Random croc', sex: 'M', date_of_birth: '1900-10-28' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' }, tags: { name: 'UpdateCrocodile' } });

http.patch(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ sex: 'F' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' }, tags: { name: 'PatchCrocodile' } });
```

### `script_96.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [1, 114]
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
    checks: ['rate>0.95']
  }
};
```

**Smell 3: Not checking requests**

- **Lines:** [13, 23, 41, 50, 82, 99]
- **Snippet:**
```js
http.post(`${URL}/user/register/`, ...);
let res = http.post(`${URL}/auth/token/login/`, ...);
http.get(`${URL}/my/crocodiles/`, ...);
res = http.post(`${URL}/my/crocodiles/`, ...);
res = http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, ...);
res = http.patch(`${URL}/my/crocodiles/${newCrocodileId}/`, ...);
```
- **Refactored:**
```js
let res = http.post(`${URL}/user/register/`, JSON.stringify(credentials), {
  headers: { 'Content-Type': 'application/json' }
});
check(res, { 'register status is 201': (r) => r.status === 201 });

res = http.post(`${URL}/auth/token/login/`, JSON.stringify({
  username: credentials.username,
  password: credentials.password
}), {
  headers: { 'Content-Type': 'application/json' }
});
check(res, {
  'login status is 200': (r) => r.status === 200,
  'access token exists': (r) => !!r.json().access
});

const accessToken = res.json().access;

res = http.get(`${URL}/my/crocodiles/`, {
  headers: { Authorization: 'Bearer ' + accessToken }
});
check(res, { 'list crocodiles status is 200': (r) => r.status === 200 });

res = http.post(`${URL}/my/crocodiles/`, JSON.stringify({
  name: 'Random croc',
  sex: 'M',
  date_of_birth: '1900-10-28'
}), {
  headers: {
    Authorization: 'Bearer ' + accessToken,
    'Content-Type': 'application/json'
  }
});
check(res, { 'create crocodile status is 201': (r) => r.status === 201 });

const newCrocodileId = res.json().id;

res = http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({
  name: 'Updated Random croc',
  sex: 'M',
  date_of_birth: '1900-10-28'
}), {
  headers: {
    Authorization: 'Bearer ' + accessToken,
    'Content-Type': 'application/json'
  }
});
check(res, { 'update crocodile status is 200': (r) => r.status === 200 });

res = http.patch(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ sex: 'F' }), {
  headers: {
    Authorization: 'Bearer ' + accessToken,
    'Content-Type': 'application/json'
  }
});
check(res, { 'patch crocodile status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [13, 23, 41, 50, 68, 82, 99]
- **Snippet:**
```js
HTTP requests are sent with params containing headers only, and no tags are attached to identify endpoints or user-flow steps.
```
- **Refactored:**
```js
http.post(`${URL}/user/register/`, JSON.stringify(credentials), {
  headers: { 'Content-Type': 'application/json' },
  tags: { name: 'RegisterUser', flow: 'CrocodileCRUD' }
});

res = http.post(`${URL}/auth/token/login/`, JSON.stringify({
  username: credentials.username,
  password: credentials.password
}), {
  headers: { 'Content-Type': 'application/json' },
  tags: { name: 'Login', flow: 'CrocodileCRUD' }
});

res = http.get(`${URL}/my/crocodiles/`, {
  headers: { Authorization: 'Bearer ' + accessToken },
  tags: { name: 'ListCrocodiles', flow: 'CrocodileCRUD' }
});

res = http.post(`${URL}/my/crocodiles/`, JSON.stringify({
  name: 'Random croc',
  sex: 'M',
  date_of_birth: '1900-10-28'
}), {
  headers: {
    Authorization: 'Bearer ' + accessToken,
    'Content-Type': 'application/json'
  },
  tags: { name: 'CreateCrocodile', flow: 'CrocodileCRUD' }
});

res = http.get(`${URL}/my/crocodiles/${newCrocodileId}/`, {
  headers: { Authorization: 'Bearer ' + accessToken },
  tags: { name: 'GetCrocodileById', flow: 'CrocodileCRUD' }
});

res = http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({
  name: 'Updated Random croc',
  sex: 'M',
  date_of_birth: '1900-10-28'
}), {
  headers: {
    Authorization: 'Bearer ' + accessToken,
    'Content-Type': 'application/json'
  },
  tags: { name: 'UpdateCrocodile', flow: 'CrocodileCRUD' }
});

res = http.patch(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ sex: 'F' }), {
  headers: {
    Authorization: 'Bearer ' + accessToken,
    'Content-Type': 'application/json'
  },
  tags: { name: 'PatchCrocodile', flow: 'CrocodileCRUD' }
});
```

### `script_96.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [6]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
import http from 'k6/http';
import { check } from 'k6';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'], 
  },
};

const URL= 'http://localhost:8000';
```

**Smell 3: Not checking requests**

- **Lines:** [13, 23, 41, 50, 82, 99]
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
check(registerRes, { 'User registered successfully': (r) => r.status === 201 });
```

**Smell 4: Not using tags**

- **Lines:** [13, 23, 41, 50, 68, 82, 99]
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
            name: 'RegisterUser',
        },
    }
);
```

---

## `script_97.js`

### `script_97.js` — CLAUDE

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
		'http_req_duration{name:Merchant - All Orders}': ['p(95)<500'],
		'http_req_duration{name:Merchant - wc-admin/onboarding/tasks?}': ['p(95)<500'],
		'http_req_duration{name:Merchant - wc-analytics/admin/notes?}': ['p(95)<500'],
		'http_req_duration{name:Merchant - wc-admin/options?options=poocommerce_ces_tracks_queue}': ['p(95)<500'],
		'http_req_duration{name:Merchant - action=heartbeat}': ['p(95)<500'],
		'http_req_duration{name:Merchant - Completed Orders}': ['p(95)<500'],
		http_req_failed: ['rate<0.01'],
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
		'http_req_duration{name:Merchant - All Orders}': ['p(95)<500'],
		'http_req_duration{name:Merchant - Completed Orders}': ['p(95)<500'],
		'http_req_duration{name:Merchant - action=heartbeat}': ['p(95)<300'],
	},
};

export default function () {
	orders();
}
```

### `script_97.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [36]
- **Snippet:**
```js
/* The script lacks an 'export const options = {}' block with thresholds to define pass/fail criteria. */
```
- **Refactored:**
```js
export const options = {
  vus: 10,
  duration: '1m',
  thresholds: {
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
    // Threshold for a specific request tagged with 'name:Merchant - All Orders'
    'http_req_duration{name:Merchant - All Orders}': ['p(95)<300'],
  },
};

export function orders( includeTests = {} ) { /* ... */ }
```

---

## `script_98.js`

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
		'http_req_duration{name:Merchant - WC-Admin}': ['p(95)<500'],
		'http_req_duration{name:Merchant - wc-admin/onboarding/tasks?}': ['p(95)<500'],
		'http_req_duration{name:Merchant - wc-analytics/admin/notes?}': ['p(95)<500'],
		'http_req_duration{name:Merchant - wc-admin/options?options=poocommerce_ces_tracks_queue}': ['p(95)<500'],
		'http_req_duration{name:Merchant - wc-analytics/orders?}': ['p(95)<500'],
		'http_req_duration{name:Merchant - wc-analytics/products/reviews?}': ['p(95)<500'],
		'http_req_duration{name:Merchant - wc-analytics/products/low-in-stock?}': ['p(95)<500'],
		'http_req_failed': ['rate<0.01'],
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
// No export const options with thresholds is defined in this script.
```
- **Refactored:**
```js
export const options = {
	thresholds: {
		http_req_failed: ['rate<0.01'],
		http_req_duration: ['p(95)<1000'],
		'http_req_duration{name:Merchant - WC-Admin}': ['p(95)<1000'],
		'http_req_duration{name:Merchant - wc-admin/onboarding/tasks?}': ['p(95)<1000'],
		'http_req_duration{name:Merchant - wc-analytics/admin/notes?}': ['p(95)<1000'],
		'http_req_duration{name:Merchant - wc-admin/options?options=poocommerce_ces_tracks_queue}': ['p(95)<1000'],
		'http_req_duration{name:Merchant - wc-analytics/orders?}': ['p(95)<1000'],
		'http_req_duration{name:Merchant - wc-analytics/products/reviews?}': ['p(95)<1000'],
		'http_req_duration{name:Merchant - wc-analytics/products/low-in-stock?}': ['p(95)<1000'],
	},
};

export default function () {
	homeWCAdmin();
}
```

### `script_98.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [26]
- **Snippet:**
```js
// The script does not export an 'options' object with a 'thresholds' configuration.
// Without thresholds, the test will always pass in a CI/CD environment,
// regardless of the system's performance.
```
- **Refactored:**
```js
/**
 * Internal dependencies
 */
import { base_url, think_time_min, think_time_max } from '../../config.js';
import {
	htmlRequestHeader,
	jsonAPIRequestHeader,
	commonRequestHeaders,
	commonGetRequestHeaders,
	commonAPIGetRequestHeaders,
	commonNonStandardHeaders,
} from '../../headers.js';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<1500'], // 95% of requests should be below 1.5s
    'http_req_duration{name:Merchant - WC-Admin}': ['p(95)<800'], // The main dashboard page should be fast
    'checks': ['rate>0.99'], // more than 99% of checks must pass
  },
};

export function homeWCAdmin( includeTests = {} ) {
```

---

## `script_99.js`

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
		http_req_duration: ['p(95)<500'],
		'http_req_duration{name:Merchant - New Order Page}': ['p(95)<3000'],
		'http_req_duration{name:Merchant - Create New Order}': ['p(95)<3000'],
		'http_req_duration{name:Merchant - Open Order}': ['p(95)<3000'],
		'http_req_duration{name:Merchant - Update Existing Order Status}': ['p(95)<3000'],
		http_req_failed: ['rate<0.01'],
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
		checks: ['rate>0.99'],
		http_req_failed: ['rate<0.01'],
		http_req_duration: ['p(95)<1000'],
		'http_req_duration{name:Merchant - New Order Page}': ['p(95)<1500'],
		'http_req_duration{name:Merchant - Create New Order}': ['p(95)<1500'],
		'http_req_duration{name:Merchant - Open Order}': ['p(95)<1000'],
		'http_req_duration{name:Merchant - Update Existing Order Status}': ['p(95)<1500'],
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
The script file does not contain an `export const options` block, and therefore, no thresholds are defined to set pass/fail criteria for the test.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    // Fail the test if more than 1% of requests return an error.
    'http_req_failed': ['rate<0.01'],
    // 95% of all requests must complete within 2000ms.
    'http_req_duration': ['p(95)<2000'],
    // 95% of requests tagged as 'Merchant - Create New Order' must be below 800ms.
    'http_req_duration{name:Merchant - Create New Order}': ['p(95)<800'],
  },
};

/* eslint-disable import/no-unresolved */
/**
 * External dependencies
 */
// ... rest of the script
```

---

## `script_100.js`

### `script_100.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [15, 30, 43, 58, 71, 85]
- **Snippet:**
```js
const ordersResponse = http.get(ordersUrl, { headers: this.headers });
const ordersTableResponse = http.get(ordersTableUrl, { headers: this.headers });
const orderDetailResponse = http.get(orderDetailUrl, { headers: this.headers });
const itemListTableResponse = http.get(itemListTableUrl, { headers: this.headers });
const totalItemListResponse = http.get(totalItemListUrl, { headers: this.headers });
const triggerEventResponse = http.get(triggerEventUrl, { headers: this.headers });
```
- **Refactored:**
```js
const ordersResponse = http.get(ordersUrl, { headers: this.headers, tags: { name: 'Orders' } });
const ordersTableResponse = http.get(ordersTableUrl, { headers: this.headers, tags: { name: 'OrdersTableData' } });
const orderDetailResponse = http.get(orderDetailUrl, { headers: this.headers, tags: { name: 'OrderDetail' } });
const itemListTableResponse = http.get(itemListTableUrl, { headers: this.headers, tags: { name: 'ItemListTable' } });
const totalItemListResponse = http.get(totalItemListUrl, { headers: this.headers, tags: { name: 'TotalItemList' } });
const triggerEventResponse = http.get(triggerEventUrl, { headers: this.headers, tags: { name: 'TriggerEvent' } });
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
const ordersResponse = http.get(ordersUrl, {
  headers: this.headers,
  tags: { name: 'Orders - All' },
});
```

---

## `script_101.js`

### `script_101.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]
- **Snippet:**
```js
res = http.post(
    `${URL}/my/crocodiles/`,
    JSON.stringify({ name: 'Random croc', sex: 'M', date_of_birth: '1900-10-28' }),
    { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' }, tags: { name: 'createNewCrocodileURL' } }
);
const newCrocodileId = res.json().id;
```
- **Refactored:**
```js
res = http.post(
    `${URL}/my/crocodiles/`,
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
        tags: {
            name: 'createNewCrocodileURL'
        }
    }
);

check(res, {
    'status is 201': (r) => r.status === 201,
    'has crocodile id': (r) => r.json().id !== undefined,
    'crocodile name': (r) => r.json().name === 'Random croc'
});

const newCrocodileId = res.json().id;
```

### `script_101.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125]
- **Snippet:**
```js
res = http.post(
    `${URL}/my/crocodiles/`,
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
        },
        tags: {
            name: 'createNewCrocodileURL'
        }
    }
);
```
- **Refactored:**
```js
res = http.post(
    `${URL}/my/crocodiles/`,
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
        },
        tags: {
            name: 'createNewCrocodileURL'
        }
    }
);

check(res, {
    'status is 201': (r) => r.status === 201,
    'crocodile name is correct': (r) => r.json().name === 'Random croc'
});
```

---

## `script_102.js`

### `script_102.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** []
- **Snippet:**
```js
No export const options with thresholds is defined in the provided k6 code.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    'http_req_duration{name:PostResource}': ['p(95)<500'],
    'http_req_duration{name:PatchResource}': ['p(95)<500'],
    'http_req_duration{name:DeleteResource}': ['p(95)<500'],
    'http_req_duration{name:GetResource}': ['p(95)<500'],
    'http_req_duration{name:RunConsoleCommands}': ['p(95)<1000']
  }
};
```

**Smell 3: Not checking requests**

- **Lines:** [57, 58, 59, 60, 61, 62, 63, 64, 65, 66]
- **Snippet:**
```js
runConsoleCommands(commands) {
  return http.post(
    http.url`${EnvironmentUtil.getBackendApiUrl()}/dynamic-fixtures`,
    JSON.stringify(this._getConsoleCommandsPayload(commands)),
    {
      headers: {
        'Content-Type': 'application/vnd.api+json',
      },
    }
  );
}
```
- **Refactored:**
```js
runConsoleCommands(commands) {
  const response = http.post(
    http.url`${EnvironmentUtil.getBackendApiUrl()}/dynamic-fixtures`,
    JSON.stringify(this._getConsoleCommandsPayload(commands)),
    {
      headers: {
        'Content-Type': 'application/vnd.api+json',
      },
      tags: { name: 'RunConsoleCommands', endpoint: '/dynamic-fixtures' },
    }
  );

  addErrorToCounter(check(response, {
    '[POST] /dynamic-fixtures was successful.': (r) => r.status >= 200 && r.status < 300,
  }));

  return response;
}
```

**Smell 4: Not using tags**

- **Lines:** [19, 32, 41, 50, 58, 59, 60, 61, 62, 63, 64, 65, 66]
- **Snippet:**
```js
http.post(fullUrl, JSON.stringify(payload), { headers: this.headers });
http.patch(fullUrl, JSON.stringify(payload), { headers: this.headers });
http.del(fullUrl, null, { headers: this.headers });
http.get(fullUrl, { headers: this.headers });
http.post(..., { headers: { 'Content-Type': 'application/vnd.api+json' } });
```
- **Refactored:**
```js
postRequest(resourceUrl, payload) {
  const fullUrl = `${EnvironmentUtil.getStorefrontApiUrl()}/${resourceUrl}`;
  const response = http.post(fullUrl, JSON.stringify(payload), {
    headers: this.headers,
    tags: { name: 'PostResource', method: 'POST', endpoint: resourceUrl },
  });
  addErrorToCounter(check(response, { [`[POST] ${fullUrl} was successful.`]: (r) => r.status === 201 }));
  return response;
}

patchRequest(resourceUrl, payload) {
  const fullUrl = `${EnvironmentUtil.getStorefrontApiUrl()}/${resourceUrl}`;
  const response = http.patch(fullUrl, JSON.stringify(payload), {
    headers: this.headers,
    tags: { name: 'PatchResource', method: 'PATCH', endpoint: resourceUrl },
  });
  addErrorToCounter(check(response, { [`[PATCH] ${fullUrl} was successful.`]: (r) => r.status === 200 }));
  return response;
}

deleteRequest(resourceUrl) {
  const fullUrl = `${EnvironmentUtil.getStorefrontApiUrl()}/${resourceUrl}`;
  const response = http.del(fullUrl, null, {
    headers: this.headers,
    tags: { name: 'DeleteResource', method: 'DELETE', endpoint: resourceUrl },
  });
  addErrorToCounter(check(response, { [`[DELETE] ${fullUrl} was successful.`]: (r) => r.status === 204 }));
  return response;
}

getRequest(resourceUrl) {
  const fullUrl = `${EnvironmentUtil.getStorefrontApiUrl()}/${resourceUrl}`;
  const response = http.get(fullUrl, {
    headers: this.headers,
    tags: { name: 'GetResource', method: 'GET', endpoint: resourceUrl },
  });
  addErrorToCounter(check(response, { [`[GET] ${fullUrl} was successful.`]: (r) => r.status === 200 }));
  return response;
}
```

### `script_102.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]
- **Snippet:**
```js
runConsoleCommands(commands) {
    return http.post(
      http.url`${EnvironmentUtil.getBackendApiUrl()}/dynamic-fixtures`,
      JSON.stringify(this._getConsoleCommandsPayload(commands)),
      {
        headers: {
          'Content-Type': 'application/vnd.api+json',
        },
      }
    );
  }
```
- **Refactored:**
```js
runConsoleCommands(commands) {
    const fullUrl = http.url`${EnvironmentUtil.getBackendApiUrl()}/dynamic-fixtures`;
    const response = http.post(
      fullUrl,
      JSON.stringify(this._getConsoleCommandsPayload(commands)),
      {
        headers: {
          'Content-Type': 'application/vnd.api+json',
        },
      }
    );

    addErrorToCounter(check(response, { [`[POST] ${fullUrl} was successful.`]: (r) => r.status === 204 })); // Assuming 204 No Content

    return response;
  }
```

**Smell 4: Not using tags**

- **Lines:** [19, 32, 41, 50, 58]
- **Snippet:**
```js
const response = http.post(fullUrl, JSON.stringify(payload), { headers: this.headers });
```
- **Refactored:**
```js
postRequest(resourceUrl, payload) {
    const fullUrl = `${EnvironmentUtil.getStorefrontApiUrl()}/${resourceUrl}`;
    const params = {
      headers: this.headers,
      tags: {
        name: resourceUrl, // Tag request by its resource URL
      },
    };
    const response = http.post(fullUrl, JSON.stringify(payload), params);

    addErrorToCounter(check(response, { [`[POST] ${fullUrl} was successful.`]: (r) => r.status === 201 }));

    if (response.status !== 201) {
      console.log(response.body);
    }

    return response;
  }
```

---

## `script_103.js`

### `script_103.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [21, 22, 28]
- **Snippet:**
```js
http.get('https://test.k6.io/assets.php');
http.get('https://test.k6.io/assets.php');
...
http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
group('Assets', function () {
    let assetRes1 = http.get('https://test.k6.io/assets.php');
    check(assetRes1, { 'assets status is 200': (r) => r.status === 200 });
    let assetRes2 = http.get('https://test.k6.io/assets.php');
    check(assetRes2, { 'assets status is 200': (r) => r.status === 200 });
});
...
group('News page', function () {
    let newsRes = http.get('https://test.k6.io/news.php');
    check(newsRes, { 'news status is 200': (r) => r.status === 200 });
});
```

**Smell 4: Not using tags**

- **Lines:** [17, 21, 22, 28]
- **Snippet:**
```js
http.get('https://test.k6.io');
http.get('https://test.k6.io/assets.php');
http.get('https://test.k6.io/assets.php');
http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
group('Main page', function () {
    let res = http.get('https://test.k6.io', { tags: { name: 'MainPage' } });
    check(res, { 'status is 200': (r) => r.status === 200 });

    group('Assets', function () {
        let assetRes1 = http.get('https://test.k6.io/assets.php', { tags: { name: 'Assets' } });
        check(assetRes1, { 'assets status is 200': (r) => r.status === 200 });
        let assetRes2 = http.get('https://test.k6.io/assets.php', { tags: { name: 'Assets' } });
        check(assetRes2, { 'assets status is 200': (r) => r.status === 200 });
    });
});

group('News page', function () {
    let newsRes = http.get('https://test.k6.io/news.php', { tags: { name: 'NewsPage' } });
    check(newsRes, { 'news status is 200': (r) => r.status === 200 });
});
```

### `script_103.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [21, 22, 28]
- **Snippet:**
```js
http.get('https://test.k6.io/assets.php');
http.get('https://test.k6.io/assets.php');
http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
group('Assets', function () {
    let assetsRes1 = http.get('https://test.k6.io/assets.php');
    check(assetsRes1, { 'assets request 1 status is 200': (r) => r.status === 200 });

    let assetsRes2 = http.get('https://test.k6.io/assets.php');
    check(assetsRes2, { 'assets request 2 status is 200': (r) => r.status === 200 });
});

group('News page', function () {
    let newsRes = http.get('https://test.k6.io/news.php');
    check(newsRes, { 'news page status is 200': (r) => r.status === 200 });
});
```

**Smell 4: Not using tags**

- **Lines:** [17, 21, 22, 28]
- **Snippet:**
```js
let res = http.get('https://test.k6.io');
http.get('https://test.k6.io/assets.php');
http.get('https://test.k6.io/assets.php');
http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
group('Main page', function () {
    let res = http.get('https://test.k6.io', { tags: { name: 'MainPage', page: 'main' } });
    check(res, { 'status is 200': (r) => r.status === 200 }, { page: 'main' });

    group('Assets', function () {
        let assetsRes1 = http.get('https://test.k6.io/assets.php', { tags: { name: 'MainAssets', page: 'main', resource: 'assets' } });
        check(assetsRes1, { 'assets request 1 status is 200': (r) => r.status === 200 }, { page: 'main', resource: 'assets' });

        let assetsRes2 = http.get('https://test.k6.io/assets.php', { tags: { name: 'MainAssets', page: 'main', resource: 'assets' } });
        check(assetsRes2, { 'assets request 2 status is 200': (r) => r.status === 200 }, { page: 'main', resource: 'assets' });
    });
});

group('News page', function () {
    let newsRes = http.get('https://test.k6.io/news.php', { tags: { name: 'NewsPage', page: 'news' } });
    check(newsRes, { 'news page status is 200': (r) => r.status === 200 }, { page: 'news' });
});
```

### `script_103.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [21, 22, 28]
- **Snippet:**
```js
group('Assets', function () {
    http.get('https://test.k6.io/assets.php');
    http.get('https://test.k6.io/assets.php');
});
...
group('News page', function () {
    http.get('https://test.k6.io/news.php');
});
```
- **Refactored:**
```js
group('Assets', function () {
    check(http.get('https://test.k6.io/assets.php'), { 'assets status is 200': (r) => r.status === 200 });
    check(http.get('https://test.k6.io/assets.php'), { 'assets status is 200': (r) => r.status === 200 });
});
...
group('News page', function () {
    check(http.get('https://test.k6.io/news.php'), { 'news status is 200': (r) => r.status === 200 });
});
```

---

## `script_104.js`

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
  check(res, {
    'status is 500': (r) => r.status == 500,
  }, { myTag: 'status500' });
```

### `script_104.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [15, 20]
- **Snippet:**
```js
res = http.get('https://quickpizza.grafana.com/api/status/500');
...
res = http.get('https://quickpizza.grafana.com/api/status/200');
```
- **Refactored:**
```js
res = http.get('https://quickpizza.grafana.com/api/status/500', {
  tags: { name: 'Status500' },
});
...
res = http.get('https://quickpizza.grafana.com/api/status/200', {
  tags: { name: 'Status200' },
});
```

---

## `script_105.js`

### `script_105.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 44, 45, 46, 47, 48, 51, 52, 53, 54]
- **Snippet:**
```js
export default function () {
    const server = __ENV.SERVER;
    const urls = {
        fastapi: { root: 'http://0.0.0.0:8000', ... },
        express: { ... },
        laravel: { ... }
    };
    const params = { headers: { 'Content-Type': 'application/json' } };
    const createItemData = JSON.stringify({ index: '3', name: 'Under pressure' });
}
```
- **Refactored:**
```js
import http from 'k6/http';
import { check, sleep } from 'k6';
import { Trend, Rate } from 'k6/metrics';

const listErrorRate = new Rate('Root_errors');
const itemErrorRate = new Rate('Item_errors');
const createErrorRate = new Rate('Create_item_error');
const RootTrend = new Trend('Show_root');
const ItemTrend = new Trend('Show_item_one');
const CreateTrend = new Trend('Create_item');

// Move static data to init context
const server = __ENV.SERVER;
const urls = {
    fastapi: {
        root: 'http://0.0.0.0:8000',
        itemOne: 'http://0.0.0.0:8000/items/1',
        create: 'http://0.0.0.0:8000/items/'
    },
    express: {
        root: 'http://0.0.0.0:8001',
        itemOne: 'http://0.0.0.0:8001/items/1',
        create: 'http://0.0.0.0:8001/items/'
    },
    laravel: {
        root: 'http://0.0.0.0:8002/api',
        itemOne: 'http://0.0.0.0:8002/api/items/1',
        create: 'http://0.0.0.0:8002/api/items/'
    }
};
const params = {
    headers: {
        'Content-Type': 'application/json',
    },
};
const createItemData = JSON.stringify({
    index: '3',
    name: 'Under pressure',
});

export const options = {
    thresholds: {
        'Show_root': ['p(95)<500'],
        'Show_item_one': ['p(95)<500'],
        'Create_item': ['p(95)<500'],
        'Root_errors': ['rate<0.01'],
        'Item_errors': ['rate<0.01'],
        'Create_item_error': ['rate<0.01'],
    },
};

export default function () {
    const urlRoot = urls[server].root;
    const urlItemOne = urls[server].itemOne;
    const urlCreate = urls[server].create;
    // ... rest of the function
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [13, 14, 15, 16]
- **Snippet:**
```js
thresholds: {
    'Show_root': ['p(95)<500'],
    'Show_item_one': ['p(95)<500'],
},
```
- **Refactored:**
```js
thresholds: {
    'Show_root': ['p(95)<500'],
    'Show_item_one': ['p(95)<500'],
    'Create_item': ['p(95)<500'],
    'Root_errors': ['rate<0.01'],
    'Item_errors': ['rate<0.01'],
    'Create_item_error': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
},
```

### `script_105.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [44, 45, 46, 47, 48, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 75]
- **Snippet:**
```js
const params = {
    headers: {
    'Content-Type': 'application/json',
    },
};

const requests = {
    'Get root': {
        method: 'GET',
        url: urlRoot,
        params: params
    },
    'Get item one': {
        method: 'GET',
        url: urlItemOne,
        params: params
    },
    'Create item': {
        method: 'POST',
        url: urlCreate,
        params: params,
        body: createItemData
    }
};

const responses = http.batch(requests);
```
- **Refactored:**
```js
const baseParams = {
    headers: {
        'Content-Type': 'application/json',
    },
};

const requests = {
    'Get root': {
        method: 'GET',
        url: urlRoot,
        params: {
            ...baseParams,
            tags: { name: 'Get root', endpoint: 'root', operation: 'read' },
        },
    },
    'Get item one': {
        method: 'GET',
        url: urlItemOne,
        params: {
            ...baseParams,
            tags: { name: 'Get item one', endpoint: 'item_one', operation: 'read' },
        },
    },
    'Create item': {
        method: 'POST',
        url: urlCreate,
        params: {
            ...baseParams,
            tags: { name: 'Create item', endpoint: 'items', operation: 'create' },
        },
        body: createItemData,
    },
};

const responses = http.batch(requests);
```

### `script_105.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [13, 14, 15, 16]
- **Snippet:**
```js
thresholds: {
        'Show_root': ['p(95)<500'],
        'Show_item_one': ['p(95)<500'],
    },
```
- **Refactored:**
```js
thresholds: {
        'Show_root': ['p(95)<500'],
        'Show_item_one': ['p(95)<500'],
        'Create_item': ['p(95)<500'],
        'Root_errors': ['rate<0.01'],
        'Item_errors': ['rate<0.01'],
        'Create_item_error': ['rate<0.01'],
    },
```

**Smell 4: Not using tags**

- **Lines:** [85, 93, 99]
- **Snippet:**
```js
RootTrend.add(rootResp.timings.duration);

ItemTrend.add(itemResp.timings.duration)

CreateTrend.add(createResp.timings.duration);
```
- **Refactored:**
```js
const tags = { server: server };

RootTrend.add(rootResp.timings.duration, tags);

ItemTrend.add(itemResp.timings.duration, tags);

CreateTrend.add(createResp.timings.duration, tags);
```

---

## `script_106.js`

### `script_106.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76]
- **Snippet:**
```js
const requests = {
    'Get root': {
        method: 'GET',
        url: urlRoot,
        params: params
    },
    'Get item one': {
        method: 'GET',
        url: urlItemOne,
        params: params
    },
    'Create item': {
        method: 'POST',
        url: urlCreate,
        params: params,
        body: createItemData
    }
};
const responses = http.batch(requests);
```
- **Refactored:**
```js
const paramsRoot = { headers: { 'Content-Type': 'application/json' }, tags: { name: 'Get root' } };
const paramsItem = { headers: { 'Content-Type': 'application/json' }, tags: { name: 'Get item one' } };
const paramsCreate = { headers: { 'Content-Type': 'application/json' }, tags: { name: 'Create item' } };

const requests = {
    'Get root': {
        method: 'GET',
        url: urlRoot,
        params: paramsRoot
    },
    'Get item one': {
        method: 'GET',
        url: urlItemOne,
        params: paramsItem
    },
    'Create item': {
        method: 'POST',
        url: urlCreate,
        params: paramsCreate,
        body: createItemData
    }
};
const responses = http.batch(requests);
```

### `script_106.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [45, 46, 47, 48, 49, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76]
- **Snippet:**
```js
const params = {
    headers: {
    'Content-Type': 'application/json',
    },
};
...
const requests = {
    'Get root': {
        method: 'GET',
        url: urlRoot,
        params: params
    },
    'Get item one': {
        method: 'GET',
        url: urlItemOne,
        params: params
    },
    'Create item': {
        method: 'POST',
        url: urlCreate,
        params: params,
        body: createItemData
    }
};

const responses = http.batch(requests);
```
- **Refactored:**
```js
const baseHeaders = {
    'Content-Type': 'application/json',
};

const requests = {
    'Get root': {
        method: 'GET',
        url: urlRoot,
        params: {
            headers: baseHeaders,
            tags: { name: 'GetRoot', endpoint: 'root', operation: 'read' },
        },
    },
    'Get item one': {
        method: 'GET',
        url: urlItemOne,
        params: {
            headers: baseHeaders,
            tags: { name: 'GetItemOne', endpoint: 'items/:id', operation: 'read' },
        },
    },
    'Create item': {
        method: 'POST',
        url: urlCreate,
        params: {
            headers: baseHeaders,
            tags: { name: 'CreateItem', endpoint: 'items', operation: 'create' },
        },
        body: createItemData,
    },
};

const responses = http.batch(requests);
```

### `script_106.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [14, 15, 16, 17]
- **Snippet:**
```js
thresholds: {
    'Show_root': ['p(95)<500'],
    'Show_item_one': ['p(95)<500'],
},
```
- **Refactored:**
```js
thresholds: {
    'Show_root': ['p(95)<500'],
    'Show_item_one': ['p(95)<500'],
    'Create_item': ['p(95)<500'], // Added threshold for the create operation
    'Root_errors': ['rate<0.01'],   // Added thresholds for error rates
    'Item_errors': ['rate<0.01'],
    'Create_item_error': ['rate<0.01'],
},
```

**Smell 4: Not using tags**

- **Lines:** [57, 58, 63, 68]
- **Snippet:**
```js
const requests = {
    'Get root': {
        method: 'GET',
        url: urlRoot,
        params: params
    },
    'Get item one': { ... },
    'Create item': { ... }
};
```
- **Refactored:**
```js
const requests = {
    'Get root': {
        method: 'GET',
        url: urlRoot,
        params: { headers: params.headers, tags: { name: 'GetRoot' } }
    },
    'Get item one': {
        method: 'GET',
        url: urlItemOne,
        params: { headers: params.headers, tags: { name: 'GetItemOne' } }
    },
    'Create item': {
        method: 'POST',
        url: urlCreate,
        params: { headers: params.headers, tags: { name: 'CreateItem' } },
        body: createItemData
    }
};
```

---

## `script_107.js`

### `script_107.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [21, 22, 28]
- **Snippet:**
```js
http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/9c2fd369-e719-4ee0-90d0-ffd889e2c8b5');
```
- **Refactored:**
```js
// nested group Assets
group('Assets', function () {
    let res1 = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
    check(res1, { 'Assets request 1 status is 200': (r) => r.status === 200 });
    let res2 = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
    check(res2, { 'Assets request 2 status is 200': (r) => r.status === 200 });
});

// Group: News page
group('News page', function () {
    let res = http.get('https://run.mocky.io/v3/9c2fd369-e719-4ee0-90d0-ffd889e2c8b5');
    check(res, { 'News page status is 200': (r) => r.status === 200 });
});
```

**Smell 4: Not using tags**

- **Lines:** [17, 21, 22, 28]
- **Snippet:**
```js
http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/9c2fd369-e719-4ee0-90d0-ffd889e2c8b5');
```
- **Refactored:**
```js
// Group: Main page
group('Main page', function () {
    let res = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms', { tags: { name: 'MainPage' } });
    check(res, { 'status is 200': (r) => r.status === 200 });
    // nested group
    group('Assets', function () {
        let res1 = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms', { tags: { name: 'MainPage_Asset1' } });
        check(res1, { 'Assets request 1 status is 200': (r) => r.status === 200 });
        let res2 = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms', { tags: { name: 'MainPage_Asset2' } });
        check(res2, { 'Assets request 2 status is 200': (r) => r.status === 200 });
    });
});

// Group: News page
group('News page', function () {
    let res = http.get('https://run.mocky.io/v3/9c2fd369-e719-4ee0-90d0-ffd889e2c8b5', { tags: { name: 'NewsPage' } });
    check(res, { 'News page status is 200': (r) => r.status === 200 });
});
```

### `script_107.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [21, 22, 28]
- **Snippet:**
```js
http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/9c2fd369-e719-4ee0-90d0-ffd889e2c8b5');
```
- **Refactored:**
```js
let assetRes1 = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
check(assetRes1, { 'asset 1 status is 200': (r) => r.status === 200 });

let assetRes2 = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
check(assetRes2, { 'asset 2 status is 200': (r) => r.status === 200 });

let newsRes = http.get('https://run.mocky.io/v3/9c2fd369-e719-4ee0-90d0-ffd889e2c8b5');
check(newsRes, { 'news page status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [17, 21, 22, 28]
- **Snippet:**
```js
let res = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/9c2fd369-e719-4ee0-90d0-ffd889e2c8b5');
```
- **Refactored:**
```js
let res = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms', {
  tags: { name: 'MainPage', page: 'main', type: 'html' }
});

let assetRes1 = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms', {
  tags: { name: 'MainPageAsset1', page: 'main', type: 'asset' }
});

let assetRes2 = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms', {
  tags: { name: 'MainPageAsset2', page: 'main', type: 'asset' }
});

let newsRes = http.get('https://run.mocky.io/v3/9c2fd369-e719-4ee0-90d0-ffd889e2c8b5', {
  tags: { name: 'NewsPage', page: 'news', type: 'html' }
});
```

### `script_107.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [21, 22, 28]
- **Snippet:**
```js
group('Assets', function () {
    http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
    http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
});
...
group('News page',  function () {
    http.get('https://run.mocky.io/v3/9c2fd369-e719-4ee0-90d0-ffd889e2c8b5');
})
```
- **Refactored:**
```js
group('Assets', function () {
    const assetRes1 = http.get('...');
    check(assetRes1, { 'asset 1 status is 200': (r) => r.status === 200 });
    const assetRes2 = http.get('...');
    check(assetRes2, { 'asset 2 status is 200': (r) => r.status === 200 });
});

group('News page',  function () {
    const newsRes = http.get('...');
    check(newsRes, { 'news page status is 200': (r) => r.status === 200 });
})
```

**Smell 4: Not using tags**

- **Lines:** [17, 21, 22, 28]
- **Snippet:**
```js
let res = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
...
http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
...
http.get('https://run.mocky.io/v3/9c2fd369-e719-4ee0-90d0-ffd889e2c8b5');
```
- **Refactored:**
```js
group('Main page',  function () {
    let res = http.get('...', { tags: { name: 'MainPageHTML' } });
    // ...
    group('Assets', function () {
        http.get('...', { tags: { name: 'Asset-CSS' } });
        http.get('...', { tags: { name: 'Asset-JS' } });
    });
})

group('News page',  function () {
    http.get('...', { tags: { name: 'NewsPageHTML' } });
})
```

---

## `script_108.js`

### `script_108.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [21, 22, 28]
- **Snippet:**
```js
http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/46ac01d8-7d2d-4994-b594-4f359c79756d');
```
- **Refactored:**
```js
group('Assets', function () {
    let res1 = http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms');
    check(res1, { 'Assets status is 200': (r) => r.status === 200 });
    let res2 = http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms');
    check(res2, { 'Assets status is 200': (r) => r.status === 200 });
});

group('News page', function () {
    let res = http.get('https://run.mocky.io/v3/46ac01d8-7d2d-4994-b594-4f359c79756d');
    check(res, { 'News page status is 200': (r) => r.status === 200 });
});
```

### `script_108.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [21, 22, 28]
- **Snippet:**
```js
http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms');
```
- **Refactored:**
```js
let res = http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms');
check(res, { 'status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [17, 21, 22, 28]
- **Snippet:**
```js
let res = http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms');
```
- **Refactored:**
```js
let res = http.get(
  'https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms',
  { tags: { name: 'MainPageHTML' } }
);
```

---

## `script_109.js`

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
		'http_req_duration{name:Shopper - View Checkout}': ['p(95)<500'],
		'http_req_duration{name:Shopper - Login to Checkout}': ['p(95)<500'],
		'http_req_duration{name:Shopper - Store API update-customer}': ['p(95)<500'],
		'http_req_duration{name:Shopper - Store API checkout}': ['p(95)<500'],
		'http_req_duration{name:Shopper - Order Received}': ['p(95)<500'],
		'http_req_duration{name:Shopper - wc-ajax=get_refreshed_fragments}': ['p(95)<500'],
		http_req_failed: ['rate<0.01'],
	},
};

export default function () {
	checkoutCustomerLogin();
}
```

### `script_109.js` — CHATGPT

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
		'http_req_duration{name:Shopper - View Checkout}': ['p(95)<1000'],
		'http_req_duration{name:Shopper - Login to Checkout}': ['p(95)<1000'],
		'http_req_duration{name:Shopper - Store API update-customer}': ['p(95)<1000'],
		'http_req_duration{name:Shopper - Store API checkout}': ['p(95)<1500'],
		'http_req_duration{name:Shopper - Order Received}': ['p(95)<1000'],
		'http_req_duration{name:Shopper - wc-ajax=get_refreshed_fragments}': ['p(95)<1000'],
	},
};

export default function () {
	checkoutCustomerLogin();
}
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

- **Lines:** [46]
- **Snippet:**
```js
import { checkResponse } from '../../utils.js';

export function checkoutCustomerLogin() {
```
- **Refactored:**
```js
import { checkResponse } from '../../utils.js';

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'], // Global failure rate should be less than 1%
    'http_req_duration{name:Shopper - View Checkout}': ['p(95)<500'], // 95% of checkout view requests should be below 500ms
    'http_req_duration{name:Shopper - Login to Checkout}': ['p(95)<800'],
    'http_req_duration{name:Shopper - Store API checkout}': ['p(95)<1500'],
  },
};

export function checkoutCustomerLogin() {
```

---

## `script_110.js`

### `script_110.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [54]
- **Snippet:**
```js
let addToCart = http.post(cartParams);
```
- **Refactored:**
```js
let addToCart = http.post(cartParams);
check(addToCart, {
  'add to cart status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [20, 42, 54, 63]
- **Snippet:**
```js
let homepage = http.get('https://onlineboutique.dev');
let productLinkClick = http.get(productLink);
let addToCart = http.post(cartParams);
let checkout = http.post(checkoutLink);
```
- **Refactored:**
```js
let homepage = http.get('https://onlineboutique.dev', { tags: { name: 'Homepage' } });
let productLinkClick = http.get(productLink, { tags: { name: 'ProductPage' } });
let addToCart = http.post(cartParams, null, { tags: { name: 'AddToCart' } });
let checkout = http.post(checkoutLink, null, { tags: { name: 'Checkout' } });
```

### `script_110.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [54]
- **Snippet:**
```js
let addToCart = http.post(cartParams);
```
- **Refactored:**
```js
let addToCart = http.post(cartParams, null, { tags: { name: 'AddToCart' } });
check(addToCart, {
  'add to cart status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [20, 42, 54, 63]
- **Snippet:**
```js
let homepage = http.get('https://onlineboutique.dev');
let productLinkClick = http.get(productLink);
let addToCart = http.post(cartParams);
let checkout = http.post(checkoutLink);
```
- **Refactored:**
```js
let homepage = http.get('https://onlineboutique.dev', { tags: { name: 'Homepage' } });
let productLinkClick = http.get(productLink, { tags: { name: 'ProductDetail' } });
let addToCart = http.post(cartParams, null, { tags: { name: 'AddToCart' } });
let checkout = http.post(checkoutLink, null, { tags: { name: 'Checkout' } });
```

### `script_110.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [54]
- **Snippet:**
```js
let addToCart = http.post(cartParams);
```
- **Refactored:**
```js
let addToCart = http.post(cartParams);
check(addToCart, {
    'add to cart status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [20, 42, 54, 63]
- **Snippet:**
```js
let homepage = http.get('https://onlineboutique.dev');
// ...
let productLinkClick = http.get(productLink);
// ...
let addToCart = http.post(cartParams);
// ...
let checkout = http.post(checkoutLink);
```
- **Refactored:**
```js
let homepage = http.get('https://onlineboutique.dev', {
  tags: { name: 'Homepage' },
});

let productLinkClick = http.get(productLink, {
  tags: { name: 'ProductPage' },
});

let addToCart = http.post(cartParams, null, {
  tags: { name: 'AddToCart' },
});

let checkout = http.post(checkoutLink, null, {
  tags: { name: 'Checkout' },
});
```

---

## `script_111.js`

### `script_111.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [19, 20, 27, 28, 34, 35, 41, 44]
- **Snippet:**
```js
const {buckets} = s3.listBuckets();
check(buckets, { ... });

const {contents: b1Objects} = s3.listObjects({bucket: "bucket1"})
check(b1Objects, { ... });

const {contents: b2Objects} = s3.listObjects({bucket: "bucket2"})
check(b2Objects, { ... });

const {body} = s3.getObject({bucket: "bucket1", key: "file1.txt"})
check(value, { ... });
```
- **Refactored:**
```js
export const options = {
	iterations: 1,
	thresholds: {
		'checks{operation:listBuckets}': [{threshold: 'rate == 1.00', abortOnFail: true}],
		'checks{operation:listObjects,bucket:bucket1}': [{threshold: 'rate == 1.00', abortOnFail: true}],
		'checks{operation:listObjects,bucket:bucket2}': [{threshold: 'rate == 1.00', abortOnFail: true}],
		'checks{operation:getObject,bucket:bucket1,key:file1.txt}': [{threshold: 'rate == 1.00', abortOnFail: true}],
	},
};

export default async function () {
	const s3 = new S3Client(config);

	const {buckets} = s3.listBuckets();
	check(buckets, {
		'it must return two buckets': (buckets) => buckets.length === 2,
		'bucket1 must be in the list': (buckets) => buckets.some(b => b.name.normalize() === 'bucket1'),
		'bucket2 must be in the list': (buckets) => buckets.some(b => b.name.normalize() === 'bucket2'),
	}, {operation: 'listBuckets'});

	const {contents: b1Objects} = s3.listObjects({bucket: 'bucket1'});
	check(b1Objects, {
		'it must return one object': (b1Objects) => b1Objects.length === 1,
		'file1.txt must be in the list': (b1Objects) => b1Objects.some(obj => obj.key.normalize() === 'file1.txt'),
	}, {operation: 'listObjects', bucket: 'bucket1'});

	const {contents: b2Objects} = s3.listObjects({bucket: 'bucket2'});
	check(b2Objects, {
		'it must return one object': (b2Objects) => b2Objects.length === 1,
		'file2.txt must be in the list': (b2Objects) => b2Objects.some(obj => obj.key.normalize() === 'file2.txt'),
	}, {operation: 'listObjects', bucket: 'bucket2'});

	const {body} = s3.getObject({bucket: 'bucket1', key: 'file1.txt'});
	const reader = body.getReader();
	const {value} = await reader.read();
	check(value, {
		'file1.txt contents are the expected ones': (value) => value === 'Hello, World',
	}, {operation: 'getObject', bucket: 'bucket1', key: 'file1.txt'});
}
```

### `script_111.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [19, 27, 34, 41]
- **Snippet:**
```js
const {buckets} = s3.listBuckets();
	// ...
	const {contents: b1Objects} = s3.listObjects({bucket: "bucket1"})
	// ...
	const {contents: b2Objects} = s3.listObjects({bucket: "bucket2"})
	// ...
	const {body} = s3.getObject({bucket: "bucket1", key: "file1.txt"})
```
- **Refactored:**
```js
import {check, group} from 'k6';
import {S3Client} from "k6/x/aws";
import {config} from './localstack.js';

// ... (options remain the same)

export default async function () {
	const s3 = new S3Client(config);

	group('S3 List Buckets', function () {
		const {buckets} = s3.listBuckets();
		check(buckets, {
				'it must return two buckets': (buckets) => buckets.length === 2,
				'bucket1 must be in the list': (buckets) => buckets.some(b => b.name.normalize() === "bucket1"),
				'bucket2 must be in the list': (buckets) => buckets.some(b => b.name.normalize() === "bucket2")
			}
		);
	});

	group('S3 List Objects in bucket1', function () {
		const {contents: b1Objects} = s3.listObjects({bucket: "bucket1"})
		check(b1Objects, {
				'it must return one object': (b1Objects) => b1Objects.length === 1,
				'file1.txt must be in the list': (b1Objects) => b1Objects.some(obj => obj.key.normalize() === "file1.txt")
			}
		);
	});

	group('S3 List Objects in bucket2', function () {
		const {contents: b2Objects} = s3.listObjects({bucket: "bucket2"})
		check(b2Objects, {
				'it must return one object': (b2Objects) => b2Objects.length === 1,
				'file1.txt must be in the list': (b2Objects) => b2Objects.some(obj => obj.key.normalize() === "file2.txt")
			}
		);
	});

	group('S3 Get Object from bucket1', async function () {
		const {body} = s3.getObject({bucket: "bucket1", key: "file1.txt"})
		const reader = body.getReader();
		const {value} = await reader.read();
		check(value, {
				'file1.txt contents are the expected ones': (value) => value === 'Hello, World',
			}
		);
	});
}
```

---

## `script_112.js`

### `script_112.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [22, 23, 24]
- **Snippet:**
```js
const data = new SharedArray('some data name', function () {
  return JSON.parse(open('./data.json')).users;
});
```
- **Refactored:**
```js
/* Use the setup life-cycle function for one-time data loading. This runs once before the test starts and passes data to VUs, making the separation of concerns clearer than loading in the global init context. */
export function setup() {
  const users = JSON.parse(open('./data.json')).users;
  return { users: users };
}

// In the default function, access the data passed from setup:
export default function main(data) {
  const user = data.users[__VU % data.users.length];
  // ...
}
```

**Smell 3: Not checking requests**

- **Lines:** [57]
- **Snippet:**
```js
response = http.get('https://doctor.mountsinai.org/fad/autocomplete/lite', { ... })
```
- **Refactored:**
```js
response = http.get('https://doctor.mountsinai.org/fad/autocomplete/lite', {
      // ... headers
    });
    check(response, {
      'autocomplete status is 200': (r) => r.status === 200,
    });
```

**Smell 4: Not using tags**

- **Lines:** [57]
- **Snippet:**
```js
response = http.get('https://doctor.mountsinai.org/fad/autocomplete/lite', { ... })
```
- **Refactored:**
```js
response = http.get('https://doctor.mountsinai.org/fad/autocomplete/lite', {
      tags: {
        my_tag: "Autocomplete tag"
      },
      headers: {
        // ... headers
      },
    });
```

---

## `script_113.js`

### `script_113.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [66, 87]
- **Snippet:**
```js
const loginRes = http.post(`${BASE_URL}/auth/token/login/`, {
  username: USERNAME,
  password: PASSWORD,
});
...
const myObjects = http.get(`${BASE_URL}/my/crocodiles/`, authHeaders).json();
```
- **Refactored:**
```js
const loginRes = http.post(`${BASE_URL}/auth/token/login/`, {
  username: USERNAME,
  password: PASSWORD,
}, { tags: { name: 'Login' } });
...
const myObjects = http.get(`${BASE_URL}/my/crocodiles/`, {
  headers: authHeaders.headers,
  tags: { name: 'GetCrocodiles' },
}).json();

// And update thresholds to leverage tags:
// thresholds: {
//   'http_req_duration{name:Login}': ['p(99)<1500'],
//   'http_req_duration{name:GetCrocodiles}': ['p(99)<1500'],
// }
```

### `script_113.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [66, 67, 68, 69, 80, 81, 82, 83, 84, 87]
- **Snippet:**
```js
const loginRes = http.post(`${BASE_URL}/auth/token/login/`, {
  username: USERNAME,
  password: PASSWORD,
});

const authHeaders = {
  headers: {
    Authorization: `Bearer ${loginRes.json('access')}`,
  },
};

const myObjects = http.get(`${BASE_URL}/my/crocodiles/`, authHeaders).json();
```
- **Refactored:**
```js
const loginRes = http.post(
  `${BASE_URL}/auth/token/login/`,
  {
    username: USERNAME,
    password: PASSWORD,
  },
  {
    tags: { name: 'Login' },
  }
);

const authHeaders = {
  headers: {
    Authorization: `Bearer ${loginRes.json('access')}`,
  },
  tags: { name: 'MyCrocodiles' },
};

const myObjects = http.get(`${BASE_URL}/my/crocodiles/`, authHeaders).json();

// Optional tagged thresholds:
// thresholds: {
//   'http_req_duration{name:Login}': ['p(99)<1500'],
//   'http_req_duration{name:MyCrocodiles}': ['p(99)<1500'],
// }
```

### `script_113.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [66, 87]
- **Snippet:**
```js
const loginRes = http.post(`${BASE_URL}/auth/token/login/`, {
  username: USERNAME,
  password: PASSWORD,
});
...
const myObjects = http.get(`${BASE_URL}/my/crocodiles/`, authHeaders).json();
```
- **Refactored:**
```js
const loginRes = http.post(`${BASE_URL}/auth/token/login/`, {
  username: USERNAME,
  password: PASSWORD,
}, { tags: { name: 'Login' } });

const authHeaders = {
  headers: {
    Authorization: `Bearer ${loginRes.json('access')}`,
  },
  tags: { name: 'GetCrocodiles' },
};
const myObjects = http.get(`${BASE_URL}/my/crocodiles/`, authHeaders).json();
```

---

## `script_114.js`

### `script_114.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [46, 67]
- **Snippet:**
```js
const loginRes = http.post(`${BASE_URL}/auth/token/login/`, {
  username: USERNAME,
  password: PASSWORD,
});
...
const myObjects = http.get(`${BASE_URL}/my/crocodiles/`, authHeaders).json();
```
- **Refactored:**
```js
const loginRes = http.post(`${BASE_URL}/auth/token/login/`, {
  username: USERNAME,
  password: PASSWORD,
}, { tags: { name: 'Login' } });

check(loginRes, {
  'logged in successfully': (resp) => resp.json('access') !== '',
});

const authHeaders = {
  headers: {
    Authorization: `Bearer ${loginRes.json('access')}`,
  },
  tags: { name: 'GetCrocodiles' },
};

const myObjects = http.get(`${BASE_URL}/my/crocodiles/`, authHeaders).json();
check(myObjects, { 'retrieved crocodiles': (obj) => obj.length > 0 });

// And update thresholds to leverage tags:
// thresholds: {
//   'http_req_duration{name:Login}': ['p(99)<1500'],
//   'http_req_duration{name:GetCrocodiles}': ['p(99)<1500'],
// }
```

### `script_114.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [46, 49, 67]
- **Snippet:**
```js
const loginRes = http.post(`${BASE_URL}/auth/token/login/`, {
  username: USERNAME,
  password: PASSWORD,
});

const myObjects = http.get(`${BASE_URL}/my/crocodiles/`, authHeaders).json();
```
- **Refactored:**
```js
export const options = {
  vus: 1,
  duration: '1m',
  thresholds: {
    'http_req_duration{endpoint:login}': ['p(99)<1500'],
    'http_req_duration{endpoint:my_crocodiles}': ['p(99)<1500'],
  },
};

export default () => {
  const loginRes = http.post(
    `${BASE_URL}/auth/token/login/`,
    {
      username: USERNAME,
      password: PASSWORD,
    },
    {
      tags: { endpoint: 'login', name: 'Login' },
    }
  );

  check(loginRes, {
    'logged in successfully': (resp) => resp.json('access') !== '',
  }, { endpoint: 'login' });

  const authParams = {
    headers: {
      Authorization: `Bearer ${loginRes.json('access')}`,
    },
    tags: { endpoint: 'my_crocodiles', name: 'MyCrocodiles' },
  };

  const crocodilesRes = http.get(`${BASE_URL}/my/crocodiles/`, authParams);
  const myObjects = crocodilesRes.json();

  check(myObjects, {
    'retrieved crocodiles': (obj) => obj.length > 0,
  }, { endpoint: 'my_crocodiles' });

  sleep(1);
};
```

### `script_114.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [46, 67]
- **Snippet:**
```js
const loginRes = http.post(`${BASE_URL}/auth/token/login/`, {
  username: USERNAME,
  password: PASSWORD,
});

// ...

const myObjects = http.get(`${BASE_URL}/my/crocodiles/`, authHeaders).json();
```
- **Refactored:**
```js
const loginRes = http.post(`${BASE_URL}/auth/token/login/`, {
  username: USERNAME,
  password: PASSWORD,
}, { tags: { name: 'Login' } });

// ...

const authHeaders = {
  headers: {
    Authorization: `Bearer ${loginRes.json('access')}`,
  },
  tags: { name: 'GetCrocodiles' },
};

const myObjects = http.get(`${BASE_URL}/my/crocodiles/`, authHeaders).json();
```

---

## `script_115.js`

### `script_115.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [93, 94, 95]
- **Snippet:**
```js
export default function () {
	wpLogin();
}
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_duration{name:Merchant - WP Login Page}': ['p(95)<500'],
    'http_req_duration{name:Merchant - Login to WP Admin}': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
  },
};

export default function () {
	wpLogin();
}
```

### `script_115.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [93, 94, 95]
- **Snippet:**
```js
export default function () {
	wpLogin();
}
```
- **Refactored:**
```js
export const options = {
	thresholds: {
		http_req_failed: ['rate<0.01'],
		checks: ['rate>0.99'],
		'http_req_duration{name:Merchant - WP Login Page}': ['p(95)<500'],
		'http_req_duration{name:Merchant - Login to WP Admin}': ['p(95)<1000'],
	},
};

export default function () {
	wpLogin();
}
```

### `script_115.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [26]
- **Snippet:**
```js
// The 'options' export with a 'thresholds' property is missing from the script.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    // Fail the test if more than 1% of requests fail.
    'http_req_failed': ['rate<0.01'],
    // 95th percentile of request duration for the login page should be below 500ms.
    'http_req_duration{name:Merchant - WP Login Page}': ['p(95)<500'],
    // 95th percentile of request duration for the admin login action should be below 800ms.
    'http_req_duration{name:Merchant - Login to WP Admin}': ['p(95)<800'],
  },
};

```

---

## `script_116.js`

### `script_116.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [43, 55, 71]
- **Snippet:**
```js
let courseRes = http.get(`${BASE_URL}/api/courses`, { headers: { Authorization: `Bearer ${token}` } });
let orderRes = http.post(`${BASE_URL}/api/orders`, payload, { headers: { ... } });
let balRes = http.get(`${BASE_URL}/api/payments/balance`, { headers: { ... } });
```
- **Refactored:**
```js
let courseRes = http.get(`${BASE_URL}/api/courses`, {
  headers: { Authorization: `Bearer ${token}` },
  tags: { name: 'GetCourses' },
});

let orderRes = http.post(`${BASE_URL}/api/orders`, payload, {
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${token}`,
  },
  tags: { name: 'CreateOrder' },
});

let balRes = http.get(`${BASE_URL}/api/payments/balance`, {
  headers: {
    Authorization: `Bearer ${token}`,
    'X-User-Id': 'sm8SaZl5PxOJSapuwlS5fce4KS53',
    'X-User-Role': 'prophet',
  },
  tags: { name: 'GetProphetBalance' },
});
```

### `script_116.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [43, 44, 45, 55, 56, 57, 58, 59, 60, 71, 72, 73, 74, 75, 76, 77]
- **Snippet:**
```js
let courseRes = http.get(`${BASE_URL}/api/courses`, {
  headers: { Authorization: `Bearer ${token}` },
});

let orderRes = http.post(`${BASE_URL}/api/orders`, payload, {
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${token}`,
  },
});

let balRes = http.get(`${BASE_URL}/api/payments/balance`, {
  headers: {
    Authorization: `Bearer ${token}`,
    'X-User-Id': 'sm8SaZl5PxOJSapuwlS5fce4KS53',
    'X-User-Role': 'prophet',
  },
});
```
- **Refactored:**
```js
let courseRes = http.get(`${BASE_URL}/api/courses`, {
  headers: { Authorization: `Bearer ${token}` },
  tags: { name: 'GetCourses', endpoint: '/api/courses', role },
});
check(courseRes, { 'get courses status 200': (r) => r.status === 200 }, { endpoint: '/api/courses', role });
courseTrend.add(courseRes.timings.duration, { endpoint: '/api/courses', role });

let orderRes = http.post(`${BASE_URL}/api/orders`, payload, {
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${token}`,
  },
  tags: { name: 'CreateOrder', endpoint: '/api/orders', role: 'customer' },
});
check(orderRes, {
  'order create ok': (r) => r.status === 201 || r.status === 200,
}, { endpoint: '/api/orders', role: 'customer' });
orderTrend.add(orderRes.timings.duration, { endpoint: '/api/orders', role: 'customer' });

let balRes = http.get(`${BASE_URL}/api/payments/balance`, {
  headers: {
    Authorization: `Bearer ${token}`,
    'X-User-Id': 'sm8SaZl5PxOJSapuwlS5fce4KS53',
    'X-User-Role': 'prophet',
  },
  tags: { name: 'GetProphetBalance', endpoint: '/api/payments/balance', role: 'prophet' },
});
check(balRes, { 'get balance ok': (r) => r.status === 200 }, { endpoint: '/api/payments/balance', role: 'prophet' });
```

### `script_116.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [43, 55, 71]
- **Snippet:**
```js
let courseRes = http.get(`${BASE_URL}/api/courses`, {
    headers: { Authorization: `Bearer ${token}` },
  });
```
- **Refactored:**
```js
// GET courses
let courseRes = http.get(`${BASE_URL}/api/courses`, {
  headers: { Authorization: `Bearer ${token}` },
  tags: { name: 'GetCourses' },
});

// CREATE order
let orderRes = http.post(`${BASE_URL}/api/orders`, payload, {
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${token}`,
  },
  tags: { name: 'CreateOrder' },
});

// GET prophet balance
let balRes = http.get(`${BASE_URL}/api/payments/balance`, {
  headers: {
    Authorization: `Bearer ${token}`,
    'X-User-Id': 'sm8SaZl5PxOJSapuwlS5fce4KS53',
    'X-User-Role': 'prophet',
  },
  tags: { name: 'GetBalance' },
});
```

---

## `script_117.js`

### `script_117.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** []
- **Snippet:**
```js
No export const options block with thresholds is defined in the provided k6 code.
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

---

## `script_118.js`

### `script_118.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [14]
- **Snippet:**
```js
initPools();
```
- **Refactored:**
```js
// Move initPools() call to the setup() function instead of the init context
export function setup() {
  initPools(); // runs once globally, not once per VU
  console.log('=== Stress Test Configuration ===');
  // ... rest of setup
}
```

### `script_118.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [13, 14]
- **Snippet:**
```js
// Initialize data pools at module level (runs once when script loads)
initPools();
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

// Use SharedArray or another shared/read-only strategy so expensive pool initialization is not repeated per VU.
const dataPools = new SharedArray('data-pools', () => {
  return initPools();
});

// Then pass/use dataPools in generateEvent(), generateMetricRequest(), or generateBulkEvents() as needed.
```

**Smell 4: Not using tags**

- **Lines:** [63]
- **Snippet:**
```js
const res = http.get(`${baseUrl}/health`, { timeout: '5s' });
```
- **Refactored:**
```js
const res = http.get(`${baseUrl}/health`, {
  timeout: '5s',
  tags: { name: 'HealthCheck' },
});
```

### `script_118.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [14]
- **Snippet:**
```js
initPools();
```
- **Refactored:**
```js
/*
 The initPools() function is called in the init context, which runs once per VU.
 If this is a costly operation (e.g., reading/parsing large data files), it should be moved
 to the setup() function, which runs only once for the entire test.
*/

// 1. Remove the call from the init context:
// import { initPools, ... } from './lib/data-generator.js';
// initPools(); // <-- REMOVE THIS LINE (14)

// 2. Add the call to the beginning of the setup() function:
export function setup() {
  initPools(); // <-- ADD THIS LINE HERE

  console.log('=== Stress Test Configuration ===');
  
  const baseUrl = __ENV.BASE_URL || 'http://localhost:50051';
  // ... rest of the setup function
}
```

---

## `script_119.js`

### `script_119.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [152, 153, 154]
- **Snippet:**
```js
export default function () {
	cartApplyCoupon();
}
```
- **Refactored:**
```js
export const options = {
	thresholds: {
		'http_req_duration{name:Shopper - wc-ajax=add_to_cart}': ['p(95)<500'],
		'http_req_duration{name:Shopper - View Cart}': ['p(95)<1000'],
		'http_req_duration{name:Shopper - wc-ajax=apply_coupon}': ['p(95)<500'],
		'http_req_duration{name:Shopper - Update Cart}': ['p(95)<500'],
		http_req_failed: ['rate<0.01'],
	},
};

export default function () {
	cartApplyCoupon();
}
```

### `script_119.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [152, 153, 154]
- **Snippet:**
```js
export default function () {
	cartApplyCoupon();
}
```
- **Refactored:**
```js
export const options = {
	thresholds: {
		http_req_failed: ['rate<0.01'],
		http_req_duration: ['p(95)<1000'],
		checks: ['rate>0.99'],
		'http_req_duration{name:Shopper - wc-ajax=add_to_cart}': ['p(95)<500'],
		'http_req_duration{name:Shopper - View Cart}': ['p(95)<800'],
		'http_req_duration{name:Shopper - wc-ajax=apply_coupon}': ['p(95)<500'],
		'http_req_duration{name:Shopper - Update Cart}': ['p(95)<800'],
	},
};

export default function () {
	cartApplyCoupon();
}
```

### `script_119.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 154]
- **Snippet:**
```js
The script is missing an `export const options` block, which is where thresholds are defined. Without thresholds, the test will always pass, regardless of the system's performance.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
    'http_req_duration{name:Shopper - wc-ajax=add_to_cart}': ['p(95)<300'],
    'http_req_duration{name:Shopper - View Cart}': ['p(95)<400'],
    'http_req_duration{name:Shopper - wc-ajax=apply_coupon}': ['p(95)<300'],
    'http_req_duration{name:Shopper - Update Cart}': ['p(95)<400'],
    checks: ['rate>0.99'], // 99% of checks should pass
  },
  // Define load profile
  vus: 10,
  duration: '1m',
};

/* ... The rest of the script remains the same ... */

export default function () {
	cartApplyCoupon();
}
```

---

## `script_120.js`

### `script_120.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [51, 52, 53]
- **Snippet:**
```js
const res = http.get(`${baseUrl}/`, {
  timeout: '10s',
});
```
- **Refactored:**
```js
const res = http.get(`${baseUrl}/`, {
  timeout: '10s',
  tags: { endpoint: 'server_ready' },
});
```

### `script_120.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [166, 167, 168, 169, 170]
- **Snippet:**
```js
check(updateRes, {
  'profile update responds': (r) => r.status === 200 || r.status === 400,
  'profile update handled': (r) => r.status !== 500,
  'profile update time < 2000ms': (r) => r.timings.duration < 2000,
});
```
- **Refactored:**
```js
check(updateRes, {
  'profile update status is 200': (r) => r.status === 200,
  'profile update time < 2000ms': (r) => r.timings.duration < 2000,
});
```

---

## `script_121.js`

### `script_121.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [117, 118, 119]
- **Snippet:**
```js
export default function () {
	myAccount();
}
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_duration{name:Shopper - My Account Login Page}': ['p(95)<500'],
    'http_req_duration{name:Shopper - Login to My Account}': ['p(95)<500'],
    'http_req_duration{name:Shopper - wc-ajax=get_refreshed_fragments}': ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};

export default function () {
	myAccount();
}
```

### `script_121.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [117, 118, 119]
- **Snippet:**
```js
export default function () {
	myAccount();
}
```
- **Refactored:**
```js
export const options = {
	thresholds: {
		http_req_failed: ['rate<0.01'],
		'http_req_duration{name:Shopper - My Account Login Page}': ['p(95)<500'],
		'http_req_duration{name:Shopper - Login to My Account}': ['p(95)<500'],
		'http_req_duration{name:Shopper - wc-ajax=get_refreshed_fragments}': ['p(95)<500'],
		checks: ['rate>0.99'],
	},
};

export default function () {
	myAccount();
}
```

### `script_121.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [30]
- **Snippet:**
```js
// The script is missing the 'options' export, and therefore, no 'thresholds' are defined to set pass/fail criteria for the test.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<1000'], // 95% of requests must complete below 1s
    'http_req_duration{name:Shopper - My Account Login Page}': ['p(95)<800'],
    'http_req_duration{name:Shopper - Login to My Account}': ['p(95)<1200'],
    'checks': ['rate>0.99'], // 99% of checks should pass
  },
};

export function myAccount() {
```

---

## `script_122.js`

### `script_122.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [36, 74, 101]
- **Snippet:**
```js
const loginRes = http.post(`${baseUrl}/api/auth/login`, loginPayload, { headers: ... });
const getUserRes = http.get(`${baseUrl}/api/auth/me`, { headers: ... });
const updateRes = http.put(`${baseUrl}/api/users`, JSON.stringify(updateData), { headers: ... });
```
- **Refactored:**
```js
const loginRes = http.post(`${baseUrl}/api/auth/login`, loginPayload, {
  headers: { 'Content-Type': 'application/json' },
  timeout: '10s',
  tags: { name: 'Login' },
});

const getUserRes = http.get(`${baseUrl}/api/auth/me`, {
  headers: authHeaders,
  timeout: '10s',
  tags: { name: 'GetUser' },
});

const updateRes = http.put(`${baseUrl}/api/users`, JSON.stringify(updateData), {
  headers: authHeaders,
  timeout: '10s',
  tags: { name: 'UpdateUser' },
});

// And update thresholds to leverage tags:
export const options = {
  vus: parseInt(__ENV.VUS || '20'),
  duration: __ENV.DURATION || '30s',
  thresholds: {
    http_req_failed: ['rate<0.1'],
    'http_req_duration{name:Login}': ['p(95)<2000'],
    'http_req_duration{name:GetUser}': ['p(95)<2000'],
    'http_req_duration{name:UpdateUser}': ['p(95)<2000'],
  },
};
```

### `script_122.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [36, 37, 38, 39, 74, 75, 76, 77, 101, 102, 103, 104]
- **Snippet:**
```js
const loginRes = http.post(`${baseUrl}/api/auth/login`, loginPayload, {
  headers: { 'Content-Type': 'application/json' },
  timeout: '10s',
});

const getUserRes = http.get(`${baseUrl}/api/auth/me`, {
  headers: authHeaders,
  timeout: '10s',
});

const updateRes = http.put(`${baseUrl}/api/users`, JSON.stringify(updateData), {
  headers: authHeaders,
  timeout: '10s',
});
```
- **Refactored:**
```js
export const options = {
  vus: parseInt(__ENV.VUS || '20'),
  duration: __ENV.DURATION || '30s',
  thresholds: {
    http_req_failed: ['rate<0.1'],
    http_req_duration: ['p(95)<2000'],
    'http_req_duration{name:Login}': ['p(95)<2000'],
    'http_req_duration{name:GetUser}': ['p(95)<2000'],
    'http_req_duration{name:UpdateUser}': ['p(95)<2000'],
  },
};

const loginRes = http.post(`${baseUrl}/api/auth/login`, loginPayload, {
  headers: { 'Content-Type': 'application/json' },
  timeout: '10s',
  tags: { name: 'Login', endpoint: 'POST /api/auth/login', flow: 'Login' },
});

const getUserRes = http.get(`${baseUrl}/api/auth/me`, {
  headers: authHeaders,
  timeout: '10s',
  tags: { name: 'GetUser', endpoint: 'GET /api/auth/me', flow: 'Get User' },
});

const updateRes = http.put(`${baseUrl}/api/users`, JSON.stringify(updateData), {
  headers: authHeaders,
  timeout: '10s',
  tags: { name: 'UpdateUser', endpoint: 'PUT /api/users', flow: 'Update User' },
});
```

---

## `script_123.js`

### `script_123.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [64, 65, 66, 67, 68, 87, 88, 89, 90, 91]
- **Snippet:**
```js
const directResponse = http.post(
    `${MAIN_SERVICE_URL}/camel/api/payload`,
    JSON.stringify(payload),
    { headers }
  );

  const clientResponse = http.post(
    `${CLIENT_BASE_URL}/api/benchmark/rest`,
    JSON.stringify(payload),
    { headers }
  );
```
- **Refactored:**
```js
const directResponse = http.post(
    `${MAIN_SERVICE_URL}/camel/api/payload`,
    JSON.stringify(payload),
    { headers, tags: { name: 'DirectREST' } }
  );

  const clientResponse = http.post(
    `${CLIENT_BASE_URL}/api/benchmark/rest`,
    JSON.stringify(payload),
    { headers, tags: { name: 'ClientREST' } }
  );

// Also update thresholds to leverage tags:
// thresholds: {
//   'http_req_duration{name:DirectREST}': ['p(95)<2000'],
//   'http_req_duration{name:ClientREST}': ['p(95)<2000'],
//   'http_req_failed{name:DirectREST}': ['rate<0.05'],
//   'http_req_failed{name:ClientREST}': ['rate<0.05'],
// }
```

### `script_123.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [64, 65, 66, 67, 87, 88, 89, 90]
- **Snippet:**
```js
const directResponse = http.post(
  `${MAIN_SERVICE_URL}/camel/api/payload`,
  JSON.stringify(payload),
  { headers }
);

const clientResponse = http.post(
  `${CLIENT_BASE_URL}/api/benchmark/rest`,
  JSON.stringify(payload),
  { headers }
);
```
- **Refactored:**
```js
const directTags = { name: 'DirectRESTPayload', endpoint: '/camel/api/payload', flow: 'direct-rest' };
const directResponse = http.post(
  `${MAIN_SERVICE_URL}/camel/api/payload`,
  JSON.stringify(payload),
  { headers, tags: directTags }
);

const clientTags = { name: 'ClientRESTBenchmark', endpoint: '/api/benchmark/rest', flow: 'client-rest' };
const clientResponse = http.post(
  `${CLIENT_BASE_URL}/api/benchmark/rest`,
  JSON.stringify(payload),
  { headers, tags: clientTags }
);
```

### `script_123.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [64, 87]
- **Snippet:**
```js
const directResponse = http.post(
    `${MAIN_SERVICE_URL}/camel/api/payload`,
    JSON.stringify(payload),
    { headers }
  );
// ...
const clientResponse = http.post(
    `${CLIENT_BASE_URL}/api/benchmark/rest`,
    JSON.stringify(payload),
    { headers }
  );
```
- **Refactored:**
```js
// Test direct REST endpoint
const directResponse = http.post(
    `${MAIN_SERVICE_URL}/camel/api/payload`,
    JSON.stringify(payload),
    { 
      headers,
      tags: { name: 'DirectREST' }
    }
  );

  // ...

// Test client service REST endpoint
const clientResponse = http.post(
    `${CLIENT_BASE_URL}/api/benchmark/rest`,
    JSON.stringify(payload),
    {
      headers,
      tags: { name: 'ClientREST' }
    }
  );
```

---

## `script_124.js`

### `script_124.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [7]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};

export default function () {
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
const response = http.get(url.toString());
```
- **Refactored:**
```js
const response = http.get(url.toString(), { tags: { name: 'SearchCustomer' } });
```

### `script_124.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [7]
- **Snippet:**
```js
export default function () {
  ...
}
// no export const options with thresholds is defined
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration{name:CustomerSearch}': ['p(95)<500'],
    'checks': ['rate>0.99']
  }
};

export default function () {
  const nameToSearch = 'John';
  const url = new URL(`${BASE_URL}/api/customer/fake/search`);
  url.searchParams.append('name', nameToSearch);

  const response = http.get(url.toString(), {
    tags: { name: 'CustomerSearch' }
  });
  const customers = response.json();

  check(customers, {
    'All customers have a full name': (c) => c.every(customer => customer['full-name']),
    'All full names contain the search string (case-insensitive)': (c) => c.every(customer => customer['full-name'].toLowerCase().includes(nameToSearch.toLowerCase()))
  });

  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
const response = http.get(url.toString());
```
- **Refactored:**
```js
const response = http.get(url.toString(), {
  tags: {
    name: 'CustomerSearch',
    endpoint: '/api/customer/fake/search'
  }
});
```

### `script_124.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7]
- **Snippet:**
```js
The script does not export an 'options' object with a 'thresholds' property, making it impossible to define success/failure criteria for the test run.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<200'],
    'checks': ['rate>0.99']
  },
};

// ... rest of the script
```

**Smell 3: Not checking requests**

- **Lines:** [12, 13, 15]
- **Snippet:**
```js
const response = http.get(url.toString());
const customers = response.json();

check(customers, ...)
```
- **Refactored:**
```js
const response = http.get(url.toString());

const isStatusOk = check(response, {
  'Search request status is 200': (r) => r.status === 200,
});

if (isStatusOk) {
  const customers = response.json();
  check(customers, {
    'All customers have a full name': (c) => {
      return c.every(customer => customer['full-name']);
    },
    'All full names contain the search string (case-insensitive)': (c) => {
      return c.every(customer => customer['full-name'].toLowerCase().includes(nameToSearch.toLowerCase()));
    }
  });
}
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
const response = http.get(url.toString());
```
- **Refactored:**
```js
const response = http.get(url.toString(), {
  tags: { name: 'CustomerSearch' },
});
```

---

## `script_125.js`

### `script_125.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
    'checks': ['rate>0.99'],
  },
};

export default function () {
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
const res = http.get('https://quickpizza.grafana.com/api/cookies');
```
- **Refactored:**
```js
const res = http.get('https://quickpizza.grafana.com/api/cookies', { tags: { name: 'GetCookies' } });
```

### `script_125.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    'http_req_duration{name:Cookies}': ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};

export default function () {
  const jar = http.cookieJar();
  jar.set('https://quickpizza.grafana.com/api/cookies', 'my_cookie', 'hello world', {
    domain: 'quickpizza.grafana.com',
    path: '/api/cookies',
    secure: true,
    max_age: 600,
  });
  const res = http.get('https://quickpizza.grafana.com/api/cookies', {
    tags: { name: 'Cookies', endpoint: '/api/cookies' },
  });

  check(res, {
    'has status 200': (r) => r.status === 200,
    'cookie has correct value': (r) => r.json().cookies.my_cookie == 'hello world',
  }, { name: 'Cookies', endpoint: '/api/cookies' });
}
```

**Smell 4: Not using tags**

- **Lines:** [12, 14]
- **Snippet:**
```js
const res = http.get('https://quickpizza.grafana.com/api/cookies');

check(res, {
```
- **Refactored:**
```js
const res = http.get('https://quickpizza.grafana.com/api/cookies', {
  tags: { name: 'Cookies', endpoint: '/api/cookies' },
});

check(res, {
  'has status 200': (r) => r.status === 200,
  'cookie has correct value': (r) => r.json().cookies.my_cookie == 'hello world',
}, { name: 'Cookies', endpoint: '/api/cookies' });
```

### `script_125.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [3]
- **Snippet:**
```js
// The options block with thresholds is missing.
```
- **Refactored:**
```js
import http from 'k6/http';
import { check } from 'k6';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
const res = http.get('https://quickpizza.grafana.com/api/cookies');
```
- **Refactored:**
```js
const res = http.get('https://quickpizza.grafana.com/api/cookies', {
    tags: { name: 'GetCookies' },
  });
```

---

## `script_126.js`

### `script_126.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [7]
- **Snippet:**
```js
export function contacts(baseUrl) {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'contact_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
  },
};

export function contacts(baseUrl) {
```

**Smell 3: Not checking requests**

- **Lines:** [10, 15]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/contacts.php`);
    // add duration property to metric
    contactsLatency.add(res.timings.duration);
    ...
    res = http.get(`${baseUrl}/`);
    // add duration property to metric
    contactsLatency.add(res.timings.duration);
```
- **Refactored:**
```js
import { check } from 'k6';

// inside the group:
let res = http.get(`${baseUrl}/contacts.php`);
check(res, {
  'contacts.php status is 200': (r) => r.status === 200,
});
contactsLatency.add(res.timings.duration);
sleep(1);

res = http.get(`${baseUrl}/`);
check(res, {
  'home status is 200': (r) => r.status === 200,
});
contactsLatency.add(res.timings.duration);
sleep(1);
```

**Smell 4: Not using tags**

- **Lines:** [10, 15]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/contacts.php`);
    ...
    res = http.get(`${baseUrl}/`);
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/contacts.php`, { tags: { name: 'Contacts' } });
contactsLatency.add(res.timings.duration, { name: 'Contacts' });
sleep(1);

res = http.get(`${baseUrl}/`, { tags: { name: 'Home' } });
contactsLatency.add(res.timings.duration, { name: 'Home' });
sleep(1);
```

### `script_126.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [1, 20]
- **Snippet:**
```js
No export const options object with thresholds is defined in the provided k6 code.
```
- **Refactored:**
```js
import http from 'k6/http';
import { Trend } from 'k6/metrics';
import { group, sleep } from 'k6';

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    'http_req_duration{name:ContactsPage}': ['p(95)<500'],
    'http_req_duration{name:HomePage}': ['p(95)<500'],
    contact_duration: ['p(95)<500'],
  },
};

const contactsLatency = new Trend('contact_duration');
```

**Smell 3: Not checking requests**

- **Lines:** [10, 15]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/contacts.php`);
...
res = http.get(`${baseUrl}/`);
```
- **Refactored:**
```js
import { group, sleep, check } from 'k6';

export function contacts(baseUrl) {
  group('Contacts flow', function () {
    let res = http.get(`${baseUrl}/contacts.php`, { tags: { name: 'ContactsPage' } });
    check(res, {
      'contacts page status is 200': (r) => r.status === 200,
    });
    contactsLatency.add(res.timings.duration, { name: 'ContactsPage' });
    sleep(1);

    res = http.get(`${baseUrl}/`, { tags: { name: 'HomePage' } });
    check(res, {
      'home page status is 200': (r) => r.status === 200,
    });
    contactsLatency.add(res.timings.duration, { name: 'HomePage' });
    sleep(1);
  });
}
```

**Smell 4: Not using tags**

- **Lines:** [10, 12, 15, 17]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/contacts.php`);
contactsLatency.add(res.timings.duration);
...
res = http.get(`${baseUrl}/`);
contactsLatency.add(res.timings.duration);
```
- **Refactored:**
```js
export function contacts(baseUrl) {
  group('Contacts flow', function () {
    let res = http.get(`${baseUrl}/contacts.php`, {
      tags: { name: 'ContactsPage', flow: 'Contacts' },
    });
    contactsLatency.add(res.timings.duration, { name: 'ContactsPage', flow: 'Contacts' });
    sleep(1);

    res = http.get(`${baseUrl}/`, {
      tags: { name: 'HomePage', flow: 'Contacts' },
    });
    contactsLatency.add(res.timings.duration, { name: 'HomePage', flow: 'Contacts' });
    sleep(1);
  });
}
```

### `script_126.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 20]
- **Snippet:**
```js
The script does not export an `options` object with a `thresholds` configuration. Without thresholds, the test will always report as successful, even if the system's performance is poor.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    // No more than 1% of requests should fail
    'http_req_failed': ['rate<0.01'],
    // 95% of requests must complete below 500ms
    'http_req_duration': ['p(95)<500'],
    // 95% of transactions for the contacts flow must be below 800ms
    'contact_duration': ['p(95)<800'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [10, 15]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/contacts.php`);
...
res = http.get(`${baseUrl}/`);
```
- **Refactored:**
```js
// Add 'check' to the k6 import on line 3
import { group, sleep, check } from 'k6';

export function contacts(baseUrl) {
  group('Contacts flow', function () {
    // Request 1: Contacts page
    let res = http.get(`${baseUrl}/contacts.php`);
    check(res, {
      'status is 200 for contacts': (r) => r.status === 200,
    });
    contactsLatency.add(res.timings.duration);
    sleep(1);

    // Request 2: Homepage
    res = http.get(`${baseUrl}/`);
    check(res, {
      'status is 200 for homepage': (r) => r.status === 200,
    });
    contactsLatency.add(res.timings.duration);
    sleep(1);
  });
}
```

**Smell 4: Not using tags**

- **Lines:** [10, 12, 15, 17]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/contacts.php`);
contactsLatency.add(res.timings.duration);
```
- **Refactored:**
```js
export function contacts(baseUrl) {
  group('Contacts flow', function () {
    // Request 1: Contacts page with tags
    const contactsTags = { name: 'ContactsPHP' };
    let res = http.get(`${baseUrl}/contacts.php`, { tags: contactsTags });
    contactsLatency.add(res.timings.duration, contactsTags);
    sleep(1);

    // Request 2: Homepage with tags
    const homepageTags = { name: 'Homepage' };
    res = http.get(`${baseUrl}/`, { tags: homepageTags });
    contactsLatency.add(res.timings.duration, homepageTags);
    sleep(1);
  });
}
```

---

## `script_127.js`

### `script_127.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [10, 24]
- **Snippet:**
```js
const loginRes = http.post(`${DEFAULT_URL}/api/user/login`, ...);
const res = http.get(`${DEFAULT_URL}/amount`, {headers});
```
- **Refactored:**
```js
const loginRes = http.post(`${DEFAULT_URL}/api/user/login`, JSON.stringify({
  name: '백현명'
}), { headers: { 'Content-Type': 'application/json' }, tags: { name: 'Login' } });

const res = http.get(`${DEFAULT_URL}/amount`, { headers, tags: { name: 'GetUserPoints' } });
```

### `script_127.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [10, 11, 12, 24]
- **Snippet:**
```js
const loginRes = http.post(`${DEFAULT_URL}/api/user/login`, JSON.stringify({
  name: '백현명'
}), { headers: { 'Content-Type': 'application/json' } });
...
const res = http.get(`${DEFAULT_URL}/amount`, {headers});
```
- **Refactored:**
```js
export default function () {
  const loginRes = http.post(
    `${DEFAULT_URL}/api/user/login`,
    JSON.stringify({ name: '백현명' }),
    {
      headers: { 'Content-Type': 'application/json' },
      tags: { name: 'Login', endpoint: 'user_login' }
    }
  );

  check(loginRes, { 'login succeeded': (r) => r.status === 200 }, { endpoint: 'user_login' });

  const authToken = loginRes.json('token');

  const headers = {
    'Authorization': `Bearer ${authToken}`,
    'Content-Type': 'application/json'
  };

  const res = http.get(`${DEFAULT_URL}/amount`, {
    headers,
    tags: { name: 'UserPoint', endpoint: 'amount' }
  });

  check(res, { '유저포인트': (r) => r.status === 200 }, { endpoint: 'amount' });
}
```

### `script_127.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [10, 24]
- **Snippet:**
```js
const loginRes = http.post(`${DEFAULT_URL}/api/user/login`, JSON.stringify({
  name: '백현명'
}), { headers: { 'Content-Type': 'application/json' } });

// ...

const res = http.get(`${DEFAULT_URL}/amount`, {headers});
```
- **Refactored:**
```js
export default function () {
  //로그인해서 토큰 얻기
  const loginRes = http.post(`${DEFAULT_URL}/api/user/login`, JSON.stringify({
    name: '백현명'
  }), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'UserLogin' }, // Tag added to group login metrics
  });

  check(loginRes, { 'login succeeded': (r) => r.status === 200 });

  const authToken = loginRes.json('token');

  const headers = {
    'Authorization': `Bearer ${authToken}`,
    'Content-Type': 'application/json'
  };

  //포인트충전
  const res = http.get(`${DEFAULT_URL}/amount`, {
    headers,
    tags: { name: 'GetAmount' }, // Tag added to group amount metrics
  });
  check(res, {'유저포인트': (r) => r.status === 200});
}
```

---

## `script_128.js`

### `script_128.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [46, 52]
- **Snippet:**
```js
const healthRes = http.get(`${BASE_URL}/health`)
  const predictionRes = http.request('POST', `${BASE_URL}/project-predict`, payload)
```
- **Refactored:**
```js
const healthRes = http.get(`${BASE_URL}/health`, { tags: { name: 'Health' } })
  check(healthRes, {
    'is 200': (r) => r.status === 200
  })

  const predictionRes = http.request('POST', `${BASE_URL}/project-predict`, payload, { tags: { name: 'Predict' } })
  check(predictionRes, {
    'is 200': (r) => r.status === 200
  })
```

### `script_128.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [46, 52]
- **Snippet:**
```js
const healthRes = http.get(`${BASE_URL}/health`)
const predictionRes = http.request('POST', `${BASE_URL}/project-predict`, payload)
```
- **Refactored:**
```js
export const options = {
  stages: [
    { duration: '30s', target: 10 },
    { duration: '7m', target: 10 },
    { duration: '3m', target: 0 },
  ],
  thresholds: {
    'http_req_duration{name:Health}': ['p(99)<2000'],
    'http_req_duration{name:ProjectPredict}': ['p(99)<2000']
  },
};

export default () => {
  const healthRes = http.get(`${BASE_URL}/health`, {
    tags: { name: 'Health', endpoint: '/health' }
  });
  check(healthRes, {
    'is 200': (r) => r.status === 200
  }, { endpoint: '/health' });

  const payload = JSON.stringify(generator(CACHE_RATE));
  const predictionRes = http.request('POST', `${BASE_URL}/project-predict`, payload, {
    tags: { name: 'ProjectPredict', endpoint: '/project-predict' }
  });
  check(predictionRes, {
    'is 200': (r) => r.status === 200
  }, { endpoint: '/project-predict' });
};
```

### `script_128.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [46, 52]
- **Snippet:**
```js
const healthRes = http.get(`${BASE_URL}/health`)
...
const predictionRes = http.request('POST', `${BASE_URL}/project-predict`, payload)
```
- **Refactored:**
```js
const healthRes = http.get(`${BASE_URL}/health`, {
  tags: { name: 'HealthCheck' },
});
...
const predictionRes = http.request('POST', `${BASE_URL}/project-predict`, payload, {
  tags: { name: 'Predict' },
});
```

---

## `script_129.js`

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
const res1 = http.get('https://test-api.k6.io/public/crocodiles', { tags: { name: 'GetAllCrocodiles' } });
const res2 = http.get('https://test-api.k6.io/public/crocodiles/1/', { tags: { name: 'GetCrocodileById' } });
```

### `script_129.js` — GEMINI

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
const res1 = http.get('https://test-api.k6.io/public/crocodiles', {
  tags: { name: 'GetAllPublicCrocodiles' },
});
// ...
const res2 = http.get('https://test-api.k6.io/public/crocodiles/1/', {
  tags: { name: 'GetPublicCrocodileById' },
});
```

---

## `script_130.js`

### `script_130.js` — CLAUDE

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
    'http_req_duration{group:::requisição todos os crocodilos}': ['p(95) < 500'],
    'http_req_duration{group:::requisição por id}': ['p(95) < 500']
}
```

**Smell 4: Not using tags**

- **Lines:** [14, 22]
- **Snippet:**
```js
const response1 = http.get('https://test-api.k6.io/public/crocodiles/');
...
const response2 = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
const response1 = http.get('https://test-api.k6.io/public/crocodiles/', { tags: { name: 'GetAllCrocodiles' } });
...
const response2 = http.get('https://test-api.k6.io/public/crocodiles/1/', { tags: { name: 'GetCrocodileById' } });
```

---

## `script_131.js`

### `script_131.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [66, 81]
- **Snippet:**
```js
http.get(`${BASE_URL}/health`)
http.post(`${BASE_URL}/orders`, JSON.stringify(order), { headers: { 'Content-Type': 'application/json' } })
```
- **Refactored:**
```js
http.get(`${BASE_URL}/health`, { tags: { name: 'HealthCheck' } })
http.post(`${BASE_URL}/orders`, JSON.stringify(order), { headers: { 'Content-Type': 'application/json' }, tags: { name: 'CreateOrder' } })
```

### `script_131.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [66, 81, 82, 83, 84, 85]
- **Snippet:**
```js
let response = http.get(`${BASE_URL}/health`);
...
response = http.post(`${BASE_URL}/orders`, JSON.stringify(order), {
  headers: {
    'Content-Type': 'application/json',
  },
});
```
- **Refactored:**
```js
let response = http.get(`${BASE_URL}/health`, {
  tags: { name: 'HealthCheck', endpoint: '/health' },
});

response = http.post(`${BASE_URL}/orders`, JSON.stringify(order), {
  headers: {
    'Content-Type': 'application/json',
  },
  tags: { name: 'CreateOrder', endpoint: '/orders' },
});
```

### `script_131.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [66, 81]
- **Snippet:**
```js
let response = http.get(`${BASE_URL}/health`);
...
response = http.post(`${BASE_URL}/orders`, JSON.stringify(order), {
  headers: {
    'Content-Type': 'application/json',
  },
});
```
- **Refactored:**
```js
let response = http.get(`${BASE_URL}/health`, {
  tags: { name: 'HealthCheck' },
});
...
response = http.post(`${BASE_URL}/orders`, JSON.stringify(order), {
  headers: {
    'Content-Type': 'application/json',
  },
  tags: { name: 'CreateOrder' },
});
```

---

## `script_133.js`

### `script_133.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
- **Snippet:**
```js
export function coinflip(baseUrl) { ... }  // no options export with thresholds defined
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'coinflip_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
  },
};

export function coinflip(baseUrl) {
  group('Coinflip game', function () {
    let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`);
    coinflipLatency.add(res.timings.duration);
    sleep(1);
    res = http.get(`${baseUrl}/flip_coin.php?bet=tails`);
    coinflipLatency.add(res.timings.duration);
    sleep(1);
  });
}
```

**Smell 3: Not checking requests**

- **Lines:** [10, 15]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`);
// no check on res
res = http.get(`${baseUrl}/flip_coin.php?bet=tails`);
// no check on res
```
- **Refactored:**
```js
import { check } from 'k6';

// inside coinflip function:
let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`);
check(res, {
  'bet=heads status is 200': (r) => r.status === 200,
  'bet=heads response has result': (r) => r.body && r.body.length > 0,
});
coinflipLatency.add(res.timings.duration);
sleep(1);
res = http.get(`${baseUrl}/flip_coin.php?bet=tails`);
check(res, {
  'bet=tails status is 200': (r) => r.status === 200,
  'bet=tails response has result': (r) => r.body && r.body.length > 0,
});
coinflipLatency.add(res.timings.duration);
sleep(1);
```

**Smell 4: Not using tags**

- **Lines:** [10, 15]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`);
// ...
res = http.get(`${baseUrl}/flip_coin.php?bet=tails`);
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`, { tags: { name: 'CoinflipHeads' } });
coinflipLatency.add(res.timings.duration, { bet: 'heads' });
sleep(1);
res = http.get(`${baseUrl}/flip_coin.php?bet=tails`, { tags: { name: 'CoinflipTails' } });
coinflipLatency.add(res.timings.duration, { bet: 'tails' });
sleep(1);
```

### `script_133.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [1, 5]
- **Snippet:**
```js
import http from 'k6/http';
import { Trend } from 'k6/metrics';
import { group, sleep } from 'k6';

const coinflipLatency = new Trend('coinflip_duration');
// no export const options with thresholds defined
```
- **Refactored:**
```js
import http from 'k6/http';
import { Trend } from 'k6/metrics';
import { group, sleep, check } from 'k6';

const coinflipLatency = new Trend('coinflip_duration');

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    coinflip_duration: ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [10, 15]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`);
...
res = http.get(`${baseUrl}/flip_coin.php?bet=tails`);
```
- **Refactored:**
```js
import { group, sleep, check } from 'k6';

export function coinflip(baseUrl) {
  group('Coinflip game', function () {
    let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`, {
      tags: { name: 'CoinflipHeads', endpoint: 'flip_coin' },
    });
    check(res, {
      'heads response status is 200': (r) => r.status === 200,
    });
    coinflipLatency.add(res.timings.duration);
    sleep(1);

    res = http.get(`${baseUrl}/flip_coin.php?bet=tails`, {
      tags: { name: 'CoinflipTails', endpoint: 'flip_coin' },
    });
    check(res, {
      'tails response status is 200': (r) => r.status === 200,
    });
    coinflipLatency.add(res.timings.duration);
    sleep(1);
  });
}
```

**Smell 4: Not using tags**

- **Lines:** [10, 15]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`);
...
res = http.get(`${baseUrl}/flip_coin.php?bet=tails`);
```
- **Refactored:**
```js
export function coinflip(baseUrl) {
  group('Coinflip game', function () {
    let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`, {
      tags: { name: 'CoinflipHeads', endpoint: 'flip_coin', bet: 'heads' },
    });
    coinflipLatency.add(res.timings.duration, { endpoint: 'flip_coin', bet: 'heads' });
    sleep(1);

    res = http.get(`${baseUrl}/flip_coin.php?bet=tails`, {
      tags: { name: 'CoinflipTails', endpoint: 'flip_coin', bet: 'tails' },
    });
    coinflipLatency.add(res.timings.duration, { endpoint: 'flip_coin', bet: 'tails' });
    sleep(1);
  });
}
```

### `script_133.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [7]
- **Snippet:**
```js
export function coinflip(baseUrl) {
```
- **Refactored:**
```js
import http from 'k6/http';
import { Trend } from 'k6/metrics';
import { group, sleep } from 'k6';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95 percent of response times must be below 500ms
    'coinflip_duration': ['p(95)<500'], // 95 percent of custom metric samples must be below 500ms
  },
};

const coinflipLatency = new Trend('coinflip_duration');

export function coinflip(baseUrl) { //...
```

**Smell 3: Not checking requests**

- **Lines:** [10, 15]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`);
```
- **Refactored:**
```js
import { group, sleep, check } from 'k6';

//...

export function coinflip(baseUrl) {
  group('Coinflip game', function () {
    let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`);
    check(res, { 'status is 200 (heads)': (r) => r.status === 200 });
    coinflipLatency.add(res.timings.duration);
    sleep(1);

    res = http.get(`${baseUrl}/flip_coin.php?bet=tails`);
    check(res, { 'status is 200 (tails)': (r) => r.status === 200 });
    coinflipLatency.add(res.timings.duration);
    sleep(1);
  });
}
```

**Smell 4: Not using tags**

- **Lines:** [10, 15]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`);
```
- **Refactored:**
```js
export function coinflip(baseUrl) {
  group('Coinflip game', function () {
    let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`, {
      tags: { bet: 'heads' },
    });
    coinflipLatency.add(res.timings.duration);
    sleep(1);

    res = http.get(`${baseUrl}/flip_coin.php?bet=tails`, {
      tags: { bet: 'tails' },
    });
    coinflipLatency.add(res.timings.duration);
    sleep(1);
  });
}
```

---

## `script_134.js`

### `script_134.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [14, 22]
- **Snippet:**
```js
http.get('http://test-api.k6.io/public/crocodiles/')
    http.get('http://test-api.k6.io/public/crocodiles/1/')
```
- **Refactored:**
```js
http.get('http://test-api.k6.io/public/crocodiles/', { tags: { name: 'GetAllCrocodiles' } })
    http.get('http://test-api.k6.io/public/crocodiles/1/', { tags: { name: 'GetCrocodileById' } })
```

---

## `script_136.js`

### `script_136.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [7]
- **Snippet:**
```js
export default function() {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
export default function() {
```

**Smell 4: Not using tags**

- **Lines:** [9, 22]
- **Snippet:**
```js
let response = http.get('https://test.k6.io/my_messages.php');
...
response = http.post('http://test.k6.io/login.php', { login: username, password: password, csrftoken: csrfToken });
```
- **Refactored:**
```js
let response = http.get('https://test.k6.io/my_messages.php', { tags: { name: 'GetMessages' } });
...
response = http.post('http://test.k6.io/login.php', { login: username, password: password, csrftoken: csrfToken }, { tags: { name: 'Login' } });
```

### `script_136.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [7]
- **Snippet:**
```js
export default function() {
    let response = http.get('https://test.k6.io/my_messages.php');
    ...
}
// No export const options with thresholds is defined.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.95'],
  },
};

export default function() {
  let response = http.get('https://test.k6.io/my_messages.php');
  check(response, {
    'is Unauthorized': r => r.body.includes('Unauthorized'),
  });

  let csrfToken = response.html().find("input[name=csrftoken]").attr("value");
  let rand = Math.floor(Math.random() * 2);
  let username = usernameArr[rand];
  let password = passwordArr[rand];

  response = http.post('http://test.k6.io/login.php', { login: username, password: password, csrftoken: csrfToken });
  check(response, {
    'is status 200': r => r.status === 200,
    'Successful login': r => r.body.includes('successfully authorized'),
  });
}
```

**Smell 4: Not using tags**

- **Lines:** [9, 22]
- **Snippet:**
```js
let response = http.get('https://test.k6.io/my_messages.php');
...
response = http.post('http://test.k6.io/login.php', { login: username, password: password, csrftoken: csrfToken });
```
- **Refactored:**
```js
let response = http.get('https://test.k6.io/my_messages.php', {
  tags: { name: 'MyMessages', flow: 'LoginFlow' },
});
check(response, {
  'is Unauthorized': r => r.body.includes('Unauthorized'),
}, { name: 'MyMessages', flow: 'LoginFlow' });

response = http.post(
  'http://test.k6.io/login.php',
  { login: username, password: password, csrftoken: csrfToken },
  { tags: { name: 'Login', flow: 'LoginFlow' } }
);
check(response, {
  'is status 200': r => r.status === 200,
  'Successful login': r => r.body.includes('successfully authorized'),
}, { name: 'Login', flow: 'LoginFlow' });
```

### `script_136.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [3]
- **Snippet:**
```js
The script does not export an `options` object with a `thresholds` property.
```
- **Refactored:**
```js
import http from 'k6/http';
import { check } from 'k6';

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],   // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests must complete below 500ms
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [9, 22]
- **Snippet:**
```js
response = http.get('https://test.k6.io/my_messages.php');
...
response = http.post('http://test.k6.io/login.php', { login: username, password: password, csrftoken: csrfToken });
```
- **Refactored:**
```js
response = http.get('https://test.k6.io/my_messages.php', {
  tags: { name: 'GetLoginPage' },
});
...
response = http.post(
  'http://test.k6.io/login.php',
  { login: username, password: password, csrftoken: csrfToken },
  { tags: { name: 'SubmitLogin' } }
);
```

---

## `script_137.js`

### `script_137.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_duration': ['p(95)<500'],
    'checks': ['rate>0.99'],
  },
};

export default function () {
```

### `script_137.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4]
- **Snippet:**
```js
export default function () {
  const res = http.post('https://quickpizza.grafana.com/api/cookies?my_cookie=hello%20world', {
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
  const res = http.post('https://quickpizza.grafana.com/api/cookies?my_cookie=hello%20world', null, {
    redirects: 0,
    tags: { name: 'Cookies' },
  });
  const jar = http.cookieJar();
  const cookies = jar.cookiesForURL('https://quickpizza.grafana.com/api/cookies');
  check(res, {
    'has cookie my_cookie': () => cookies.my_cookie && cookies.my_cookie.length > 0,
    'cookie has correct value': () => cookies.my_cookie && cookies.my_cookie[0] === 'hello world',
  });
}
```

**Smell 4: Not using tags**

- **Lines:** [5, 6, 7]
- **Snippet:**
```js
const res = http.post('https://quickpizza.grafana.com/api/cookies?my_cookie=hello%20world', {
  redirects: 0,
});
```
- **Refactored:**
```js
const res = http.post('https://quickpizza.grafana.com/api/cookies?my_cookie=hello%20world', null, {
  redirects: 0,
  tags: { name: 'Cookies' },
});
```

### `script_137.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4]
- **Snippet:**
```js
import http from 'k6/http';
import { check } from 'k6';

export default function () {
```
- **Refactored:**
```js
import http from 'k6/http';
import { check } from 'k6';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
    'checks': ['rate>0.99'],
  },
};

export default function () {
```

**Smell 4: Not using tags**

- **Lines:** [5, 6, 7]
- **Snippet:**
```js
const res = http.post('https://quickpizza.grafana.com/api/cookies?my_cookie=hello%20world', {
    redirects: 0,
  });
```
- **Refactored:**
```js
const res = http.post('https://quickpizza.grafana.com/api/cookies?my_cookie=hello%20world', {
    redirects: 0,
    tags: { name: 'SetCookieAPI' },
  });
```

---

## `script_138.js`

### `script_138.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1]
- **Snippet:**
```js
// No export const options = { thresholds: { ... } } defined anywhere in the file
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_duration{name:Get default product data by url}': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
  },
};
```

### `script_138.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [1, 63]
- **Snippet:**
```js
No export const options with thresholds is defined in this k6 code.
```
- **Refactored:**
```js
export const options = {
	thresholds: {
		http_req_failed: ['rate<0.01'],
		'http_req_duration{name:Get default product data by url}': ['p(95)<500'],
		checks: ['rate>0.99'],
	},
};

const getDefaultProduct = ( tag ) => {
	const requestHeaders = Object.assign(
		{},
		jsonAPIRequestHeader,
		commonAPIGetRequestHeaders,
		commonRequestHeaders,
		commonNonStandardHeaders
	);

	const response = http.get(
		`${ base_url }/wp-json/wc/store/v1/products/${ product_url }`,
		{
			requestHeaders,
			tags: { name: `${ tag } - Get default product data by url` },
		}
	);

	check( response, {
		'url query is status 200': ( r ) => r.status === 200,
		'url query response matches retrieved product data sku': ( r ) =>
			r.body.includes( `"sku":"${ product_sku }"` ),
	} );

	return response.json();
};
```

### `script_138.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1]
- **Snippet:**
```js
The script is missing an 'options' export with a 'thresholds' configuration. Without it, a test run has no defined pass/fail criteria.
```
- **Refactored:**
```js
/* This options block should be added to the top level of the script. */
export const options = {
  thresholds: {
    // 95% of requests should complete within 500ms.
    'http_req_duration': ['p(95)<500'],
    // The failure rate should be less than 1%.
    'http_req_failed': ['rate<0.01'],
    // Over 99% of all checks should pass.
    'checks': ['rate>0.99'],
  },
};
```

---

## `script_140.js`

### `script_140.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [50]
- **Snippet:**
```js
res = http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
res = http.get('https://test.k6.io/news.php', { tags: { name: 'NewsPage' } });
check(res, {
  'news page status is 200': (r) => r.status === 200,
  'news page body is not empty': (r) => r.body && r.body.length > 0
});
```

**Smell 4: Not using tags**

- **Lines:** [34, 50]
- **Snippet:**
```js
let res = http.get('https://test.k6.io/' + (execution.scenario.iterationInTest === 7 ? 'foo': ''));
res = http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
const isFooIteration = execution.scenario.iterationInTest === 7;
let res = http.get(`https://test.k6.io/${isFooIteration ? 'foo' : ''}`, {
  tags: { name: isFooIteration ? 'FooPage' : 'HomePage' }
});

res = http.get('https://test.k6.io/news.php', {
  tags: { name: 'NewsPage' }
});
```

### `script_140.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [34, 50]
- **Snippet:**
```js
let res = http.get('https://test.k6.io/' + (execution.scenario.iterationInTest === 7 ? 'foo': ''));
...
res = http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
let res = http.get('https://test.k6.io/' + (execution.scenario.iterationInTest === 7 ? 'foo': ''), {
    tags: { name: 'HomePage' },
  });
...
res = http.get('https://test.k6.io/news.php', {
    tags: { name: 'NewsPage' },
  });
```

**Smell 3: Not checking requests**

- **Lines:** [50]
- **Snippet:**
```js
res = http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
res = http.get('https://test.k6.io/news.php');
  check(res, {
    'news page status is 200': (r) => r.status === 200,
  });
```

---

## `script_143.js`

### `script_143.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
  },
};

export default function () {
```

**Smell 4: Not using tags**

- **Lines:** [6, 15]
- **Snippet:**
```js
const res = http.get('https://dummyjson.com/todos')
...
const res = http.get('https://dummyjson.com/todos/'+i)
```
- **Refactored:**
```js
const res = http.get('https://dummyjson.com/todos', { tags: { name: 'semua_todo' } })
...
const res = http.get('https://dummyjson.com/todos/'+i, { tags: { name: 'detail_todo' } })
```

### `script_143.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4]
- **Snippet:**
```js
export default function () {
	group('semua todo', function () {
		const res = http.get('https://dummyjson.com/todos')
...
}
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    'http_req_duration{name:TodosList}': ['p(95)<500'],
    'http_req_duration{name:TodoDetail}': ['p(95)<500'],
    checks: ['rate>0.99']
  }
}

export default function () {
  group('semua todo', function () {
    const res = http.get('https://dummyjson.com/todos', { tags: { name: 'TodosList' } })
    check(res, {
      'statusnya 200': r => r.status === 200
    })
  })

  group('detail todo', function () {
    for (let i = 0; i < 5; i++) {
      const res = http.get('https://dummyjson.com/todos/' + i, { tags: { name: 'TodoDetail' } })
      check(res, {
        'request detail statusnya 200': r => r.status === 200
      })
    }
  })
}
```

**Smell 4: Not using tags**

- **Lines:** [6, 15]
- **Snippet:**
```js
const res = http.get('https://dummyjson.com/todos')
...
const res = http.get('https://dummyjson.com/todos/'+i)
```
- **Refactored:**
```js
const res = http.get('https://dummyjson.com/todos', {
  tags: { name: 'TodosList', endpoint: 'todos' }
})

const res = http.get('https://dummyjson.com/todos/' + i, {
  tags: { name: 'TodoDetail', endpoint: 'todo-detail' }
})
```

### `script_143.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [3]
- **Snippet:**
```js
The script does not define an 'options' object with a 'thresholds' property to set pass/fail criteria for the test.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // fail if more than 1% of requests fail
    'http_req_duration': ['p(95)<500'],   // 95% of requests must complete below 500ms
    'http_req_duration{group:::semua todo}': ['p(95)<200'],
    'http_req_duration{group:::detail todo}': ['p(95)<300'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [6, 15]
- **Snippet:**
```js
const res = http.get('https://dummyjson.com/todos')
```
- **Refactored:**
```js
// At line 6:
const res = http.get('https://dummyjson.com/todos', {
  tags: { name: 'GetAllTodos' },
});

// At line 15:
const res = http.get('https://dummyjson.com/todos/'+i, {
  tags: { name: 'GetTodoByID' },
});
```

---

## `script_144.js`

### `script_144.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [16, 38]
- **Snippet:**
```js
const response = http.get(`${EnvironmentUtil.getStorefrontUrl()}/cart`, { headers: this.headers });
...
const response = http.post(`${EnvironmentUtil.getStorefrontUrl()}/cart/add/${sku}`, payload, params);
```
- **Refactored:**
```js
// In get():
const response = http.get(`${EnvironmentUtil.getStorefrontUrl()}/cart`, {
  headers: this.headers,
  tags: { name: 'Cart_Get' },
});

// In addItem():
let params = {
  redirects: 0,
  tags: { name: 'Cart_AddItem' },
};
if (this.headers) {
  params.headers = this.headers;
}
const response = http.post(`${EnvironmentUtil.getStorefrontUrl()}/cart/add/${sku}`, payload, params);
```

### `script_144.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [16, 30, 38]
- **Snippet:**
```js
const response = http.get(`${EnvironmentUtil.getStorefrontUrl()}/cart`, { headers: this.headers });

let params = {
  redirects: 0,
};

const response = http.post(`${EnvironmentUtil.getStorefrontUrl()}/cart/add/${sku}`, payload, params);
```
- **Refactored:**
```js
get() {
  const response = http.get(`${EnvironmentUtil.getStorefrontUrl()}/cart`, {
    headers: this.headers,
    tags: { name: 'Cart' },
  });

  addErrorToCounter(
    check(response, {
      'Cart was successful': (r) => r.status === 200 && r.body,
    })
  );

  return response;
}

addItem(sku, token, productOfferReference = null) {
  const payload = this._getAddToCartPayload(token, productOfferReference);

  let params = {
    redirects: 0,
    tags: { name: 'Add item to cart', endpoint: '/cart/add/:sku' },
  };

  if (this.headers) {
    params.headers = this.headers;
  }

  const response = http.post(`${EnvironmentUtil.getStorefrontUrl()}/cart/add/${sku}`, payload, params);

  addErrorToCounter(
    check(response, {
      'Add item to cart was successful': (r) => r.status === 302 && r.body,
    })
  );

  return response;
}
```

### `script_144.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [16]
- **Snippet:**
```js
const response = http.get(`${EnvironmentUtil.getStorefrontUrl()}/cart`, { headers: this.headers });
```
- **Refactored:**
```js
const response = http.get(`${EnvironmentUtil.getStorefrontUrl()}/cart`, {
  headers: this.headers,
  tags: { name: 'Cart-Get' },
});
```

**Smell 4: Not using tags**

- **Lines:** [38]
- **Snippet:**
```js
const response = http.post(`${EnvironmentUtil.getStorefrontUrl()}/cart/add/${sku}`, payload, params);
```
- **Refactored:**
```js
let params = {
  redirects: 0,
  tags: { name: 'Cart-AddItem' },
};

if (this.headers) {
  params.headers = this.headers;
}

const response = http.post(`${EnvironmentUtil.getStorefrontUrl()}/cart/add/${sku}`, payload, params);
```

---

## `script_145.js`

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
// no thresholds defined in any options object
```
- **Refactored:**
```js
export let loadOptions = {
    stages: [
        { duration: '2m', target: rampVus },
        { duration: '3m', target: rampVus },
        { duration: '3m', target: maxVus },
        { duration: '3m', target: maxVus },
        { duration: '2m', target: rampVus },
        { duration: '3m', target: rampVus },
        { duration: '2m', target: 0 },
    ],
    thresholds: {
        http_req_duration: ['p(95)<500', 'p(99)<1000'],
        http_req_failed: ['rate<0.01'],
        errors: ['rate<0.05'],
        authentication_successful: ['rate>0.95'],
    },
};
export let smokeOptions = {
    vus: 1,
    iterations: 1,
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
        errors: ['rate<0.05'],
        authentication_successful: ['rate>0.95'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [233, 263, 297, 344, 399, 434, 445, 475]
- **Snippet:**
```js
let response = http.get(ConfigurationUrl);
// ...
let response = http.get(OpenIdConnect.AuthorityEndpoint + '/.well-known/openid-configuration');
// ...
var res = http.post(OpenIdConnect.TokenEndpoint, auth_form_data, { headers: {...} });
// ...
let res = http.post(OpenIdConnect.TokenEndpoint, refresh_form_data);
// No tags attached to any request
```
- **Refactored:**
```js
// In getConfigurations():
let response = http.get(ConfigurationUrl, { tags: { name: 'GetConfiguration' } });

// In getOpenIdConfigurations():
let response = http.get(OpenIdConnect.AuthorityEndpoint + '/.well-known/openid-configuration', { tags: { name: 'GetOpenIdConfiguration' } });

// In authenticateUser():
var res = http.post(OpenIdConnect.TokenEndpoint, auth_form_data, {
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    tags: { name: 'Authenticate' },
});

// In refreshUser():
let res = http.post(OpenIdConnect.TokenEndpoint, refresh_form_data, { tags: { name: 'RefreshToken' } });

// In timelineRequests(), add tags to each request params, e.g.:
'comments': {
    method: 'GET',
    url: ServiceEndpoints.GatewayApi + 'UserProfile/' + user.hdid + '/Comment',
    params: { ...params(user), tags: { name: 'GetComments' } },
},
// ... and similarly for encounter, immz, labs, meds, notes, patient, profile, baseSite, etc.
```

### `script_145.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [67, 79, 83, 91, 106]
- **Snippet:**
```js
export let loadOptions = {
    stages: [
        { duration: "2m", target: rampVus }, // simulate ramp-up of traffic from 1 users over a few minutes.
        { duration: "3m", target: rampVus }, // stay at number of users for several minutes
        { duration: "3m", target: maxVus }, // ramp-up to users peak for some minutes (peak hour starts)
        { duration: "3m", target: maxVus }, // stay at users for short amount of time (peak hour)
        { duration: "2m", target: rampVus }, // ramp-down to lower users over 3 minutes (peak hour ends)
        { duration: "3m", target: rampVus }, // continue for additional time
        { duration: "2m", target: 0 }, // ramp-down to 0 users
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
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
        'errors': ['rate<0.01'], // custom error rate should be less than 1%
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [233, 263]
- **Snippet:**
```js
let response = http.get(ConfigurationUrl);
if (response.status == 200) {
```
- **Refactored:**
```js
let response = http.get(ConfigurationUrl);
check(response, { 'configuration GET was 200': (r) => r.status === 200 });
if (response.status == 200) {
```

**Smell 4: Not using tags**

- **Lines:** [233, 263, 297, 344]
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
        tags: { name: 'Authentication' }
    });
```

---

## `script_146.js`

### `script_146.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [34]
- **Snippet:**
```js
http.post(url,  JSON.stringify(payload), params);
```
- **Refactored:**
```js
import { check } from 'k6';

const res = http.post(url, JSON.stringify(payload), params);
check(res, {
  'status is 201': (r) => r.status === 201,
  'response body is not empty': (r) => r.body && r.body.length > 0,
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
  tags: { name: 'CreateUser' },
};
const res = http.post(url, JSON.stringify(payload), params);
check(res, {
  'status is 201': (r) => r.status === 201,
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
// ...
// NOTE: The 'return' on line 32 made the http.post call unreachable and has been removed.
const res = http.post(url, JSON.stringify(payload), params);
check(res, {
  'status is 201 (Created)': (r) => r.status === 201,
});
```

**Smell 4: Not using tags**

- **Lines:** [25, 34]
- **Snippet:**
```js
var params = {
  headers: {
    'Content-Type': 'application/json',
  },
};
// ...
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
// ...
// NOTE: The 'return' on line 32 made the http.post call unreachable and has been removed.
http.post(url, JSON.stringify(payload), params);
```

---

## `script_148.js`

### `script_148.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [23]
- **Snippet:**
```js
const response = http.get(url, { headers });
```
- **Refactored:**
```js
import { check } from 'k6';

const response = http.get(url, { headers });
check(response, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [23]
- **Snippet:**
```js
const response = http.get(url, { headers });
```
- **Refactored:**
```js
const response = http.get(url, { headers, tags: { name: 'BasicFast' } });
// Also update thresholds to leverage tags:
// 'http_req_duration{name:BasicFast}': ['p(95)<200']
```

### `script_148.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [23]
- **Snippet:**
```js
const response = http.get(url, { headers });
```
- **Refactored:**
```js
import { sleep, check } from 'k6';
import http from 'k6/http';

export default function () {
    const url = `${BASE_URL}/api/basic/fast`;
    const headers = { 'Accept': 'application/json' };

    const response = http.get(url, { headers });

    check(response, {
        'status is 200': (r) => r.status === 200,
        'response is JSON': (r) => r.headers['Content-Type'] && r.headers['Content-Type'].includes('application/json'),
    });

    sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [23]
- **Snippet:**
```js
const response = http.get(url, { headers });
```
- **Refactored:**
```js
const response = http.get(url, {
    headers,
    tags: {
        name: 'BasicFast',
        endpoint: '/api/basic/fast'
    }
});
```

### `script_148.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [23]
- **Snippet:**
```js
const response = http.get(url, { headers });
```
- **Refactored:**
```js
import { sleep, check } from 'k6';
import http from 'k6/http';

// ...

export default function () {
    const url = `${BASE_URL}/api/basic/fast`;
    const headers = { 'Accept': 'application/json' };

    const response = http.get(url, { headers });

    check(response, {
        'is status 200': (r) => r.status === 200,
    });

    sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [23]
- **Snippet:**
```js
const response = http.get(url, { headers });
```
- **Refactored:**
```js
const response = http.get(url, {
  headers,
  tags: { name: 'FastAPI' },
});
```

---

## `script_149.js`

### `script_149.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
import { test_options } from './options.js';

// Merge imported options with performance thresholds
export let options = Object.assign({}, test_options, {
  thresholds: {
    'http_req_failed': ['rate<0.01'],                // http errors should be less than 1%
    'http_req_duration{name:GET}': ['p(95)<500'], // 95% of 'GET' requests must complete below 500ms
    'checks': ['rate>0.99']                          // 99% of checks must pass
  }
});
```

---

## `script_150.js`

### `script_150.js` — CLAUDE

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
        'checks': ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [22, 23, 24]
- **Snippet:**
```js
const resCo = httppost("A-1536", {
        operation: "test",
    })
```
- **Refactored:**
```js
const resCo = http.post(`${hostprefix}/SYNC-A-1536`, JSON.stringify({ operation: "test" }), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'SYNC-A-1536' },
});
```

### `script_150.js` — CHATGPT

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
        tags: { name: `SYNC-${task}`, endpoint: `SYNC-${task}` },
    }
);

export default function (data) {
    const task = 'A-1536';
    const resCo = httppost(task, {
        operation: 'test',
    });
    check(resCo, { 'A status was 200': (r) => r.status == 200 }, { endpoint: `SYNC-${task}` });
}
```

### `script_150.js` — GEMINI

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
            preAllocatedVUs: 100,
            maxVUs: 200,
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
const httppost = (task, body) => http.post(
    `${hostprefix}/SYNC-${task}`,
    JSON.stringify(body),
    {
        headers: { 'Content-Type': 'application/json' },
        tags: { name: task },
    }
)
```

---

## `script_151.js`

### `script_151.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [59]
- **Snippet:**
```js
let res = http.get(SEAT_LOOKUP_ENDPOINT, { headers });
```
- **Refactored:**
```js
let res = http.get(SEAT_LOOKUP_ENDPOINT, { headers, tags: { name: 'SeatLookup' } });
```

### `script_151.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [14, 18, 19]
- **Snippet:**
```js
let res = http.post(TOKEN_ISSUE_ENDPOINT, JSON.stringify({ userId: i, concertId: 1 }), {
    headers: { 'Content-Type': 'application/json' },
});

if (res.status === 201) {
    let responseBody = JSON.parse(res.body);
```
- **Refactored:**
```js
let res = http.post(TOKEN_ISSUE_ENDPOINT, JSON.stringify({ userId: i, concertId: 1 }), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'TokenIssue' },
});

let responseBody = {};
try {
    responseBody = JSON.parse(res.body);
} catch (e) {}

check(res, {
    'token issue status is 201': (r) => r.status === 201,
    'token exists': () => Boolean(responseBody?.data?.token),
}, { name: 'TokenIssue' });

if (res.status === 201 && responseBody?.data?.token) {
    tokens.push(responseBody.data.token);
}
```

**Smell 4: Not using tags**

- **Lines:** [14, 59]
- **Snippet:**
```js
let res = http.post(TOKEN_ISSUE_ENDPOINT, JSON.stringify({ userId: i, concertId: 1 }), {
    headers: { 'Content-Type': 'application/json' },
});

let res = http.get(SEAT_LOOKUP_ENDPOINT, { headers });
```
- **Refactored:**
```js
let res = http.post(TOKEN_ISSUE_ENDPOINT, JSON.stringify({ userId: i, concertId: 1 }), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'TokenIssue', endpoint: 'queue_token' },
});

let headers = { 'X-Queue-Token': token };
let res = http.get(SEAT_LOOKUP_ENDPOINT, {
    headers,
    tags: { name: 'SeatLookup', endpoint: 'seat_lookup' },
});

check(res, {
    'status is 200': (r) => r.status === 200,
    'response time is < 2000ms': (r) => r.timings.duration < 2000,
}, { name: 'SeatLookup', endpoint: 'seat_lookup' });
```

### `script_151.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [14, 59]
- **Snippet:**
```js
let res = http.post(TOKEN_ISSUE_ENDPOINT, JSON.stringify({ userId: i, concertId: 1 }), {
            headers: { 'Content-Type': 'application/json' },
        });

// ...

let res = http.get(SEAT_LOOKUP_ENDPOINT, { headers });
```
- **Refactored:**
```js
let res = http.post(TOKEN_ISSUE_ENDPOINT, JSON.stringify({ userId: i, concertId: 1 }), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'IssueToken' },
});

// ...

let res = http.get(SEAT_LOOKUP_ENDPOINT, { 
    headers, 
    tags: { name: 'SeatLookup' } 
});
```

---

## `script_152.js`

### `script_152.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [6]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  vus: 10,
  duration: '30s',
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};

export default function () {
```

**Smell 3: Not checking requests**

- **Lines:** [10]
- **Snippet:**
```js
const response = http.get(url, { headers });
```
- **Refactored:**
```js
import { check } from 'k6';

const response = http.get(url, { headers });
check(response, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [10]
- **Snippet:**
```js
const response = http.get(url, { headers });
```
- **Refactored:**
```js
const response = http.get(url, { headers, tags: { name: 'FastRandom' } });
```

### `script_152.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [6]
- **Snippet:**
```js
export default function () {
    const url = `${BASE_URL}/api/basic/fast-random`;
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    'http_req_duration{name:FastRandom}': ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};

export default function () {
  const url = `${BASE_URL}/api/basic/fast-random`;
  const headers = { Accept: 'application/json' };
  const response = http.get(url, { headers, tags: { name: 'FastRandom' } });
  check(response, {
    'status is 200': (r) => r.status === 200,
  });
  sleep(1);
}
```

**Smell 3: Not checking requests**

- **Lines:** [10]
- **Snippet:**
```js
const response = http.get(url, { headers });
```
- **Refactored:**
```js
import { sleep, check } from 'k6';
import http from 'k6/http';

export default function () {
  const url = `${BASE_URL}/api/basic/fast-random`;
  const headers = { Accept: 'application/json' };

  const response = http.get(url, { headers });
  check(response, {
    'status is 200': (r) => r.status === 200,
    'content type is JSON': (r) => r.headers['Content-Type'] && r.headers['Content-Type'].includes('application/json'),
  });

  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [10]
- **Snippet:**
```js
const response = http.get(url, { headers });
```
- **Refactored:**
```js
export default function () {
  const url = `${BASE_URL}/api/basic/fast-random`;
  const headers = { Accept: 'application/json' };
  const params = {
    headers,
    tags: {
      name: 'FastRandom',
      endpoint: '/api/basic/fast-random',
    },
  };

  const response = http.get(url, params);
  sleep(1);
}
```

### `script_152.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5]
- **Snippet:**
```js
// The script does not define an 'options' export with a 'thresholds' object.
```
- **Refactored:**
```js
Add an 'options' export with a 'thresholds' object to define pass/fail criteria for the test.

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [10]
- **Snippet:**
```js
const response = http.get(url, { headers });
```
- **Refactored:**
```js
Import 'check' from the 'k6' module and use it to validate the response status after the request is made.

import { sleep, check } from 'k6';
// ...
const response = http.get(url, { headers });
check(response, {
  'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [10]
- **Snippet:**
```js
const response = http.get(url, { headers });
```
- **Refactored:**
```js
Add a 'tags' object to the request parameters to categorize its metrics, making them easier to filter and analyze.

const response = http.get(url, {
  headers,
  tags: { name: 'GetFastRandom' },
});
```

---

## `script_153.js`

### `script_153.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '3s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '3s',
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01']
    }
}
```

### `script_153.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '3s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '3s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500']
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [10]
- **Snippet:**
```js
const res = http.get('http://test.k6.io/')
```
- **Refactored:**
```js
const res = http.get('http://test.k6.io/', {
    tags: { name: 'Home' }
});
```

### `script_153.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '3s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '3s',
    thresholds: {
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
    },
}
```

**Smell 4: Not using tags**

- **Lines:** [10]
- **Snippet:**
```js
const res = http.get('http://test.k6.io/')
```
- **Refactored:**
```js
const res = http.get('http://test.k6.io/', {
        tags: { name: 'Homepage' },
    });
```

---

## `script_154.js`

### `script_154.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [33, 34, 35, 36, 37, 38]
- **Snippet:**
```js
export const options = {
  stages: [
    { duration: '1s', target: 1 }, // warm-up
    { duration: '20s', target: 300 },
  ],
};
```
- **Refactored:**
```js
export const options = {
  stages: [
    { duration: '1s', target: 1 }, // warm-up
    { duration: '20s', target: 300 },
  ],
  thresholds: {
    'http_req_duration': ['p(95)<300'],
    'http_reqs': ['rate>500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [42]
- **Snippet:**
```js
const res = http.get(`${API_URL}${url}`);
```
- **Refactored:**
```js
const res = http.get(`${API_URL}${url}`, { tags: { name: url } });
```

### `script_154.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [33, 34, 35, 36, 37, 38]
- **Snippet:**
```js
export const options = {
  stages: [
    { duration: '1s', target: 1 }, // warm-up
    { duration: '20s', target: 300 },
  ],
};
```
- **Refactored:**
```js
export const options = {
  stages: [
    { duration: '1s', target: 1 }, // warm-up
    { duration: '20s', target: 300 },
  ],
  thresholds: {
    'http_req_duration{name:Products}': ['p(95)<300'],
    http_reqs: ['rate>500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [42]
- **Snippet:**
```js
const res = http.get(`${API_URL}${url}`);
```
- **Refactored:**
```js
const res = http.get(`${API_URL}${url}`, {
  tags: {
    name: 'Products',
    endpoint: url,
  },
});

check(res, { 'status is 200': (r) => r.status === 200 }, {
  endpoint: url,
});
```

### `script_154.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [33, 34, 35, 36, 37, 38]
- **Snippet:**
```js
export const options = {
  stages: [
    { duration: '1s', target: 1 }, // warm-up
    { duration: '20s', target: 300 },
  ],
};
```
- **Refactored:**
```js
export const options = {
  stages: [
    { duration: '1s', target: 1 }, // warm-up
    { duration: '20s', target: 300 },
  ],
  thresholds: {
    'http_req_duration': ['p(95)<300'], // As per requirements
    'checks': ['rate>0.95'], // More than 95% of checks must pass
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [42]
- **Snippet:**
```js
const res = http.get(`${API_URL}${url}`);
```
- **Refactored:**
```js
const res = http.get(`${API_URL}${url}`, {
    tags: { endpoint: url },
  });
```

---

## `script_155.js`

### `script_155.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
  vus: 5,
  duration: '1m',
};
```
- **Refactored:**
```js
export let options = {
  vus: 5,
  duration: '1m',
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [10]
- **Snippet:**
```js
let res = http.get('http://localhost:8080/');
```
- **Refactored:**
```js
let res = http.get('http://localhost:8080/', { tags: { name: 'Homepage' } });
```

### `script_155.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
  vus: 5,
  duration: '1m',
};
```
- **Refactored:**
```js
export let options = {
  vus: 5,
  duration: '1m',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [10]
- **Snippet:**
```js
let res = http.get('http://localhost:8080/');
```
- **Refactored:**
```js
let res = http.get('http://localhost:8080/', {
  tags: { name: 'Home' },
});
check(res, { 'status is 200': (r) => r.status === 200 }, { name: 'Home' });
```

### `script_155.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
  vus: 5,   // 5 usuários simultâneos
  duration: '1m',  // Teste de 1 minuto
};
```
- **Refactored:**
```js
export let options = {
  vus: 5,   // 5 usuários simultâneos
  duration: '1m',  // Teste de 1 minuto
  thresholds: {
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [10]
- **Snippet:**
```js
let res = http.get('http://localhost:8080/');
```
- **Refactored:**
```js
let res = http.get('http://localhost:8080/', {
  tags: { name: 'Homepage' },
});
```

---

## `script_156.js`

### `script_156.js` — CLAUDE

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
        http_req_failed: ['rate<0.01']
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [20, 21, 22]
- **Snippet:**
```js
const response = http.post(`${apiUrl}/v-fluent-res/users`, JSON.stringify(request), {
        headers: { "Content-Type": "application/json" }
    });
```
- **Refactored:**
```js
const response = http.post(`${apiUrl}/v-fluent-res/users`, JSON.stringify(request), {
        headers: { "Content-Type": "application/json" },
        tags: { name: "CreateUser" }
    });
```

### `script_156.js` — CHATGPT

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
        http_req_duration: ["p(95)<500"],
        checks: ["rate>0.95"]
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [20, 21, 22]
- **Snippet:**
```js
const response = http.post(`${apiUrl}/v-fluent-res/users`, JSON.stringify(request), {
    headers: { "Content-Type": "application/json" }
});
```
- **Refactored:**
```js
const response = http.post(`${apiUrl}/v-fluent-res/users`, JSON.stringify(request), {
    headers: { "Content-Type": "application/json" },
    tags: { name: "CreateUserValidation", endpoint: "/v-fluent-res/users" }
});
```

### `script_156.js` — GEMINI

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
        'http_req_failed': ['rate<0.01'], // less than 1% failed requests
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
        'checks{ "response code was 400" }': ['rate>0.9'], // example: ensure over 90% of checks for 400 pass
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [20, 21, 22]
- **Snippet:**
```js
const response = http.post(`${apiUrl}/v-fluent-res/users`, JSON.stringify(request), {
    headers: { "Content-Type": "application/json" }
});
```
- **Refactored:**
```js
const response = http.post(`${apiUrl}/v-fluent-res/users`, JSON.stringify(request), {
    headers: { "Content-Type": "application/json" },
    tags: { name: 'CreateUser' }
});
```

---

## `script_158.js`

### `script_158.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [53, 58]
- **Snippet:**
```js
orderReference = JSON.parse(checkoutResource.checkout().body).data.attributes.orderReference;
// ...
const response = cartReorderResource.reorder();
```
- **Refactored:**
```js
// At the top of the file, add: import { check } from 'k6';

// Inside the 'Checkout' group:
const checkoutResponse = checkoutResource.checkout();
check(checkoutResponse, { 'checkout succeeded': (r) => r.status === 200 });
orderReference = JSON.parse(checkoutResponse.body).data.attributes.orderReference;

// Inside the testConfiguration.group:
const response = cartReorderResource.reorder();
check(response, { 'reorder succeeded': (r) => r.status === 200 });
```

---

## `script_160.js`

### `script_160.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
    vus: 30,
    duration: '30s',
};
```
- **Refactored:**
```js
export const options = {
    vus: 30,
    duration: '30s',
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [14]
- **Snippet:**
```js
const res = http.get(url);
```
- **Refactored:**
```js
const res = http.get(url, { tags: { name: 'GetConcerts' } });
```

### `script_160.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
    vus: 30,
    duration: '30s',
};
```
- **Refactored:**
```js
export const options = {
    vus: 30,
    duration: '30s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        'http_req_duration{name:ConcertsByDate}': ['p(95)<500'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [14]
- **Snippet:**
```js
const res = http.get(url);
```
- **Refactored:**
```js
const res = http.get(url, {
    tags: {
        name: 'ConcertsByDate',
        endpoint: 'GET /concerts',
    },
});

const success = check(res, {
    'status is 200': (r) => r.status === 200,
}, {
    name: 'ConcertsByDate',
    endpoint: 'GET /concerts',
});
```

### `script_160.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
    vus: 30, // 동시에 실행할 가상 사용자 수
    duration: '30s', // 테스트 지속 시간
};
```
- **Refactored:**
```js
export const options = {
    vus: 30, // 동시에 실행할 가상 사용자 수
    duration: '30s', // 테스트 지속 시간
    thresholds: {
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [14]
- **Snippet:**
```js
const res = http.get(url);
```
- **Refactored:**
```js
const res = http.get(url, {
    tags: { name: 'GetConcerts' },
});
```

---

## `script_161.js`

### `script_161.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [6]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  vus: 1,
  duration: '30s',
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [7]
- **Snippet:**
```js
const response = http.get(`${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`);
```
- **Refactored:**
```js
import { check, sleep } from 'k6';

const response = http.get(`${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`);
check(response, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [7]
- **Snippet:**
```js
const response = http.get(`${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`);
```
- **Refactored:**
```js
const response = http.get(`${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`, {
  tags: { name: 'EchoEndpoint' },
});
```

### `script_161.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [6]
- **Snippet:**
```js
export default function () {
  const response = http.get(`${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`);
  ...
}
```
- **Refactored:**
```js
import { sleep } from 'k6';
import http from 'k6/http';

const BASE_URL = 'http://localhost:8888/alphamart';

export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01']
  }
};

export default function () {
  const response = http.get(`${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`);
  sleep(1);
}
```

**Smell 3: Not checking requests**

- **Lines:** [7]
- **Snippet:**
```js
const response = http.get(`${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`);
```
- **Refactored:**
```js
import { sleep, check } from 'k6';
import http from 'k6/http';

const BASE_URL = 'http://localhost:8888/alphamart';

export default function () {
  const response = http.get(`${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`);

  check(response, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0
  });

  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [7]
- **Snippet:**
```js
const response = http.get(`${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`);
```
- **Refactored:**
```js
import { sleep, check } from 'k6';
import http from 'k6/http';

const BASE_URL = 'http://localhost:8888/alphamart';

export const options = {
  thresholds: {
    'http_req_duration{name:BasicEcho}': ['p(95)<500'],
    'http_req_failed{name:BasicEcho}': ['rate<0.01']
  }
};

export default function () {
  const response = http.get(
    `${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`,
    { tags: { name: 'BasicEcho', endpoint: '/api/basic/echo' } }
  );

  check(response, {
    'status is 200': (r) => r.status === 200
  }, { name: 'BasicEcho' });

  sleep(1);
}
```

### `script_161.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** []
- **Snippet:**
```js
The script does not export an `options` object, and therefore does not define any thresholds to validate the test results against performance goals.
```
- **Refactored:**
```js
import { sleep } from 'k6';
import http from 'k6/http';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
  },
};

// ...
```

**Smell 3: Not checking requests**

- **Lines:** [7]
- **Snippet:**
```js
const response = http.get(`${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`);
```
- **Refactored:**
```js
import { sleep, check } from 'k6';
import http from 'k6/http';

//... inside default function
const response = http.get(`${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`);
check(response, {
  'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [7]
- **Snippet:**
```js
const response = http.get(`${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`);
```
- **Refactored:**
```js
//... inside default function
const response = http.get(
  `${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`,
  {
    tags: { name: 'EchoAPI' },
  }
);
```

---

## `script_162.js`

### `script_162.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [33, 62, 65, 66, 69, 70]
- **Snippet:**
```js
const to = {
  failed_requests: ['rate<0.1'],
  insert_trend: ['p(95)<1000'],
}
// ...
try {
  // ...
  myFailRate.add(false)
} catch (e) {
  // ...
  myFailRate.add(true)
  counterFailed.add(1)
}
// ...
counterInserts.add(1)
insertTrend.add(exFinish - exStart)
```
- **Refactored:**
```js
// Refactor thresholds to be tag-specific
const to = {
  failed_requests: ['rate<0.1'],
  'insert_trend{name:insert_position}': ['p(95)<1000'],
}

// ... in default function

const requestTags = { name: 'insert_position' };

// ... inside the try/catch blocks
try {
  // ...
  myFailRate.add(false, requestTags)
} catch (e) {
  // ...
  myFailRate.add(true, requestTags)
  counterFailed.add(1, requestTags)
}
// ...
counterInserts.add(1, requestTags)
insertTrend.add(exFinish - exStart, requestTags)
```

---

## `script_163.js`

### `script_163.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
  vus: 1,
  iterations: 10
};
```
- **Refactored:**
```js
export let options = {
  vus: 1,
  iterations: 10,
  thresholds: {
    'http_req_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.1'],
    'checks': ['rate>=1.0']
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [21]
- **Snippet:**
```js
const res = http.post('http://localhost:3000/guestUser/logIn', payload, { headers });
```
- **Refactored:**
```js
const res = http.post('http://localhost:3000/guestUser/logIn', payload, { headers, tags: { name: 'Login' } });
```

### `script_163.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
  vus: 1,
  iterations: 10
};
```
- **Refactored:**
```js
export let options = {
  vus: 1,
  iterations: 10,
  thresholds: {
    http_req_failed: ['rate<0.01'],
    'http_req_duration{name:GuestUserLogin}': ['p(95)<500'],
    checks: ['rate>0.95']
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [21]
- **Snippet:**
```js
const res = http.post('http://localhost:3000/guestUser/logIn', payload, { headers });
```
- **Refactored:**
```js
const params = {
  headers,
  tags: {
    name: 'GuestUserLogin',
    endpoint: '/guestUser/logIn',
    flow: 'rate-limit-login'
  }
};

const res = http.post('http://localhost:3000/guestUser/logIn', payload, params);

check(res, {
  'status is 200/400/401': (r) => [200, 400, 401].includes(r.status),
}, { name: 'GuestUserLogin', endpoint: '/guestUser/logIn', flow: 'rate-limit-login' });
```

### `script_163.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
  vus: 1,                // 1 virtual user = 1 IP
  iterations: 10         // Send only 10 requests total
};
```
- **Refactored:**
```js
export let options = {
  vus: 1,
  iterations: 10,
  thresholds: {
    // Ensure the check for valid status codes passes for every request
    'checks': ['rate==1.0'],
    // Ensure 95% of requests complete within 500ms
    'http_req_duration': ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [21]
- **Snippet:**
```js
const res = http.post('http://localhost:3000/guestUser/logIn', payload, { headers });
```
- **Refactored:**
```js
const res = http.post('http://localhost:3000/guestUser/logIn', payload, {
    headers: headers,
    tags: {
      name: 'GuestLogin',
    },
  });
```

---

## `script_165.js`

### `script_165.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [43, 44, 45, 46, 47, 48]
- **Snippet:**
```js
const response = categoryPage.get(category.url, {
  'label[]': 'KSixTestLabel',
  'color[]': 'Black',
  brand: 'Nike',
  ipp: 36,
});
```
- **Refactored:**
```js
import { group, check } from 'k6';

export default function (data) {
  const category = fixture.iterateData(data);

  group('Category Filter Products', () => {
    const categoryPage = new CategoryPage();
    const response = categoryPage.get(category.url, {
      'label[]': 'KSixTestLabel',
      'color[]': 'Black',
      brand: 'Nike',
      ipp: 36,
    });

    check(response, {
      'category filter returned 200': (r) => r.status === 200,
      'category filter response is not empty': (r) => r.body && r.body.length > 0,
    });

    metrics[testConfiguration.metrics[0]].add(response.timings.duration);
  });
}
```

**Smell 4: Not using tags**

- **Lines:** [43, 50]
- **Snippet:**
```js
const response = categoryPage.get(category.url, {
  'label[]': 'KSixTestLabel',
  'color[]': 'Black',
  brand: 'Nike',
  ipp: 36,
});

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
export default function (data) {
  const category = fixture.iterateData(data);

  group('Category Filter Products', () => {
    const categoryPage = new CategoryPage();
    const tags = {
      name: 'S25_get_category',
      group: 'Category',
      flow: 'Category Filter Products',
    };

    const response = categoryPage.get(
      category.url,
      {
        'label[]': 'KSixTestLabel',
        'color[]': 'Black',
        brand: 'Nike',
        ipp: 36,
      },
      { tags }
    );

    metrics[testConfiguration.metrics[0]].add(response.timings.duration, tags);
  });
}
```

### `script_165.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [43, 50]
- **Snippet:**
```js
const response = categoryPage.get(category.url, {
      'label[]': 'KSixTestLabel',
      'color[]': 'Black',
      brand: 'Nike',
      ipp: 36,
    });

    metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const response = categoryPage.get(category.url, {
  'label[]': 'KSixTestLabel',
  'color[]': 'Black',
  brand: 'Nike',
  ipp: 36,
});

const isSuccessful = check(response, {
  'response status is 200': (r) => r.status === 200,
});

if (isSuccessful) {
  metrics[testConfiguration.metrics[0]].add(response.timings.duration);
}
```

**Smell 4: Not using tags**

- **Lines:** [43]
- **Snippet:**
```js
const response = categoryPage.get(category.url, {
      'label[]': 'KSixTestLabel',
      'color[]': 'Black',
      brand: 'Nike',
      ipp: 36,
    });
```
- **Refactored:**
```js
// The underlying HTTP request inside the Page Object should be tagged.
// This allows for better filtering and using thresholds on built-in metrics.
// Assuming the `categoryPage.get` method is updated to accept tags:

const response = categoryPage.get(category.url, 
  {
    'label[]': 'KSixTestLabel',
    'color[]': 'Black',
    brand: 'Nike',
    ipp: 36,
  }, 
  { name: 'CategoryFilterProducts' } // Tag added to the request
);
```

---

## `script_166.js`

### `script_166.js` — CLAUDE

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
    'checks': ['rate>0.99'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [12, 13, 14, 15, 16, 17]
- **Snippet:**
```js
let responses = http.batch([
    ['GET', domain + '/'],
    ['GET', domain + '/static/css/site.css'],
    ['GET', domain + '/static/js/prisms.js'],
    ['GET', domain + '/static/favicon.ico']
])
```
- **Refactored:**
```js
let responses = http.batch([
    ['GET', domain + '/'],
    ['GET', domain + '/static/css/site.css'],
    ['GET', domain + '/static/js/prisms.js'],
    ['GET', domain + '/static/favicon.ico']
]);

check(responses[0], {
  'Homepage status is 200': (r) => r.status === 200,
  'Homepage successfully loaded': (r) => r.body.includes('Collection of simple web-pages suitable for load testing'),
});
check(responses[1], {
  'CSS file status is 200': (r) => r.status === 200,
});
check(responses[2], {
  'JS file status is 200': (r) => r.status === 200,
});
check(responses[3], {
  'Favicon status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [12, 13, 14, 15, 16, 17]
- **Snippet:**
```js
let responses = http.batch([
    ['GET', domain + '/'],
    ['GET', domain + '/static/css/site.css'],
    ['GET', domain + '/static/js/prisms.js'],
    ['GET', domain + '/static/favicon.ico']
])
```
- **Refactored:**
```js
let responses = http.batch([
    ['GET', domain + '/', null, { tags: { name: 'Homepage' } }],
    ['GET', domain + '/static/css/site.css', null, { tags: { name: 'CSS' } }],
    ['GET', domain + '/static/js/prisms.js', null, { tags: { name: 'JS' } }],
    ['GET', domain + '/static/favicon.ico', null, { tags: { name: 'Favicon' } }]
]);
```

### `script_166.js` — CHATGPT

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
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [12, 13, 14, 15, 16, 17, 24, 25, 26]
- **Snippet:**
```js
let responses = http.batch([
  ['GET', domain + '/'],
  ['GET', domain + '/static/css/site.css'],
  ['GET', domain + '/static/js/prisms.js'],
  ['GET', domain + '/static/favicon.ico']
]);

check(responses[0], {
  'Homepage successfully loaded': (r) => r.body.includes("Collection of simple web-pages suitable for load testing"),
});
```
- **Refactored:**
```js
let responses = http.batch([
  ['GET', domain + '/'],
  ['GET', domain + '/static/css/site.css'],
  ['GET', domain + '/static/js/prisms.js'],
  ['GET', domain + '/static/favicon.ico']
]);

check(responses, {
  'Homepage status is 200': (r) => r[0].status === 200,
  'Homepage successfully loaded': (r) => r[0].body.includes('Collection of simple web-pages suitable for load testing'),
  'CSS status is 200': (r) => r[1].status === 200,
  'JS status is 200': (r) => r[2].status === 200,
  'Favicon status is 200': (r) => r[3].status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [12, 13, 14, 15, 16, 17]
- **Snippet:**
```js
let responses = http.batch([
  ['GET', domain + '/'],
  ['GET', domain + '/static/css/site.css'],
  ['GET', domain + '/static/js/prisms.js'],
  ['GET', domain + '/static/favicon.ico']
]);
```
- **Refactored:**
```js
let responses = http.batch([
  ['GET', domain + '/', null, { tags: { name: 'Homepage', endpoint: 'home' } }],
  ['GET', domain + '/static/css/site.css', null, { tags: { name: 'SiteCSS', endpoint: 'static-css' } }],
  ['GET', domain + '/static/js/prisms.js', null, { tags: { name: 'PrismsJS', endpoint: 'static-js' } }],
  ['GET', domain + '/static/favicon.ico', null, { tags: { name: 'Favicon', endpoint: 'favicon' } }]
]);
```

### `script_166.js` — GEMINI

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
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [12, 13, 14, 15, 16, 17]
- **Snippet:**
```js
let responses = http.batch([
    ['GET', domain + '/'],
    ['GET', domain + '/static/css/site.css'],
    ['GET', domain + '/static/js/prisms.js'],
    ['GET', domain + '/static/favicon.ico']
])
```
- **Refactored:**
```js
check(responses[0], {
  'Homepage status is 200': (r) => r.status === 200,
  'Homepage successfully loaded': (r) => r.body.includes("Collection of simple web-pages suitable for load testing"),
});
check(responses[1], { 'CSS status is 200': (r) => r.status === 200 });
check(responses[2], { 'JS status is 200': (r) => r.status === 200 });
check(responses[3], { 'Favicon status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [12, 13, 14, 15, 16, 17]
- **Snippet:**
```js
let responses = http.batch([
    ['GET', domain + '/'],
    ['GET', domain + '/static/css/site.css'],
    ['GET', domain + '/static/js/prisms.js'],
    ['GET', domain + '/static/favicon.ico']
])
```
- **Refactored:**
```js
let responses = http.batch([
    { method: 'GET', url: domain + '/', params: { tags: { name: 'Homepage' } } },
    { method: 'GET', url: domain + '/static/css/site.css', params: { tags: { name: 'Assets' } } },
    { method: 'GET', url: domain + '/static/js/prisms.js', params: { tags: { name: 'Assets' } } },
    { method: 'GET', url: domain + '/static/favicon.ico', params: { tags: { name: 'Assets' } } }
])
```

---

## `script_167.js`

### `script_167.js` — CLAUDE

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
        'checks': ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [22, 23, 24]
- **Snippet:**
```js
const resCo = httppost("A-2048", {
        operation: "test",
    })
```
- **Refactored:**
```js
const httppost = (task, body) => http.post(
    `${hostprefix}/SYNC-${task}`,
    JSON.stringify(body),
    {
        headers: { 'Content-Type': 'application/json' },
        tags: { name: `SYNC-${task}` }
    }
);

// In default function:
const resCo = httppost("A-2048", {
    operation: "test",
});
```

### `script_167.js` — CHATGPT

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
        tags: { name: `SYNC-${task}`, endpoint: `/SYNC-${task}`, operation: task },
    }
);
```

### `script_167.js` — GEMINI

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
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: `SYNC-${task}` },
})
```

---

## `script_168.js`

### `script_168.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '5s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '5s',
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01']
    }
}
```

**Smell 3: Not checking requests**

- **Lines:** [11, 12, 13, 14, 15]
- **Snippet:**
```js
export default function (data) {
    console.log('-- VU stage --');
    // console.log(data);
    sleep(1);
}
```
- **Refactored:**
```js
import { check } from 'k6';

export default function (data) {
    console.log('-- VU stage --');
    const res = http.get('https://your-endpoint.com');
    check(res, {
        'status is 200': (r) => r.status === 200,
        'response time < 500ms': (r) => r.timings.duration < 500
    });
    sleep(1);
}
```

### `script_168.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '5s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '5s',
    thresholds: {
        iteration_duration: ['p(95)<1500']
    }
};
```

### `script_168.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '5s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '5s',
    thresholds: {
        // For example, ensure 95% of iterations complete within 1.5s
        'iteration_duration': ['p(95)<1500'],
    },
}
```

---

## `script_170.js`

### `script_170.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
  vus: 1000,
  duration: '300s',
};
```
- **Refactored:**
```js
export let options = {
  vus: 1000,
  duration: '300s',
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
let response = http.get('https://gqfnc7ztrujstj3fyuzjdzjb2u0nqvus.lambda-url.us-east-2.on.aws');
```
- **Refactored:**
```js
let response = http.get('https://gqfnc7ztrujstj3fyuzjdzjb2u0nqvus.lambda-url.us-east-2.on.aws', { tags: { name: 'LambdaEndpoint' } });
```

### `script_170.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
  vus: 1000,
  duration: '300s',
};
```
- **Refactored:**
```js
export let options = {
  vus: 1000,
  duration: '300s',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
let response = http.get('https://gqfnc7ztrujstj3fyuzjdzjb2u0nqvus.lambda-url.us-east-2.on.aws');
```
- **Refactored:**
```js
const params = {
  tags: {
    name: 'LambdaEndpoint',
    endpoint: 'lambda-url',
  },
};
let response = http.get('https://gqfnc7ztrujstj3fyuzjdzjb2u0nqvus.lambda-url.us-east-2.on.aws', params);
```

### `script_170.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
  vus: 1000, // Number of virtual users
  duration: '300s', // Duration of the test
};
```
- **Refactored:**
```js
export let options = {
  vus: 1000,
  duration: '300s',
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
let response = http.get('https://gqfnc7ztrujstj3fyuzjdzjb2u0nqvus.lambda-url.us-east-2.on.aws');
```
- **Refactored:**
```js
let response = http.get(
    'https://gqfnc7ztrujstj3fyuzjdzjb2u0nqvus.lambda-url.us-east-2.on.aws',
    { tags: { name: 'LambdaRequest' } }
  );
```

---

## `script_172.js`

### `script_172.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
    stages: [
        { duration: '2m', target: 2000 },
        { duration: '1m', target: 0 }
    ]
}
```
- **Refactored:**
```js
export const options = {
    stages: [
        { duration: '2m', target: 2000 },
        { duration: '1m', target: 0 }
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01']
    }
}
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
const urlRes = http.get('https://test-api.k6.io')
```
- **Refactored:**
```js
const urlRes = http.get('https://test-api.k6.io', { tags: { name: 'Homepage' } })
```

### `script_172.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
    stages: [
        { duration: '2m', target: 2000 },
        { duration: '1m', target: 0 }
    ]
}
```
- **Refactored:**
```js
export const options = {
    stages: [
        { duration: '2m', target: 2000 },
        { duration: '1m', target: 0 }
    ],
    thresholds: {
        http_req_failed: ['rate<0.01'],
        'http_req_duration{name:Home}': ['p(95)<500']
    }
}
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
const urlRes = http.get('https://test-api.k6.io')
```
- **Refactored:**
```js
const urlRes = http.get('https://test-api.k6.io', {
    tags: { name: 'Home' }
})
```

### `script_172.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
    stages: [
        { duration: '2m', target: 2000 },
        { duration: '1m', target: 0 }
    ]
}
```
- **Refactored:**
```js
export const options = {
    stages: [
        { duration: '2m', target: 2000 },
        { duration: '1m', target: 0 }
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [12]
- **Snippet:**
```js
const urlRes = http.get('https://test-api.k6.io')
```
- **Refactored:**
```js
const urlRes = http.get('https://test-api.k6.io', {
      tags: { name: 'PublicAPICheck' },
    });
```

---

## `script_173.js`

### `script_173.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
- **Snippet:**
```js
export const options = {
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '60s',
      preAllocatedVUs: 50,
      rate: 1200,
      timeUnit: '60s',
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
      duration: '60s',
      preAllocatedVUs: 50,
      rate: 1200,
      timeUnit: '60s',
    },
  },
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [26]
- **Snippet:**
```js
const res = http.get(`http://backend-ellis-jodus-reyes.us-east-1.elasticbeanstalk.com/purchasesTest/provider/${providerId}?from="${from}"&to="${to}"`, { headers });
```
- **Refactored:**
```js
const res = http.get(`http://backend-ellis-jodus-reyes.us-east-1.elasticbeanstalk.com/purchasesTest/provider/${providerId}?from="${from}"&to="${to}"`, { headers, tags: { name: 'GetProviderPurchases' } });
```

### `script_173.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
- **Snippet:**
```js
export const options = {
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '60s',
      preAllocatedVUs: 50,
      rate: 1200,
      timeUnit: '60s',
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
      duration: '60s',
      preAllocatedVUs: 50,
      rate: 1200,
      timeUnit: '60s',
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

- **Lines:** [26]
- **Snippet:**
```js
const res = http.get(`http://backend-ellis-jodus-reyes.us-east-1.elasticbeanstalk.com/purchasesTest/provider/${providerId}?from="${from}"&to="${to}"`, { headers });
```
- **Refactored:**
```js
const res = http.get(
  `http://backend-ellis-jodus-reyes.us-east-1.elasticbeanstalk.com/purchasesTest/provider/${providerId}?from="${from}"&to="${to}"`,
  {
    headers,
    tags: {
      name: 'ProviderPurchases',
      endpoint: 'provider_purchases',
    },
  }
);
```

### `script_173.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
- **Snippet:**
```js
export const options = {
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '60s', // total duration
      preAllocatedVUs: 50, // to allocate runtime resources

      rate: 1200, // number of constant iterations given `timeUnit`
      timeUnit: '60s',
    },
  },
};
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '60s', // total duration
      preAllocatedVUs: 50, // to allocate runtime resources

      rate: 1200, // number of constant iterations given `timeUnit`
      timeUnit: '60s',
    },
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [26]
- **Snippet:**
```js
const res = http.get(`http://backend-ellis-jodus-reyes.us-east-1.elasticbeanstalk.com/purchasesTest/provider/${providerId}?from="${from}"&to="${to}"`, { headers });
```
- **Refactored:**
```js
const res = http.get(`http://backend-ellis-jodus-reyes.us-east-1.elasticbeanstalk.com/purchasesTest/provider/${providerId}?from="${from}"&to="${to}"`, {
    headers,
    tags: {
      name: 'GetProviderPurchases',
    },
  });
```

---

## `script_174.js`

### `script_174.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
const response = http.get(url);
```
- **Refactored:**
```js
const params = {
  tags: {
    name: 'GetAllEmployees',
    endpoint: 'GetAllEmployees'
  }
};
const response = http.get(url, params);
```

### `script_174.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
const response = http.get(url);
```
- **Refactored:**
```js
const response = http.get(url, { tags: { name: 'GetAllEmployees' } });
```

---

## `script_175.js`

### `script_175.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10]
- **Snippet:**
```js
export const options = {
    stages: [
        { duration: '5m', target: 100 },
        { duration: '30m', target: 100 },
        { duration: '5m', target: 0 }
    ]
}
```
- **Refactored:**
```js
export const options = {
    stages: [
        { duration: '5m', target: 100 },
        { duration: '30m', target: 100 },
        { duration: '5m', target: 0 }
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01']
    }
}
```

**Smell 4: Not using tags**

- **Lines:** [13]
- **Snippet:**
```js
const urlRes = http.get('https://test-api.k6.io')
```
- **Refactored:**
```js
const urlRes = http.get('https://test-api.k6.io', { tags: { name: 'HomePage' } })
```

### `script_175.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10]
- **Snippet:**
```js
export const options = {
    stages: [
        { duration: '5m', target: 100 },
        { duration: '30m', target: 100 },
        { duration: '5m', target: 0 }
    ]
}
```
- **Refactored:**
```js
export const options = {
    stages: [
        { duration: '5m', target: 100 },
        { duration: '30m', target: 100 },
        { duration: '5m', target: 0 }
    ],
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99']
    }
}
```

**Smell 4: Not using tags**

- **Lines:** [13]
- **Snippet:**
```js
const urlRes = http.get('https://test-api.k6.io')
```
- **Refactored:**
```js
const urlRes = http.get('https://test-api.k6.io', {
    tags: { name: 'Home', endpoint: 'root' }
})
```

### `script_175.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10]
- **Snippet:**
```js
export const options = {
    stages: [
        { duration: '5m', target: 100 },
        { duration: '30m', target: 100 },
        { duration: '5m', target: 0 }
    ]
}
```
- **Refactored:**
```js
export const options = {
    stages: [
        { duration: '5m', target: 100 },
        { duration: '30m', target: 100 },
        { duration: '5m', target: 0 }
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
    }
}
```

**Smell 4: Not using tags**

- **Lines:** [13]
- **Snippet:**
```js
const urlRes = http.get('https://test-api.k6.io')
```
- **Refactored:**
```js
const urlRes = http.get('https://test-api.k6.io', { tags: { name: 'Public-CrocAPI' } });
```

---

## `script_177.js`

### `script_177.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
const response = http.get(url);
```
- **Refactored:**
```js
const response = http.get(url, { tags: { name: 'GetAllEmployees' } });
```

### `script_177.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
const response = http.get(url);
```
- **Refactored:**
```js
const response = http.get(url, {
  tags: {
    name: 'GetAllEmployees',
    endpoint: 'GetAllEmployees'
  }
});
```

### `script_177.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
const response = http.get(url);
```
- **Refactored:**
```js
const response = http.get(url, { tags: { name: 'GetAllEmployees' } });
```

---

## `script_178.js`

### `script_178.js` — CLAUDE

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
        'checks': ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [22, 23, 24]
- **Snippet:**
```js
const resCo = httppost("G-3300", {
        operation: "test",
    })
```
- **Refactored:**
```js
const httppost = (task, body) => http.post(
    `${hostprefix}/SYNC-${task}`,
    JSON.stringify(body),
    {
        headers: { 'Content-Type': 'application/json' },
        tags: { name: `SYNC-${task}` }
    }
)

// Then thresholds can be scoped:
// 'http_req_duration{name:SYNC-G-3300}': ['p(95)<500']
```

### `script_178.js` — CHATGPT

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [19, 22]
- **Snippet:**
```js
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {headers: { 'Content-Type': 'application/json' }})

const resCo = httppost("G-3300", {
    operation: "test",
})
```
- **Refactored:**
```js
const httppost = (task, body) => http.post(
    `${hostprefix}/SYNC-${task}`,
    JSON.stringify(body),
    {
        headers: { 'Content-Type': 'application/json' },
        tags: { name: `SYNC-${task}`, endpoint: `/SYNC-${task}` },
    }
);

export default function () {
    const resCo = httppost("G-3300", {
        operation: "test",
    });
    check(resCo, { 'A status was 200': (r) => r.status == 200 }, { endpoint: '/SYNC-G-3300' });
}
```

### `script_178.js` — GEMINI

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
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [19, 22]
- **Snippet:**
```js
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {headers: { 'Content-Type': 'application/json' }})

// ...

const resCo = httppost("G-3300", {
```
- **Refactored:**
```js
const httppost = (task, body) => http.post(
    `${hostprefix}/SYNC-${task}`,
    JSON.stringify(body),
    {
        headers: { 'Content-Type': 'application/json' },
        tags: { name: `SYNC-${task}` }, // Tag request by task name
    }
);

// ...

const resCo = httppost("G-3300", {
```

---

## `script_180.js`

### `script_180.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
import { test_options, path } from './options.js';

export let options = {
  ...test_options, // assuming test_options contains VUs, duration, etc.
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    'checks': ['rate>0.99']            // 99% of checks must pass
  }
};
```

---

## `script_183.js`

### `script_183.js` — GEMINI

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
import { check } from 'k6';

// ... inside the 'Checkout' group
const response = checkoutResource.checkout();
check(response, {
  'Checkout successful (status 2xx)': (r) => r.status >= 200 && r.status < 300,
});
const responseJson = response.json(); // Use .json() for safe parsing
orderReference = responseJson?.data?.attributes?.orderReference;
```

**Smell 4: Not using tags**

- **Lines:** [82]
- **Snippet:**
```js
metrics['SAPI16_post_cart_reorder'].add(response.timings.duration);
```
- **Refactored:**
```js
metrics['SAPI16_post_cart_reorder'].add(response.timings.duration, { name: 'AmendOrder' });
```

---

## `script_186.js`

### `script_186.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [30]
- **Snippet:**
```js
const res = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
import { check } from 'k6';

// inside default function:
const res = http.get('https://test-api.k6.io/public/crocodiles/1/');
check(res, {
  'status is 200': (r) => r.status === 200,
  'body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [30]
- **Snippet:**
```js
const res = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
const res = http.get('https://test-api.k6.io/public/crocodiles/1/', {
  tags: { name: 'GetCrocodile' },
});
```

### `script_186.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [30]
- **Snippet:**
```js
const res = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
import { sleep, check } from 'k6';

export default function () {
  const res = http.get('https://test-api.k6.io/public/crocodiles/1/');

  check(res, {
    'status is 200': (r) => r.status === 200,
    'body is not empty': (r) => r.body && r.body.length > 0,
  });

  const randomNum = generateRandom(min, max);
  GaugeContentSize.add(res.body.length + randomNum);
  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [30, 33]
- **Snippet:**
```js
const res = http.get('https://test-api.k6.io/public/crocodiles/1/');
GaugeContentSize.add(res.body.length+randomNum);
```
- **Refactored:**
```js
export const options = {
  vus: 1,
  duration: '1m',
  thresholds: {
    'ContentSize{endpoint:CrocodileDetail}': ['value<4000'],
    'http_req_duration{name:CrocodileDetail}': ['p(95)<500'],
  },
};

export default function () {
  const tags = { name: 'CrocodileDetail', endpoint: 'CrocodileDetail' };
  const res = http.get('https://test-api.k6.io/public/crocodiles/1/', { tags });

  const randomNum = generateRandom(min, max);
  GaugeContentSize.add(res.body.length + randomNum, tags);
  sleep(1);
}
```

### `script_186.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [30]
- **Snippet:**
```js
const res = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const res = http.get('https://test-api.k6.io/public/crocodiles/1/');
check(res, { 'status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [30]
- **Snippet:**
```js
const res = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
const res = http.get('https://test-api.k6.io/public/crocodiles/1/', {
  tags: { name: 'GetPublicCrocodile' },
});
```

---

## `script_188.js`

### `script_188.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [22]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  vus: 10,
  duration: '30s',
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};

export default function () {
```

**Smell 3: Not checking requests**

- **Lines:** [46]
- **Snippet:**
```js
http.post(`${BASE_URL}/api/customer/fake`, payload, params);
```
- **Refactored:**
```js
import { check } from 'k6';

// inside default function:
const res = http.post(`${BASE_URL}/api/customer/fake`, payload, params);
check(res, {
  'status is 200 or 201': (r) => r.status === 200 || r.status === 201,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [46]
- **Snippet:**
```js
http.post(`${BASE_URL}/api/customer/fake`, payload, params);
```
- **Refactored:**
```js
var params = {
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
  tags: { name: 'CreateFakeCustomer' },
};

const res = http.post(`${BASE_URL}/api/customer/fake`, payload, params);
// Then in thresholds you can filter by tag:
// 'http_req_duration{name:CreateFakeCustomer}': ['p(95)<500']
```

### `script_188.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [18, 19, 20]
- **Snippet:**
```js
const customerFake = new SharedArray('customerFakeData', function () {
    return JSON.parse(open('./data-customer-fake.json'));
});
```
- **Refactored:**
```js
// Prefer using a reduced/preprocessed fixture file and keep SharedArray to avoid per-VU copies.
const customerFake = new SharedArray('customerFakeData', function () {
    const data = open('./data-customer-fake-small.json');
    return JSON.parse(data);
});
```

**Smell 2: Do not use thresholds**

- **Lines:** [22]
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
        'http_req_duration{name:CreateFakeCustomer}': ['p(95)<500'],
        'http_req_failed{name:CreateFakeCustomer}': ['rate<0.01'],
        'checks{name:CreateFakeCustomer}': ['rate>0.99']
    }
};
```

**Smell 3: Not checking requests**

- **Lines:** [46]
- **Snippet:**
```js
http.post(`${BASE_URL}/api/customer/fake`, payload, params);
```
- **Refactored:**
```js
import { check, sleep } from 'k6';

const res = http.post(`${BASE_URL}/api/customer/fake`, payload, params);
check(res, {
    'CreateFakeCustomer status is 200 or 201': (r) => r.status === 200 || r.status === 201,
    'CreateFakeCustomer response is not empty': (r) => r.body && r.body.length > 0
}, { name: 'CreateFakeCustomer' });
```

**Smell 4: Not using tags**

- **Lines:** [39, 40, 41, 42, 43, 44, 46]
- **Snippet:**
```js
var params = {
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    },
};

http.post(`${BASE_URL}/api/customer/fake`, payload, params);
```
- **Refactored:**
```js
var params = {
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    },
    tags: {
        name: 'CreateFakeCustomer',
        endpoint: '/api/customer/fake',
        flow: 'customer-registration'
    }
};

const res = http.post(`${BASE_URL}/api/customer/fake`, payload, params);
```

### `script_188.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [21]
- **Snippet:**
```js
// The script is missing the 'options' export with a 'thresholds' object.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [46]
- **Snippet:**
```js
http.post(`${BASE_URL}/api/customer/fake`, payload, params);
```
- **Refactored:**
```js
import { check } from 'k6';

//... inside default function
const res = http.post(`${BASE_URL}/api/customer/fake`, payload, params);
check(res, {
    'is status 201': (r) => r.status === 201,
});
```

**Smell 4: Not using tags**

- **Lines:** [46]
- **Snippet:**
```js
http.post(`${BASE_URL}/api/customer/fake`, payload, params);
```
- **Refactored:**
```js
var params = {
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    },
    tags: {
        name: 'CreateFakeCustomer',
    },
};

http.post(`${BASE_URL}/api/customer/fake`, payload, params);
```

---

## `script_190.js`

### `script_190.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '5s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '5s',
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01']
    }
}
```

**Smell 3: Not checking requests**

- **Lines:** [11, 12, 13, 14, 15]
- **Snippet:**
```js
export default function (data) {
    console.log('-- VU stage --');
    // console.log(data);
    sleep(1);
}
```
- **Refactored:**
```js
import { check } from 'k6';

export default function (data) {
    console.log('-- VU stage --');
    const res = http.get('https://your-endpoint.com');
    check(res, {
        'status is 200': (r) => r.status === 200
    });
    sleep(1);
}
```

### `script_190.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '5s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '5s',
    thresholds: {
        iteration_duration: ['p(95)<1500']
    }
};
```

### `script_190.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '5s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '5s',
    thresholds: {
      // e.g., fail if 95% of iterations take more than 1.5 seconds
      'iteration_duration': ['p(95)<1500'],
    },
}
```

---

## `script_192.js`

### `script_192.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 250,
  iterations: 250,
};
```
- **Refactored:**
```js
export const options = {
  vus: 250,
  iterations: 250,
  thresholds: {
    'http_req_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
    'response_time': ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [31, 32, 33, 34, 35]
- **Snippet:**
```js
const res = http.post(
    'https://petstore.swagger.io/v2/user',
    payload,
    { headers }
  );
```
- **Refactored:**
```js
const res = http.post(
    'https://petstore.swagger.io/v2/user',
    payload,
    { headers, tags: { name: 'CreateUser' } }
  );
```

### `script_192.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 250, // Jumlah VUs
  iterations: 250,
};
```
- **Refactored:**
```js
export const options = {
  vus: 250,
  iterations: 250,
  thresholds: {
    http_req_failed: ['rate<0.01'],
    'http_req_duration{name:CreateUser}': ['p(95)<500'],
    checks: ['rate>0.95'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [31, 32, 33, 34, 35]
- **Snippet:**
```js
const res = http.post(
  'https://petstore.swagger.io/v2/user',
  payload,
  { headers }
);
```
- **Refactored:**
```js
const params = {
  headers,
  tags: {
    name: 'CreateUser',
    endpoint: '/v2/user',
    method: 'POST',
  },
};

const res = http.post(
  'https://petstore.swagger.io/v2/user',
  payload,
  params
);

responseTime.add(res.timings.duration, {
  name: 'CreateUser',
  endpoint: '/v2/user',
});

check(res, {
  'Status is 200': (r) => r.status === 200,
  'Response time < 500ms': (r) => r.timings.duration < 500,
}, {
  name: 'CreateUser',
  endpoint: '/v2/user',
});
```

### `script_192.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 250, // Jumlah VUs
  iterations: 250,
};
```
- **Refactored:**
```js
export const options = {
  vus: 250,
  iterations: 250,
  thresholds: {
    'http_req_failed': ['rate<0.01'],        // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'],      // 95% of requests should be below 500ms
    'response_time': ['p(95)<500'],          // 95% of our custom metric should be below 500ms
    'checks': ['rate>0.99']                  // 99% of checks must pass
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [31, 32, 33, 34, 35]
- **Snippet:**
```js
const res = http.post(
  'https://petstore.swagger.io/v2/user',
  payload,
  { headers }
);
```
- **Refactored:**
```js
const res = http.post(
  'https://petstore.swagger.io/v2/user',
  payload,
  {
    headers,
    tags: { name: 'CreateUser' }, // Tag to identify this specific request
  }
);
```

---

## `script_194.js`

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
  },
}
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
    // The rate of inserts should be at least 95% of the target rate.
    'inserts': [`rate > ${rate * 0.95}`],
  },
}
```

**Smell 3: Not checking requests**

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
try {
    db.exec(
      `insert into load_messages(room_id) values('room${getRandomInt(
        0,
        rooms
      )}');`
    );
    counterInserts.add(1); // Only increment counter on success
  } catch (e) {
    // Log the error but continue execution
    console.error(`DB insert failed: ${e}`);
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
const roomID = `room${getRandomInt(0, rooms)}`;
  db.exec(
    `insert into load_messages(room_id) values('${roomID}');`
  )
  // Tag the metric with the specific room ID for better analysis
  counterInserts.add(1, { room: roomID });
```

---

## `script_195.js`

### `script_195.js` — CLAUDE

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
        http_req_duration: ['p(95)<500', 'p(99)<1000'],
        http_req_failed: ['rate<0.01'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/flow-service/api/v1/flows?vertical=k12&segment=101&modality=after_purchase&product=10091`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/flow-service/api/v1/flows?vertical=k12&segment=101&modality=after_purchase&product=10091`, {
    headers: headers,
    tags: { name: 'GetFlows' },
});
```

### `script_195.js` — CHATGPT

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
export const options = {
    vus: 2000,
    duration: '10s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        'http_req_duration{name:Flows}': ['p(95)<500'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/flow-service/api/v1/flows?vertical=k12&segment=101&modality=after_purchase&product=10091`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/flow-service/api/v1/flows?vertical=k12&segment=101&modality=after_purchase&product=10091`, {
    headers: headers,
    tags: { name: 'Flows', endpoint: 'flow-service-flows' },
});
```

### `script_195.js` — GEMINI

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
        'http_req_duration': ['p(95)<1500'], // 95% of requests must complete below 1.5s
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/flow-service/api/v1/flows?vertical=k12&segment=101&modality=after_purchase&product=10091`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/flow-service/api/v1/flows?vertical=k12&segment=101&modality=after_purchase&product=10091`, {
    headers: headers,
    tags: {
        name: 'GetFlows',
    }
});
```

---

## `script_196.js`

### `script_196.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export const options = {
    vus: 1,
    iterations: 20,
};
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    iterations: 20,
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [29]
- **Snippet:**
```js
const res = http.post('http://localhost:5000/api/cadastro', body, { headers: headers });
```
- **Refactored:**
```js
const res = http.post('http://localhost:5000/api/cadastro', body, { headers: headers, tags: { name: 'Cadastro' } });
```

### `script_196.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export const options = {
    vus: 1, // Apenas um usuário virtual
    iterations: 20, // Número total de iterações
};
```
- **Refactored:**
```js
export const options = {
    vus: 1, // Apenas um usuário virtual
    iterations: 20, // Número total de iterações
    thresholds: {
        'http_req_failed': ['rate<0.01'], // less than 1% of requests should fail
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [29]
- **Snippet:**
```js
const res = http.post('http://localhost:5000/api/cadastro', body, { headers: headers });
```
- **Refactored:**
```js
const params = {
    headers: headers,
    tags: {
        name: 'CadastroUsuario',
    },
};
const res = http.post('http://localhost:5000/api/cadastro', body, params);
```

---

## `script_197.js`

### `script_197.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 20000,
    duration: '10s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 20000,
    duration: '10s',
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
        'checks': ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/discovery-service/api/v1/products/ghore-boshe-spoken-english/free-products?lang=bn`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/discovery-service/api/v1/products/ghore-boshe-spoken-english/free-products?lang=bn`, {
    headers: headers,
    tags: { name: 'FreeProducts' },
});
```

### `script_197.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 20000,
    duration: '10s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 20000,
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
let res = http.get(`${baseUrl}/discovery-service/api/v1/products/ghore-boshe-spoken-english/free-products?lang=bn`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/discovery-service/api/v1/products/ghore-boshe-spoken-english/free-products?lang=bn`, {
    headers: headers,
    tags: {
        name: 'FreeProducts',
        endpoint: 'free-products',
        flow: 'discovery-service'
    }
});
```

### `script_197.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 20000,
    duration: '10s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 20000,
    duration: '10s',
    thresholds: {
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/discovery-service/api/v1/products/ghore-boshe-spoken-english/free-products?lang=bn`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/discovery-service/api/v1/products/ghore-boshe-spoken-english/free-products?lang=bn`, {
    headers: headers,
    tags: {
        name: 'GetFreeProducts',
    },
});
```

---

## `script_198.js`

### `script_198.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [12, 13, 14, 15, 16]
- **Snippet:**
```js
export let options = {
	iterations: 5,
	vus: 1,
    duration: '6s',
};
```
- **Refactored:**
```js
export let options = {
	iterations: 5,
	vus: 1,
    duration: '6s',
    thresholds: {
        'http_req_duration': ['p(95)<200'],
        'checks': ['rate>0.95'],
        'http_req_failed': ['rate<0.05'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [35, 36, 37]
- **Snippet:**
```js
let getProduct = http.get(`${baseUrl}/${i}`, {
    headers: headers
});
```
- **Refactored:**
```js
let getProduct = http.get(`${baseUrl}/${i}`, {
    headers: headers,
    tags: { name: 'GetProduct' }
});
```

### `script_198.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [12, 13, 14, 15, 16]
- **Snippet:**
```js
export let options = {
	iterations: 5,
	vus: 1,
    duration: '6s',
};
```
- **Refactored:**
```js
export let options = {
  iterations: 5,
  vus: 1,
  duration: '6s',
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<200'],
    'checks': ['rate>0.99']
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [35, 36, 37]
- **Snippet:**
```js
let getProduct = http.get(`${baseUrl}/${i}`, {
    headers: headers
});
```
- **Refactored:**
```js
let getProduct = http.get(`${baseUrl}/${i}`, {
  headers: headers,
  tags: {
    name: 'GetProductById',
    endpoint: 'products/:id'
  }
});

check(getProduct, {
  'status is 200': (r) => r.status === 200,
  'response time < 200ms': (r) => r.timings.duration < 200
}, {
  endpoint: 'products/:id'
});
```

### `script_198.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [12, 13, 14, 15, 16]
- **Snippet:**
```js
export let options = {
	iterations: 5,
	vus: 1,
    duration: '6s',
};
```
- **Refactored:**
```js
export let options = {
	iterations: 5,
	vus: 1,
    duration: '6s',
    thresholds: {
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<200'],
        'checks': ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [35, 36, 37]
- **Snippet:**
```js
let getProduct = http.get(`${baseUrl}/${i}`, {
    headers: headers
});
```
- **Refactored:**
```js
let getProduct = http.get(`${baseUrl}/${i}`, {
    headers: headers,
    tags: {
        name: 'GetProductByID',
    },
});
```

---

## `script_201.js`

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
  ...test_options, // Merges imported options (like VUs, duration)
  thresholds: {    // Defines explicit success criteria for the test
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    'checks': ['rate>0.99'],            // over 99% of checks must pass
  },
};
```

---

## `script_203.js`

### `script_203.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [25, 26, 27]
- **Snippet:**
```js
const res = http.post(url, JSON.stringify(store), {
    headers: { 'Content-Type': 'application/json' },
});
```
- **Refactored:**
```js
const res = http.post(url, JSON.stringify(store), {
    headers: { 'Content-Type': 'application/json' },
    tags: {
        name: 'CreateMongoEmbeddedSchema',
        endpoint: 'mongo-embedded-schema',
        operation: 'insert'
    },
});
```

### `script_203.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [29, 30, 31]
- **Snippet:**
```js
check(res, {
    'insert failed': (r) => r.status === 500
});
```
- **Refactored:**
```js
check(res, {
    'status is 201 (Created)': (r) => r.status === 201
});
```

**Smell 4: Not using tags**

- **Lines:** [25, 26, 27]
- **Snippet:**
```js
const res = http.post(url, JSON.stringify(store), {
    headers: { 'Content-Type': 'application/json' },
});
```
- **Refactored:**
```js
const res = http.post(url, JSON.stringify(store), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'CreateStore' },
});
```

---

## `script_204.js`

### `script_204.js` — CLAUDE

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
        'http_req_duration': ['p(95)<500'],
        'http_req_failed': ['rate<0.01'],
        'checks': ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/discovery-service/api/v1/products/ssc-23-smp-sci/variants`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/discovery-service/api/v1/products/ssc-23-smp-sci/variants`, {
    headers: headers,
    tags: { name: 'GetProductVariants' },
});
```

### `script_204.js` — CHATGPT

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
        'http_req_duration{name:ProductVariants}': ['p(95)<500'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/discovery-service/api/v1/products/ssc-23-smp-sci/variants`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/discovery-service/api/v1/products/ssc-23-smp-sci/variants`, {
    headers: headers,
    tags: {
        name: 'ProductVariants',
        endpoint: '/discovery-service/api/v1/products/:slug/variants',
    },
});
```

### `script_204.js` — GEMINI

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
        'http_req_duration': ['p(95)<1500'], // 95% of requests must complete below 1.5s
        'checks': ['rate>0.99'],           // 99% of checks must pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/discovery-service/api/v1/products/ssc-23-smp-sci/variants`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/discovery-service/api/v1/products/ssc-23-smp-sci/variants`, {
    headers: headers,
    tags: {
        name: 'GetProductVariants',
    },
});
```

---

## `script_205.js`

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
    'iteration_duration': ['p(95)<2000'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [59, 60, 61, 62, 63]
- **Snippet:**
```js
db.exec(
  `insert into rls_messages (domain) values ('${domains[getRandomInt(0, 5)]}');`
)
```
- **Refactored:**
```js
import { check } from 'k6';

// inside default function:
let result;
try {
  result = db.exec(
    `insert into rls_messages (domain) values ('${domains[getRandomInt(0, 5)]}');`
  );
  check(result, {
    'insert succeeded': (r) => r !== null && r !== undefined,
  });
} catch (e) {
  check(null, { 'insert succeeded': () => false });
}
```

**Smell 4: Not using tags**

- **Lines:** [59, 60, 61, 62, 63]
- **Snippet:**
```js
db.exec(
  `insert into rls_messages (domain) values ('${domains[getRandomInt(0, 5)]}');`
)
```
- **Refactored:**
```js
import { tagWithCurrentStageIndex } from 'k6/execution';

// Use tags to annotate the database operation metrics:
counterInserts.add(1, { operation: 'insert', table: 'rls_messages' });

// Or, if using a custom metric with tags:
const insertDuration = new Trend('insert_duration');
const start = new Date();
db.exec(
  `insert into rls_messages (domain) values ('${domains[getRandomInt(0, 5)]}');`
);
const finish = new Date();
insertDuration.add(finish - start, { operation: 'insert', table: 'rls_messages' });
counterInserts.add(1, { operation: 'insert', table: 'rls_messages' });
```

### `script_205.js` — GEMINI

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
    'sql_req_duration': ['p(95)<500'], // 95% of queries should be below 500ms
    'inserts': ['count>0'], // Ensure at least some inserts were attempted
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
// At top of file: import { check } from 'k6';

const domain = domains[getRandomInt(0, 5)];
const res = db.exec(
  `insert into rls_messages (domain) values ('${domain}');`
);

check(res, {
  'insert successful (1 row affected)': (r) => r.rowsAffected === 1,
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
// The 'domain' variable must be captured from the query before this call
const domain = domains[getRandomInt(0, 5)];
db.exec(`insert into rls_messages (domain) values ('${domain}');`);
// ...
counterInserts.add(1, { domain: domain });
```

---

## `script_206.js`

### `script_206.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
    vus: 30,
    duration: '30s',
};
```
- **Refactored:**
```js
export const options = {
    vus: 30,
    duration: '30s',
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21]
- **Snippet:**
```js
const res = http.get(url, params);
```
- **Refactored:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json',
        'X-Queue-Token': 'eyJjb25jZXJ0SWQiOjEsInRva2VuVXVpZCI6IjJjZDg5ZGY3LWI4MzMtNDgwMS1iNDFhLTZjN2Q4NmU1ZjI0YyJ9'
    },
    tags: { name: 'GetConcertSeats' },
};
const res = http.get(url, params);
```

### `script_206.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
    vus: 30,
    duration: '30s',
};
```
- **Refactored:**
```js
export const options = {
    vus: 30,
    duration: '30s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        'http_req_duration{name:ConcertSeats}': ['p(95)<500'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [14, 15, 16, 17, 18, 19, 21]
- **Snippet:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json',
        'X-Queue-Token': '...'
    }
};

const res = http.get(url, params);
```
- **Refactored:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json',
        'X-Queue-Token': 'eyJjb25jZXJ0SWQiOjEsInRva2VuVXVpZCI6IjJjZDg5ZGY3LWI4MzMtNDgwMS1iNDFhLTZjN2Q4NmU1ZjI0YyJ9'
    },
    tags: {
        name: 'ConcertSeats',
        endpoint: 'concert-seats',
        flow: 'seat-availability'
    }
};

const res = http.get(url, params);

const success = check(res, {
    'status is 200': (r) => r.status === 200,
}, { name: 'ConcertSeats' });
```

### `script_206.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [6, 7, 8, 9]
- **Snippet:**
```js
export const options = {
    vus: 30, // 동시에 실행할 가상 사용자 수
    duration: '30s', // 테스트 지속 시간
};
```
- **Refactored:**
```js
export const options = {
    vus: 30, // 동시에 실행할 가상 사용자 수
    duration: '30s', // 테스트 지속 시간
    thresholds: {
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21]
- **Snippet:**
```js
const res = http.get(url, params);
```
- **Refactored:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json',
        'X-Queue-Token': 'eyJjb25jZXJ0SWQiOjEsInRva2VuVXVpZCI6IjJjZDg5ZGY3LWI4MzMtNDgwMS1iNDFhLTZjN2Q4NmU1ZjI0YyJ9'
    },
    tags: {
        name: 'GetConcertSeats',
    },
};

const res = http.get(url, params);
```

---

## `script_207.js`

### `script_207.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
const response = http.get(url);
```
- **Refactored:**
```js
const response = http.get(url, { tags: { name: 'GetAllEmployees' } });
```

### `script_207.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
const response = http.get(url);
```
- **Refactored:**
```js
const response = http.get(url, {
  tags: {
    name: 'GetAllEmployees',
    endpoint: 'GetAllEmployees'
  }
});
```

### `script_207.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
const response = http.get(url);
```
- **Refactored:**
```js
const response = http.get(url, { tags: { name: 'GetAllEmployees' } });
```

---

## `script_208.js`

### `script_208.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [12, 13, 14, 15, 16, 17, 18]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '30s', target: 100 },
        { duration: '1m30s', target: 100 },
        { duration: '20s', target: 140 }
    ]
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '30s', target: 100 },
        { duration: '1m30s', target: 100 },
        { duration: '20s', target: 140 }
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
        'checks': ['rate>0.99'],
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [24]
- **Snippet:**
```js
const response = postStoreOrder.execute();
```
- **Refactored:**
```js
const response = postStoreOrder.execute({ tags: { name: 'PostStoreOrder' } });
check(response, {
    'Create store order Status is 200': (r) => r.status === 200,
});
```

### `script_208.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [12, 13, 14, 15, 16, 17, 18]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '30s', target: 100 },
        { duration: '1m30s', target: 100 },
        { duration: '20s', target: 140 }
    ]
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '30s', target: 100 },
        { duration: '1m30s', target: 100 },
        { duration: '20s', target: 140 }
    ],
    thresholds: {
        'http_req_duration{name:CreateStoreOrder}': ['p(95)<500'],
        'http_req_failed{name:CreateStoreOrder}': ['rate<0.01'],
        'checks{name:CreateStoreOrder}': ['rate>0.99']
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [24, 25, 26, 27]
- **Snippet:**
```js
const response = postStoreOrder.execute();
check(response, {
    'Create store order Status is 200': (r) => r.status === 200,
});
```
- **Refactored:**
```js
const tags = { name: 'CreateStoreOrder', endpoint: '/store/order' };
const response = postStoreOrder.execute({ tags });
check(response, {
    'Create store order Status is 200': (r) => r.status === 200,
}, tags);
```

### `script_208.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [12, 13, 14, 15, 16, 17, 18]
- **Snippet:**
```js
export let options = {
    stages: [
        { duration: '30s', target: 100 },
        { duration: '1m30s', target: 100 },
        { duration: '20s', target: 140 }
    ]
};
```
- **Refactored:**
```js
export let options = {
    stages: [
        { duration: '30s', target: 100 },
        { duration: '1m30s', target: 100 },
        { duration: '20s', target: 140 }
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [24]
- **Snippet:**
```js
const response = postStoreOrder.execute();
```
- **Refactored:**
```js
const response = postStoreOrder.execute({ name: 'CreateOrder' });
```

---

## `script_209.js`

### `script_209.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '10s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '10s',
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01']
    }
}
```

### `script_209.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '10s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '10s',
    thresholds: {
        iteration_duration: ['p(95)<1000']
    }
};
```

### `script_209.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export const options = {
    vus: 1,
    duration: '10s'
}
```
- **Refactored:**
```js
export const options = {
    vus: 1,
    duration: '10s',
    thresholds: {
        // Example: 95% of iterations must complete within 1.1 seconds
        'iteration_duration': ['p(95)<1100'],
    }
}
```

---

## `script_212.js`

### `script_212.js` — CLAUDE

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
const response = http.post(`${apiUrl}/v-fail/users`, JSON.stringify(request), {
        headers: { "Content-Type": "application/json" }
    });
```
- **Refactored:**
```js
const response = http.post(`${apiUrl}/v-fail/users`, JSON.stringify(request), {
        headers: { "Content-Type": "application/json" },
        tags: { name: 'CreateUser' }
    });
```

### `script_212.js` — CHATGPT

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
        'http_req_duration{name:CreateInvalidUser}': ['p(95)<500'],
        'http_req_failed{name:CreateInvalidUser}': ['rate<0.01'],
        'checks{name:CreateInvalidUser}': ['rate>0.99']
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [20, 21, 22]
- **Snippet:**
```js
const response = http.post(`${apiUrl}/v-fail/users`, JSON.stringify(request), {
    headers: { "Content-Type": "application/json" }
});
```
- **Refactored:**
```js
const response = http.post(`${apiUrl}/v-fail/users`, JSON.stringify(request), {
    headers: { "Content-Type": "application/json" },
    tags: { name: 'CreateInvalidUser', endpoint: '/v-fail/users', flow: 'user-validation' }
});

check(response, {
    "response code was 400 or 409": (res) => res.status === 400 || res.status === 409
}, { name: 'CreateInvalidUser', endpoint: '/v-fail/users', flow: 'user-validation' });
```

### `script_212.js` — GEMINI

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
        'http_req_duration': ['p(95)<200'], // 95% of requests should be below 200ms
        'checks': ['rate>0.99'] // 99% of checks must pass
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [20, 21, 22]
- **Snippet:**
```js
const response = http.post(`${apiUrl}/v-fail/users`, JSON.stringify(request), {
    headers: { "Content-Type": "application/json" }
});
```
- **Refactored:**
```js
const response = http.post(`${apiUrl}/v-fail/users`, JSON.stringify(request), {
    headers: { "Content-Type": "application/json" },
    tags: { name: 'CreateUser-Fail' }
});
```

---

## `script_213.js`

### `script_213.js` — GEMINI

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
  ...test_options, // assuming test_options contains VUs, duration, etc.
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration{name:GET /mongo-embedded/stores/withOfferCount}': ['p(95)<500'], // 95% of requests for this endpoint must be below 500ms
    'checks': ['rate>0.99'], // Over 99% of checks must pass
  },
};
```

---

## `script_214.js`

### `script_214.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [26, 28]
- **Snippet:**
```js
const resp = http.get('https://test-api.k6.io/public/crocodiles/1/');
  errorRate.add(resp.status >= 400);
```
- **Refactored:**
```js
import { check } from 'k6';

export default function () {
  const resp = http.get('https://test-api.k6.io/public/crocodiles/1/');

  const success = check(resp, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
  });

  errorRate.add(!success);

  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [26]
- **Snippet:**
```js
const resp = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
const resp = http.get('https://test-api.k6.io/public/crocodiles/1/', {
  tags: { name: 'GetCrocodile' },
});
```

### `script_214.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [26, 28]
- **Snippet:**
```js
const resp = http.get('https://test-api.k6.io/public/crocodiles/1/');

errorRate.add(resp.status >= 400);
```
- **Refactored:**
```js
import { check, sleep } from 'k6';

export default function () {
  const resp = http.get('https://test-api.k6.io/public/crocodiles/1/', {
    tags: { name: 'GetCrocodileById' },
  });

  const ok = check(resp, {
    'GET crocodile by id returns 200': (r) => r.status === 200,
  });

  errorRate.add(!ok);

  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [26]
- **Snippet:**
```js
const resp = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
const resp = http.get('https://test-api.k6.io/public/crocodiles/1/', {
  tags: { name: 'GetCrocodileById', endpoint: 'crocodiles/:id' },
});
```

### `script_214.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [26, 28]
- **Snippet:**
```js
const resp = http.get('https://test-api.k6.io/public/crocodiles/1/');

errorRate.add(resp.status >= 400);
```
- **Refactored:**
```js
import { check } from 'k6';
// ... inside the default function:
const resp = http.get('https://test-api.k6.io/public/crocodiles/1/');
const success = check(resp, {
  'status is 2xx': (r) => r.status >= 200 && r.status < 300,
});
errorRate.add(!success);
```

**Smell 4: Not using tags**

- **Lines:** [26]
- **Snippet:**
```js
const resp = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
const resp = http.get('https://test-api.k6.io/public/crocodiles/1/', {
  tags: { name: 'GetCrocodile' },
});
```

---

## `script_215.js`

### `script_215.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11, 12, 13]
- **Snippet:**
```js
export const options = {
  stages: [
    { duration: '2s', target: 20 },
    { duration: '10s', target: 100 },
    { duration: '1m', target: 500 },
    { duration: '2s', target: 20 },
  ],
  summaryTrendStats: ['avg', 'med', 'p(95)', 'p(99)']
}
```
- **Refactored:**
```js
export const options = {
  stages: [
    { duration: '2s', target: 20 },
    { duration: '10s', target: 100 },
    { duration: '1m', target: 500 },
    { duration: '2s', target: 20 },
  ],
  summaryTrendStats: ['avg', 'med', 'p(95)', 'p(99)'],
  thresholds: {
    http_req_duration: ['p(95)<500', 'p(99)<1000'],
    http_req_failed: ['rate<0.01'],
    'checks': ['rate>0.99'],
  },
}
```

**Smell 4: Not using tags**

- **Lines:** [16, 17, 18, 19, 20, 21]
- **Snippet:**
```js
const res = http.post(`${BASE_URL}/api/messages`, JSON.stringify({
    authorId: 'test-user-id',
    content: `
      some content number ${Math.floor(Math.random() * 9000 + 1000)} posted from k6
    `
  }));
```
- **Refactored:**
```js
const res = http.post(`${BASE_URL}/api/messages`, JSON.stringify({
    authorId: 'test-user-id',
    content: `
      some content number ${Math.floor(Math.random() * 9000 + 1000)} posted from k6
    `
  }), { tags: { name: 'CreateMessage' } });
```

### `script_215.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11, 12, 13]
- **Snippet:**
```js
export const options = {
  stages: [
    { duration: '2s', target: 20 },
    { duration: '10s', target: 100 },
    { duration: '1m', target: 500 },
    { duration: '2s', target: 20 },
  ],
  summaryTrendStats: ['avg', 'med', 'p(95)', 'p(99)']
}
```
- **Refactored:**
```js
export const options = {
  stages: [
    { duration: '2s', target: 20 },
    { duration: '10s', target: 100 },
    { duration: '1m', target: 500 },
    { duration: '2s', target: 20 },
  ],
  summaryTrendStats: ['avg', 'med', 'p(95)', 'p(99)'],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    'http_req_duration{name:CreateMessage}': ['p(95)<500', 'p(99)<1000'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [16, 17, 18, 19, 20, 21, 23]
- **Snippet:**
```js
const res = http.post(`${BASE_URL}/api/messages`, JSON.stringify({
  authorId: 'test-user-id',
  content: `
    some content number ${Math.floor(Math.random() * 9000 + 1000)} posted from k6
  `
}));

check(res, { ['Create message Success'] : (r) => r.status === 200 });
```
- **Refactored:**
```js
const params = {
  headers: { 'Content-Type': 'application/json' },
  tags: {
    name: 'CreateMessage',
    endpoint: '/api/messages',
    flow: 'messages',
  },
};

const res = http.post(`${BASE_URL}/api/messages`, JSON.stringify({
  authorId: 'test-user-id',
  content: `
    some content number ${Math.floor(Math.random() * 9000 + 1000)} posted from k6
  `,
}), params);

check(res, { 'Create message Success': (r) => r.status === 200 }, { name: 'CreateMessage' });
```

### `script_215.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11, 12, 13]
- **Snippet:**
```js
export const options = {
  stages: [
    { duration: '2s', target: 20 },
    { duration: '10s', target: 100 },
    { duration: '1m', target: 500 },
    { duration: '2s', target: 20 },
  ],
  summaryTrendStats: ['avg', 'med', 'p(95)', 'p(99)']
}
```
- **Refactored:**
```js
export const options = {
  stages: [
    { duration: '2s', target: 20 },
    { duration: '10s', target: 100 },
    { duration: '1m', target: 500 },
    { duration: '2s', target: 20 },
  ],
  summaryTrendStats: ['avg', 'med', 'p(95)', 'p(99)'],
  thresholds: {
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
}
```

**Smell 4: Not using tags**

- **Lines:** [16, 17, 18, 19, 20, 21]
- **Snippet:**
```js
const res = http.post(`${BASE_URL}/api/messages`, JSON.stringify({
    authorId: 'test-user-id',
    content: `
      some content number ${Math.floor(Math.random() * 9000 + 1000)} posted from k6
    `
  }));
```
- **Refactored:**
```js
const res = http.post(`${BASE_URL}/api/messages`, JSON.stringify({
    authorId: 'test-user-id',
    content: `
      some content number ${Math.floor(Math.random() * 9000 + 1000)} posted from k6
    `
  }), {
    tags: { name: 'CreateMessage' },
  });
```

---

## `script_216.js`

### `script_216.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
    vus: 10, 
    iterations: 10,
};
```
- **Refactored:**
```js
export let options = {
    vus: 10,
    iterations: 10,
    thresholds: {
        'http_req_duration': ['p(95)<500'],
        'checks': ['rate>0.95'],
        'http_req_failed': ['rate<0.05'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [35]
- **Snippet:**
```js
let res = http.post(url, payload, { headers });
```
- **Refactored:**
```js
let res = http.post(url, payload, { headers, tags: { name: 'PostPetById', petId: String(petId) } });
```

### `script_216.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
    vus: 10, 
    iterations: 10,
};
```
- **Refactored:**
```js
export let options = {
    vus: 10,
    iterations: 10,
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.95'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [35]
- **Snippet:**
```js
let res = http.post(url, payload, { headers });
```
- **Refactored:**
```js
let res = http.post(url, payload, {
    headers,
    tags: {
        name: 'PostPetById',
        endpoint: '/v2/pet/{petId}',
        flow: 'pet-update',
    },
});
```

### `script_216.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7]
- **Snippet:**
```js
export let options = {
    vus: 10, 
    iterations: 10, // 10 request dengan variasi yang berbeda
};
```
- **Refactored:**
```js
export let options = {
    vus: 10, 
    iterations: 10, 
    thresholds: {
        'http_req_failed': ['rate<0.01'], // fail the test if less than 1% of requests fail
        'http_req_duration': ['p(95)<500'], // 95% of requests must be below 500ms
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [35]
- **Snippet:**
```js
let res = http.post(url, payload, { headers });
```
- **Refactored:**
```js
let res = http.post(url, payload, { 
        headers: headers, 
        tags: {
            name: 'UpdatePet',
        },
    });
```

---

## `script_217.js`

### `script_217.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [58]
- **Snippet:**
```js
let res = http.get(SEAT_LOOKUP_ENDPOINT, { headers });
```
- **Refactored:**
```js
let res = http.get(SEAT_LOOKUP_ENDPOINT, { headers, tags: { name: 'SeatLookup' } });
```

### `script_217.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [14, 18, 19, 20]
- **Snippet:**
```js
let res = http.post(TOKEN_ISSUE_ENDPOINT, JSON.stringify({ userId: i, concertId: 1 }), {
    headers: { 'Content-Type': 'application/json' },
});

if (res.status === 201) {
    let responseBody = JSON.parse(res.body);
```
- **Refactored:**
```js
let res = http.post(TOKEN_ISSUE_ENDPOINT, JSON.stringify({ userId: i, concertId: 1 }), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'TokenIssue' },
});

const tokenIssueOk = check(res, {
    'token issue status is 201': (r) => r.status === 201,
    'token issue response has token': (r) => {
        try {
            return !!JSON.parse(r.body)?.data?.token;
        } catch (e) {
            return false;
        }
    },
});

if (tokenIssueOk) {
    let responseBody = JSON.parse(res.body);
    let token = responseBody?.data?.token;
    tokens.push(token);
}
```

**Smell 4: Not using tags**

- **Lines:** [14, 58]
- **Snippet:**
```js
let res = http.post(TOKEN_ISSUE_ENDPOINT, JSON.stringify({ userId: i, concertId: 1 }), {
    headers: { 'Content-Type': 'application/json' },
});
...
let res = http.get(SEAT_LOOKUP_ENDPOINT, { headers });
```
- **Refactored:**
```js
let res = http.post(TOKEN_ISSUE_ENDPOINT, JSON.stringify({ userId: i, concertId: 1 }), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'TokenIssue', endpoint: 'queue_token' },
});

...

let res = http.get(SEAT_LOOKUP_ENDPOINT, {
    headers,
    tags: { name: 'SeatLookup', endpoint: 'seat_lookup' },
});

// Optional tagged thresholds:
export let options = {
    scenarios: {
        seat_lookup: {
            executor: 'ramping-arrival-rate',
            startRate: 50,
            timeUnit: '1s',
            preAllocatedVUs: 100,
            maxVUs: 300,
            startTime: '15s',
            stages: [
                { duration: '30s', target: 100 },
                { duration: '1m', target: 150 },
                { duration: '30s', target: 120 },
                { duration: '30s', target: 0 },
            ],
        },
    },
    thresholds: {
        'http_req_duration{name:SeatLookup}': ['p(95)<2000'],
        'http_req_failed{name:SeatLookup}': ['rate<0.01'],
        'http_req_duration{name:TokenIssue}': ['p(95)<2000'],
        'http_req_failed{name:TokenIssue}': ['rate<0.01'],
    },
};
```

### `script_217.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [14, 58]
- **Snippet:**
```js
let res = http.get(SEAT_LOOKUP_ENDPOINT, { headers });
```
- **Refactored:**
```js
/* In setup function */
let res_setup = http.post(TOKEN_ISSUE_ENDPOINT, JSON.stringify({ userId: i, concertId: 1 }), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'TokenIssue' },
});

/* In default function */
let res = http.get(SEAT_LOOKUP_ENDPOINT, {
    headers,
    tags: { name: 'SeatLookup' },
});
```

---

## `script_218.js`

### `script_218.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export const options = {};
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
    'checks': ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [20, 21, 22]
- **Snippet:**
```js
const res = http.post('https://httpbin.test.k6.io/post', payload, {
    headers,
  });
```
- **Refactored:**
```js
const res = http.post('https://httpbin.test.k6.io/post', payload, {
    headers,
    tags: { name: 'PostUser' },
  });
```

### `script_218.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export const options = {};
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [20, 21, 22]
- **Snippet:**
```js
const res = http.post('https://httpbin.test.k6.io/post', payload, {
  headers,
});
```
- **Refactored:**
```js
const tags = { name: 'CreateUser', endpoint: '/post', flow: 'create_user' };

const res = http.post('https://httpbin.test.k6.io/post', payload, {
  headers,
  tags,
});

check(res, {
  'Post status is 200': (r) => r.status === 200,
  'Post Content-Type header': (r) => r.headers['Content-Type'] === 'application/json',
  'Post response name': (r) => r.status === 200 && r.json().json.name === user.username,
}, tags);
```

### `script_218.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export const options = {};
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks': ['rate>0.99'], // 99% of checks should pass
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [20, 21, 22]
- **Snippet:**
```js
const res = http.post('https://httpbin.test.k6.io/post', payload, {
    headers,
  });
```
- **Refactored:**
```js
const res = http.post('https://httpbin.test.k6.io/post', payload, {
    headers,
    tags: {
      name: 'CreateUser',
    },
  });
```

---

## `script_219.js`

### `script_219.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 2000,
    duration: '20s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 2000,
    duration: '20s',
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/k12-course-service/api/v1/programs?type=admission`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/k12-course-service/api/v1/programs?type=admission`, {
    headers: headers,
    tags: { name: 'GetPrograms' },
});
```

### `script_219.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 2000,
    duration: '20s',
};
```
- **Refactored:**
```js
export const options = {
    vus: 2000,
    duration: '20s',
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
let res = http.get(`${baseUrl}/k12-course-service/api/v1/programs?type=admission`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/k12-course-service/api/v1/programs?type=admission`, {
    headers: headers,
    tags: {
        name: 'ProgramsAdmission',
        endpoint: '/k12-course-service/api/v1/programs',
        flow: 'admission'
    }
});
```

### `script_219.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 2000,
    duration: '20s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 2000,
    duration: '20s',
    thresholds: {
        'http_req_failed': ['rate<0.01'], // fail test if more than 1% of requests fail
        'http_req_duration': ['p(95)<500'], // 95% of requests must be below 500ms
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/k12-course-service/api/v1/programs?type=admission`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/k12-course-service/api/v1/programs?type=admission`, {
    headers: headers,
    tags: { name: 'GetAdmissionPrograms' }
});
```

---

## `script_221.js`

### `script_221.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 10000,
    duration: '10s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 10000,
    duration: '10s',
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/cart-service/api/v1/carts?identifier=658ad45415e59054c0983e52`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/cart-service/api/v1/carts?identifier=658ad45415e59054c0983e52`, {
    headers: headers,
    tags: { name: 'GetCart' },
});
```

### `script_221.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 10000,
    duration: '10s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 10000,
    duration: '10s',
    thresholds: {
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/cart-service/api/v1/carts?identifier=658ad45415e59054c0983e52`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/cart-service/api/v1/carts?identifier=658ad45415e59054c0983e52`, {
    headers: headers,
    tags: {
        name: 'GetCart',
        endpoint: 'cart-service-carts',
        flow: 'cart'
    }
});
```

### `script_221.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8]
- **Snippet:**
```js
export let options = {
    vus: 10000,
    duration: '10s',
};
```
- **Refactored:**
```js
export let options = {
    vus: 10000,
    duration: '10s',
    thresholds: {
        http_req_failed: ['rate<0.01'],   // http errors should be less than 1%
        http_req_duration: ['p(95)<500'], // 95% of requests must complete below 500ms
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/cart-service/api/v1/carts?identifier=658ad45415e59054c0983e52`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/cart-service/api/v1/carts?identifier=658ad45415e59054c0983e52`, {
    headers: headers,
    tags: {
        name: 'GetCart',
    },
});
```

---

## `script_223.js`

### `script_223.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 10,
  duration: '10m',
};
```
- **Refactored:**
```js
export const options = {
  vus: 10,
  duration: '10m',
  thresholds: {
    'http_req_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
    'response_time': ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [25]
- **Snippet:**
```js
const res = http.get(url);
```
- **Refactored:**
```js
const res = http.get(url, { tags: { name: 'findByStatus', status: status } });
```

### `script_223.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 10,
  duration: '10m',
};
```
- **Refactored:**
```js
export const options = {
  vus: 10,
  duration: '10m',
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.95'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [25]
- **Snippet:**
```js
const res = http.get(url);
```
- **Refactored:**
```js
const res = http.get(url, {
  tags: {
    name: 'FindPetsByStatus',
    endpoint: '/v2/pet/findByStatus',
    status: status,
  },
});
```

### `script_223.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [8, 9, 10, 11]
- **Snippet:**
```js
export const options = {
  vus: 10, // Jumlah VUs
  duration: '10m', // Durasi pengujian
};
```
- **Refactored:**
```js
export const options = {
  vus: 10, // Jumlah VUs
  duration: '10m', // Durasi pengujian
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    'response_time': ['p(95)<500'], // Threshold on custom metric
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [25, 28]
- **Snippet:**
```js
const res = http.get(url);

// Menyimpan metrik tambahan
responseTime.add(res.timings.duration);
```
- **Refactored:**
```js
const params = {
  tags: {
    name: 'PetFindByStatus',
    status: status,
  },
};

// Kirim request ke API dengan tags
const res = http.get(url, params);

// Menyimpan metrik tambahan dengan tags
responseTime.add(res.timings.duration, { status: status });
```

---

## `script_224.js`

### `script_224.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [36, 38]
- **Snippet:**
```js
const response = concreteProductsResource.get(product.sku);

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
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
      'concrete products response status is 200': (r) => r.status === 200,
      'concrete products response body is not empty': (r) => r.body && r.body.length > 0,
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

  group(testConfiguration.group, () => {
    const concreteProductsResource = new ConcreteProductsResource();
    const tags = {
      name: 'SAPI3_get_concrete_products',
      endpoint: 'concrete-products',
      flow: testConfiguration.group,
    };

    const response = concreteProductsResource.get(product.sku, { tags });

    metrics[testConfiguration.metrics[0]].add(response.timings.duration, tags);
  });
}
```

### `script_224.js` — GEMINI

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
// ... inside default function
const response = concreteProductsResource.get(product.sku);

check(response, {
  'status is 200': (r) => r.status === 200,
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
const tags = { name: testConfiguration.metrics[0] }; // e.g., 'SAPI3_get_concrete_products'
const response = concreteProductsResource.get(product.sku, { tags });

// Note: The 'ConcreteProductsResource.get' method must be updated to pass these
// tags to the underlying k6/http request.
```

---

## `script_227.js`

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
const res = http.get('http://api:3000/', { tags: { name: 'Homepage' } });
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
    checks: ['rate>0.99'],
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
  tags: { name: 'RootEndpoint', endpoint: '/' },
});
check(res, {
  'status is 200': (r) => r.status === 200,
}, { name: 'RootEndpoint' });
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
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<200'], // 95% of requests must complete below 200ms
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

---

## `script_229.js`

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
let res = http.get('http://localhost:3000/endpoint', { tags: { name: 'Endpoint' } });
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
        'http_req_duration{name:Endpoint}': ['p(95)<500'],
        'checks{name:Endpoint}': ['rate>0.99'],
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
let res = http.get('http://localhost:3000/endpoint', {
    tags: { name: 'Endpoint', endpoint: '/endpoint' },
});
check(res, { 'status was 200': (r) => r.status === 200 }, {
    name: 'Endpoint',
    endpoint: '/endpoint',
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
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
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

---

## `script_231.js`

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

- **Lines:** [14]
- **Snippet:**
```js
const res = http.get('https://quickpizza.grafana.com');
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    ContentSize: ['value<4000'],
    'http_req_duration{name:Home}': ['p(95)<500'],
  },
};

export default function () {
  const res = http.get('https://quickpizza.grafana.com', {
    tags: { name: 'Home' },
  });
  GaugeContentSize.add(res.body.length);
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
import { check } from 'k6';
// ...
const res = http.get('https://quickpizza.grafana.com');
check(res, {
  'status is 200': (r) => r.status === 200,
});
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
  tags: {
    name: 'Homepage',
  },
});
```

---

## `script_232.js`

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
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
    'http_req_duration{name:Home}': ['p(95)<500'],
    'checks{name:Home}': ['rate>0.99'],
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
const params = { tags: { name: 'Home', endpoint: 'home' } };
let res = http.get('https://www.cruzeiro.com.br/', params);
check(res, {
  'status foi 200': (r) => r.status === 200,
  'tempo de resposta foi menor que 500ms': (r) => r.timings.duration < 500,
}, params.tags);
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
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
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
  tags: { name: 'Homepage' },
});
```

---

## `script_233.js`

### `script_233.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [9]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
export let options = {
  ...test_options, // keep existing options from ./options.js
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks': ['rate>0.99'] // 99% of checks should pass
  }
};
```

---

## `script_234.js`

### `script_234.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
export default function () {
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
check(responses[0], {
    'status is 200': (res) => res.status === 200,
    'response body is not empty': (res) => res.body && res.body.length > 0,
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

### `script_234.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [1, 11]
- **Snippet:**
```js
import http from 'k6/http';
import { check } from 'k6';

export default function () { ... }
```
- **Refactored:**
```js
import http from 'k6/http';
import { check } from 'k6';

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    'http_req_duration{name:UserSearch}': ['p(95)<500'],
  },
};

export default function () {
  // test logic
}
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

check(responses[0], {
  'user search status is 200': (res) => res.status === 200,
  'user search response body is not empty': (res) => res.body && res.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [4, 19]
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
    'Authorization': 'Bearer ...',
  },
  tags: {
    name: 'UserSearch',
    endpoint: 'user_search',
  },
};

request.push({
  method: 'GET',
  url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
  params,
});
```

### `script_234.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [3]
- **Snippet:**
```js
// The 'options' object with a 'thresholds' property is not defined.
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

- **Lines:** [25, 29, 30, 31]
- **Snippet:**
```js
const responses = http.batch(request);

// ...
// check(responses[2], {
//     'form data OK': (res) => JSON.parse(res.body)['form']['hello'] == 'world!',
// });
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
    params: params,
    tags: { name: 'UserSearch' },
});
```

---

## `script_235.js`

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
const res = http.post('https://httpbin.test.k6.io/post', payload, { headers, tags: { name: 'Post-HttpBin' } });
```

### `script_235.js` — CHATGPT

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
    'http_req_duration{name:CreatePost}': ['p(95)<500'],
    'http_req_failed{name:CreatePost}': ['rate<0.01'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [23, 25, 26, 27, 28, 29]
- **Snippet:**
```js
const res = http.post('https://httpbin.test.k6.io/post', payload, { headers });

check(res, {
  'Post status is 200': (r) => res.status === 200,
  'Post Content-Type header': (r) => res.headers['Content-Type'] === 'application/json',
  'Post response name': (r) => res.status === 200 && res.json().json.name === 'lorem',
});
```
- **Refactored:**
```js
const params = {
  headers,
  tags: {
    name: 'CreatePost',
    endpoint: '/post',
    flow: 'post_creation',
  },
};

const res = http.post('https://httpbin.test.k6.io/post', payload, params);

check(res, {
  'Post status is 200': (r) => r.status === 200,
  'Post Content-Type header': (r) => r.headers['Content-Type'] === 'application/json',
  'Post response name': (r) => r.status === 200 && r.json().json.name === 'lorem',
}, {
  name: 'CreatePost',
  endpoint: '/post',
  flow: 'post_creation',
});
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
      duration: '30s',
      preAllocatedVUs: 50,
      rate: 50,
      timeUnit: '1s',
    },
  },
  thresholds: {
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests must complete below 500ms
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
    tags: { name: 'CreateUser' } 
  });
```

---

## `script_236.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
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
    tags: { name: 'RegisterMember' },
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
        name: 'CreateMember',
        endpoint: '/api/members',
        method: 'POST',
    },
};
let response = http.post('http://localhost:8080/api/members', body, params);
check(response, {
    'is status 200': (r) => r.status === 200,
}, { name: 'CreateMember' });
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
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
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

---

## `script_237.js`

### `script_237.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4]
- **Snippet:**
```js
export default function() {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
  })
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
const response = http.get(BASE_URL, { tags: { name: 'HomePage' } })
```

### `script_237.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [4]
- **Snippet:**
```js
export default function() {
  const BASE_URL = __ENV.URL
  const response = http.get(BASE_URL)
  sleep(1)
}
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
import { sleep, check } from 'k6';

export default function() {
  const BASE_URL = __ENV.URL;
  const response = http.get(BASE_URL);
  check(response, {
    'status is 200': (r) => r.status === 200,
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
export default function() {
  const BASE_URL = __ENV.URL;
  const response = http.get(BASE_URL, {
    tags: { name: 'BaseURL' },
  });
  sleep(1);
}
```

### `script_237.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [3]
- **Snippet:**
```js
import { sleep, sllep } from 'k6'

export default function() {
```
- **Refactored:**
```js
import http from 'k6/http'
import { sleep, sllep } from 'k6'

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
};

export default function() {
  // ...
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
import { check } from 'k6';
// ... inside default function
const response = http.get(BASE_URL);
check(response, {
  'status is 200': (r) => r.status === 200,
});
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

---

## `script_238.js`

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

// inside the group callback:
const response = productPage.get(product.url);

check(response, {
  'status is 200': (r) => r.status === 200,
  'body is not empty': (r) => r.body && r.body.length > 0,
});

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```

**Smell 4: Not using tags**

- **Lines:** [39]
- **Snippet:**
```js
const response = productPage.get(product.url);
```
- **Refactored:**
```js
// Pass tags as part of the request params so metrics can be filtered by endpoint/group.
// Assuming ProductPage.get() accepts a params argument forwarded to k6/http:
const response = productPage.get(product.url, {
  tags: { name: 'GetProduct', group: testConfiguration.group, testId: testConfiguration.id },
});

// Also update the threshold to leverage the tag:
// thresholds: {
//   'http_req_duration{name:GetProduct}': ['avg<600'],
// }
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
let fixture;

export function setup() {
  fixture = FullProductFixture.createFixture({
    productCount: testConfiguration.vus ?? EnvironmentUtil.getRampVus(),
  });
  return fixture.getData();
}

export default function (data) {
  const product = FullProductFixture.iterateData(data);
  // test logic
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
import { check, group } from 'k6';

const response = productPage.get(product.url);
check(response, {
  'product page status is 200': (r) => r.status === 200,
  'product page response is not empty': (r) => r.body && r.body.length > 0,
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
const requestTags = {
  name: 'S8_get_product',
  group: testConfiguration.group,
  test_id: testConfiguration.id,
};

const response = productPage.get(product.url, { tags: requestTags });

metrics[testConfiguration.metrics[0]].add(response.timings.duration, requestTags);
```

### `script_238.js` — GEMINI

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
// ...
const response = productPage.get(product.url);

const isSuccessful = check(response, {
  'is status 200': (r) => r.status === 200,
});

if (isSuccessful) {
  metrics[testConfiguration.metrics[0]].add(response.timings.duration);
}
```

---

## `script_239.js`

### `script_239.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [5]
- **Snippet:**
```js
export default function(){
    const res = http.get(__ENV.URL);
    sleep(1);
}
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
import { check, sleep } from 'k6';

export default function(){
    const res = http.get(__ENV.URL);
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
const res = http.get(__ENV.URL);
```
- **Refactored:**
```js
const res = http.get(__ENV.URL, { tags: { name: 'MainEndpoint' } });
```

### `script_239.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [1, 10]
- **Snippet:**
```js
import http from 'k6/http';
import { sleep } from 'k6';

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
import http from 'k6/http';
import { sleep, check } from 'k6';

export default function(){
    const res = http.get(__ENV.URL);
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
const res = http.get(__ENV.URL);
```
- **Refactored:**
```js
const res = http.get(__ENV.URL, {
  tags: {
    name: 'TargetURL',
    endpoint: 'target-url',
  },
});
```

### `script_239.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 10]
- **Snippet:**
```js
The script does not define an `options` object with a `thresholds` property, making it impossible to programmatically determine if the test passed or failed.
```
- **Refactored:**
```js
import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],   // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests must complete below 500ms
  },
};

export default function(){ ... }
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
// ...
const res = http.get(__ENV.URL);
check(res, { 'status is 200': (r) => r.status === 200 });
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
  tags: { name: 'Homepage' }, 
});
```

---

## `script_240.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
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
    tags: { name: 'GetPrograms' },
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
    tags: { name: 'Programs', endpoint: 'programs' },
});

check(res, {
    'status is 200': (r) => r.status === 200,
    'response time <= 500ms': (r) => r.timings.duration <= 500,
}, { name: 'Programs', endpoint: 'programs' });
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
        'http_req_failed': ['rate<0.01'], // fail if more than 1% of requests fail
        'http_req_duration': ['p(95)<500'], // 95th percentile response time must be below 500ms
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
    tags: {
        name: 'GetPrograms',
    },
});
```

---

## `script_241.js`

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
    'http_req_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
    'response_time': ['p(95)<500'],
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
const res = http.get(url, { headers, tags: { name: 'UserLogout' } });
```

### `script_241.js` — CHATGPT

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
    'http_req_duration{name:UserLogout}': ['p(95)<500', 'p(99)<1000'],
    'http_req_failed{name:UserLogout}': ['rate<0.01'],
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
const tags = { name: 'UserLogout', endpoint: 'user_logout' };
const params = {
  headers,
  tags,
};

const res = http.get(url, params);

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
    'http_req_failed': ['rate<0.01'], // fail if more than 1% of requests fail
    'response_time': ['p(95)<500'],    // 95th percentile of response time must be below 500ms
    'checks{Status is 200}': ['rate>0.95'] // more than 95% of checks for status 200 must pass
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [19, 22]
- **Snippet:**
```js
const res = http.get(url, { headers });

  // Menyimpan metrik tambahan
  responseTime.add(res.timings.duration);
```
- **Refactored:**
```js
// Kirim request ke API
  const params = {
    headers,
    tags: { name: 'UserLogout' },
  };
  const res = http.get(url, params);

  // Menyimpan metrik tambahan
  responseTime.add(res.timings.duration, { name: 'UserLogout' });
```

---

## `script_242.js`

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
    'http_req_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
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
  tags: { name: 'UpdatePetStatus', endpoint: 'pet/:petId' },
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
    response_time: ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [26, 29, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]
- **Snippet:**
```js
const res = http.post(url, payload);
responseTime.add(res.timings.duration);
check(res, {
  'Status is 200': (r) => r.status === 200,
  'Response time < 200ms': (r) => r.timings.duration < 200,
});
```
- **Refactored:**
```js
const tags = { endpoint: 'UpdatePetById', method: 'POST' };
const params = { tags };
const res = http.post(url, payload, params);
responseTime.add(res.timings.duration, tags);
check(res, {
  'Status is expected': (r) => [200, 400, 404, 405, 429, 500].includes(r.status),
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
    // 95% of requests must complete below 500ms
    'http_req_duration': ['p(95)<500'],
    // The custom metric for response time should also meet the P95 criteria
    'response_time': ['p(95)<500'],
    // Less than 1% of requests should fail
    'http_req_failed': ['rate<0.01'],
    // Ensure at least 99% of checks pass
    'checks': ['rate>0.99'],
  },
};
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
    name: 'CreateOrUpdatePet',
  },
};
// Kirim request POST dengan form data dan tambahkan tag
const res = http.post(url, payload, params);

// Menyimpan metrik tambahan dengan tag yang sama
responseTime.add(res.timings.duration, { name: 'CreateOrUpdatePet' });
```

---

## `script_245.js`

### `script_245.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [43, 44, 45]
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
  'addItem status is 2xx': (r) => r.status >= 200 && r.status < 300,
  'addItem response has body': (r) => r.body && r.body.length > 0,
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
// Pass tags via params when making the request so metrics can be filtered by endpoint/operation.
// Assuming GuestCartsResource.addItem accepts an optional params argument:
const response = guestCartsResource.addItem(
  null,
  product.sku,
  1,
  { tags: { name: 'SAPI31_post_guest_cart_items', group: testConfiguration.group } }
);
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

export default function (data) {
  const product = fixture.iterateData(data);
  const anonymousCustomerUniqueId = `ananymous-${exec.vu.iterationInScenario}`;

  group(testConfiguration.group, () => {
    const guestCartsResource = new GuestCartsResource(anonymousCustomerUniqueId);
    const response = guestCartsResource.addItem(null, product.sku, 1);

    check(response, {
      'guest cart item added successfully': (r) => r.status === 200 || r.status === 201,
    });

    metrics[testConfiguration.metrics[0]].add(response.timings.duration);
  });
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
import { group, check } from 'k6';

export default function (data) {
  const product = fixture.iterateData(data);
  const anonymousCustomerUniqueId = `ananymous-${exec.vu.iterationInScenario}`;

  group(testConfiguration.group, () => {
    const guestCartsResource = new GuestCartsResource(anonymousCustomerUniqueId);
    const tags = {
      name: 'PostGuestCartItems',
      endpoint: 'guest-carts/items',
      flow: 'Cart',
    };

    const response = guestCartsResource.addItem(null, product.sku, 1, { tags });

    check(response, {
      'guest cart item added successfully': (r) => r.status === 200 || r.status === 201,
    }, tags);

    metrics[testConfiguration.metrics[0]].add(response.timings.duration, tags);
  });
}
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
import { group, check } from 'k6';
// ...

group(testConfiguration.group, () => {
  const guestCartsResource = new GuestCartsResource(anonymousCustomerUniqueId);
  const response = guestCartsResource.addItem(null, product.sku, 1);

  check(response, {
    'item added to cart successfully': (r) => r.status >= 200 && r.status < 300,
  });

  metrics[testConfiguration.metrics[0]].add(response.timings.duration);
});
```

---

## `script_247.js`

### `script_247.js` — CLAUDE

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};

export default function () {
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

- **Lines:** [14]
- **Snippet:**
```js
const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);
```
- **Refactored:**
```js
const params = {
  headers: {
    'my-header-one': 'hello',
    'my-header-two': 'world',
  },
  tags: { name: 'DeleteEcho' },
};

const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);
```

### `script_247.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [6]
- **Snippet:**
```js
export default function () { ... } // no export const options with thresholds defined
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
    checks: ['rate>0.99'],
  },
};

export default function () {
  // test code
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

const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);

check(response, {
  'DELETE echo returned 2xx': (r) => r.status >= 200 && r.status < 300,
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
    name: 'DeleteEcho',
    endpoint: '/api/basic/echo',
    flow: 'basic-echo-delete',
  },
};

const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);
```

### `script_247.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 21]
- **Snippet:**
```js
// The script does not export an 'options' object with a 'thresholds' property.
```
- **Refactored:**
```js
import { sleep } from 'k6';
import http from 'k6/http';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<300'],
  },
};

const BASE_URL = 'http://localhost:8888/alphamart';
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
// ...
const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);
check(response, {
  'DELETE /api/basic/echo was successful (2xx)': (r) => r.status >= 200 && r.status < 300,
});
```

**Smell 4: Not using tags**

- **Lines:** [14]
- **Snippet:**
```js
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
    name: 'DeleteEchoAPI',
  },
};

const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);
```

---

## `script_248.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [22, 23, 24, 25]
- **Snippet:**
```js
const resCo = httppost("G-4096", {
        operation: "test",
    })
    check(resCo, { 'A status was 200': (r) => r.status == 200 });
```
- **Refactored:**
```js
const resCo = http.post(`${hostprefix}/SYNC-G-4096`, JSON.stringify({ operation: 'test' }), {
        headers: { 'Content-Type': 'application/json' },
        tags: { name: 'SYNC-G-4096' },
    });
    check(resCo, { 'A status was 200': (r) => r.status == 200 });
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
        tags: { name: `SYNC-${task}`, task: task }
    }
);
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
            preAllocatedVUs: 100, 
            maxVUs: 200,
        },
    },
    thresholds: {
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'checks': ['rate>0.99'],           // 99% of checks must pass
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

---

## `script_249.js`

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
    'http_req_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
    'response_time': ['p(95)<500'],
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
const res = http.del(url, null, { tags: { name: 'DeletePet' } });
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
    'http_req_duration{name:DeletePet}': ['p(95)<500'],
    checks: ['rate>0.95'],
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
const requestTags = {
  name: 'DeletePet',
  endpoint: '/v2/pet/{petId}',
  method: 'DELETE',
};

const res = http.del(url, null, { tags: requestTags });
responseTime.add(res.timings.duration, requestTags);

check(res, {
  'Status is expected': (r) => [200, 400, 404, 429, 500].includes(r.status),
  'Response time < 500ms': (r) => r.timings.duration < 500,
}, requestTags);
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
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    'response_time': ['p(95)<500'], // 95% of response times should be below 500ms
    'checks{Status is 200}': ['rate>0.95'], // success rate for status 200 should be >95%
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [20, 23]
- **Snippet:**
```js
const res = http.del(url);

// Menyimpan metrik tambahan
responseTime.add(res.timings.duration);
```
- **Refactored:**
```js
const url = `https://petstore.swagger.io/v2/pet/${petId}`;
const params = {
  tags: { name: 'DeletePet' },
};

// Kirim request DELETE ke API
const res = http.del(url, null, params);

// Menyimpan metrik tambahan
responseTime.add(res.timings.duration, { name: 'DeletePet' });
```

---

## `script_250.js`

### `script_250.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [23]
- **Snippet:**
```js
const response = http.get('http://test.k6.io');
```
- **Refactored:**
```js
import { check } from 'k6';

// inside default function:
const response = http.get('http://test.k6.io');
check(response, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

- **Lines:** [23]
- **Snippet:**
```js
const response = http.get('http://test.k6.io');
```
- **Refactored:**
```js
const response = http.get('http://test.k6.io', { tags: { name: 'HomePage' } });

// and update thresholds to leverage the tag:
thresholds: {
  'http_req_duration{name:HomePage}': ['p(95)<500'],
  'success_rate': ['rate>0.95'],
  'requests_counter': ['count>3'],
}
```

### `script_250.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [23]
- **Snippet:**
```js
const response = http.get('http://test.k6.io');
```
- **Refactored:**
```js
const tags = { name: 'Home' };
const response = http.get('http://test.k6.io', { tags });
```

### `script_250.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [23, 32, 33, 34, 35, 36]
- **Snippet:**
```js
const response = http.get('http://test.k6.io');
// ...
if (response.status === 200) {
    successRate.add(true);
} else {
    successRate.add(false);
}
```
- **Refactored:**
```js
import { check } from 'k6'; // Add this to the import section

//... inside default function
const response = http.get('http://test.k6.io');
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

---

## `script_251.js`

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

// ...

group(testConfiguration.group, () => {
  const checkoutResource = new CheckoutResource(idCart, customerEmail, bearerToken);
  const response = checkoutResource.checkout();

  check(response, {
    'checkout status is 200': (r) => r.status === 200,
  });

  metrics[testConfiguration.metrics[0]].add(response.timings.duration);
});
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
group(testConfiguration.group, () => {
  const checkoutResource = new CheckoutResource(idCart, customerEmail, bearerToken);
  const tags = {
    name: 'Checkout',
    endpoint: 'POST /checkout',
    flow: testConfiguration.group,
  };

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
const response = checkoutResource.checkout();
const isSuccessful = check(response, {
  'checkout successful (status 200)': (r) => r.status === 200,
});
if (isSuccessful) {
  metrics[testConfiguration.metrics[0]].add(response.timings.duration);
}
```

---

## `script_252.js`

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
    'checks{name:success login}': ['rate>0.99'],
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
  tags: { name: 'Login' },
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

- **Lines:** [22]
- **Snippet:**
```js
let res = http.post('http://localhost:5680/api/v1/auth/token', data)
```
- **Refactored:**
```js
let res = http.post('http://localhost:5680/api/v1/auth/token', data, {
  tags: {
    name: 'AuthToken',
    endpoint: '/api/v1/auth/token',
    flow: 'login',
  },
})
```

### `script_252.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
- **Snippet:**
```js
export const options = {
  scenarios: {
    contacts: {
      // ...
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
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
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
  tags: { name: 'Authentication' },
};
let res = http.post('http://localhost:5680/api/v1/auth/token', data, params);
```

---

## `script_253.js`

### `script_253.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
responses.forEach((res, index) => {
    check(res, {
        [`response ${index} status is 200`]: (r) => r.status === 200,
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
        tags: { name: 'UserSearch' },
    }
});
```

### `script_253.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [11]
- **Snippet:**
```js
export default function () {
    ...
}
// No export const options with thresholds is defined.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    'http_req_duration{name:UserSearch}': ['p(95)<500'],
    checks: ['rate>0.99'],
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
    tags: {
      name: 'UserSearch',
      endpoint: 'user_search',
    },
  },
});
```

### `script_253.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** []
- **Snippet:**
```js
The script does not export an `options` object with a `thresholds` property. Without it, the test will always pass in a CI/CD environment, regardless of the system's performance.
```
- **Refactored:**
```js
import http from 'k6/http';
import { check } from 'k6';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
  },
};
// ...
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
    'is status 200': (r) => r.status === 200,
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
for (let req = 0; req < countRequest; req++) {
    request.push({
        method: 'GET',
        url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
        params: {
            ...params,
            tags: { name: 'UserSearch' },
        }
    });
}
```

---

## `script_254.js`

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [23]
- **Snippet:**
```js
let res = http.post(url, payload, params);
```
- **Refactored:**
```js
const params = {
  headers: { 'Content-Type': 'application/json' },
  tags: { name: 'PostPayload' },
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
  tags: { name: 'CreatePayload', endpoint: '/api/payload' },
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
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [23]
- **Snippet:**
```js
let res = http.post(url, payload, params);
```
- **Refactored:**
```js
const params = {
  headers: { 'Content-Type': 'application/json' },
  tags: { name: 'CreatePayloadAPI' },
};
let res = http.post(url, payload, params);
```

---

## `script_255.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
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
let params = { headers: { 'Content-Type': 'application/json' }, tags: { name: 'CreateUsersWithArray' } };
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
        'http_req_duration{name:CreateUsersWithArray}': ['p(95)<500'],
        'checks{name:CreateUsersWithArray}': ['rate>0.95'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [27, 29]
- **Snippet:**
```js
let params = { headers: { 'Content-Type': 'application/json' } };

let res = http.post(url, invalidPayload, params);
```
- **Refactored:**
```js
let params = {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'CreateUsersWithArray', endpoint: '/v2/user/createWithArray' },
};

let res = http.post(url, invalidPayload, params);

check(res, {
    'status is expected': (r) => [200, 400, 429, 500].includes(r.status),
    'response contains message': (r) => r.body.includes('message'),
}, { name: 'CreateUsersWithArray' });
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
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
        'checks': ['rate>0.99']
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
let res = http.post(url, invalidPayload, { 
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'CreateUserWithArray' } 
});
```

---

## `script_257.js`

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
  const fixture = FullProductFixture.createFixture({ productCount: 0 });
  const product = fixture.iterateData(data);
  // test logic
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
  name: 'CatalogSearch',
  group: testConfiguration.group,
  endpoint: 'catalog_search',
};

const response = catalogSearchResource.get(
  { q: product.sku },
  { tags }
);

check(response, {
  'catalog search status is 200': (r) => r.status === 200,
}, tags);

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
let fixture;

export function setup() {
  // Initialize the fixture inside setup, which runs once for the entire test
  fixture = FullProductFixture.createFixture({
    productCount: testConfiguration.vus ?? EnvironmentUtil.getRampVus(),
  });
  return fixture.getData();
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
import { group, check } from 'k6';
// ... inside default function
group(testConfiguration.group, () => {
  const catalogSearchResource = new CatalogSearchResource();
  const response = catalogSearchResource.get({ q: product.sku });

  check(response, {
    'status is 200': (r) => r.status === 200,
  });

  metrics[testConfiguration.metrics[0]].add(response.timings.duration);
});
```

**Smell 4: Not using tags**

- **Lines:** [39]
- **Snippet:**
```js
const response = catalogSearchResource.get({ q: product.sku });
```
- **Refactored:**
```js
// The resource method should be updated to accept and pass k6 request parameters, including tags.
const params = {
  tags: {
    name: 'SAPI2_get_catalog_search',
  },
};
const response = catalogSearchResource.get({ q: product.sku }, params);
```

---

## `script_259.js`

### `script_259.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [7]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};

export default function () {
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

// inside default function:
const res = http.get('https://www.google.com');
check(res, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
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
const res = http.get('https://www.google.com', { tags: { name: 'GoogleHome' } });
```

### `script_259.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [7]
- **Snippet:**
```js
export default function () {
    const res = http.get('https://www.google.com');
    ...
}
// No export const options block with thresholds is defined.
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
  const res = http.get('https://www.google.com', {
    tags: { name: 'GoogleHome' },
  });
  sleep(1);
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
import { sleep, check } from 'k6';
import http from 'k6/http';

export default function () {
  const res = http.get('https://www.google.com', {
    tags: { name: 'GoogleHome' },
  });

  check(res, {
    'Google home returned status 200': (r) => r.status === 200,
  });

  sleep(1);
}
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
    name: 'GoogleHome',
    endpoint: 'home',
  },
});
```

### `script_259.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 18]
- **Snippet:**
```js
// The 'options' export with a 'thresholds' object is missing.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
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
// ...
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
  tags: { name: 'GoogleHomepage' },
});
```

---

## `script_260.js`

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
  ...test_options, // Keep the imported options (VUs, duration, etc.)
  thresholds: {
    'http_req_failed': ['rate<0.01'], // Fail test if more than 1% of requests fail
    'http_req_duration{name:GET}': ['p(95)<500'], // 95% of 'GET' requests must be below 500ms
    'checks': ['rate>0.99'], // More than 99% of checks must pass
  },
};
```

---

## `script_262.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
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
    tags: { name: 'GetNotices' },
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
let res = http.get(
    `${baseUrl}/notice-service/api/v1/notices?identification_id=101&identification_type=segments&page=1&type=notice&limit=1`,
    {
        headers: headers,
        tags: {
            name: 'GetNotices',
            endpoint: 'notices',
            flow: 'notice-service'
        }
    }
);
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

---

## `script_264.js`

### `script_264.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [15]
- **Snippet:**
```js
const db = sql.open('postgres', pdConnectionString)
```
- **Refactored:**
```js
/* Move DB connection logic into setup() to run only once per test, not once per VU. */
export function setup() {
  const pgUser = __ENV.PG_USER ? __ENV.PG_USER : 'postgres';
  const pgPass = __ENV.PG_PASS;
  const pgDB = __ENV.PG_DB ? __ENV.PG_DB : 'postgres';
  const pgPort = __ENV.PG_PORT ? __ENV.PG_PORT : '5432';
  const pgHost = __ENV.PG_HOST ? __ENV.PG_HOST : 'db.proj.supabase.com';
  const pdConnectionString = `postgres://${pgUser}:${pgPass}@${pgHost}:${pgPort}/${pgDB}?sslmode=disable`;
  const db = sql.open('postgres', pdConnectionString);

  db.exec(`create table if not exists "load_messages" (...);`);
  
  return { db: db }; // Pass the connection object to VUs
}

export function teardown(data) {
  if (data.db) {
    data.db.close();
  }
}

// The default function now receives the data object from setup
export default (data) => {
  // use data.db instead of the global db object
  data.db.exec(...);
};
```

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
    'iteration_duration': ['p(95)<2000'], // e.g., 95% of iterations must be under 2s
    'inserts{rate>1.5}': ['rate>1.5'], // e.g., ensure the insert rate is above 1.5/s
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
import { check } from 'k6';
// ... inside the default function
const room = rooms[getRandomInt(0, rooms.length)];
const insertSuccessful = check(null, {
  'database insert successful': () => {
    try {
      db.exec(
        `insert into load_messages (room_id, data) values ('${room}', '...');`
      );
      return true;
    } catch (e) {
      console.error(`DB insert failed: ${e}`);
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
// ... inside the default function
const room = rooms[getRandomInt(0, rooms.length)];
db.exec(
  `insert into load_messages (room_id, data) values ('${room}', '...');`
)
counterInserts.add(1, { room: room });
```

---

## `script_265.js`

### `script_265.js` — CLAUDE

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};

export default function () {
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
...
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
const res = http.get(`https://${__ENV.MY_HOSTNAME}`, { tags: { name: 'Homepage' } });
```

### `script_265.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 6, 7, 8, 9]
- **Snippet:**
```js
import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
  const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
  sleep(1);
}
```
- **Refactored:**
```js
import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
import http from 'k6/http';
import { check, sleep } from 'k6';

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
import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
  const res = http.get(`https://${__ENV.MY_HOSTNAME}`, {
    tags: { name: 'Home' },
  });
  sleep(1);
}
```

### `script_265.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 6, 7, 8, 9]
- **Snippet:**
```js
import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
  const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
  sleep(1);
}
```
- **Refactored:**
```js
import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
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
import http from 'k6/http';
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
const res = http.get(`https://${__ENV.MY_HOSTNAME}`, {
  tags: {
    name: 'Homepage',
  },
});
```

---

## `script_266.js`

### `script_266.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [62, 64, 70]
- **Snippet:**
```js
const response = ordersResource.all();

orderId = JSON.parse(response.body).data[0].id;
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const ordersResource = new OrdersResource(bearerToken);
const response = ordersResource.all();

const isSuccessful = check(response, {
  'Get Orders | status is 200': (r) => r.status === 200,
  'Get Orders | body contains data': (r) => {
    try {
      return JSON.parse(r.body).data.length > 0;
    } catch (e) {
      return false;
    }
  }
});

if (isSuccessful) {
  orderId = JSON.parse(response.body).data[0].id;
  metrics['SAPI38_get_orders'].add(response.timings.duration);
} else {
  // Handle the error, e.g., fail the iteration
  fail('Failed to get orders');
}
```

---

## `script_267.js`

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
        http_req_duration: ['p(95)<500', 'p(99)<1000'],
        http_req_failed: ['rate<0.01'],
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
    tags: { name: 'EnrolledCourses' },
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
        name: 'EnrolledCourses',
        endpoint: 'premium_content_courses_enrolled',
    },
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
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<1500'],
        'checks': ['rate>0.99']
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
        name: 'Get Enrolled Courses',
    },
});
```

---

## `script_268.js`

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
        http_req_failed: ['rate<0.01']
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
        tags: { name: "CreateUser" }
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
        'http_req_duration{name:CreateUserValidation}': ['p(95)<500'],
        'http_req_failed': ['rate<0.01'],
        'checks{name:CreateUserValidation}': ['rate>0.95']
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
    tags: {
        name: "CreateUserValidation",
        endpoint: "/v-throw/users",
        method: "POST"
    }
});

check(response, {
    "response code was 400 or 409": (res) => res.status === 400 || res.status === 409
}, { name: "CreateUserValidation" });
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
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
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
        tags: { name: 'CreateUser' }
    });
```

---

## `script_269.js`

### `script_269.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [6]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  vus: 1,
  duration: '30s',
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
export default function () {
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
http.get('https://self-signed.badssl.com/', { tags: { name: 'BadSSLHome' } });
```

### `script_269.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [1, 6]
- **Snippet:**
```js
import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
    http.get('https://self-signed.badssl.com/');
    sleep(1);
}
```
- **Refactored:**
```js
import http from 'k6/http';
import { sleep } from 'k6';

export const options = {
  thresholds: {
    'http_req_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01']
  }
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
import http from 'k6/http';
import { check, sleep } from 'k6';

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
http.get('https://self-signed.badssl.com/', {
  tags: {
    name: 'SelfSignedHome',
    endpoint: 'home'
  }
});
```

### `script_269.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 6, 7, 8, 9]
- **Snippet:**
```js
import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
    http.get('https://self-signed.badssl.com/');
    sleep(1);
}
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
import http from 'k6/http';
import { check } from 'k6';
//...
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

---

## `script_270.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
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
const response = http.post(url, { cookies }, { tags: { name: 'Logout' } });
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

- **Lines:** [22]
- **Snippet:**
```js
const response = http.post(url, { cookies });
```
- **Refactored:**
```js
const params = {
    cookies,
    tags: {
        name: 'Logout',
        endpoint,
    },
};
const response = http.post(url, null, params);
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
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
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
    tags: { name: 'Logout' } 
});
```

---

## `script_271.js`

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
// ...
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
http.get('https://www.google.com', { tags: { name: 'Google Homepage' } });
```

### `script_271.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [6]
- **Snippet:**
```js
export default function () {
    http.get('https://www.google.com');
    ...
}
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    'http_req_duration{name:GoogleHome}': ['p(95)<500']
  }
};

export default function () {
  http.get('https://www.google.com', { tags: { name: 'GoogleHome' } });
  sleep(randomIntBetween(1, 3));
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
import { sleep, check } from 'k6';

export default function () {
  const res = http.get('https://www.google.com', { tags: { name: 'GoogleHome' } });

  check(res, {
    'Google home returned HTTP 200': (r) => r.status === 200
  });

  sleep(randomIntBetween(1, 3));
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
export default function () {
  http.get('https://www.google.com', {
    tags: {
      name: 'GoogleHome',
      endpoint: 'home'
    }
  });

  sleep(randomIntBetween(1, 3));
}
```

### `script_271.js` — GEMINI

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
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
  },
};

export default function () { ... }
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
// ...
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
  tags: { name: 'GoogleHomepage' } 
});
```

---

## `script_273.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
        'checks': ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [22, 23, 24]
- **Snippet:**
```js
const resCo = httppost("G-1536", {
        operation: "test",
    })
```
- **Refactored:**
```js
const resCo = http.post(`${hostprefix}/SYNC-G-1536`, JSON.stringify({ operation: 'test' }), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'SYNC-G-1536' },
});
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
        tags: { name: `SYNC-${task}`, task: task },
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
const httppost = (task, body) => http.post(
    `${hostprefix}/SYNC-${task}`,
    JSON.stringify(body),
    {
        headers: { 'Content-Type': 'application/json' },
        tags: { name: task }
    }
)
```

---

## `script_276.js`

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
    checks: ['rate>0.99'],
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
  tags: {
    name: 'LambdaEndpoint',
    endpoint: 'lambda-url',
  },
});
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
    'checks': ['rate>0.99'],             // 99% of checks should pass
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
    tags: { name: 'GetLambdaURL' },
  });
```

---

## `script_277.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
        'checks': ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [19, 22, 23, 24]
- **Snippet:**
```js
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {headers: { 'Content-Type': 'application/json' }})

    const resCo = httppost("A-128", {
        operation: "test",
    })
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
)

// In options, thresholds can then filter by tag:
// 'http_req_duration{name:SYNC-A-128}': ['p(95)<500']
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
        'http_req_duration{name:SYNC-A-128}': ['p(95)<500'],
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
        tags: { name: `SYNC-${task}`, task },
    }
);
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
            rate: __ENV.RPS,
            timeUnit: '1s',
            duration: `${__ENV.DURATION}s`,
            preAllocatedVUs: 100,
            maxVUs: 200,
        },
    },
    thresholds: {
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
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

---

## `script_278.js`

### `script_278.js` — GEMINI

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
const tags = { name: 'insert_position' };
// ...
try {
  db.exec(
    // ... SQL statement
  );
  myFailRate.add(false, tags);
} catch (e) {
  console.log(e);
  myFailRate.add(true, tags);
  counterFailed.add(1, tags);
}
// ...
counterInserts.add(1, tags);
insertTrend.add(exFinish - exStart, tags);
```

---

## `script_279.js`

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
const res = http.get('http://localhost:3000/products', { headers, tags: { name: 'GetProducts' } });
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
    'http_req_duration{name:Products}': ['p(95)<500'],
    checks: ['rate>0.99'],
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
  tags: { name: 'Products', endpoint: 'products' },
});
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
    http_req_failed: ['rate<0.01'],   // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
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
    tags: { name: 'GetProducts' },
  });
```

---

## `script_280.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
        'checks': ['rate>0.99'],
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
    tags: { name: 'AuthenticateUser' },
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

- **Lines:** [22, 23, 24, 27]
- **Snippet:**
```js
let authHeaders = {
    headers: { 'Content-Type': 'application/json' },
};

let authResponse = http.post(`${BASE_URL}${AUTH_ENDPOINT}`, authPayload, authHeaders);
```
- **Refactored:**
```js
let authParams = {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'AuthenticateUser', endpoint: AUTH_ENDPOINT },
};

let authResponse = http.post(`${BASE_URL}${AUTH_ENDPOINT}`, authPayload, authParams);
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
    vus: 1000, // Number of virtual users
    duration: '100s', // Duration of the test
    thresholds: {
        http_req_failed: ['rate<0.01'],   // http errors should be less than 1%
        http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
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
    let authParams = {
        headers: { 'Content-Type': 'application/json' },
        tags: { name: 'Authentication' },
    };

    // Send the POST request to the authentication endpoint
    let authResponse = http.post(`${BASE_URL}${AUTH_ENDPOINT}`, authPayload, authParams);
```

---

## `script_281.js`

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
import { check, sleep } from 'k6'
import http from 'k6/http'

export const options = {
    stages: [
        { duration: '1m', target: 20 },
        { duration: '3m', target: 20 },
        { duration: '1m', target: 0 },
    ],
    thresholds: {
        'http_req_failed{name:GetCrocodiles}': ['rate<0.02'],
        'http_req_duration{name:GetCrocodiles}': ['p(95)<2000'],
    }
}

export default function main() {
    let response = http.get('https://test-api.k6.io/public/crocodiles/', { tags: { name: 'GetCrocodiles' } })
    check(response, {
        'status is 200': (r) => r.status === 200,
    })
    sleep(1)
}
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
    let response = http.get('https://test-api.k6.io/public/crocodiles/')
    check(response, {
        'GET crocodiles returns 200': (r) => r.status === 200,
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
export const options = {
    stages: [
        { duration: '1m', target: 20 },
        { duration: '3m', target: 20 },
        { duration: '1m', target: 0 },
    ],
    thresholds: {
        http_req_failed: ['rate<0.02'],
        'http_req_duration{name:Crocodiles}': ['p(95)<2000'],
    }
}

export default function main() {
    let response = http.get('https://test-api.k6.io/public/crocodiles/', {
        tags: { name: 'Crocodiles' },
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
import { check } from 'k6';

// In main function
let response = http.get('https://test-api.k6.io/public/crocodiles/');
check(response, {
    'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [20]
- **Snippet:**
```js
let response = http.get('https://test-api.k6.io/public/crocodiles/')
```
- **Refactored:**
```js
let response = http.get(
    'https://test-api.k6.io/public/crocodiles/',
    { tags: { name: 'GetCrocodiles' } }
);
```

---

## `script_282.js`

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
        http_req_duration: ['p(95)<500'],
        http_req_failed: ['rate<0.01'],
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
const response = storeOrderGetService.execute({ tags: { name: 'GetStoreOrder' } });
// Ensure the execute() function in getStoreOrder.js accepts and forwards tags to the http request, e.g.:
// export function execute(params = {}) {
//   return http.get(`${BASE_URL}/store/order/${orderId}`, { tags: { name: 'GetStoreOrder' }, ...params });
// }
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
    const tags = { name: 'GetStoreOrderById', endpoint: 'store-orders/:id' };
    const response = storeOrderGetService.execute({ tags });
    check(response, {
        'Get store order by Id Status is 200': (r) => r.status === 200,
    }, tags);
}

// Ensure storeOrderGetService.execute forwards the tags to the underlying HTTP request, for example:
// http.get(url, { tags });
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
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
        'checks': ['rate>0.99']
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [23, 24, 25, 26, 27, 28]
- **Snippet:**
```js
export default function () {
    const response = storeOrderGetService.execute();
    check(response, {
        'Get store order by Id Status is 200': (r) => r.status === 200,
    });
}
```
- **Refactored:**
```js
export default function () {
    // The service method should be adapted to accept k6's `params` object,
    // allowing tags to be added to the underlying HTTP request.
    const response = storeOrderGetService.execute({
        tags: { name: 'GetStoreOrderById' },
    });
    check(response, {
        'Get store order by Id Status is 200': (r) => r.status === 200,
    }, { name: 'GetStoreOrderById' }); // Tagging checks is also a good practice.
}
```

---

## `script_285.js`

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

// inside the group block:
const response = cartsResource.get(idCart, ['items']);

check(response, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
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
// Assuming CartsResource.get() accepts an optional params argument and passes it to the underlying http call:
const response = cartsResource.get(idCart, ['items'], { tags: { name: 'GetCartById', group: testConfiguration.group } });

// If CartsResource does not support params, update the resource method to accept and forward tags:
// Inside carts.resource.js:
// get(idCart, includes, params = {}) {
//   return http.get(`${baseUrl}/carts/${idCart}?include=${includes.join(',')}`, { tags: { name: 'GetCartById' }, ...params });
// }
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

// ...

group(testConfiguration.group, () => {
  const cartsResource = new CartsResource(bearerToken);
  const response = cartsResource.get(idCart, ['items']);

  check(response, {
    'GET cart by id returns 200': (r) => r.status === 200,
    'GET cart by id has a response body': (r) => !!r.body,
  });

  metrics[testConfiguration.metrics[0]].add(response.timings.duration);
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
  const tags = {
    name: 'GetCartById',
    endpoint: 'GET /carts/{id}',
    flow: testConfiguration.group,
  };

  const response = cartsResource.get(idCart, ['items'], { tags });

  metrics[testConfiguration.metrics[0]].add(response.timings.duration, tags);
});
```

### `script_285.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [47, 49]
- **Snippet:**
```js
const response = cartsResource.get(idCart, ['items']);

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
import { group, check } from 'k6'; // Add 'check' to the import
// ...
const response = cartsResource.get(idCart, ['items']);

check(response, {
  'Get cart by ID status is 200': (r) => r.status === 200,
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
  tags: { name: 'GetCartByID' },
});
// Note: This assumes the CartsResource.get method is updated to pass these tags to the underlying k6 http request.
```

---

## `script_286.js`

### `script_286.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [22]
- **Snippet:**
```js
const db = sql.open('postgres', pdConnectionString)
```
- **Refactored:**
```js
// Move the database connection inside the default function or use setup()/teardown() properly.
// If sql.open must be in init, consider using a single shared connection via setup().
// However, since k6 does not support sharing objects across VUs from setup(),
// the best practice is to open the connection inside the default function:

export default () => {
  const db = sql.open('postgres', pdConnectionString)
  // ... rest of the function
  db.close()
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
    'inserts': ['count>0'],
    'http_req_failed': ['rate<0.01'],
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
import { check } from 'k6'

// Inside default function:
let result
try {
  result = db.exec(
    `insert into rls_messages_authenticated (domain) values ('${
      domains[getRandomInt(0, 5)]
    }');`
  )
  check(result, {
    'insert succeeded': (r) => r !== null && r !== undefined,
  })
} catch (e) {
  check(null, { 'insert succeeded': () => false })
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
import { tagWithCurrentStageIndex } from 'k6/execution'

// Attach tags to metrics to allow filtering by operation type:
counterInserts.add(1, { operation: 'insert', table: 'rls_messages_authenticated' })

// If using custom metrics or trends for the DB exec, wrap with tags:
const dbExecTrend = new Trend('db_exec_duration', true)
const start = new Date()
db.exec(
  `insert into rls_messages_authenticated (domain) values ('${
    domains[getRandomInt(0, 5)]
  }');`
)
const finish = new Date()
dbExecTrend.add(finish - start, { operation: 'insert', table: 'rls_messages_authenticated' })
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
  },
}
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
    'iteration_duration': ['p(95)<200'], // e.g., 95% of iterations finish within 200ms
    'inserts': ['count>0'],            // e.g., ensure at least one insert succeeded
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

//... inside the default function

check(null, {
  'insert successful': () => {
    try {
      db.exec(
        `insert into rls_messages_authenticated (domain) values ('${domains[getRandomInt(0, 5)]}');`
      );
      return true;
    } catch (e) {
      return false;
    }
  }
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
counterInserts.add(1, { query: 'insert_message' });
```

---

## `script_287.js`

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
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
let res = http.get('https://quickpizza.grafana.com', {
  tags: { name: 'HomePage' },
});
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
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
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

---

## `script_288.js`

### `script_288.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [68, 73, 80, 88, 93, 100]
- **Snippet:**
```js
bearerToken = AuthUtil.getInstance().getBearerToken(customerEmail);
const response = checkoutResource.checkout();
const response = orderAmendmentResource.amendOrder();
const response = cartsResource.delete(reorderedIdCart);
```
- **Refactored:**
```js
import { check } from 'k6';

// Authorization
group('Authorization', () => {
  const response = AuthUtil.getInstance().getBearerToken(customerEmail);
  check(response, {
    'authorization succeeded': (r) => r && r.status >= 200 && r.status < 300,
  });
  bearerToken = response.json('access_token');
});

// Checkout
group('Checkout', () => {
  const checkoutResource = new CheckoutResource(idCart, customerEmail, bearerToken);
  const response = checkoutResource.checkout();
  check(response, {
    'checkout status is successful': (r) => r.status >= 200 && r.status < 300,
    'checkout response has orderReference': (r) => JSON.parse(r.body).data.attributes.orderReference !== undefined,
  });
  const responseJson = JSON.parse(response.body);
  orderReference = responseJson.data.attributes.orderReference;
});

// Start Order Amendment
group('Start Order Amendment', () => {
  const response = orderAmendmentResource.amendOrder();
  check(response, {
    'amend order status is successful': (r) => r.status >= 200 && r.status < 300,
    'amend order response has cart id': (r) => JSON.parse(r.body).data.id !== undefined,
  });
  const responseJson = JSON.parse(response.body);
  metrics['SAPI20_post_cart_reorder'].add(response.timings.duration);
  reorderedIdCart = responseJson.data.id;
});

// Cancel Order Amendment
group('Cancel Order Amendment', () => {
  const response = cartsResource.delete(reorderedIdCart);
  check(response, {
    'delete cart status is successful': (r) => r.status >= 200 && r.status < 300,
  });
  metrics['SAPI21_delete_carts'].add(response.timings.duration);
});
```

**Smell 4: Not using tags**

- **Lines:** [68, 73, 80, 82, 88, 89, 93, 100, 101]
- **Snippet:**
```js
const response = checkoutResource.checkout();
const response = orderAmendmentResource.amendOrder();
metrics['SAPI20_post_cart_reorder'].add(response.timings.duration);
const response = cartsResource.delete(reorderedIdCart);
metrics['SAPI21_delete_carts'].add(response.timings.duration);
```
- **Refactored:**
```js
// Example assuming resource methods accept k6 request params/options.
group('Checkout', () => {
  const tags = { name: 'SAPI22_post_checkout', flow: 'Checkout', endpoint: 'checkout' };
  const checkoutResource = new CheckoutResource(idCart, customerEmail, bearerToken);
  const response = checkoutResource.checkout({ tags });
  metrics['SAPI22_post_checkout'].add(response.timings.duration, tags);
});

group('Start Order Amendment', () => {
  const tags = { name: 'SAPI20_post_cart_reorder', flow: 'Start Order Amendment', endpoint: 'cart_reorder' };
  const response = orderAmendmentResource.amendOrder({ tags });
  const responseJson = JSON.parse(response.body);
  metrics['SAPI20_post_cart_reorder'].add(response.timings.duration, tags);
  reorderedIdCart = responseJson.data.id;
});

group('Cancel Order Amendment', () => {
  const tags = { name: 'SAPI21_delete_carts', flow: 'Cancel Order Amendment', endpoint: 'delete_carts' };
  const response = cartsResource.delete(reorderedIdCart, { tags });
  metrics['SAPI21_delete_carts'].add(response.timings.duration, tags);
});
```

### `script_288.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [73, 80, 88, 93, 100]
- **Snippet:**
```js
const response = checkoutResource.checkout();
const responseJson = JSON.parse(response.body);
orderReference = responseJson.data.attributes.orderReference;
```
- **Refactored:**
```js
import { check } from 'k6';
//...
const response = checkoutResource.checkout();
check(response, {
  'checkout status is 200': (r) => r.status === 200,
  'order reference exists': (r) => r.json('data.attributes.orderReference') !== undefined,
});
const responseJson = response.json();
orderReference = responseJson.data.attributes.orderReference;
```

**Smell 4: Not using tags**

- **Lines:** [80, 82, 88, 89, 100, 101]
- **Snippet:**
```js
const response = orderAmendmentResource.amendOrder();
metrics['SAPI20_post_cart_reorder'].add(response.timings.duration);
```
- **Refactored:**
```js
// The underlying http call in the resource class should be tagged.
// Example inside orderAmendmentResource.amendOrder():
// http.post(url, payload, { tags: { name: 'SAPI20_post_cart_reorder' } });

// The custom metric logic can then be removed from the script, and
// thresholds can be applied directly to built-in k6 metrics:
// 'http_req_duration{name:SAPI20_post_cart_reorder}': ['avg<300']
```

---

## `script_289.js`

### `script_289.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [11]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};

export default function () {
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
        tags: { name: 'UserSearch' },
    },
});
```

### `script_289.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [11]
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
  },
};

export default function () {
  // test logic
}
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
    tags: {
      name: 'UserSearch',
      endpoint: 'user_search'
    }
  }
});
```

### `script_289.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [3]
- **Snippet:**
```js
The script does not export an `options` object with a `thresholds` property, which is crucial for defining pass/fail criteria.
```
- **Refactored:**
```js
import http from 'k6/http';
import { check } from 'k6';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
};

//... rest of the script
```

**Smell 3: Not checking requests**

- **Lines:** [24]
- **Snippet:**
```js
const responses = http.batch(request);
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
for (let req = 0; req < countRequest; req++) {
    request.push({
        method: 'GET',
        url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
        params: {
            headers: params.headers,
            tags: { name: 'UserSearch' },
        }
    });
}
```

---

## `script_290.js`

### `script_290.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [54, 61]
- **Snippet:**
```js
const response = cartsResource.get(idCart, ['items']);
...
const response = cartsResource.removeItem(idCart, skuForRemove);
```
- **Refactored:**
```js
import { check } from 'k6';

// Inside 'Gets customer cart info' group:
group('Gets customer cart info', () => {
  const response = cartsResource.get(idCart, ['items']);
  check(response, {
    'get cart status is 200': (r) => r.status === 200,
    'get cart body is not empty': (r) => r.body && r.body.length > 0,
  });
  const bodyJson = JSON.parse(response.body);
  skuForRemove = bodyJson.included[0].attributes.sku;
});

// Inside testConfiguration.group group:
group(testConfiguration.group, () => {
  const response = cartsResource.removeItem(idCart, skuForRemove);
  check(response, {
    'remove item status is 204': (r) => r.status === 204,
  });
  metrics[testConfiguration.metrics[0]].add(response.timings.duration);
});
```

### `script_290.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [54, 61]
- **Snippet:**
```js
const response = cartsResource.get(idCart, ['items']);
...
const response = cartsResource.removeItem(idCart, skuForRemove);
```
- **Refactored:**
```js
import { check, fail, group } from 'k6';

// ...

group('Gets customer cart info', () => {
  const response = cartsResource.get(idCart, ['items']);

  const isValid = check(response, {
    'get cart status is 200': (r) => r.status === 200,
    'get cart response has body': (r) => !!r.body,
  });

  if (!isValid) {
    fail(`Failed to get cart info for cart ${idCart}`);
  }

  const bodyJson = JSON.parse(response.body);
  skuForRemove = bodyJson.included[0].attributes.sku;
});

group(testConfiguration.group, () => {
  const response = cartsResource.removeItem(idCart, skuForRemove);

  const isValid = check(response, {
    'remove cart item status is successful': (r) => r.status >= 200 && r.status < 300,
  });

  if (!isValid) {
    fail(`Failed to remove item ${skuForRemove} from cart ${idCart}`);
  }

  metrics[testConfiguration.metrics[0]].add(response.timings.duration);
});
```

**Smell 4: Not using tags**

- **Lines:** [54, 61, 63]
- **Snippet:**
```js
const response = cartsResource.get(idCart, ['items']);
...
const response = cartsResource.removeItem(idCart, skuForRemove);
...
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
group('Gets customer cart info', () => {
  const response = cartsResource.get(idCart, ['items'], {
    tags: {
      name: 'GetCustomerCartInfo',
      endpoint: 'GET /carts/{id}',
      test_id: testConfiguration.id,
      flow: testConfiguration.group,
    },
  });

  const bodyJson = JSON.parse(response.body);
  skuForRemove = bodyJson.included[0].attributes.sku;
});

group(testConfiguration.group, () => {
  const response = cartsResource.removeItem(idCart, skuForRemove, {
    tags: {
      name: 'RemoveCartItem',
      endpoint: 'DELETE /carts/{id}/items/{sku}',
      test_id: testConfiguration.id,
      flow: testConfiguration.group,
    },
  });

  metrics[testConfiguration.metrics[0]].add(response.timings.duration, {
    name: 'RemoveCartItem',
    endpoint: 'DELETE /carts/{id}/items/{sku}',
    test_id: testConfiguration.id,
    flow: testConfiguration.group,
  });
});
```

### `script_290.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [54, 61]
- **Snippet:**
```js
const response = cartsResource.get(idCart, ['items']);
//...
const response = cartsResource.removeItem(idCart, skuForRemove);
```
- **Refactored:**
```js
import { check } from 'k6';
//...
const getResponse = cartsResource.get(idCart, ['items']);
check(getResponse, { 'get cart status is 200': (r) => r.status === 200 });
//...
const removeItemResponse = cartsResource.removeItem(idCart, skuForRemove);
check(removeItemResponse, { 'remove item status is 204': (r) => r.status === 204 });
```

**Smell 4: Not using tags**

- **Lines:** [54, 61]
- **Snippet:**
```js
const response = cartsResource.get(idCart, ['items']);
//...
const response = cartsResource.removeItem(idCart, skuForRemove);
```
- **Refactored:**
```js
// This refactoring assumes the resource methods are updated to accept k6 http params.
const response = cartsResource.get(idCart, ['items'], { tags: { name: 'GetCartInfo' } });
//...
const response = cartsResource.removeItem(idCart, skuForRemove, { tags: { name: 'RemoveCartItem' } });
```

---

## `script_291.js`

### `script_291.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
- **Snippet:**
```js
const payload = JSON.stringify({
  meta: { ... },
  webhook_meta: { ... },
});
```
- **Refactored:**
```js
// Move JSON.stringify inside the default function to avoid heavy computation in init context
export default function () {
  const payload = JSON.stringify({
    meta: {
      user_id: "b66adzazdazdazdazd7bd06-2753-44ae-adazd8848f60-26df8d351d0f",
      resource_id: "b66adzazdazdazdazd7bd06-2753-44ae-adazd8848f60-26df8d351d0f",
      status: "pos",
    },
    webhook_meta: {
      client_id: "hello-this-is-aclient-id",
      webhook_config_id: "config-id",
      webhook_msg_timestamp: 1729651095,
      webhook_msg_uuid: "b66adzazdazdazdazd7bd06-2753-44ae-adazd8848f60-26df8d351d0f",
    },
  });
  const res = http.post("http://localhost:3000/api", payload, { headers });
  check(res, { "status is 200": (r) => r.status === 200 });
}
```

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
    'checks': ['rate>0.99'],
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
  tags: { name: "PostAPI" },
});
check(res, { "status is 200": (r) => r.status === 200 }, { tags: { name: "PostAPI" } });
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
const res = http.post("http://localhost:3000/api", payload, {
  headers,
  tags: { name: "PostAPI", endpoint: "/api" },
});
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
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
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
  tags: { name: 'ApiPost' },
});
```

---

## `script_292.js`

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
		http_req_duration: ['p(95)<500'],
		http_req_failed: ['rate<0.01'],
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
	tags: { name: 'GetRoutine' },
});
```

### `script_292.js` — CHATGPT

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
        'http_req_duration{name:RoutineAPI}': ['p(95)<500'],
        checks: ['rate>0.99'],
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
let commentRes = http.get(baseUrl, {
    headers: headers,
    tags: {
        name: 'RoutineAPI',
        endpoint: 'k12_routine',
        flow: 'routine_lookup'
    }
});
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
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
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
            name: 'GetRoutine',
        },
    });
```

---

## `script_295.js`

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
    'http_req_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
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
const res = http.put(url, payload, { headers, tags: { name: 'UpdateUser' } });
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
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.95'],
    response_time: ['p(95)<500'],
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
const params = {
  headers,
  tags: {
    name: 'UpdateUser',
    endpoint: '/v2/user/{username}',
    flow: 'user_update',
  },
};

const res = http.put(url, payload, params);
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
    'http_req_failed': ['rate<0.01'],        // Fail test if error rate > 1%
    'http_req_duration': ['p(95)<500'],      // 95% of requests must complete below 500ms
    'checks{Status is 200}': ['rate>0.95'],  // More than 95% of requests must be successful
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
const res = http.put(url, payload, {
    headers: headers,
    tags: { name: 'UpdateUser' },
  });
```

---

## `script_296.js`

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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [11, 14, 17]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
...
http.get('https://quickpizza.grafana.com/contacts.php');
...
http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
import { check, sleep } from 'k6';

// inside default function:
const res1 = http.get('https://quickpizza.grafana.com/test.k6.io/');
check(res1, { 'test.k6.io status 200': (r) => r.status === 200 });
sleep(1);
const res2 = http.get('https://quickpizza.grafana.com/contacts.php');
check(res2, { 'contacts status 200': (r) => r.status === 200 });
sleep(2);
const res3 = http.get('https://quickpizza.grafana.com/news.php');
check(res3, { 'news status 200': (r) => r.status === 200 });
sleep(2);
```

**Smell 4: Not using tags**

- **Lines:** [11, 14, 17]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
...
http.get('https://quickpizza.grafana.com/contacts.php');
...
http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/', { tags: { name: 'Home' } });
...
http.get('https://quickpizza.grafana.com/contacts.php', { tags: { name: 'Contacts' } });
...
http.get('https://quickpizza.grafana.com/news.php', { tags: { name: 'News' } });
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
    'http_req_duration{name:Home}': ['p(95)<500'],
    'http_req_duration{name:Contacts}': ['p(95)<500'],
    'http_req_duration{name:News}': ['p(95)<500'],
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
import { check, sleep } from 'k6';

export default () => {
  const homeRes = http.get('https://quickpizza.grafana.com/test.k6.io/', { tags: { name: 'Home' } });
  check(homeRes, {
    'Home status is 200': (r) => r.status === 200,
  });
  sleep(1);

  const contactsRes = http.get('https://quickpizza.grafana.com/contacts.php', { tags: { name: 'Contacts' } });
  check(contactsRes, {
    'Contacts status is 200': (r) => r.status === 200,
  });
  sleep(2);

  const newsRes = http.get('https://quickpizza.grafana.com/news.php', { tags: { name: 'News' } });
  check(newsRes, {
    'News status is 200': (r) => r.status === 200,
  });
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
  http.get('https://quickpizza.grafana.com/test.k6.io/', { tags: { name: 'Home', flow: 'browse' } });
  sleep(1);

  http.get('https://quickpizza.grafana.com/contacts.php', { tags: { name: 'Contacts', flow: 'browse' } });
  sleep(2);

  http.get('https://quickpizza.grafana.com/news.php', { tags: { name: 'News', flow: 'browse' } });
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
// ...
http.get('https://quickpizza.grafana.com/contacts.php');
// ...
http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const res1 = http.get('https://quickpizza.grafana.com/test.k6.io/');
check(res1, { 'Homepage status is 200': (r) => r.status === 200 });
// ...
const res2 = http.get('https://quickpizza.grafana.com/contacts.php');
check(res2, { 'Contacts status is 200': (r) => r.status === 200 });
// ...
const res3 = http.get('https://quickpizza.grafana.com/news.php');
check(res3, { 'News status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [11, 14, 17]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
// ...
http.get('https://quickpizza.grafana.com/contacts.php');
// ...
http.get('https://quickpizza.grafana.com/news.php');
```
- **Refactored:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/', {
  tags: { name: 'Homepage' },
});
// ...
http.get('https://quickpizza.grafana.com/contacts.php', {
  tags: { name: 'Contacts' },
});
// ...
http.get('https://quickpizza.grafana.com/news.php', {
  tags: { name: 'News' },
});
```

---

