# k6 Performance Smell Analysis
Generated: 08/06/2026 12:07

S1 = Costly init | S2 = No thresholds | S3 = No checks | S4 = No tags

| File | LLM | S1 | S2 | S3 | S4 | Lines with smells |
|------|-----|:--:|:--:|:--:|:--:|-------------------|
| `script_01.js` | claude | x | x | x | x | S1:L22, S1:L23, S2:L26, S2:L27, S2:L28, S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S3:L52, S3:L53, S3:L54, S3:L82, S3:L83, S3:L84, S4:L52, S4:L53, S4:L54, S4:L82, S4:L83, S4:L84 |
|  | chatgpt | x | x | x | x | S1:L22, S1:L23, S2:L26, S2:L27, S2:L28, S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S3:L52, S3:L53, S3:L54, S3:L82, S3:L83, S3:L84, S4:L52, S4:L53, S4:L54, S4:L82, S4:L83, S4:L84 |
|  | gemini | x | x | x | x | S1:L22, S1:L23, S2:L26, S2:L27, S2:L28, S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S3:L56, S3:L86, S4:L52, S4:L82 |
| `script_02.js` | claude |  | x |  | x | S2:L6, S2:L32, S2:L58, S2:L104, S4:L183, S4:L193, S4:L205, S4:L228, S4:L238, S4:L250 |
|  | chatgpt |  | x |  | x | S2:L32, S2:L33, S2:L34, S2:L35, S2:L36, S2:L37, S2:L38, S2:L39, S2:L40, S2:L41, S2:L42, S2:L43, S2:L44, S2:L45, S2:L46, S2:L47, S2:L48, S2:L49, S2:L50, S2:L51, S2:L52, S2:L53, S2:L54, S2:L55, S4:L183, S4:L193, S4:L205, S4:L228, S4:L238, S4:L250 |
|  | gemini |  | x |  | x | S2:L6, S2:L32, S2:L58, S2:L104, S4:L183, S4:L193, S4:L205, S4:L228, S4:L238, S4:L250 |
| `script_03.js` | claude |  | x |  | x | S2:L27, S2:L31, S4:L60, S4:L85, S4:L103, S4:L128 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x |  | x | S1:L38, S2:L27, S2:L31, S4:L60, S4:L85, S4:L103, S4:L128 |
| `script_04.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S3:L22, S3:L24, S3:L26, S4:L22, S4:L24, S4:L26 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S3:L22, S3:L24, S3:L26, S4:L22, S4:L24, S4:L26 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S3:L22, S3:L24, S3:L26, S4:L22, S4:L24, S4:L26 |
| `script_05.js` | claude |  | x | x | x | S2:L7, S2:L8, S2:L9, S3:L29, S3:L31, S3:L33, S4:L29, S4:L31, S4:L33 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L26, S3:L29, S3:L31, S3:L33, S4:L17, S4:L18, S4:L19, S4:L29, S4:L31, S4:L33 |
|  | gemini |  | x | x | x | S2:L7, S2:L8, S2:L9, S3:L29, S3:L31, S3:L33, S4:L29, S4:L31, S4:L33 |
| `script_06.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L16, S3:L18, S3:L20, S4:L16, S4:L18, S4:L20 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L16, S3:L18, S3:L20, S4:L16, S4:L18, S4:L20 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L16, S3:L18, S3:L20, S4:L16, S4:L18, S4:L20 |
| `script_07.js` | claude | x | x | x | x | S1:L22, S2:L7, S2:L8, S2:L9, S2:L10, S3:L48, S3:L49, S3:L50, S4:L48 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x | x | x | S1:L22, S2:L7, S2:L8, S2:L9, S2:L10, S3:L48, S4:L48 |
| `script_08.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L11, S4:L11 |
|  | chatgpt | x | x | x | x | S1:L4, S3:L11, S4:L11 |
|  | gemini | x | x | x | x | S1:L4, S2:L1, S2:L13, S3:L11, S4:L11 |
| `script_09.js` | claude |  |  | x | x | S3:L70, S3:L71, S3:L72, S3:L74, S3:L88, S3:L89, S3:L90, S3:L91, S3:L92, S4:L70, S4:L71, S4:L72, S4:L88, S4:L89, S4:L90, S4:L91, S4:L92 |
|  | chatgpt |  |  | x | x | S3:L70, S3:L71, S3:L72, S3:L74, S3:L88, S3:L89, S3:L90, S3:L91, S3:L92, S4:L70, S4:L71, S4:L72, S4:L74, S4:L88, S4:L89, S4:L90, S4:L91, S4:L92 |
|  | gemini |  |  | x | x | S3:L70, S3:L71, S3:L72, S3:L74, S4:L70, S4:L71, S4:L72 |
| `script_10.js` | claude |  | x |  | x | S2:L16, S4:L29, S4:L92, S4:L132, S4:L178, S4:L217, S4:L260, S4:L328, S4:L401, S4:L501, S4:L567, S4:L633, S4:L700, S4:L766, S4:L832, S4:L898, S4:L967, S4:L1035, S4:L1108, S4:L1176, S4:L1244, S4:L1328, S4:L1389, S4:L1450, S4:L1512, S4:L1573, S4:L1634, S4:L1695, S4:L1759, S4:L1827, S4:L1900, S4:L1968, S4:L2027, S4:L2077, S4:L2128, S4:L2179, S4:L2231, S4:L2282, S4:L2333, S4:L2384, S4:L2438, S4:L2506, S4:L2574, S4:L2633, S4:L2683, S4:L2734, S4:L2785, S4:L2837, S4:L2888, S4:L2939, S4:L2990, S4:L3044, S4:L3112, S4:L3185, S4:L3245, S4:L3304, S4:L3354, S4:L3405, S4:L3456, S4:L3508, S4:L3559, S4:L3610, S4:L3661, S4:L3715, S4:L3775, S4:L3825, S4:L3878, S4:L3931, S4:L3985, S4:L4038, S4:L4091, S4:L4144, S4:L4200, S4:L4268, S4:L4350, S4:L4411, S4:L4472, S4:L4534, S4:L4595, S4:L4656, S4:L4717 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L16, S4:L33 |
| `script_100.js` | claude |  |  |  |  | - |
|  | chatgpt |  | x |  | x | S4:L15, S4:L30, S4:L43, S4:L58, S4:L71, S4:L85 |
|  | gemini |  | x |  | x | S2:L1, S4:L15, S4:L30, S4:L43, S4:L58, S4:L71, S4:L85 |
| `script_101.js` | claude |  |  | x |  | S3:L107, S3:L108, S3:L109, S3:L110, S3:L111, S3:L112, S3:L113, S3:L114, S3:L115, S3:L116, S3:L117, S3:L118, S3:L119, S3:L120, S3:L121, S3:L122, S3:L123, S3:L124, S3:L125, S3:L126 |
|  | chatgpt |  |  | x |  | S3:L107, S3:L108, S3:L109, S3:L110, S3:L111, S3:L112, S3:L113, S3:L114, S3:L115, S3:L116, S3:L117, S3:L118, S3:L119, S3:L120, S3:L121, S3:L122, S3:L123, S3:L124, S3:L125, S3:L126 |
|  | gemini |  |  | x |  | S3:L107, S3:L126 |
| `script_102.js` | claude |  | x |  | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L6, S4:L19, S4:L32, S4:L41, S4:L50, S4:L58 |
|  | chatgpt |  | x | x | x | S3:L57, S3:L58, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S3:L64, S3:L65, S3:L66, S4:L19, S4:L32, S4:L41, S4:L50, S4:L58, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63, S4:L64, S4:L65 |
|  | gemini |  | x | x | x | S2:L1, S3:L58, S3:L67, S4:L19, S4:L32, S4:L41, S4:L50, S4:L58 |
| `script_103.js` | claude |  |  | x | x | S3:L21, S3:L22, S3:L28, S4:L17, S4:L21, S4:L22, S4:L28 |
|  | chatgpt |  |  | x | x | S3:L21, S3:L22, S3:L28, S4:L17, S4:L21, S4:L22, S4:L28 |
|  | gemini |  |  | x | x | S3:L21, S3:L22, S3:L28, S4:L17, S4:L21, S4:L22, S4:L28 |
| `script_104.js` | claude |  |  |  | x | S4:L15, S4:L16, S4:L17, S4:L18 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  | x | S4:L15, S4:L16 |
| `script_105.js` | claude |  | x |  | x | S2:L13, S2:L14, S2:L15, S2:L16, S4:L56, S4:L57, S4:L58, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63, S4:L64, S4:L65, S4:L66, S4:L67, S4:L68, S4:L69, S4:L70, S4:L71, S4:L72, S4:L73 |
|  | chatgpt |  |  |  | x | S4:L44, S4:L45, S4:L46, S4:L47, S4:L48, S4:L56, S4:L57, S4:L58, S4:L59, S4:L60, S4:L62, S4:L63, S4:L64, S4:L65, S4:L67, S4:L68, S4:L69, S4:L70, S4:L71, S4:L75 |
|  | gemini |  | x |  | x | S2:L13, S2:L14, S2:L15, S2:L16, S4:L56, S4:L57, S4:L58, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63, S4:L64, S4:L65, S4:L66, S4:L67, S4:L68, S4:L69, S4:L70, S4:L71, S4:L72, S4:L73 |
| `script_106.js` | claude | x | x |  | x | S4:L57, S4:L58, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63, S4:L64, S4:L65, S4:L66, S4:L67, S4:L68, S4:L69, S4:L70, S4:L71, S4:L72, S4:L73, S4:L74, S4:L76, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S1:L20, S1:L21, S1:L22, S1:L23, S1:L24, S1:L25, S1:L26, S1:L27, S1:L28, S1:L29, S1:L30, S1:L31, S1:L32, S1:L33, S1:L34, S1:L35, S1:L36, S1:L37, S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L49, S1:L50, S1:L51, S1:L52, S1:L53, S1:L54, S1:L55 |
|  | chatgpt |  |  |  | x | S4:L45, S4:L46, S4:L47, S4:L48, S4:L49, S4:L57, S4:L58, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63, S4:L64, S4:L65, S4:L66, S4:L67, S4:L68, S4:L69, S4:L70, S4:L71, S4:L72, S4:L73, S4:L74 |
|  | gemini |  | x |  | x | S2:L14, S2:L15, S2:L16, S2:L17, S4:L57, S4:L58, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63, S4:L64, S4:L65, S4:L66, S4:L67, S4:L68, S4:L69, S4:L70, S4:L71, S4:L72, S4:L73, S4:L74 |
| `script_107.js` | claude |  |  | x | x | S3:L21, S3:L22, S3:L28, S4:L17, S4:L21, S4:L22, S4:L28 |
|  | chatgpt |  |  | x | x | S3:L21, S3:L22, S3:L28, S4:L17, S4:L21, S4:L22, S4:L28 |
|  | gemini |  |  | x | x | S3:L21, S3:L22, S3:L28, S4:L17, S4:L21, S4:L22, S4:L28 |
| `script_108.js` | claude |  |  | x | x | S3:L21, S3:L22, S3:L28, S4:L17, S4:L21, S4:L22, S4:L28 |
|  | chatgpt |  |  | x | x | S3:L21, S3:L22, S3:L28, S4:L17, S4:L21, S4:L22, S4:L28 |
|  | gemini |  |  | x | x | S3:L21, S3:L22, S3:L28, S4:L17, S4:L21, S4:L22, S4:L28 |
| `script_109.js` | claude |  | x |  |  | S2:L269, S2:L270, S2:L271 |
|  | chatgpt |  | x |  | x | S2:L269, S2:L270, S2:L271, S4:L254, S4:L255, S4:L256, S4:L257, S4:L258, S4:L259, S4:L260 |
|  | gemini |  | x |  |  | - |
| `script_11.js` | claude |  |  | x | x | S3:L99, S3:L106, S3:L132, S3:L133, S3:L134, S3:L138, S3:L139, S3:L140, S3:L146, S3:L154, S3:L155, S3:L156, S3:L162, S3:L163, S3:L164, S3:L196, S3:L197, S3:L198, S3:L204, S3:L205, S3:L206, S3:L213, S3:L219, S3:L220, S3:L221, S3:L229, S3:L233, S3:L234, S3:L262, S3:L263, S3:L264, S3:L269, S3:L270, S3:L271, S3:L302, S3:L310, S3:L311, S3:L312, S3:L319, S3:L327, S3:L328, S3:L334, S3:L341, S3:L342, S3:L343, S3:L348, S3:L349, S3:L350, S3:L376, S3:L383, S3:L384, S3:L385, S3:L390, S3:L396, S3:L397, S3:L398, S3:L404, S3:L411, S3:L412, S3:L413, S3:L419, S3:L426, S3:L427, S3:L428, S4:L99, S4:L132, S4:L138, S4:L146, S4:L162, S4:L196, S4:L204, S4:L213, S4:L229, S4:L262, S4:L269, S4:L302, S4:L319, S4:L334, S4:L348, S4:L376, S4:L390, S4:L404, S4:L419 |
|  | chatgpt |  |  | x | x | S3:L99, S3:L108, S3:L132, S3:L134, S3:L138, S3:L140, S3:L146, S3:L156, S3:L162, S3:L164, S3:L196, S3:L198, S3:L204, S3:L206, S3:L213, S3:L221, S3:L229, S3:L234, S3:L262, S3:L264, S3:L269, S3:L271, S3:L302, S3:L312, S3:L319, S3:L328, S3:L334, S3:L343, S3:L348, S3:L350, S3:L376, S3:L385, S3:L390, S3:L399, S3:L404, S3:L414, S3:L419, S3:L429, S4:L99, S4:L105, S4:L132, S4:L138, S4:L153, S4:L162, S4:L196, S4:L204, S4:L218, S4:L229, S4:L262, S4:L269, S4:L309, S4:L325, S4:L340, S4:L348, S4:L382, S4:L396, S4:L411, S4:L426 |
|  | gemini |  |  | x | x | S3:L132, S3:L134, S4:L99, S4:L132, S4:L138, S4:L146, S4:L162 |
| `script_110.js` | claude |  |  | x | x | S3:L54, S3:L55, S3:L56, S3:L57, S4:L20, S4:L42, S4:L54, S4:L63 |
|  | chatgpt |  |  | x | x | S3:L54, S4:L20, S4:L42, S4:L54, S4:L63 |
|  | gemini |  |  | x | x | S3:L54, S4:L20, S4:L42, S4:L54, S4:L63 |
| `script_111.js` | claude |  |  |  | x | S4:L19, S4:L27, S4:L34, S4:L41 |
|  | chatgpt |  |  |  | x | S4:L19, S4:L20, S4:L27, S4:L28, S4:L34, S4:L35, S4:L41, S4:L44 |
|  | gemini |  |  |  | x | S4:L20, S4:L28, S4:L35, S4:L44 |
| `script_112.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L57, S3:L71, S4:L57, S4:L71 |
| `script_113.js` | claude |  |  |  | x | S4:L66, S4:L87 |
|  | chatgpt |  |  |  | x | S4:L66, S4:L87 |
|  | gemini |  |  | x | x | S3:L75, S3:L87, S4:L66, S4:L87 |
| `script_114.js` | claude |  |  |  | x | S4:L46, S4:L67 |
|  | chatgpt |  |  |  | x | S4:L46, S4:L67 |
|  | gemini |  |  | x | x | S3:L55, S3:L67, S4:L46, S4:L67 |
| `script_115.js` | claude |  | x |  |  | S2:L93, S2:L94, S2:L95 |
|  | chatgpt |  | x |  |  | S2:L93, S2:L94, S2:L95 |
|  | gemini |  | x |  |  | S2:L26 |
| `script_116.js` | claude |  |  |  | x | S4:L43, S4:L44, S4:L45, S4:L55, S4:L56, S4:L57, S4:L58, S4:L59, S4:L60, S4:L71, S4:L72, S4:L73, S4:L74, S4:L75, S4:L76, S4:L77 |
|  | chatgpt |  |  |  | x | S4:L43, S4:L46, S4:L47, S4:L55, S4:L61, S4:L64, S4:L65, S4:L66, S4:L71, S4:L78 |
|  | gemini |  |  |  | x | S4:L43, S4:L55, S4:L71 |
| `script_117.js` | claude |  | x |  |  | S2:L1, S2:L191 |
|  | chatgpt |  | x |  |  | S2:L5, S2:L6, S2:L11 |
|  | gemini |  |  |  | x | S4:L54, S4:L82 |
| `script_118.js` | claude | x |  |  |  | S1:L14 |
|  | chatgpt | x |  |  |  | S1:L13, S1:L14 |
|  | gemini | x |  |  |  | S1:L14 |
| `script_119.js` | claude |  | x |  |  | S2:L1, S2:L154 |
|  | chatgpt |  | x |  |  | S2:L32, S2:L152 |
|  | gemini |  | x |  |  | S2:L31 |
| `script_12.js` | claude | x |  |  | x | S1:L21, S1:L22, S1:L23, S1:L24, S1:L27, S1:L28, S1:L29, S1:L30, S1:L31, S1:L32, S1:L33, S1:L34, S1:L36, S4:L43, S4:L50, S4:L64, S4:L72, S4:L110, S4:L122, S4:L134, S4:L141, S4:L148, S4:L158, S4:L170, S4:L176, S4:L195, S4:L210 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x |  |  | x | S1:L36, S4:L134, S4:L141, S4:L148, S4:L195, S4:L210 |
| `script_120.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x |  | S3:L167 |
| `script_121.js` | claude |  | x |  |  | S2:L117, S2:L118, S2:L119 |
|  | chatgpt |  | x |  | x | S2:L117, S2:L118, S2:L119, S4:L102, S4:L103, S4:L104, S4:L105, S4:L106, S4:L107, S4:L108 |
|  | gemini |  | x |  |  | S2:L117 |
| `script_122.js` | claude |  |  |  | x | S4:L36, S4:L74, S4:L101 |
|  | chatgpt |  |  |  | x | S4:L36, S4:L37, S4:L38, S4:L39, S4:L43, S4:L54, S4:L74, S4:L75, S4:L76, S4:L77, S4:L79, S4:L90, S4:L101, S4:L102, S4:L103, S4:L104, S4:L106, S4:L110 |
|  | gemini |  |  |  | x | S4:L36, S4:L74, S4:L101 |
| `script_123.js` | claude |  |  |  | x | S4:L64, S4:L65, S4:L66, S4:L67, S4:L68, S4:L87, S4:L88, S4:L89, S4:L90, S4:L91 |
|  | chatgpt |  |  |  | x | S4:L64, S4:L67, S4:L70, S4:L71, S4:L73, S4:L80, S4:L83, S4:L87, S4:L90, S4:L93 |
|  | gemini |  |  |  | x | S4:L64, S4:L70, S4:L71, S4:L80, S4:L83, S4:L87 |
| `script_124.js` | claude |  | x |  | x | S2:L7, S4:L12 |
|  | chatgpt |  | x | x | x | S2:L7, S3:L12, S3:L15, S4:L12 |
|  | gemini |  | x | x | x | S2:L1, S2:L6, S3:L12, S3:L15, S4:L12 |
| `script_125.js` | claude |  | x |  | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L12 |
|  | chatgpt |  | x |  | x | S2:L1, S2:L18, S4:L12, S4:L14 |
|  | gemini |  | x |  | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L12 |
| `script_126.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S3:L10, S3:L15, S4:L10, S4:L15 |
|  | chatgpt |  | x | x | x | S3:L10, S3:L15, S4:L10, S4:L12, S4:L15, S4:L17 |
|  | gemini |  | x | x | x | S2:L1, S2:L20, S3:L10, S3:L15, S4:L10, S4:L12, S4:L15, S4:L17 |
| `script_127.js` | claude |  |  |  | x | S4:L10, S4:L24 |
|  | chatgpt |  |  |  | x | S4:L10, S4:L12, S4:L24 |
|  | gemini |  | x |  | x | S2:L5, S4:L10, S4:L24 |
| `script_128.js` | claude |  |  |  | x | S4:L46, S4:L52 |
|  | chatgpt |  |  |  | x | S4:L46, S4:L52 |
|  | gemini |  |  |  | x | S4:L46, S4:L52 |
| `script_129.js` | claude |  |  |  | x | S4:L20, S4:L27 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  | x | S4:L20, S4:L27 |
| `script_13.js` | claude |  | x | x | x | S2:L15, S2:L16, S2:L17, S3:L30, S3:L93, S3:L140, S3:L200, S3:L250, S3:L303, S3:L356, S3:L410, S3:L463, S3:L516, S3:L569, S4:L30, S4:L93, S4:L140, S4:L200, S4:L250, S4:L303, S4:L356, S4:L410, S4:L463, S4:L516, S4:L569 |
|  | chatgpt |  | x |  | x | S2:L15, S2:L16, S2:L17, S4:L30, S4:L93, S4:L140, S4:L200, S4:L250, S4:L303, S4:L356, S4:L410, S4:L463, S4:L516, S4:L569 |
|  | gemini |  | x | x | x | S2:L15, S2:L16, S2:L17, S3:L69, S3:L71, S3:L74, S4:L30, S4:L31, S4:L33 |
| `script_130.js` | claude |  | x |  | x | S4:L14, S4:L22, S2:L7, S2:L8, S2:L9 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  | x | S4:L14, S4:L22 |
| `script_131.js` | claude |  |  |  | x | S4:L66, S4:L81 |
|  | chatgpt |  |  |  | x | S4:L66, S4:L67, S4:L73, S4:L81, S4:L87, S4:L101 |
|  | gemini |  |  |  | x | S4:L66, S4:L81 |
| `script_133.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S3:L10, S3:L15, S4:L10, S4:L15 |
|  | chatgpt |  | x | x | x | S3:L10, S3:L15, S4:L10, S4:L12, S4:L15, S4:L17 |
|  | gemini |  | x | x | x | S2:L7, S3:L10, S3:L15, S4:L12, S4:L17 |
| `script_134.js` | claude |  | x |  | x | S2:L7, S2:L8, S2:L9, S4:L14, S4:L22 |
|  | chatgpt |  |  |  | x | S4:L14, S4:L22 |
|  | gemini |  |  |  | x | S4:L14, S4:L22 |
| `script_136.js` | claude |  | x |  | x | S2:L1, S2:L27, S4:L9, S4:L22 |
|  | chatgpt |  | x |  | x | S2:L1, S2:L27, S4:L9, S4:L10, S4:L22, S4:L23 |
|  | gemini |  | x |  | x | S2:L1, S2:L27, S4:L9, S4:L22 |
| `script_137.js` | claude |  | x |  | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S4:L5 |
|  | chatgpt |  | x |  | x | S2:L4, S4:L5, S4:L6, S4:L7, S4:L10, S4:L11, S4:L12, S4:L13 |
|  | gemini |  | x | x | x | S2:L4, S3:L10, S3:L11, S3:L12, S3:L13, S4:L5, S4:L6, S4:L7 |
| `script_138.js` | claude |  | x |  |  | S2:L1, S2:L63 |
|  | chatgpt |  | x |  |  | S2:L16 |
|  | gemini |  | x |  |  | S2:L1 |
| `script_140.js` | claude |  |  | x | x | S4:L34, S4:L50, S3:L50, S3:L53 |
|  | chatgpt |  |  | x | x | S3:L50, S4:L34, S4:L40, S4:L43, S4:L50, S4:L53 |
|  | gemini |  |  | x | x | S3:L50, S4:L34, S4:L50 |
| `script_143.js` | claude |  | x |  | x | S2:L1, S2:L2, S2:L3, S2:L4, S4:L6, S4:L15 |
|  | chatgpt |  | x |  | x | S2:L4, S4:L6, S4:L8, S4:L15, S4:L17 |
|  | gemini |  | x |  | x | S2:L1, S2:L23, S4:L6, S4:L15 |
| `script_144.js` | claude |  | x |  | x | S2:L1, S2:L66, S4:L16, S4:L38 |
|  | chatgpt |  | x |  | x | S2:L1, S2:L66, S4:L16, S4:L30, S4:L31, S4:L32, S4:L38 |
|  | gemini |  | x |  | x | S4:L16, S4:L38 |
| `script_145.js` | claude |  | x |  | x | S2:L67, S2:L79, S2:L83, S2:L91, S2:L106, S4:L297, S4:L344, S4:L399, S4:L405, S4:L411, S4:L416, S4:L422, S4:L427, S4:L437, S4:L448, S4:L452, S4:L457, S4:L462, S4:L467, S4:L477, S4:L483 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L67, S2:L79, S2:L83, S2:L91, S2:L106, S3:L233, S3:L234, S4:L398, S4:L432 |
| `script_146.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x |  | x | x | S1:L6, S3:L34, S4:L34 |
| `script_148.js` | claude |  |  | x | x | S3:L23, S4:L23 |
|  | chatgpt |  |  | x | x | S3:L23, S4:L23 |
|  | gemini |  |  | x | x | S3:L23, S4:L23 |
| `script_149.js` | claude |  |  |  |  | - |
|  | chatgpt |  | x |  |  | S2:L9 |
|  | gemini |  | x |  |  | S2:L9 |
| `script_15.js` | claude |  |  | x | x | S4:L121, S4:L153, S4:L199, S4:L231, S4:L249, S4:L260, S4:L302, S4:L314, S4:L326, S4:L343, S3:L149, S3:L151, S3:L152, S3:L153, S3:L154, S3:L155, S3:L156, S3:L157, S3:L158, S3:L161, S3:L162, S3:L163, S3:L164, S3:L165, S3:L166, S3:L167, S3:L248, S3:L249, S3:L250, S3:L251, S3:L252, S3:L253, S3:L254, S3:L255, S3:L256, S3:L257 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L161, S3:L162, S3:L163, S3:L164, S3:L165, S3:L166, S3:L167, S4:L302, S4:L303, S4:L304, S4:L305, S4:L306 |
| `script_150.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19, S4:L22, S4:L23, S4:L24 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19 |
| `script_151.js` | claude |  |  |  | x | S4:L59 |
|  | chatgpt |  |  | x | x | S3:L14, S3:L18, S3:L19, S3:L20, S3:L21, S3:L22, S3:L23, S3:L24, S4:L14, S4:L15, S4:L16, S4:L59, S4:L61, S4:L62, S4:L63, S4:L64 |
|  | gemini |  |  |  | x | S4:L59 |
| `script_152.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L10, S4:L10 |
|  | chatgpt |  | x | x | x | S2:L6, S3:L10, S4:L10 |
|  | gemini |  | x | x | x | S2:L1, S2:L13, S3:L10, S4:L10 |
| `script_153.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10, S4:L12 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
| `script_154.js` | claude |  | x |  | x | S2:L33, S2:L34, S2:L35, S2:L36, S2:L37, S2:L38, S4:L41, S4:L42, S4:L43, S4:L44 |
|  | chatgpt |  | x |  | x | S2:L33, S2:L34, S2:L35, S2:L36, S2:L37, S2:L38, S4:L42, S4:L44 |
|  | gemini |  | x |  | x | S2:L33, S2:L34, S2:L35, S2:L36, S2:L37, S2:L38, S4:L42 |
| `script_155.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10, S4:L11 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10, S4:L11 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
| `script_156.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
| `script_157.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  |  | - |
| `script_158.js` | claude |  |  | x | x | S3:L53, S3:L58, S3:L59, S4:L47, S4:L53, S4:L58 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L53, S3:L58, S3:L59, S4:L53, S4:L58, S4:L59 |
| `script_16.js` | claude | x | x |  |  | S1:L18, S2:L5, S2:L6, S2:L7, S2:L8 |
|  | chatgpt |  | x | x | x | S2:L5, S2:L6, S2:L7, S2:L8, S3:L35, S3:L36, S3:L37, S3:L38, S3:L39, S3:L40, S3:L41, S3:L43, S3:L44, S4:L25, S4:L26, S4:L27, S4:L28, S4:L29, S4:L30, S4:L31, S4:L35, S4:L36, S4:L37, S4:L38, S4:L39, S4:L40, S4:L41 |
|  | gemini |  | x |  |  | S2:L5, S2:L6, S2:L7, S2:L8 |
| `script_160.js` | claude |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L14 |
|  | chatgpt |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L14, S4:L16, S4:L17, S4:L18 |
|  | gemini |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L14 |
| `script_161.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S3:L7, S4:L7 |
|  | chatgpt |  | x | x | x | S2:L6, S3:L7, S4:L7 |
|  | gemini |  | x | x | x | S2:L1, S2:L14, S3:L7, S3:L11, S4:L7 |
| `script_162.js` | claude | x |  | x | x | S1:L45, S3:L57, S3:L58, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S3:L64, S3:L65, S3:L66, S3:L67, S4:L58, S4:L59, S4:L60, S4:L61 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  | x | S4:L62, S4:L65, S4:L66, S4:L69, S4:L70 |
| `script_163.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L21 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L21, S4:L24, S4:L25, S4:L26 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L21 |
| `script_165.js` | claude | x |  | x | x | S1:L25, S1:L26, S1:L27, S1:L28, S3:L43, S3:L44, S3:L45, S3:L46, S3:L47, S3:L48, S4:L43, S4:L44, S4:L45, S4:L46, S4:L47, S4:L48 |
|  | chatgpt |  |  | x | x | S3:L43, S3:L44, S3:L45, S3:L46, S3:L47, S3:L48, S4:L43, S4:L44, S4:L45, S4:L46, S4:L47, S4:L48, S4:L50 |
|  | gemini | x |  | x | x | S1:L25, S1:L26, S1:L27, S1:L28, S3:L43, S3:L50, S4:L50 |
| `script_166.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L12, S3:L13, S3:L14, S3:L15, S3:L16, S3:L17, S3:L24, S3:L25, S3:L26, S4:L12, S4:L13, S4:L14, S4:L15, S4:L16, S4:L17 |
|  | chatgpt |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L12, S3:L13, S3:L14, S3:L15, S3:L16, S3:L17, S3:L24, S3:L25, S3:L26, S4:L12, S4:L13, S4:L14, S4:L15, S4:L16, S4:L17 |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L12, S3:L13, S3:L14, S3:L15, S3:L16, S3:L17, S3:L24, S3:L25, S3:L26, S4:L12, S4:L13, S4:L14, S4:L15, S4:L16, S4:L17 |
| `script_167.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L22, S4:L23, S4:L24, S4:L25 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19, S4:L25 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19 |
| `script_168.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L11, S3:L12, S3:L13, S3:L14, S3:L15, S4:L11, S4:L12, S4:L13, S4:L14, S4:L15 |
|  | chatgpt |  | x |  |  | S2:L4, S2:L5, S2:L6, S2:L7 |
|  | gemini |  | x |  |  | S2:L4, S2:L5, S2:L6, S2:L7 |
| `script_17.js` | claude |  | x |  |  | S2:L6, S2:L7, S2:L8, S2:L9 |
|  | chatgpt |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L13, S4:L16, S4:L24, S4:L27, S4:L30, S4:L35 |
|  | gemini |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L13, S4:L16, S4:L24, S4:L27, S4:L30, S4:L35 |
| `script_170.js` | claude |  | x |  |  | S2:L4, S2:L5, S2:L6, S2:L7 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L11, S4:L14, S4:L15, S4:L16 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L11 |
| `script_172.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L12 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L12, S4:L14, S4:L15, S4:L16 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L12 |
| `script_173.js` | claude |  | x |  | x | S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L26 |
|  | chatgpt |  | x |  | x | S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L26 |
|  | gemini |  | x |  | x | S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L26 |
| `script_174.js` | claude |  |  |  | x | S4:L11 |
|  | chatgpt |  |  |  | x | S4:L11 |
|  | gemini |  |  |  | x | S4:L11 |
| `script_175.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S4:L13 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S4:L13, S4:L15, S4:L16, S4:L17 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S4:L13 |
| `script_176.js` | claude |  |  |  | x | S4:L63, S4:L64, S4:L65, S4:L66 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  | x | S4:L67, S4:L70, S4:L71, S4:L74, S4:L75 |
| `script_177.js` | claude |  |  |  | x | S4:L11 |
|  | chatgpt |  |  |  | x | S4:L11 |
|  | gemini |  |  |  | x | S4:L11 |
| `script_178.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19, S4:L22, S4:L23, S4:L24, S4:L25 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19, S4:L25 |
|  | gemini |  | x |  | x | S2:L5, S4:L19 |
| `script_180.js` | claude |  |  |  |  | - |
|  | chatgpt |  | x |  |  | S2:L9 |
|  | gemini |  | x |  |  | S2:L9 |
| `script_183.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L73, S3:L80, S3:L88, S3:L93, S3:L100, S4:L82, S4:L89, S4:L101 |
| `script_186.js` | claude |  |  | x | x | S3:L30, S3:L33, S4:L30 |
|  | chatgpt |  |  | x | x | S3:L30, S4:L30, S4:L33 |
|  | gemini |  |  | x | x | S3:L30, S4:L30 |
| `script_188.js` | claude |  | x | x | x | S2:L1, S2:L50, S3:L46, S4:L39, S4:L40, S4:L41, S4:L42, S4:L43, S4:L44, S4:L46 |
|  | chatgpt | x | x | x | x | S1:L18, S1:L19, S1:L20, S2:L22, S3:L46, S4:L39, S4:L40, S4:L41, S4:L42, S4:L43, S4:L44, S4:L46 |
|  | gemini |  | x | x | x | S2:L22, S3:L46, S4:L46 |
| `script_19.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x |  | x |  | S1:L110, S1:L112, S1:L120, S3:L128, S3:L132, S3:L136, S3:L140, S3:L144 |
| `script_190.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L11, S3:L12, S3:L13, S3:L14, S3:L15, S4:L11, S4:L12, S4:L13, S4:L14, S4:L15 |
|  | chatgpt |  | x |  |  | S2:L4, S2:L5, S2:L6, S2:L7 |
|  | gemini |  | x |  |  | S2:L4, S2:L5, S2:L6, S2:L7 |
| `script_192.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L31, S4:L32, S4:L33, S4:L34, S4:L35 |
|  | chatgpt |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L31, S4:L32, S4:L33, S4:L34, S4:L35, S4:L38, S4:L44, S4:L45, S4:L46, S4:L47, S4:L48, S4:L49, S4:L50, S4:L51, S4:L52, S4:L53 |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L31, S4:L32, S4:L33, S4:L34, S4:L35, S4:L38 |
| `script_194.js` | claude |  | x | x | x | S2:L33, S2:L34, S2:L35, S2:L36, S3:L66, S3:L67, S3:L68, S3:L69, S3:L70, S3:L71, S4:L66, S4:L67, S4:L68, S4:L69, S4:L70, S4:L71 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L33, S2:L34, S2:L35, S2:L36, S4:L58, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63, S4:L64, S4:L65, S4:L66, S4:L67, S4:L68, S4:L69, S4:L70, S4:L71, S4:L72, S4:L73, S4:L74, S4:L75 |
| `script_195.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
| `script_196.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L29 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L29 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L29 |
| `script_197.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
| `script_198.js` | claude |  | x |  | x | S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L35, S4:L36, S4:L37 |
|  | chatgpt |  | x |  | x | S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L35, S4:L36, S4:L37 |
|  | gemini |  | x |  | x | S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L35, S4:L36, S4:L37 |
| `script_20.js` | claude |  | x |  | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S4:L38, S4:L39, S4:L40, S4:L41, S4:L42, S4:L43, S4:L44, S4:L45, S4:L46, S4:L47, S4:L48, S4:L49, S4:L50, S4:L51, S4:L52, S4:L53, S4:L54, S4:L55, S4:L56 |
|  | chatgpt |  | x |  | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S4:L25, S4:L26, S4:L27, S4:L28, S4:L29, S4:L38, S4:L39, S4:L40, S4:L41, S4:L42, S4:L43, S4:L44, S4:L45, S4:L46, S4:L47, S4:L48, S4:L49, S4:L50, S4:L51, S4:L52, S4:L53, S4:L54, S4:L55, S4:L56 |
|  | gemini |  | x |  | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S4:L5, S4:L6, S4:L63, S4:L64, S4:L65, S4:L66, S4:L67 |
| `script_201.js` | claude |  |  |  |  | - |
|  | chatgpt |  | x |  |  | S2:L9 |
|  | gemini |  | x |  |  | S2:L9 |
| `script_202.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  | x | S4:L101 |
| `script_203.js` | claude |  | x | x | x | S2:L12, S3:L29, S3:L30, S3:L31, S4:L25, S4:L26, S4:L27 |
|  | chatgpt |  |  |  | x | S4:L25, S4:L26, S4:L27 |
|  | gemini |  | x | x | x | S2:L12, S3:L29, S3:L30, S3:L31, S4:L25, S4:L26, S4:L27 |
| `script_204.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
| `script_205.js` | claude |  | x | x | x | S2:L39, S2:L40, S2:L41, S2:L42, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63, S4:L65 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L39, S2:L40, S2:L41, S2:L42, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S4:L65 |
| `script_206.js` | claude |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L21 |
|  | chatgpt |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L14, S4:L15, S4:L16, S4:L17, S4:L18, S4:L19, S4:L21, S4:L23, S4:L24, S4:L25 |
|  | gemini |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L14, S4:L15, S4:L16, S4:L17, S4:L18, S4:L19, S4:L21 |
| `script_207.js` | claude |  |  |  | x | S4:L11 |
|  | chatgpt |  |  |  | x | S4:L11 |
|  | gemini |  | x |  | x | S2:L4, S2:L7, S4:L11 |
| `script_208.js` | claude |  | x |  | x | S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L24 |
|  | chatgpt |  | x |  | x | S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L24, S4:L25, S4:L26, S4:L27 |
|  | gemini |  | x |  | x | S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L24, S4:L25, S4:L26, S4:L27 |
| `script_209.js` | claude |  | x | x | x | S2:L5, S2:L6, S2:L7, S2:L8, S3:L11, S3:L12, S3:L13, S3:L14, S4:L11, S4:L12, S4:L13, S4:L14 |
|  | chatgpt |  | x |  |  | S2:L5, S2:L6, S2:L7, S2:L8 |
|  | gemini |  | x |  |  | S2:L5, S2:L6, S2:L7, S2:L8 |
| `script_21.js` | claude |  | x |  | x | S2:L1, S2:L51, S4:L10, S4:L14, S4:L31, S4:L45 |
|  | chatgpt |  | x | x | x | S3:L10, S4:L10, S4:L14, S4:L31, S4:L45 |
|  | gemini |  | x |  | x | S2:L4, S4:L10, S4:L14, S4:L31, S4:L45 |
| `script_210.js` | claude |  |  |  |  | - |
|  | chatgpt |  | x |  |  | S2:L9 |
|  | gemini |  | x |  |  | S2:L9 |
| `script_212.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22, S4:L24, S4:L25, S4:L26, S4:L27 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
| `script_213.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L9 |
| `script_214.js` | claude |  |  | x | x | S3:L26, S3:L28, S4:L26 |
|  | chatgpt |  |  | x | x | S3:L26, S3:L28, S4:L26, S4:L28 |
|  | gemini |  |  | x | x | S3:L28, S4:L26 |
| `script_215.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20, S4:L21 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S4:L16, S4:L23 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20, S4:L21 |
| `script_216.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L35 |
|  | chatgpt |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L35 |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L35 |
| `script_217.js` | claude |  |  |  | x | S4:L58 |
|  | chatgpt |  |  | x | x | S3:L14, S4:L14, S4:L58 |
|  | gemini |  |  |  | x | S4:L58 |
| `script_218.js` | claude |  | x |  | x | S2:L9, S4:L20, S4:L21, S4:L22 |
|  | chatgpt |  | x |  | x | S2:L9, S4:L20, S4:L21, S4:L22 |
|  | gemini |  | x |  | x | S2:L9, S4:L20, S4:L21, S4:L22 |
| `script_219.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
| `script_22.js` | claude |  | x |  | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S4:L38, S4:L39, S4:L40, S4:L41, S4:L42, S4:L43, S4:L44, S4:L45, S4:L46, S4:L47, S4:L48, S4:L49, S4:L50, S4:L51, S4:L52, S4:L53, S4:L54, S4:L55, S4:L56 |
|  | chatgpt |  | x |  | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S4:L25, S4:L26, S4:L27, S4:L28, S4:L29, S4:L38, S4:L39, S4:L40, S4:L41, S4:L42, S4:L43, S4:L44, S4:L45, S4:L46, S4:L47, S4:L48, S4:L49, S4:L50, S4:L51, S4:L52, S4:L53, S4:L54, S4:L55, S4:L56 |
|  | gemini |  | x |  | x | S2:L14, S4:L38 |
| `script_220.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  |  | - |
| `script_221.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23, S4:L25, S4:L26, S4:L27, S4:L28, S4:L29, S4:L30, S4:L31, S4:L32, S4:L33, S4:L34 |
|  | gemini |  | x | x | x | S2:L5, S2:L6, S2:L7, S2:L8, S3:L25, S3:L26, S3:L27, S3:L28, S3:L29, S3:L30, S3:L31, S3:L32, S3:L33, S3:L34, S4:L21, S4:L22, S4:L23 |
| `script_223.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L25 |
|  | chatgpt |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L25, S4:L28, S4:L34 |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L25, S4:L28 |
| `script_224.js` | claude |  |  | x | x | S3:L36, S3:L38, S4:L36 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L36, S4:L36 |
| `script_227.js` | claude |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L12 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S4:L12 |
| `script_229.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
| `script_23.js` | claude | x | x |  | x | S1:L37, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L44 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L44 |
| `script_230.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L9 |
| `script_231.js` | claude |  |  | x | x | S3:L14, S3:L15, S4:L14 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L14, S4:L14 |
| `script_232.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S4:L13 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S4:L13 |
| `script_233.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L9 |
| `script_234.js` | claude |  | x | x | x | S2:L1, S2:L32, S3:L25, S3:L29, S3:L30, S3:L31, S4:L15, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20, S4:L21 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L1, S3:L25, S3:L26, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20 |
| `script_235.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S4:L23 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S4:L23 |
| `script_236.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L26, S4:L27, S4:L28, S4:L29, S4:L30, S4:L33 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L33 |
| `script_237.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S3:L6, S4:L6 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L4, S3:L6, S4:L6 |
| `script_238.js` | claude |  |  | x | x | S3:L39, S3:L41, S4:L39, S4:L41 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x |  | x | x | S1:L26, S1:L27, S1:L28, S1:L35, S3:L39, S3:L41, S4:L39, S4:L41 |
| `script_239.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S3:L7, S4:L7 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L1, S3:L7, S4:L7 |
| `script_24.js` | claude |  | x | x | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S2:L21, S2:L22, S2:L23, S3:L76, S3:L77, S3:L78, S3:L84, S3:L85, S3:L86, S4:L60, S4:L61, S4:L62, S4:L76, S4:L77, S4:L84, S4:L85 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L14, S3:L76, S3:L84, S4:L60, S4:L76, S4:L84 |
| `script_240.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
| `script_241.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L19 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L19, S4:L22 |
| `script_242.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L26 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L26 |
| `script_245.js` | claude |  |  | x | x | S3:L43, S3:L45, S4:L43 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L43, S4:L43 |
| `script_247.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S2:L21, S3:L14, S4:L7, S4:L8, S4:L9, S4:L10, S4:L11, S4:L12, S4:L14 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S2:L19, S2:L20, S2:L21, S3:L14, S4:L14 |
| `script_248.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L22, S4:L23, S4:L24, S4:L25 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19 |
| `script_249.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L20 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L20 |
| `script_25.js` | claude |  | x |  | x | S2:L26, S2:L30, S4:L38, S4:L126, S4:L147, S4:L163 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L26, S2:L30 |
| `script_250.js` | claude |  |  | x | x | S3:L23, S3:L32, S3:L33, S3:L34, S3:L35, S3:L36, S4:L23 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  | x | S4:L23 |
| `script_251.js` | claude |  |  | x | x | S3:L57, S3:L58, S4:L57 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x |  | x | x | S1:L35, S3:L57, S3:L58, S4:L57 |
| `script_252.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L22, S4:L24 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L22 |
| `script_253.js` | claude |  | x | x | x | S2:L1, S2:L32, S3:L25, S3:L29, S3:L30, S3:L31, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L3, S3:L25, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20 |
| `script_254.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L20, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L23 |
| `script_255.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L29 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L27, S4:L29 |
| `script_257.js` | claude |  |  | x | x | S3:L39, S3:L41, S4:L39 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x |  | x | x | S1:L26, S1:L27, S1:L28, S3:L39, S3:L41, S4:L39 |
| `script_259.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S3:L8, S4:L8 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L1, S2:L18, S3:L8, S4:L8 |
| `script_26.js` | claude |  | x |  |  | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L1, S3:L1031, S4:L1075, S4:L1076, S4:L1077 |
| `script_260.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L9 |
| `script_262.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L5, S2:L6, S2:L7, S2:L8, S3:L25, S3:L26, S3:L27, S3:L28, S3:L29, S3:L30, S3:L31, S3:L32, S4:L21, S4:L22, S4:L23 |
| `script_264.js` | claude |  | x |  | x | S2:L39, S2:L40, S2:L41, S2:L42, S4:L73, S4:L74, S4:L75 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L39, S2:L40, S2:L41, S2:L42, S4:L77 |
| `script_265.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S3:L7, S4:L7 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L1, S2:L9, S3:L7, S3:L8, S4:L7 |
| `script_266.js` | claude |  |  | x | x | S3:L56, S3:L62, S3:L64, S3:L65, S3:L70, S3:L71, S4:L56, S4:L62, S4:L70 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L62, S3:L70, S4:L65, S4:L71 |
| `script_267.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S4:L21, S4:L22, S4:L23 |
| `script_268.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S4:L20, S4:L21, S4:L22 |
| `script_269.js` | claude |  | x | x | x | S2:L6, S3:L7, S4:L7 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L1, S2:L2, S2:L6, S2:L7, S2:L8, S2:L9, S3:L7, S4:L7 |
| `script_27.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L32, S4:L33, S4:L34, S4:L35, S4:L36, S4:L42 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L5, S2:L11, S4:L32, S4:L42 |
| `script_270.js` | claude |  | x |  | x | S2:L7, S2:L8, S2:L9, S2:L10, S4:L22 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L7, S2:L8, S2:L9, S2:L10, S4:L22 |
| `script_271.js` | claude |  | x | x | x | S2:L6, S3:L7, S4:L7 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L1, S2:L15, S3:L7, S4:L7 |
| `script_272.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L9 |
| `script_273.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L22, S4:L23, S4:L24, S4:L25 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L19 |
| `script_276.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S4:L12 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S4:L12 |
| `script_277.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S4:L22, S4:L23, S4:L24, S4:L25 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L5, S4:L19 |
| `script_278.js` | claude | x |  |  | x | S1:L45, S4:L58, S4:L59, S4:L60, S4:L61 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  | x | S4:L62, S4:L65, S4:L66, S4:L69, S4:L70 |
| `script_279.js` | claude |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L25 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L25 |
| `script_28.js` | claude | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L81, S1:L82, S1:L83, S1:L84, S1:L85, S1:L86, S1:L87, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
| `script_280.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L27 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L27 |
| `script_281.js` | claude |  |  | x | x | S3:L20, S4:L20 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L20, S4:L20 |
| `script_282.js` | claude |  | x |  | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L24 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L14, S2:L15, S2:L16, S2:L17, S2:L18, S4:L23, S4:L24, S4:L25, S4:L26, S4:L27, S4:L28 |
| `script_285.js` | claude |  |  | x | x | S3:L47, S3:L48, S3:L49, S3:L50, S4:L47 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x |  | x | x | S1:L27, S1:L31, S1:L33, S1:L34, S1:L37, S1:L38, S3:L47, S3:L49, S4:L49 |
| `script_286.js` | claude |  | x | x | x | S2:L39, S2:L40, S2:L41, S2:L42, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S4:L59, S4:L60, S4:L61, S4:L62, S4:L63 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L39, S2:L40, S2:L41, S2:L42, S4:L65 |
| `script_287.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L10 |
| `script_288.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L73, S3:L80, S3:L88, S3:L93, S3:L100, S4:L82, S4:L89, S4:L101 |
| `script_289.js` | claude |  | x | x | x | S2:L1, S2:L31, S3:L24, S3:L28, S3:L29, S3:L30, S3:L31, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20, S4:L21 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L11, S3:L24, S3:L28, S3:L29, S3:L30, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20 |
| `script_29.js` | claude | x | x |  |  | S1:L11, S1:L12, S1:L13, S1:L14, S1:L15, S1:L16, S1:L17, S1:L18, S1:L19, S1:L20, S1:L21, S2:L28, S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S2:L36 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x |  |  | S1:L11, S1:L12, S1:L13, S1:L14, S1:L15, S1:L16, S1:L17, S1:L18, S1:L19, S1:L20, S1:L21, S2:L28, S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S2:L36 |
| `script_290.js` | claude |  |  | x | x | S3:L54, S3:L55, S3:L56, S3:L57, S3:L61, S3:L62, S3:L63, S4:L54, S4:L61 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L61, S3:L63, S4:L63 |
| `script_291.js` | claude |  | x |  | x | S2:L22, S2:L23, S2:L24, S2:L25, S4:L28 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L22, S2:L23, S2:L24, S2:L25, S4:L28 |
| `script_292.js` | claude |  | x |  | x | S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S2:L36, S2:L37, S2:L38, S4:L58, S4:L59, S4:L60 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L29, S2:L30, S2:L31, S2:L32, S2:L33, S2:L34, S2:L35, S2:L36, S2:L37, S2:L38, S4:L58, S4:L59, S4:L60 |
| `script_295.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L32 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S4:L32, S4:L35 |
| `script_296.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S3:L11, S3:L14, S3:L17, S4:L11, S4:L14, S4:L17 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S3:L11, S3:L14, S3:L17, S4:L11, S4:L14, S4:L17 |
| `script_30.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L30, S4:L31, S4:L32, S4:L33, S4:L34, S4:L40 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L40 |
| `script_31.js` | claude |  | x |  | x | S2:L14, S4:L50 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L14, S3:L62, S4:L50 |
| `script_32.js` | claude | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L81, S1:L82, S1:L83, S1:L84, S1:L85, S1:L86, S1:L87, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
| `script_33.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L42, S4:L43, S4:L44, S4:L45, S4:L46 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L52 |
| `script_34.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L36 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L36 |
| `script_35.js` | claude |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L14, S4:L23 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L4, S2:L5, S2:L6, S2:L7, S4:L14, S4:L23 |
| `script_36.js` | claude | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L81, S1:L82, S1:L83, S1:L84, S1:L85, S1:L86, S1:L87, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x |  |  | S1:L38, S1:L39, S1:L40, S1:L41, S1:L42, S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S2:L55, S2:L56, S2:L57, S2:L58, S2:L59, S2:L60, S2:L61, S2:L62, S2:L63, S2:L64, S2:L65, S2:L66 |
| `script_37.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S4:L19, S4:L20, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S4:L25, S4:L26, S4:L27, S4:L28, S4:L29, S4:L30, S4:L31 |
| `script_38.js` | claude |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S4:L19, S4:L20, S4:L21, S4:L22, S4:L23 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S4:L19, S4:L20, S4:L21, S4:L22, S4:L23 |
| `script_39.js` | claude |  |  | x | x | S3:L29, S3:L30, S3:L31, S3:L32, S3:L39, S4:L29, S4:L39 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  |  | - |
| `script_40.js` | claude |  |  | x | x | S3:L18, S3:L22, S4:L18, S4:L22 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L18, S3:L22, S4:L18, S4:L22 |
| `script_41.js` | claude |  | x | x | x | S2:L4010, S2:L4011, S2:L4012, S2:L4013, S2:L4014, S2:L4015, S2:L4016, S2:L4017, S2:L4018, S2:L4019, S3:L4052, S3:L4053, S3:L4054, S3:L4055, S3:L4056, S3:L4057, S3:L4058, S4:L4026, S4:L4027, S4:L4028, S4:L4029, S4:L4030, S4:L4031, S4:L4052, S4:L4053, S4:L4054 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x |  | x | S1:L5, S1:L4006, S2:L4010, S2:L4019, S4:L4026, S4:L4031, S4:L4052, S4:L4054 |
| `script_42.js` | claude |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L45, S4:L46, S4:L47, S4:L48, S4:L49, S4:L54 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S4:L54 |
| `script_45.js` | claude | x | x |  | x | S1:L22, S1:L23, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S4:L41, S4:L42, S4:L43 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x |  | x | S1:L22, S1:L23, S2:L6, S2:L15, S4:L41, S4:L43 |
| `script_47.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S3:L12, S4:L12 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S3:L12, S4:L12 |
| `script_51.js` | claude |  | x | x | x | S2:L6, S2:L7, S2:L8, S2:L9, S3:L18, S4:L18 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L6, S2:L7, S2:L8, S2:L9, S3:L18, S4:L18 |
| `script_52.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S3:L18, S4:L18 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S3:L18, S4:L18 |
| `script_53.js` | claude |  | x | x |  | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S3:L22, S3:L23, S3:L24, S3:L25, S3:L26, S3:L27, S3:L28 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x |  | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S3:L22, S3:L23, S3:L24, S3:L25, S3:L26, S3:L27, S3:L28 |
| `script_55.js` | claude | x | x |  | x | S1:L19, S1:L20, S1:L21, S1:L22, S1:L23, S1:L24, S1:L25, S1:L26, S1:L27, S1:L28, S1:L29, S1:L30, S1:L31, S1:L32, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L34 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x |  | x | S1:L19, S1:L20, S1:L21, S1:L22, S2:L8, S2:L17, S4:L27, S4:L31 |
| `script_56.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L4, S2:L13, S3:L16, S4:L16 |
| `script_59.js` | claude | x | x |  | x | S1:L16, S1:L17, S2:L20, S2:L21, S2:L22, S2:L23, S2:L24, S2:L25, S2:L26, S2:L27, S2:L28, S2:L29, S4:L46, S4:L47, S4:L48 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x |  | x | S1:L16, S1:L17, S2:L20, S2:L21, S2:L22, S2:L23, S2:L24, S2:L25, S2:L26, S2:L27, S2:L28, S2:L29, S4:L46, S4:L47, S4:L48 |
| `script_60.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
| `script_61.js` | claude | x | x |  | x | S1:L19, S1:L20, S1:L21, S1:L22, S1:L23, S1:L24, S1:L25, S1:L26, S1:L27, S1:L28, S1:L29, S1:L30, S1:L31, S1:L32, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L34 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x |  | x | S1:L19, S1:L20, S1:L21, S1:L22, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S2:L17, S4:L27, S4:L28, S4:L29, S4:L30, S4:L31, S4:L34 |
| `script_62.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S3:L16, S4:L16 |
| `script_63.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S3:L13, S4:L13 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S3:L13, S4:L13 |
| `script_69.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S3:L17, S4:L17 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L4, S3:L17, S4:L17 |
| `script_70.js` | claude |  | x | x | x | S2:L5, S2:L6, S2:L7, S2:L8, S3:L11, S4:L11 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L5, S2:L6, S2:L7, S2:L8, S3:L11, S4:L11 |
| `script_71.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S3:L18, S4:L18 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S3:L18, S4:L18 |
| `script_76.js` | claude |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L21, S3:L22, S4:L16, S4:L17, S4:L18, S4:L19, S4:L20, S4:L21 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L21, S4:L16, S4:L17, S4:L18, S4:L19 |
| `script_77.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L15, S4:L15 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S2:L8, S2:L9, S2:L10, S2:L11, S2:L12, S3:L15, S4:L15 |
| `script_78.js` | claude |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S3:L14, S4:L14 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L8, S2:L9, S2:L10, S2:L11, S3:L14, S4:L14 |
| `script_80.js` | claude |  | x | x | x | S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S3:L20, S3:L29, S3:L30, S3:L31, S3:L32, S3:L33, S4:L20 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L10, S2:L11, S2:L12, S2:L13, S2:L14, S2:L15, S2:L16, S3:L20, S3:L29, S3:L30, S3:L31, S3:L32, S3:L33, S4:L20 |
| `script_82.js` | claude |  | x | x | x | S2:L7, S2:L8, S2:L9, S3:L12, S4:L12 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L7, S2:L8, S2:L9, S3:L12, S4:L12 |
| `script_83.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L24, S4:L24 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L24, S4:L24 |
| `script_85.js` | claude | x | x |  |  | S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L49, S1:L50, S1:L51, S1:L52, S1:L53, S1:L54, S1:L55, S1:L56, S1:L57, S2:L67, S2:L68, S2:L69, S2:L70, S2:L71, S2:L72, S2:L73, S2:L74, S2:L75, S2:L76, S2:L77 |
|  | chatgpt |  |  |  |  | - |
|  | gemini | x | x |  |  | S1:L43, S1:L44, S1:L45, S1:L46, S1:L47, S1:L48, S1:L49, S1:L50, S1:L51, S1:L52, S1:L53, S1:L54, S1:L55, S1:L56, S1:L57, S2:L67, S2:L68, S2:L69, S2:L70, S2:L71, S2:L72, S2:L73, S2:L74, S2:L75, S2:L76, S2:L77 |
| `script_89.js` | claude |  | x | x | x | S2:L9, S2:L10, S2:L11, S3:L16, S4:L16 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L9, S2:L10, S2:L11, S3:L16, S4:L16 |
| `script_90.js` | claude |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L10, S4:L10 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L4, S2:L5, S2:L6, S2:L7, S3:L10, S4:L10 |
| `script_92.js` | claude |  |  |  | x | S4:L45, S4:L63, S4:L87, S4:L104, S4:L131, S4:L150, S4:L167, S4:L230 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  |  | x | S4:L45, S4:L63, S4:L87, S4:L104, S4:L131, S4:L150, S4:L167, S4:L230 |
| `script_93.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S3:L12, S3:L13, S3:L14, S3:L15, S3:L16, S3:L17, S3:L18, S3:L19, S3:L20, S3:L22, S3:L23, S3:L24, S3:L25, S3:L26, S3:L27, S3:L28, S3:L29, S3:L30, S3:L31, S3:L32, S3:L33, S3:L34, S3:L35, S3:L40, S3:L41, S3:L42, S3:L43, S3:L44, S3:L45, S3:L46, S3:L47, S3:L49, S3:L50, S3:L51, S3:L52, S3:L53, S3:L54, S3:L55, S3:L56, S3:L57, S3:L58, S3:L59, S3:L60, S3:L61, S3:L62, S3:L63, S3:L64, S3:L81, S3:L82, S3:L83, S3:L84, S3:L85, S3:L86, S3:L87, S3:L88, S3:L89, S3:L90, S3:L91, S3:L92, S3:L93, S3:L94, S3:L95, S3:L96, S3:L98, S3:L99, S3:L100, S3:L101, S3:L102, S3:L103, S3:L104, S3:L105, S3:L106, S3:L107, S3:L108, S3:L109, S3:L110, S3:L111, S3:L113, S3:L114, S3:L115, S3:L116, S3:L117, S3:L118, S3:L119, S3:L120, S3:L121, S4:L12, S4:L22, S4:L40, S4:L49, S4:L67, S4:L81, S4:L98, S4:L113 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L1, S3:L12, S3:L20, S4:L12, S4:L20 |
| `script_94.js` | claude |  |  |  |  | - |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  |  | x | x | S3:L96, S4:L39, S4:L56, S4:L80, S4:L96, S4:L116, S4:L132, S4:L156, S4:L178 |
| `script_95.js` | claude |  | x |  | x | S2:L6, S4:L19, S4:L28, S4:L47, S4:L58, S4:L76, S4:L88, S4:L99, S4:L116 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  | x | S2:L5, S4:L18, S4:L19, S4:L20, S4:L21, S4:L22, S4:L23, S4:L24, S4:L25 |
| `script_96.js` | claude |  | x | x | x | S2:L1, S2:L2, S2:L3, S2:L4, S2:L5, S2:L6, S3:L13, S3:L21, S3:L23, S3:L36, S3:L41, S3:L48, S3:L50, S3:L65, S3:L82, S3:L97, S3:L99, S3:L112, S4:L13, S4:L23, S4:L41, S4:L50, S4:L68, S4:L82, S4:L99 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x | x | x | S2:L6, S3:L13, S3:L21, S4:L13, S4:L21 |
| `script_97.js` | claude |  | x |  |  | S2:L197, S2:L198, S2:L199 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L1, S2:L199 |
| `script_98.js` | claude |  | x |  |  | S2:L203, S2:L204, S2:L205 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L1 |
| `script_99.js` | claude |  | x |  |  | S2:L502, S2:L503, S2:L504 |
|  | chatgpt |  |  |  |  | - |
|  | gemini |  | x |  |  | S2:L1, S2:L504 |

## Refactoring Suggestions

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
// These lines are acceptable in the init context as 'open()' is k6's built-in for init-phase file reading.
// However, papaparse.parse() on a potentially large CSV is a heavy computation run once per VU.
// To mitigate cost, ensure the CSV is as small as needed and consider caching parsed results.
// If SharedArray is available, use it to parse only once across all VUs:
import { SharedArray } from 'k6/data';
const userTokenData = new SharedArray('users', function () {
    const csvData = open('../loginSuccess.csv');
    return papaparse.parse(csvData, { header: false }).data;
});
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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<2000'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [52, 53, 54, 82, 83, 84]
- **Snippet:**
```js
let orderRes = http.post(`${baseUrl}/api/v1/orders`, orderJSON, { headers: headers });
...
let orderIPNRes = http.post(`${baseUrl}/api/v1/orders/ipn`, orderipnJSON, { headers: headersIPN });
```
- **Refactored:**
```js
let orderRes = http.post(`${baseUrl}/api/v1/orders`, orderJSON, { headers: headers });
check(orderRes, {
    'order API status is 201': (r) => r.json().status_code === 201,
    'order API response time < 2000ms': (r) => r.timings.duration < 2000,
});

// ... inside the else-if block:
let orderIPNRes = http.post(`${baseUrl}/api/v1/orders/ipn`, orderipnJSON, { headers: headersIPN });
check(orderIPNRes, {
    'order IPN API status is 201': (r) => r.status === 201,
    'order IPN API response time < 2000ms': (r) => r.timings.duration < 2000,
});
```

**Smell 4: Not using tags**

- **Lines:** [52, 53, 54, 82, 83, 84]
- **Snippet:**
```js
let orderRes = http.post(`${baseUrl}/api/v1/orders`, orderJSON, { headers: headers });
...
let orderIPNRes = http.post(`${baseUrl}/api/v1/orders/ipn`, orderipnJSON, { headers: headersIPN });
```
- **Refactored:**
```js
let orderRes = http.post(`${baseUrl}/api/v1/orders`, orderJSON, {
    headers: headers,
    tags: { name: 'CreateOrder', endpoint: '/api/v1/orders' },
});

let orderIPNRes = http.post(`${baseUrl}/api/v1/orders/ipn`, orderipnJSON, {
    headers: headersIPN,
    tags: { name: 'OrderIPN', endpoint: '/api/v1/orders/ipn' },
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
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
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
  tags: { name: 'CreateOrder', endpoint: '/api/v1/orders', flow: 'purchase_order' },
});

check(orderRes, {
  'create order HTTP status is 201': (r) => r.status === 201,
  'create order business status_code is 201': (r) => r.json('status_code') === 201,
});

let orderIPNRes = http.post(`${baseUrl}/api/v1/orders/ipn`, orderipnJSON, {
  headers: headersIPN,
  tags: { name: 'OrderIPN', endpoint: '/api/v1/orders/ipn', flow: 'purchase_order' },
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
  tags: { name: 'CreateOrder', endpoint: '/api/v1/orders', flow: 'purchase_order' },
});

let orderIPNRes = http.post(`${baseUrl}/api/v1/orders/ipn`, orderipnJSON, {
  headers: headersIPN,
  tags: { name: 'OrderIPN', endpoint: '/api/v1/orders/ipn', flow: 'purchase_order' },
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
import { SharedArray } from 'k6/data';

const userTokenData = new SharedArray('user data', function () {
  // Papaparse can accept the file path directly
  return papaparse.parse(open('../loginSuccess.csv'), { header: false }).data;
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
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
        'checks': ['rate>0.99'], // 99% of checks should pass
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [56, 86]
- **Snippet:**
```js
if(orderRes.json().status_code !== 201){
    // ...
}
// ...
if(orderIPNRes.status !== 201){
    // ...
}
```
- **Refactored:**
```js
const orderRes = http.post(`${baseUrl}/api/v1/orders`, orderJSON, { headers: headers });

const orderSuccess = check(orderRes, {
    'Order creation status is 201': (r) => r.status === 201,
});

if (orderSuccess) {
    // ... existing success logic ...
    const orderIPNRes = http.post(`${baseUrl}/api/v1/orders/ipn`, orderipnJSON, { headers: headersIPN });
    check(orderIPNRes, {
        'Order IPN status is 201': (r) => r.status === 201,
    });
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

### `script_02.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [6, 32, 58, 104]
- **Snippet:**
```js
export const options1 = { scenarios: { ... } };
export const options = { scenarios: { ... } };
export const options3 = { scenarios: { ... } };
export const options4 = { scenarios: { ... } };
```
- **Refactored:**
```js
export const options = {
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<3000'],
        'http_req_duration{group:::fullRegistration::regContext}': ['p(95)<3000'],
        'http_req_duration{group:::fullAuthentication::authContext}': ['p(95)<3000']
    },
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
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [183, 193, 205, 228, 238, 250]
- **Snippet:**
```js
let res = http.get(`https://${url}/trumfid/biometri/registration/context?returnUrl=`+returnUrl);
let res = http.get(`https://${url}/trumfid/biometri/registration/options?returnUrl=`+returnUrl);
let res = http.post(registerUrl, fakeAttestation, params);
let res = http.get('https://test.id.trumf.no/trumfid/login/context?returnUrl=' + returnUrl);
let res = http.get('https://test.id.trumf.no/trumfid/biometri/login/options');
let res = http.post(url, fakeAssertionLogin);
```
- **Refactored:**
```js
// registration context
let res = http.get(`https://${url}/trumfid/biometri/registration/context?returnUrl=` + returnUrl, { tags: { name: 'regContext', flow: 'registration' } });

// registration options
let res = http.get(`https://${url}/trumfid/biometri/registration/options?returnUrl=` + returnUrl, { tags: { name: 'regOptions', flow: 'registration' } });

// register
let res = http.post(registerUrl, fakeAttestation, Object.assign({}, params, { tags: { name: 'register', flow: 'registration' } }));

// auth context
let res = http.get('https://test.id.trumf.no/trumfid/login/context?returnUrl=' + returnUrl, { tags: { name: 'authContext', flow: 'authentication' } });

// auth options
let res = http.get('https://test.id.trumf.no/trumfid/biometri/login/options', { tags: { name: 'authOptions', flow: 'authentication' } });

// authenticate
let res = http.post(url, fakeAssertionLogin, { tags: { name: 'authenticate', flow: 'authentication' } });
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
const jsonParams = {
  headers: {
    'Content-Type': 'application/json'
  }
};

let res = http.get(`https://${url}/trumfid/biometri/registration/context?returnUrl=${returnUrl}`, {
  tags: { flow: 'registration', endpoint: 'regContext' }
});

let res = http.get(`https://${url}/trumfid/biometri/registration/options?returnUrl=${returnUrl}`, {
  tags: { flow: 'registration', endpoint: 'regOptions' }
});

let res = http.post(registerUrl, fakeAttestation, {
  ...jsonParams,
  tags: { flow: 'registration', endpoint: 'register' }
});

let res = http.get(`https://test.id.trumf.no/trumfid/login/context?returnUrl=${returnUrl}`, {
  tags: { flow: 'authentication', endpoint: 'authContext' }
});

let res = http.get('https://test.id.trumf.no/trumfid/biometri/login/options', {
  tags: { flow: 'authentication', endpoint: 'authOptions' }
});

let res = http.post(url, fakeAssertionLogin, {
  tags: { flow: 'authentication', endpoint: 'authenticate' }
});
```

### `script_02.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [6, 32, 58, 104]
- **Snippet:**
```js
export const options = {
    scenarios: {
       // ...
    }
};
```
- **Refactored:**
```js
export const options = {
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<2000'], // 95% of requests should be below 2000ms
        'checks': ['rate>0.99'] // over 99% of checks must pass
    },
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
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [183, 193, 205, 228, 238, 250]
- **Snippet:**
```js
let res = http.get(`https://${url}/trumfid/biometri/registration/context?returnUrl=`+returnUrl);
```
- **Refactored:**
```js
let res = http.get(`https://${url}/trumfid/biometri/registration/context?returnUrl=`+returnUrl, {
  tags: { name: 'registration-context' },
});
```

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
  tags: { name: 'create_multipart_upload', operation: 'upload_init' },
})

const offsetRes = http.head(location, {
  headers,
  tags: { name: 'check_upload_offset', operation: 'upload_chunk' },
})

const uploadChunkRes = http.patch(location, chunk, {
  headers: Object.assign({ 'Content-Type': 'application/offset+octet-stream', 'Upload-Offset': offset, 'Content-Length': chunk.byteLength }, headers),
  tags: { name: 'upload_chunk', operation: 'upload_chunk' },
})

const removeRes = http.del(`${storageObjectUri}/tus`, JSON.stringify({ prefixes: [path] }), {
  headers: { authorization: `Bearer ${serviceToken}`, apikey: serviceToken, 'Content-Type': 'application/json' },
  tags: { name: 'delete_object', operation: 'cleanup' },
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
/*
This change requires modifying the default function signature to accept data from setup():
from: export default () => {
to:   export default (data) => {
and using `data.binFile` instead of `binFile` inside the function.
*/

// Remove from init context: const binFile = open('./large_file.png', 'b')

export function setup() {
  // open() is called once for the whole test, and its result is passed to VUs.
  const binFile = open('./large_file.png', 'b');
  return { binFile: binFile };
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
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<2000'], // 95% of requests should be below 2000ms
    'upload_duration': ['p(95)<15000'], // 95% of full uploads should be below 15s
  },
  // ... rest of options
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
})
```
- **Refactored:**
```js
const uploadRes = http.post(`${storageMultipartUri}`, null, {
  tags: { name: 'TUS-Create' },
  headers: Object.assign(
    // ...
  ),
})
```

### `script_04.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
- **Snippet:**
```js
export const options = {
    stages: [
        {
            duration: '10s',
            target: 100,
        },
        {
            duration: '30s',
            target: 100,
        },
        {
            duration: '10s',
            target: 0,
        },
    ]
}
```
- **Refactored:**
```js
export const options = {
    stages: [
        {
            duration: '10s',
            target: 100,
        },
        {
            duration: '30s',
            target: 100,
        },
        {
            duration: '10s',
            target: 0,
        },
    ],
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
    }
}
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
check(res1, { 'test.k6.io status is 200': (r) => r.status === 200 });
const res2 = http.get('https://quickpizza.grafana.com/contacts.php');
check(res2, { 'contacts.php status is 200': (r) => r.status === 200 });
const res3 = http.get('https://quickpizza.grafana.com/news.php');
check(res3, { 'news.php status is 200': (r) => r.status === 200 });
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
http.get('https://quickpizza.grafana.com/test.k6.io/', { tags: { name: 'home' } });
http.get('https://quickpizza.grafana.com/contacts.php', { tags: { name: 'contacts' } });
http.get('https://quickpizza.grafana.com/news.php', { tags: { name: 'news' } });
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
    check(homeRes, {
        'home status is 200': (r) => r.status === 200,
    });
    sleep(1);

    const contactsRes = http.get('https://quickpizza.grafana.com/contacts.php');
    check(contactsRes, {
        'contacts status is 200': (r) => r.status === 200,
    });
    sleep(1);

    const newsRes = http.get('https://quickpizza.grafana.com/news.php');
    check(newsRes, {
        'news status is 200': (r) => r.status === 200,
    });
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
        tags: { endpoint: 'home', flow: 'main' },
    });
    sleep(1);

    http.get('https://quickpizza.grafana.com/contacts.php', {
        tags: { endpoint: 'contacts', flow: 'main' },
    });
    sleep(1);

    http.get('https://quickpizza.grafana.com/news.php', {
        tags: { endpoint: 'news', flow: 'main' },
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
        {
            duration: '10s',
            target: 100, // Ramp up to 100 users
        },
        {
            duration: '30s',
            target: 100, // Ramp up to 100 users
        },
        {
            duration: '10s',
            target: 0, // Ramp down to 0 users
        },
    ]
}
```
- **Refactored:**
```js
export const options = {
    stages: [
        {
            duration: '10s',
            target: 100,
        },
        {
            duration: '30s',
            target: 100,
        },
        {
            duration: '10s',
            target: 0,
        },
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [22, 24, 26]
- **Snippet:**
```js
http.get('https://quickpizza.grafana.com/test.k6.io/');
```
- **Refactored:**
```js
import { check } from 'k6';
// ... in default function
const res = http.get('https://quickpizza.grafana.com/test.k6.io/');
check(res, { 'status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [22, 24, 26]
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
thresholds: {
    http_req_duration: ['p(95)<200'], // 95% of requests should complete below 200ms
    http_req_failed: ['rate<0.01'], // Less than 1% of requests should fail
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

// Inside default function:
let res1 = http.get('https://test.k6.io');
check(res1, { 'homepage status is 200': (r) => r.status === 200 });

let res2 = http.get('https://test.k6.io/contact.php');
check(res2, { 'contact page status is 200': (r) => r.status === 200 });

let res3 = http.get('https://test.k6.io/news.php');
check(res3, { 'news page status is 200': (r) => r.status === 200 });
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
http.get('https://test.k6.io', { tags: { name: 'homepage' } });
http.get('https://test.k6.io/contact.php', { tags: { name: 'contact_page' } });
http.get('https://test.k6.io/news.php', { tags: { name: 'news_page' } });
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
        checks: ['rate>0.99'],
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
import http from 'k6/http';
import { sleep, check } from 'k6';

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

- **Lines:** [17, 18, 19, 29, 31, 33]
- **Snippet:**
```js
// tags: {
//     my_custom_tag: 'my_value',
// },
http.get('https://test.k6.io');
http.get('https://test.k6.io/contact.php');
http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
export default function () {
    http.get('https://test.k6.io', {
        tags: { endpoint: 'home', flow: 'main' },
    });
    sleep(1);

    http.get('https://test.k6.io/contact.php', {
        tags: { endpoint: 'contact', flow: 'main' },
    });
    sleep(2);

    http.get('https://test.k6.io/news.php', {
        tags: { endpoint: 'news', flow: 'main' },
    });
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
export const options = {
    vus: 1,
    duration: '30s',
    thresholds: {
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [29, 31, 33]
- **Snippet:**
```js
http.get('https://test.k6.io');
```
- **Refactored:**
```js
import http from 'k6/http';
import { sleep, check } from 'k6';

// ... in default function
const res = http.get('https://test.k6.io');
check(res, {
  'status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [29, 31, 33]
- **Snippet:**
```js
http.get('https://test.k6.io');
```
- **Refactored:**
```js
http.get('https://test.k6.io', {
  tags: { name: 'Homepage' },
});
sleep(1);
http.get('https://test.k6.io/contact.php', {
  tags: { name: 'Contact' },
});
sleep(2);
http.get('https://test.k6.io/news.php', {
  tags: { name: 'News' },
});
```

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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500']
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

// inside default function:
let res1 = http.get('https://test.k6.io');
check(res1, { 'homepage status 200': (r) => r.status === 200 });

let res2 = http.get('https://test.k6.io/contacts.php');
check(res2, { 'contacts status 200': (r) => r.status === 200 });

let res3 = http.get('https://test.k6.io/news.php');
check(res3, { 'news status 200': (r) => r.status === 200 });
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
http.get('https://test.k6.io', { tags: { name: 'homepage' } });
http.get('https://test.k6.io/contacts.php', { tags: { name: 'contacts' } });
http.get('https://test.k6.io/news.php', { tags: { name: 'news' } });
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
        http_req_duration: ['p(95)<500']
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
    const homeRes = http.get('https://test.k6.io');
    check(homeRes, { 'home status is 200': (r) => r.status === 200 });

    sleep(1);

    const contactsRes = http.get('https://test.k6.io/contacts.php');
    check(contactsRes, { 'contacts status is 200': (r) => r.status === 200 });

    sleep(2);

    const newsRes = http.get('https://test.k6.io/news.php');
    check(newsRes, { 'news status is 200': (r) => r.status === 200 });

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
        tags: { endpoint: 'home', page: 'home' }
    });

    sleep(1);

    http.get('https://test.k6.io/contacts.php', {
        tags: { endpoint: 'contacts', page: 'contacts' }
    });

    sleep(2);

    http.get('https://test.k6.io/news.php', {
        tags: { endpoint: 'news', page: 'news' }
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
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should complete below 500ms
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
```
- **Refactored:**
```js
import { check } from 'k6';

// ... inside default function
const res = http.get('https://test.k6.io');
check(res, { 'status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [16, 18, 20]
- **Snippet:**
```js
http.get('https://test.k6.io');
```
- **Refactored:**
```js
// ... inside default function
http.get('https://test.k6.io', { 
  tags: { name: 'Homepage' } 
});
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
// Use SharedArray to load and parse JSON only once, shared across VUs
import { SharedArray } from 'k6/data';
const payloadArray = new SharedArray('testdata', function() {
    return [JSON.parse(open('./testdata_v1.json'))];
});
// Then inside default function: let user = Object.assign({}, payloadArray[0]);
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
    tags: { name: 'post_echo', endpoint: 'echo_hoppscotch' },
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
/* The file is read and parsed once for each VU, which is inefficient.
   It should be moved to the setup function to be run only once for the entire test. */

export function setup() {
    const payloadData = JSON.parse(open('./testdata_v1.json'));
    // Other setup code...
    return { payload: payloadData };
}

export default function(data) {
    // Use a deep copy to prevent VUs from interfering with each other's data
    let user = JSON.parse(JSON.stringify(data.payload)); 
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
// ... in the default function ...
const res = http.post(`https://echo.hoppscotch.io`, f);
check(res, { 'status is 200': (r) => r.status === 200 });
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
    tags: { name: 'EchoPost' }
};
const res = http.post(`https://echo.hoppscotch.io`, f, params);
```

### `script_08.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
- **Snippet:**
```js
export default function () { ... }
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<2000'],
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
...
const res = http.post('https://example.com/upload', data);
check(res, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
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
  tags: { name: 'upload', endpoint: '/upload' },
});
```

### `script_08.js` — CHATGPT

**Smell 1: Costly operations in the init context**

- **Lines:** [4]
- **Snippet:**
```js
const binFile = open('./file.bin', 'b');
```
- **Refactored:**
```js
// Prefer using a small fixture file for upload tests, or avoid loading large binary files in init.
// If the file must be uploaded, keep it minimal and document that it is intentionally loaded once per VU.
const binFile = open('./small-test-file.bin', 'b');
```

**Smell 2: Do not use thresholds**

- **Lines:** []
- **Snippet:**
```js
No export const options with thresholds is defined.
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

- **Lines:** [11]
- **Snippet:**
```js
http.post('https://example.com/upload', data);
```
- **Refactored:**
```js
import { check, sleep } from 'k6';

const res = http.post('https://example.com/upload', data, {
  tags: { endpoint: 'upload' },
});

check(res, {
  'upload status is 200': (r) => r.status === 200,
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
  tags: {
    endpoint: 'upload',
    flow: 'file_upload',
  },
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
import http from 'k6/http';
import { sleep } from 'k6';

let binFile;

export function setup() {
  // The file is now opened only once for the entire test run
  binFile = open('./file.bin', 'b');
  return { fileData: binFile };
}

export default function (data) {
  const payload = {
    field: 'this is a standard form field',
    file: http.file(data.fileData, 'test.bin'),
  };
  http.post('https://example.com/upload', payload);
  sleep(3);
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [1, 13]
- **Snippet:**
```js
// The script lacks an 'options' export with a 'thresholds' object, which defines pass/fail criteria for the test.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<2000'], // 95% of requests must complete below 2000ms
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

// ... inside the default function
const res = http.post('https://example.com/upload', data);
check(res, {
  'upload was successful': (r) => r.status === 201, // Check for a specific successful status code
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
const params = {
  tags: {
    name: 'FileUpload',
  },
};
http.post('https://example.com/upload', data, params);
```

### `script_09.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [70, 71, 72, 74, 88, 89, 90, 91, 92]
- **Snippet:**
```js
const res = http.post(restURI + '/insert_positions', body, {
        headers: headers,
      })

      myFailRate.add(res.status !== 204)
```
- **Refactored:**
```js
const res = http.post(restURI + '/insert_positions', body, {
        headers: headers,
      })

      const success = check(res, {
        'status is 204': (r) => r.status === 204,
        'response time < 1000ms': (r) => r.timings.duration < 1000,
      })
      myFailRate.add(!success)
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
        tags: { name: 'insert_positions', endpoint: '/insert_positions' },
      })
...
http.del(
    restURI + '/positions?title=eq.Load%20Tester',
    {},
    {
      headers: Object.assign(headers, { Prefer: 'count=exact' }),
      tags: { name: 'delete_positions', endpoint: '/positions' },
    }
  )
```

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
  headers,
  tags: { endpoint: 'insert_positions', operation: 'insert' },
})

check(res, {
  'insert_positions returns 204': (r) => r.status === 204,
})
myFailRate.add(res.status !== 204)

export function teardown(data) {
  const cleanupRes = http.del(
    restURI + '/positions?title=eq.Load%20Tester',
    {},
    {
      headers: { ...headers, Prefer: 'count=exact' },
      tags: { endpoint: 'positions', operation: 'cleanup' },
    }
  )

  check(cleanupRes, {
    'cleanup request succeeds': (r) => r.status >= 200 && r.status < 300,
  })
}
```

**Smell 4: Not using tags**

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
  headers,
  tags: { endpoint: 'insert_positions', operation: 'insert' },
})

myFailRate.add(res.status !== 204, {
  endpoint: 'insert_positions', operation: 'insert'
})

export function teardown(data) {
  http.del(
    restURI + '/positions?title=eq.Load%20Tester',
    {},
    {
      headers: { ...headers, Prefer: 'count=exact' },
      tags: { endpoint: 'positions', operation: 'cleanup' },
    }
  )
}
```

### `script_09.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [70, 71, 72, 74]
- **Snippet:**
```js
const res = http.post(restURI + '/insert_positions', body, {
  headers: headers,
})

myFailRate.add(res.status !== 204)
```
- **Refactored:**
```js
const res = http.post(restURI + '/insert_positions', body, {
  headers: headers,
});

const isSuccess = check(res, {
  'status is 204': (r) => r.status === 204,
});

myFailRate.add(!isSuccess);
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
    name: 'RPC-InsertPositions',
  },
})
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
});
```
- **Refactored:**
```js
postman[Request]({
  name: "Registration",
  method: "POST",
  address: "{{APIURL}}/users",
  tags: { endpoint: 'registration', group: 'Registration and Authentication' },
  ...
});
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
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks': ['rate>0.99']              // 99% of checks must pass
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [33]
- **Snippet:**
```js
options: { timeout: timeout },
```
- **Refactored:**
```js
      options: {
        timeout: timeout,
        tags: {
          name: "Registration",
          flow: "authentication"
        }
      },
```

### `script_100.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** []
- **Snippet:**
```js
No export const options with thresholds is defined anywhere in the provided code.
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
const ordersResponse = http.get(ordersUrl, { headers: this.headers, tags: { page: 'orders', endpoint: 'orders_all' } });
const ordersTableResponse = http.get(ordersTableUrl, { headers: this.headers, tags: { page: 'orders', endpoint: 'orders_table_data' } });
const orderDetailResponse = http.get(orderDetailUrl, { headers: this.headers, tags: { page: 'orders', endpoint: 'order_detail' } });
const itemListTableResponse = http.get(itemListTableUrl, { headers: this.headers, tags: { page: 'orders', endpoint: 'item_list_table' } });
const totalItemListResponse = http.get(totalItemListUrl, { headers: this.headers, tags: { page: 'orders', endpoint: 'total_item_list' } });
const triggerEventResponse = http.get(triggerEventUrl, { headers: this.headers, tags: { page: 'orders', endpoint: 'trigger_event', event } });
```

### `script_100.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1]
- **Snippet:**
```js
// The provided script file does not export an 'options' object with thresholds defined.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete within 500ms
    'http_req_failed': ['rate<0.01'],   // Error rate must be less than 1%
    'checks': ['rate>0.99'],           // Success rate of checks must be higher than 99%
  },
};

// ... existing script code
```

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
  tags: { name: 'OrdersPage-All' } 
});
```

### `script_101.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]
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
    const newCrocodileId = res.json().id;
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
        'has crocodile id': (r) => r.json().id !== undefined
    });

    const newCrocodileId = res.json().id;
```

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

- **Lines:** [107, 126]
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
    const newCrocodileId = res.json().id;
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
        'crocodile name': (r) => r.json().name === 'Random croc'
    });
    const newCrocodileId = res.json().id;
```

### `script_102.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 6]
- **Snippet:**
```js
export default class AbstractResource { ... }
```
- **Refactored:**
```js
Add a thresholds configuration in the exported 'options' object of the main script that uses this class. For example:

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [19, 32, 41, 50, 58]
- **Snippet:**
```js
const response = http.post(fullUrl, JSON.stringify(payload), { headers: this.headers });
const response = http.patch(fullUrl, JSON.stringify(payload), { headers: this.headers });
const response = http.del(fullUrl, null, { headers: this.headers });
const response = http.get(fullUrl, { headers: this.headers });
```
- **Refactored:**
```js
postRequest(resourceUrl, payload) {
  const fullUrl = `${EnvironmentUtil.getStorefrontApiUrl()}/${resourceUrl}`;
  const response = http.post(fullUrl, JSON.stringify(payload), {
    headers: this.headers,
    tags: { name: resourceUrl, method: 'POST' },
  });
  addErrorToCounter(check(response, { [`[POST] ${fullUrl} was successful.`]: (r) => r.status === 201 }));
  if (response.status !== 201) { console.log(response.body); }
  return response;
}

patchRequest(resourceUrl, payload) {
  const fullUrl = `${EnvironmentUtil.getStorefrontApiUrl()}/${resourceUrl}`;
  const response = http.patch(fullUrl, JSON.stringify(payload), {
    headers: this.headers,
    tags: { name: resourceUrl, method: 'PATCH' },
  });
  addErrorToCounter(check(response, { [`[PATCH] ${fullUrl} was successful.`]: (r) => r.status === 200 }));
  return response;
}

deleteRequest(resourceUrl) {
  const fullUrl = `${EnvironmentUtil.getStorefrontApiUrl()}/${resourceUrl}`;
  const response = http.del(fullUrl, null, {
    headers: this.headers,
    tags: { name: resourceUrl, method: 'DELETE' },
  });
  addErrorToCounter(check(response, { [`[DELETE] ${fullUrl} was successful.`]: (r) => r.status === 204 }));
  return response;
}

getRequest(resourceUrl) {
  const fullUrl = `${EnvironmentUtil.getStorefrontApiUrl()}/${resourceUrl}`;
  const response = http.get(fullUrl, {
    headers: this.headers,
    tags: { name: resourceUrl, method: 'GET' },
  });
  addErrorToCounter(check(response, { [`[GET] ${fullUrl} was successful.`]: (r) => r.status === 200 }));
  return response;
}
```

### `script_102.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** []
- **Snippet:**
```js
No export const options object with thresholds is defined in the provided k6 code.
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
      tags: { endpoint: 'dynamic-fixtures', operation: 'runConsoleCommands' },
    }
  );

  addErrorToCounter(check(response, {
    '[POST] dynamic-fixtures was successful.': (r) => r.status >= 200 && r.status < 300,
  }));

  return response;
}
```

**Smell 4: Not using tags**

- **Lines:** [19, 32, 41, 50, 58, 59, 60, 61, 62, 63, 64, 65]
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
    tags: { endpoint: resourceUrl, method: 'POST' },
  });
  addErrorToCounter(check(response, { [`[POST] ${fullUrl} was successful.`]: (r) => r.status === 201 }));
  return response;
}

patchRequest(resourceUrl, payload) {
  const fullUrl = `${EnvironmentUtil.getStorefrontApiUrl()}/${resourceUrl}`;
  const response = http.patch(fullUrl, JSON.stringify(payload), {
    headers: this.headers,
    tags: { endpoint: resourceUrl, method: 'PATCH' },
  });
  addErrorToCounter(check(response, { [`[PATCH] ${fullUrl} was successful.`]: (r) => r.status === 200 }));
  return response;
}

deleteRequest(resourceUrl) {
  const fullUrl = `${EnvironmentUtil.getStorefrontApiUrl()}/${resourceUrl}`;
  const response = http.del(fullUrl, null, {
    headers: this.headers,
    tags: { endpoint: resourceUrl, method: 'DELETE' },
  });
  addErrorToCounter(check(response, { [`[DELETE] ${fullUrl} was successful.`]: (r) => r.status === 204 }));
  return response;
}

getRequest(resourceUrl) {
  const fullUrl = `${EnvironmentUtil.getStorefrontApiUrl()}/${resourceUrl}`;
  const response = http.get(fullUrl, {
    headers: this.headers,
    tags: { endpoint: resourceUrl, method: 'GET' },
  });
  addErrorToCounter(check(response, { [`[GET] ${fullUrl} was successful.`]: (r) => r.status === 200 }));
  return response;
}
```

### `script_102.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1]
- **Snippet:**
```js
The script lacks an `export const options = { ... }` block with a `thresholds` definition to set pass/fail criteria for the test run. Without thresholds, the test will always be reported as successful in CI/CD environments, regardless of the system's performance.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks': ['rate>0.99'] // 99% of checks should pass
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [58, 67]
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
    const url = http.url`${EnvironmentUtil.getBackendApiUrl()}/dynamic-fixtures`;
    const response = http.post(
      url,
      JSON.stringify(this._getConsoleCommandsPayload(commands)),
      {
        headers: {
          'Content-Type': 'application/vnd.api+json',
        },
      }
    );

    check(response, {
      '[POST] /dynamic-fixtures was successful.': (r) => r.status === 200,
    });

    return response;
  }
```

**Smell 4: Not using tags**

- **Lines:** [19, 32, 41, 50, 58]
- **Snippet:**
```js
const response = http.get(fullUrl, { headers: this.headers });
```
- **Refactored:**
```js
const response = http.get(fullUrl, {
  headers: this.headers,
  tags: { 
    name: resourceUrl // Tagging with the resource URL helps filter results
  },
});
```

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
    let res1 = http.get('https://test.k6.io/assets.php');
    check(res1, { 'assets status is 200': (r) => r.status === 200 });
    let res2 = http.get('https://test.k6.io/assets.php');
    check(res2, { 'assets status is 200': (r) => r.status === 200 });
});
...
group('News page', function () {
    let res = http.get('https://test.k6.io/news.php');
    check(res, { 'news status is 200': (r) => r.status === 200 });
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
let res = http.get('https://test.k6.io', { tags: { name: 'main_page' } });
...
http.get('https://test.k6.io/assets.php', { tags: { name: 'assets' } });
http.get('https://test.k6.io/assets.php', { tags: { name: 'assets' } });
...
http.get('https://test.k6.io/news.php', { tags: { name: 'news_page' } });
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
let assetsRes1 = http.get('https://test.k6.io/assets.php', { tags: { endpoint: 'assets', page: 'main' } });
check(assetsRes1, { 'assets status is 200': (r) => r.status === 200 });

let assetsRes2 = http.get('https://test.k6.io/assets.php', { tags: { endpoint: 'assets', page: 'main' } });
check(assetsRes2, { 'assets status is 200': (r) => r.status === 200 });

let newsRes = http.get('https://test.k6.io/news.php', { tags: { endpoint: 'news', page: 'news' } });
check(newsRes, { 'news status is 200': (r) => r.status === 200 });
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
let res = http.get('https://test.k6.io', { tags: { endpoint: 'home', page: 'main' } });
check(res, { 'home status is 200': (r) => r.status === 200 }, { endpoint: 'home', page: 'main' });

let assetsRes1 = http.get('https://test.k6.io/assets.php', { tags: { endpoint: 'assets', page: 'main' } });
check(assetsRes1, { 'assets status is 200': (r) => r.status === 200 }, { endpoint: 'assets', page: 'main' });

let assetsRes2 = http.get('https://test.k6.io/assets.php', { tags: { endpoint: 'assets', page: 'main' } });
check(assetsRes2, { 'assets status is 200': (r) => r.status === 200 }, { endpoint: 'assets', page: 'main' });

let newsRes = http.get('https://test.k6.io/news.php', { tags: { endpoint: 'news', page: 'news' } });
check(newsRes, { 'news status is 200': (r) => r.status === 200 }, { endpoint: 'news', page: 'news' });
```

### `script_103.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [21, 22, 28]
- **Snippet:**
```js
http.get('https://test.k6.io/assets.php');
http.get('https://test.k6.io/assets.php');
// ...
http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
let res;
res = http.get('https://test.k6.io/assets.php');
check(res, { 'assets status is 200': (r) => r.status === 200 });

res = http.get('https://test.k6.io/news.php');
check(res, { 'news status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [17, 21, 22, 28]
- **Snippet:**
```js
let res = http.get('https://test.k6.io');
// ...
http.get('https://test.k6.io/assets.php');
http.get('https://test.k6.io/assets.php');
// ...
http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
let res = http.get('https://test.k6.io', { tags: { name: 'Homepage' } });
// ...
http.get('https://test.k6.io/assets.php', { tags: { name: 'Asset-1' } });
http.get('https://test.k6.io/assets.php', { tags: { name: 'Asset-2' } });
// ...
http.get('https://test.k6.io/news.php', { tags: { name: 'News' } });
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
  check(res, { 'status is 500': (r) => r.status == 500 }, { myTag: 'status500' });
```

### `script_104.js` — GEMINI

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
res = http.get('https://quickpizza.grafana.com/api/status/500', {
    tags: { name: 'GetStatus500' },
  });
  check(
    res,
    {
      'status is 500': (r) => r.status == 500,
    },
    { name: 'GetStatus500' }
  );
```

### `script_105.js` — CLAUDE

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
    'http_req_failed': ['rate<0.01'],
},
```

**Smell 4: Not using tags**

- **Lines:** [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]
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
```
- **Refactored:**
```js
const requests = {
    'Get root': {
        method: 'GET',
        url: urlRoot,
        params: { ...params, tags: { name: 'Get root', endpoint: 'root', server: server } }
    },
    'Get item one': {
        method: 'GET',
        url: urlItemOne,
        params: { ...params, tags: { name: 'Get item one', endpoint: 'itemOne', server: server } }
    },
    'Create item': {
        method: 'POST',
        url: urlCreate,
        params: { ...params, tags: { name: 'Create item', endpoint: 'create', server: server } },
        body: createItemData
    }
};
```

### `script_105.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [44, 45, 46, 47, 48, 56, 57, 58, 59, 60, 62, 63, 64, 65, 67, 68, 69, 70, 71, 75]
- **Snippet:**
```js
const params = {
    headers: {
    'Content-Type': 'application/json',
    },
};
...
const requests = {
    'Get root': { method: 'GET', url: urlRoot, params: params },
    'Get item one': { method: 'GET', url: urlItemOne, params: params },
    'Create item': { method: 'POST', url: urlCreate, params: params, body: createItemData }
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
            tags: { endpoint: 'root', operation: 'get_root', server },
        },
    },
    'Get item one': {
        method: 'GET',
        url: urlItemOne,
        params: {
            headers: baseHeaders,
            tags: { endpoint: 'item_one', operation: 'get_item', server },
        },
    },
    'Create item': {
        method: 'POST',
        url: urlCreate,
        params: {
            headers: baseHeaders,
            tags: { endpoint: 'items', operation: 'create_item', server },
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
        'Create_item_error': ['rate<0.01']
    },
```

**Smell 4: Not using tags**

- **Lines:** [56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73]
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
const params = {
    headers: {
        'Content-Type': 'application/json',
    },
    tags: { endpoint: 'root', server: server },
};

const paramsItem = {
    headers: {
        'Content-Type': 'application/json',
    },
    tags: { endpoint: 'item_one', server: server },
};

const paramsCreate = {
    headers: {
        'Content-Type': 'application/json',
    },
    tags: { endpoint: 'create_item', server: server },
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

**Smell 2: Do not use thresholds**

- **Lines:** [13, 14, 15, 16, 17, 18]
- **Snippet:**
```js
export const options = {
    thresholds: {
        'Show_root': ['p(95)<500'],
        'Show_item_one': ['p(95)<500'],
    },
};
```
- **Refactored:**
```js
export const options = {
    thresholds: {
        'Show_root': ['p(95)<500'],
        'Show_item_one': ['p(95)<500'],
        'Create_item': ['p(95)<500'],
        'Root_errors': ['rate<0.01'],
        'Item_errors': ['rate<0.01'],
        'Create_item_error': ['rate<0.01'],
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
    },
};
```

**Smell 1: Costly operations in the init context**

- **Lines:** [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
- **Snippet:**
```js
export default function () {
    const server = __ENV.SERVER;
    const urls = {
        fastapi: { ... },
        express: { ... },
        laravel: { ... }
    };
    const params = { headers: { 'Content-Type': 'application/json' } };
    const createItemData = JSON.stringify({ index: '3', name: 'Under pressure' });
    ...
}
```
- **Refactored:**
```js
// Move static data to the init context (outside the default function)
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
    headers: { 'Content-Type': 'application/json' },
};
const createItemData = JSON.stringify({ index: '3', name: 'Under pressure' });

export default function () {
    const urlRoot = urls[server].root;
    const urlItemOne = urls[server].itemOne;
    const urlCreate = urls[server].create;
    // ... rest of the function
}
```

### `script_106.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [45, 46, 47, 48, 49, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
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
            tags: { endpoint: 'root', operation: 'get_root' },
        },
    },
    'Get item one': {
        method: 'GET',
        url: urlItemOne,
        params: {
            headers: baseHeaders,
            tags: { endpoint: 'item_one', operation: 'get_item' },
        },
    },
    'Create item': {
        method: 'POST',
        url: urlCreate,
        body: createItemData,
        params: {
            headers: baseHeaders,
            tags: { endpoint: 'items', operation: 'create_item' },
        },
    },
};
```

### `script_106.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [14, 15, 16, 17]
- **Snippet:**
```js
export const options = {
    thresholds: {
        'Show_root': ['p(95)<500'],
        'Show_item_one': ['p(95)<500'],
    },
};
```
- **Refactored:**
```js
export const options = {
    thresholds: {
        'Show_root': ['p(95)<500'],
        'Show_item_one': ['p(95)<500'],
        'Create_item': ['p(95)<500'], // Added threshold for create operation
        'Root_errors': ['rate<0.01'],   // Added threshold for error rates
        'Item_errors': ['rate<0.01'],
        'Create_item_error': ['rate<0.01'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
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
```
- **Refactored:**
```js
const requests = {
    'Get root': {
        method: 'GET',
        url: urlRoot,
        params: { 
            headers: { 'Content-Type': 'application/json' },
            tags: { name: 'GetRoot' } 
        }
    },
    'Get item one': {
        method: 'GET',
        url: urlItemOne,
        params: { 
            headers: { 'Content-Type': 'application/json' },
            tags: { name: 'GetItemOne' } 
        }
    },
    'Create item': {
        method: 'POST',
        url: urlCreate,
        body: createItemData,
        params: { 
            headers: { 'Content-Type': 'application/json' },
            tags: { name: 'CreateItem' }
        }
    }
};
```

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
group('Assets', function () {
    let res1 = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
    check(res1, { 'Assets status 200': (r) => r.status === 200 });
    let res2 = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
    check(res2, { 'Assets status 200': (r) => r.status === 200 });
});

// Group: News page
group('News page', function () {
    let res = http.get('https://run.mocky.io/v3/9c2fd369-e719-4ee0-90d0-ffd889e2c8b5');
    check(res, { 'News page status is 200': (r) => r.status === 200 });
})
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
// Main page
let res = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms', { tags: { name: 'main_page' } });

// Assets
http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms', { tags: { name: 'asset_1' } });
http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms', { tags: { name: 'asset_2' } });

// News page
http.get('https://run.mocky.io/v3/9c2fd369-e719-4ee0-90d0-ffd889e2c8b5', { tags: { name: 'news_page' } });
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
const assetRes1 = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
check(assetRes1, { 'asset 1 status is 200': (r) => r.status === 200 });

const assetRes2 = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
check(assetRes2, { 'asset 2 status is 200': (r) => r.status === 200 });

const newsRes = http.get('https://run.mocky.io/v3/9c2fd369-e719-4ee0-90d0-ffd889e2c8b5');
check(newsRes, { 'news page status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [17, 21, 22, 28]
- **Snippet:**
```js
let res = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/9c2fd369-e719-4ee0-90d0-ffd889e2c8b5');
```
- **Refactored:**
```js
const mainPageParams = { tags: { page: 'main', endpoint: 'main_page', type: 'document' } };
const assetParams = { tags: { page: 'main', endpoint: 'main_asset', type: 'asset' } };
const newsPageParams = { tags: { page: 'news', endpoint: 'news_page', type: 'document' } };

let res = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms', mainPageParams);
check(res, { 'status is 200': (r) => r.status === 200 }, { page: 'main', endpoint: 'main_page' });

const assetRes1 = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms', assetParams);
check(assetRes1, { 'asset 1 status is 200': (r) => r.status === 200 }, { page: 'main', endpoint: 'main_asset' });

const assetRes2 = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms', assetParams);
check(assetRes2, { 'asset 2 status is 200': (r) => r.status === 200 }, { page: 'main', endpoint: 'main_asset' });

const newsRes = http.get('https://run.mocky.io/v3/9c2fd369-e719-4ee0-90d0-ffd889e2c8b5', newsPageParams);
check(newsRes, { 'news page status is 200': (r) => r.status === 200 }, { page: 'news', endpoint: 'news_page' });
```

### `script_107.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [21, 22, 28]
- **Snippet:**
```js
http.get('https://run.mocky.io/v3/9c2fd369-e719-4ee0-90d0-ffd889e2c8b5');
```
- **Refactored:**
```js
let newsRes = http.get('https://run.mocky.io/v3/9c2fd369-e719-4ee0-90d0-ffd889e2c8b5');
check(newsRes, { 'News page status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [17, 21, 22, 28]
- **Snippet:**
```js
let res = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms');
```
- **Refactored:**
```js
let res = http.get('https://run.mocky.io/v3/9b229fc9-64b5-4823-99b6-c9f1f6834fde?mocky-delay=900ms', {
  tags: { name: 'MainPageHTML' },
});
```

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
    check(res1, { 'Assets request 1 status is 200': (r) => r.status === 200 });
    let res2 = http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms');
    check(res2, { 'Assets request 2 status is 200': (r) => r.status === 200 });
});

group('News page', function () {
    let res = http.get('https://run.mocky.io/v3/46ac01d8-7d2d-4994-b594-4f359c79756d');
    check(res, { 'News page status is 200': (r) => r.status === 200 });
});
```

**Smell 4: Not using tags**

- **Lines:** [17, 21, 22, 28]
- **Snippet:**
```js
http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/46ac01d8-7d2d-4994-b594-4f359c79756d');
```
- **Refactored:**
```js
group('Main page', function () {
    let res = http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms', { tags: { name: 'main_page' } });
    check(res, { 'status is 200': (r) => r.status === 200 });

    group('Assets', function () {
        let res1 = http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms', { tags: { name: 'main_page_asset_1' } });
        check(res1, { 'Assets request 1 status is 200': (r) => r.status === 200 });
        let res2 = http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms', { tags: { name: 'main_page_asset_2' } });
        check(res2, { 'Assets request 2 status is 200': (r) => r.status === 200 });
    });
});

group('News page', function () {
    let res = http.get('https://run.mocky.io/v3/46ac01d8-7d2d-4994-b594-4f359c79756d', { tags: { name: 'news_page' } });
    check(res, { 'News page status is 200': (r) => r.status === 200 });
});
```

### `script_108.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [21, 22, 28]
- **Snippet:**
```js
http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/46ac01d8-7d2d-4994-b594-4f359c79756d');
```
- **Refactored:**
```js
group('Assets', function () {
    let assetRes1 = http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms');
    check(assetRes1, { 'asset 1 status is 200': (r) => r.status === 200 });

    let assetRes2 = http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms');
    check(assetRes2, { 'asset 2 status is 200': (r) => r.status === 200 });
});

group('News page', function () {
    let newsRes = http.get('https://run.mocky.io/v3/46ac01d8-7d2d-4994-b594-4f359c79756d');
    check(newsRes, { 'news page status is 200': (r) => r.status === 200 });
});
```

**Smell 4: Not using tags**

- **Lines:** [17, 21, 22, 28]
- **Snippet:**
```js
let res = http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms');
http.get('https://run.mocky.io/v3/46ac01d8-7d2d-4994-b594-4f359c79756d');
```
- **Refactored:**
```js
group('Main page', function () {
    let res = http.get(
        'https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms',
        { tags: { page: 'main', endpoint: 'main_page' } }
    );
    check(res, { 'status is 200': (r) => r.status === 200 }, { page: 'main', endpoint: 'main_page' });

    group('Assets', function () {
        let assetRes1 = http.get(
            'https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms',
            { tags: { page: 'main', endpoint: 'asset_1' } }
        );
        check(assetRes1, { 'asset 1 status is 200': (r) => r.status === 200 }, { page: 'main', endpoint: 'asset_1' });

        let assetRes2 = http.get(
            'https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms',
            { tags: { page: 'main', endpoint: 'asset_2' } }
        );
        check(assetRes2, { 'asset 2 status is 200': (r) => r.status === 200 }, { page: 'main', endpoint: 'asset_2' });
    });
});

group('News page', function () {
    let newsRes = http.get(
        'https://run.mocky.io/v3/46ac01d8-7d2d-4994-b594-4f359c79756d',
        { tags: { page: 'news', endpoint: 'news_page' } }
    );
    check(newsRes, { 'news page status is 200': (r) => r.status === 200 }, { page: 'news', endpoint: 'news_page' });
});
```

### `script_108.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [21, 22, 28]
- **Snippet:**
```js
http.get('https://run.mocky.io/v3/46ac01d8-7d2d-4994-b594-4f359c79756d');
```
- **Refactored:**
```js
let res = http.get('https://run.mocky.io/v3/46ac01d8-7d2d-4994-b594-4f359c79756d');
check(res, { 'status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [17, 21, 22, 28]
- **Snippet:**
```js
http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms');
```
- **Refactored:**
```js
http.get('https://run.mocky.io/v3/38f88596-c9ca-44d5-82b9-00a3c20f866f?mocky-delay=900ms', { tags: { name: 'asset' } });
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
		http_req_duration: ['p(95)<1000'],
		checks: ['rate>0.99'],
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

- **Lines:** []
- **Snippet:**
```js
// The script does not export an `options` object with a `thresholds` property, which is a file-level omission.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    'checks': ['rate>0.99'], // 99% of checks should pass
  },
};

export function checkoutCustomerLogin() { 
  // ... script content
}
```

### `script_11.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [99, 106, 132, 133, 134, 138, 139, 140, 146, 154, 155, 156, 162, 163, 164, 196, 197, 198, 204, 205, 206, 213, 219, 220, 221, 229, 233, 234, 262, 263, 264, 269, 270, 271, 302, 310, 311, 312, 319, 327, 328, 334, 341, 342, 343, 348, 349, 350, 376, 383, 384, 385, 390, 396, 397, 398, 404, 411, 412, 413, 419, 426, 427, 428]
- **Snippet:**
```js
let res = http.get(`${BASE_URL}/api/v1/dashboard`, { headers });
userActions.add(1);
actionSuccess.add(res.status === 200);
```
- **Refactored:**
```js
let res = http.get(`${BASE_URL}/api/v1/dashboard`, { headers });
userActions.add(1);
const dashboardOk = check(res, {
  'dashboard status is 200': (r) => r.status === 200,
  'dashboard response has body': (r) => r.body && r.body.length > 0,
});
actionSuccess.add(dashboardOk);
```

**Smell 4: Not using tags**

- **Lines:** [99, 132, 138, 146, 162, 196, 204, 213, 229, 262, 269, 302, 319, 334, 348, 376, 390, 404, 419]
- **Snippet:**
```js
let res = http.get(`${BASE_URL}/api/v1/dashboard`, { headers });

res = http.get(`${BASE_URL}/api/v1/assets?sort=-created_at&limit=20`, { headers });

const res = http.get(`${BASE_URL}/api/v1/search?q=${query}`, { headers });
```
- **Refactored:**
```js
let res = http.get(`${BASE_URL}/api/v1/dashboard`, {
  headers,
  tags: { name: 'dashboard', scenario: 'morning_surge', endpoint: 'GET /api/v1/dashboard' },
});

res = http.get(`${BASE_URL}/api/v1/assets?sort=-created_at&limit=20`, {
  headers,
  tags: { name: 'list_recent_assets', scenario: 'morning_surge', endpoint: 'GET /api/v1/assets' },
});

const res = http.get(`${BASE_URL}/api/v1/search?q=${query}`, {
  headers,
  tags: { name: 'search_assets', scenario: 'workday_activity', endpoint: 'GET /api/v1/search' },
});
```

### `script_11.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [99, 108, 132, 134, 138, 140, 146, 156, 162, 164, 196, 198, 204, 206, 213, 221, 229, 234, 262, 264, 269, 271, 302, 312, 319, 328, 334, 343, 348, 350, 376, 385, 390, 399, 404, 414, 419, 429]
- **Snippet:**
```js
const res = http.get(`${BASE_URL}/api/v1/dashboard`, { headers });
userActions.add(1);
actionSuccess.add(res.status === 200);
```
- **Refactored:**
```js
const tags = { endpoint: 'dashboard', flow: 'morning' };
const res = http.get(`${BASE_URL}/api/v1/dashboard`, { headers, tags });
const ok = check(res, {
  'dashboard returned 200': (r) => r.status === 200,
});
userActions.add(1, tags);
actionSuccess.add(ok, tags);

// Apply the same pattern to every HTTP request, including authentication:
function authenticate() {
  const tags = { endpoint: 'auth_login', flow: 'auth' };
  const loginRes = http.post(
    `${BASE_URL}/api/v1/auth/login`,
    JSON.stringify({
      email: `user${Math.floor(Math.random() * 1000)}@mams.local`,
      password: 'TestUser123!',
    }),
    { headers: { 'Content-Type': 'application/json' }, tags }
  );

  const ok = check(loginRes, {
    'login returned 200': (r) => r.status === 200,
    'login returned access token': (r) => Boolean(r.json('data.accessToken')),
  });

  return ok ? loginRes.json('data.accessToken') : null;
}
```

**Smell 4: Not using tags**

- **Lines:** [99, 105, 132, 138, 153, 162, 196, 204, 218, 229, 262, 269, 309, 325, 340, 348, 382, 396, 411, 426]
- **Snippet:**
```js
http.get(`${BASE_URL}/api/v1/assets/${assetId}`, { headers });
userActions.add(1);
actionSuccess.add(res.status === 200 || res.status === 404);
```
- **Refactored:**
```js
const tags = { endpoint: 'asset_details', flow: 'workday' };
const res = http.get(`${BASE_URL}/api/v1/assets/${assetId}`, { headers, tags });
const ok = check(res, {
  'asset details returned 200 or 404': (r) => r.status === 200 || r.status === 404,
});
userActions.add(1, tags);
actionSuccess.add(ok, tags);

// Reuse a helper to avoid repeating tags:
function requestParams(headers, endpoint, flow, extra = {}) {
  return {
    ...extra,
    headers,
    tags: { endpoint, flow },
  };
}

const searchTags = { endpoint: 'search', flow: 'workday' };
const searchRes = http.get(
  `${BASE_URL}/api/v1/search?q=${query}`,
  requestParams(headers, 'search', 'workday')
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
const success = check(res, {
  'Dashboard loaded successfully': (r) => r.status === 200,
});
userActions.add(1);
actionSuccess.add(success);
```

**Smell 4: Not using tags**

- **Lines:** [99, 132, 138, 146, 162]
- **Snippet:**
```js
let res = http.get(`${BASE_URL}/api/v1/dashboard`, { headers });
```
- **Refactored:**
```js
let res = http.get(`${BASE_URL}/api/v1/dashboard`, {
  headers,
  tags: {
    name: 'GetDashboard',
    scenario: 'morning_surge'
  }
});
```

### `script_110.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [54, 55, 56, 57]
- **Snippet:**
```js
let addToCart = http.post(cartParams);
console.log(cartParams);
console.log(addToCart.url);
console.log(addToCart.status);
```
- **Refactored:**
```js
let addToCart = http.post(cartParams);
console.log(cartParams);
console.log(addToCart.url);
console.log(addToCart.status);
check(addToCart, {
  'add to cart status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [20, 42, 54, 63]
- **Snippet:**
```js
let homepage = http.get('https://onlineboutique.dev');
...
let productLinkClick = http.get(productLink);
...
let addToCart = http.post(cartParams);
...
let checkout = http.post(checkoutLink);
```
- **Refactored:**
```js
let homepage = http.get('https://onlineboutique.dev', { tags: { name: 'homepage' } });
...
let productLinkClick = http.get(productLink, { tags: { name: 'product_page' } });
...
let addToCart = http.post(cartParams, null, { tags: { name: 'add_to_cart' } });
...
let checkout = http.post(checkoutLink, null, { tags: { name: 'checkout' } });
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
let homepage = http.get('https://onlineboutique.dev', { tags: { endpoint: 'home', flow: 'browse' } });
let productLinkClick = http.get(productLink, { tags: { endpoint: 'product', flow: 'browse' } });
let addToCart = http.post(cartParams, null, { tags: { endpoint: 'cart', flow: 'checkout' } });
let checkout = http.post(checkoutLink, null, { tags: { endpoint: 'checkout', flow: 'checkout' } });
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
  'Add to Cart - status is 200': (r) => r.status === 200,
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
  tags: { name: '01_Homepage' },
});

// ...

let productLinkClick = http.get(productLink, {
  tags: { name: '02_ProductPage' },
});

// ...

// For post requests with no body, the second argument must be null
let addToCart = http.post(cartParams, null, {
  tags: { name: '03_AddToCart' },
});

// ...

let checkout = http.post(checkoutLink, null, {
  tags: { name: '04_Checkout' },
});
```

### `script_111.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [19, 27, 34, 41]
- **Snippet:**
```js
const {buckets} = s3.listBuckets();
...
const {contents: b1Objects} = s3.listObjects({bucket: "bucket1"})
...
const {contents: b2Objects} = s3.listObjects({bucket: "bucket2"})
...
const {body} = s3.getObject({bucket: "bucket1", key: "file1.txt"})
```
- **Refactored:**
```js
// Add tags to each S3 operation to allow filtering and grouping of metrics
const {buckets} = s3.listBuckets({ tags: { operation: 'listBuckets' } });
...
const {contents: b1Objects} = s3.listObjects({ bucket: "bucket1", tags: { operation: 'listObjects', bucket: 'bucket1' } });
...
const {contents: b2Objects} = s3.listObjects({ bucket: "bucket2", tags: { operation: 'listObjects', bucket: 'bucket2' } });
...
const {body} = s3.getObject({ bucket: "bucket1", key: "file1.txt", tags: { operation: 'getObject', bucket: 'bucket1' } });
```

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
export default async function () {
	const s3 = new S3Client(config);

	const {buckets} = s3.listBuckets();
	check(buckets, {
		'it must return two buckets': (buckets) => buckets.length === 2,
		'bucket1 must be in the list': (buckets) => buckets.some(b => b.name.normalize() === "bucket1"),
		'bucket2 must be in the list': (buckets) => buckets.some(b => b.name.normalize() === "bucket2")
	}, {operation: 'listBuckets', resource: 's3'});

	const {contents: b1Objects} = s3.listObjects({bucket: "bucket1"});
	check(b1Objects, {
		'it must return one object': (b1Objects) => b1Objects.length === 1,
		'file1.txt must be in the list': (b1Objects) => b1Objects.some(obj => obj.key.normalize() === "file1.txt")
	}, {operation: 'listObjects', resource: 's3', bucket: 'bucket1'});

	const {contents: b2Objects} = s3.listObjects({bucket: "bucket2"});
	check(b2Objects, {
		'it must return one object': (b2Objects) => b2Objects.length === 1,
		'file2.txt must be in the list': (b2Objects) => b2Objects.some(obj => obj.key.normalize() === "file2.txt")
	}, {operation: 'listObjects', resource: 's3', bucket: 'bucket2'});

	const {body} = s3.getObject({bucket: "bucket1", key: "file1.txt"});
	const reader = body.getReader();
	const {value} = await reader.read();
	check(value, {
		'file1.txt contents are the expected ones': (value) => value === 'Hello, World'
	}, {operation: 'getObject', resource: 's3', bucket: 'bucket1', key: 'file1.txt'});
}
```

### `script_111.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [20, 28, 35, 44]
- **Snippet:**
```js
check(buckets, {
			'it must return two buckets': (buckets) => buckets.length === 2,
			'bucket1 must be in the list': (buckets) => buckets.some(b => b.name.normalize() === "bucket1"),
			'bucket2 must be in the list': (buckets) => buckets.some(b => b.name.normalize() === "bucket1")
		}
	);
```
- **Refactored:**
```js
check(buckets, {
			'it must return two buckets': (buckets) => buckets.length === 2,
			'bucket1 must be in the list': (buckets) => buckets.some(b => b.name.normalize() === "bucket1"),
			'bucket2 must be in the list': (buckets) => buckets.some(b => b.name.normalize() === "bucket2")
		},
		{ operation: 'list_buckets' }
	);
```

### `script_112.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [57, 71]
- **Snippet:**
```js
response = http.get('https://doctor.mountsinai.org/fad/autocomplete/lite', {
      headers: {
        // ... headers
      },
    })
```
- **Refactored:**
```js
response = http.get('https://doctor.mountsinai.org/fad/autocomplete/lite', {
      // ... headers
    })
    check(response, {
      'autocomplete status is 200': (r) => r.status === 200,
    })
```

**Smell 4: Not using tags**

- **Lines:** [57, 71]
- **Snippet:**
```js
response = http.get('https://doctor.mountsinai.org/fad/autocomplete/lite', {
      headers: {
        // ... headers
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
        // ... headers
      },
    })
```

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
}, { tags: { name: 'login', endpoint: '/auth/token/login/' } });
...
const myObjects = http.get(`${BASE_URL}/my/crocodiles/`, Object.assign({}, authHeaders, { tags: { name: 'getCrocodiles', endpoint: '/my/crocodiles/' } })).json();
```

### `script_113.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [66, 87]
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
const loginRes = http.post(
  `${BASE_URL}/auth/token/login/`,
  {
    username: USERNAME,
    password: PASSWORD,
  },
  {
    tags: { endpoint: 'login', flow: 'auth' },
  }
);

const authHeaders = {
  headers: {
    Authorization: `Bearer ${loginRes.json('access')}`,
  },
  tags: { endpoint: 'my_crocodiles', flow: 'authenticated_user' },
};

const myObjects = http.get(`${BASE_URL}/my/crocodiles/`, authHeaders).json();
```

### `script_113.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [75, 87]
- **Snippet:**
```js
check(loginRes, {
  'logged in successfully': (resp) => resp.json('access') !== '',
});
...
const myObjects = http.get(`${BASE_URL}/my/crocodiles/`, authHeaders).json();
```
- **Refactored:**
```js
check(loginRes, {
  'login status is 200': (r) => r.status === 200,
  'has access token': (r) => r.json('access') !== '',
});

const myCrocsRes = http.get(`${BASE_URL}/my/crocodiles/`, authHeaders);
check(myCrocsRes, {
  'get crocodiles status is 200': (r) => r.status === 200,
  'retrieved crocodiles': (r) => r.json().length > 0,
});
```

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
const loginPayload = JSON.stringify({
  username: USERNAME,
  password: PASSWORD,
});
const loginParams = {
  headers: { 'Content-Type': 'application/json' },
  tags: { name: 'Login' },
};
const loginRes = http.post(`${BASE_URL}/auth/token/login/`, loginPayload, loginParams);

const authParams = {
  headers: {
    Authorization: `Bearer ${loginRes.json('access')}`,
  },
  tags: { name: 'GetCrocodiles' },
};
const myCrocsRes = http.get(`${BASE_URL}/my/crocodiles/`, authParams);
```

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
}, { tags: { name: 'login', endpoint: '/auth/token/login/' } });
...
const myObjects = http.get(`${BASE_URL}/my/crocodiles/`, {
  ...authHeaders,
  tags: { name: 'getCrocodiles', endpoint: '/my/crocodiles/' },
}).json();
```

### `script_114.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [46, 67]
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
const loginRes = http.post(
  `${BASE_URL}/auth/token/login/`,
  {
    username: USERNAME,
    password: PASSWORD,
  },
  {
    tags: { endpoint: 'login', flow: 'auth' },
  }
);

check(loginRes, {
  'logged in successfully': (resp) => resp.json('access') !== '',
}, { endpoint: 'login', flow: 'auth' });

const authHeaders = {
  headers: {
    Authorization: `Bearer ${loginRes.json('access')}`,
  },
  tags: { endpoint: 'my_crocodiles', flow: 'authenticated_user' },
};

const crocodilesRes = http.get(`${BASE_URL}/my/crocodiles/`, authHeaders);
const myObjects = crocodilesRes.json();

check(myObjects, {
  'retrieved crocodiles': (obj) => obj.length > 0,
}, { endpoint: 'my_crocodiles', flow: 'authenticated_user' });
```

### `script_114.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [55, 67]
- **Snippet:**
```js
check(loginRes, {
  'logged in successfully': (resp) => resp.json('access') !== '',
});
...
const myObjects = http.get(`${BASE_URL}/my/crocodiles/`, authHeaders).json();
```
- **Refactored:**
```js
check(loginRes, {
  'login status is 200': (r) => r.status === 200,
  'has access token': (r) => r.json('access') !== '',
});
...
const myCrocsRes = http.get(`${BASE_URL}/my/crocodiles/`, authHeaders);
check(myCrocsRes, {
  'get crocodiles status is 200': (r) => r.status === 200,
  'retrieved crocodiles': (r) => r.json().length > 0,
});
```

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
const loginRes = http.post(
  `${BASE_URL}/auth/token/login/`,
  JSON.stringify({ username: USERNAME, password: PASSWORD }),
  {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'Login' },
  }
);
...
const authParams = {
  headers: {
    Authorization: `Bearer ${loginRes.json('access')}`,
  },
  tags: { name: 'GetCrocodiles' },
};
const myObjectsRes = http.get(`${BASE_URL}/my/crocodiles/`, authParams);
```

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
		http_req_failed: ['rate<0.01'],
		http_req_duration: ['p(95)<500'],
		'checks': ['rate>0.99'],
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
// No export const options with thresholds is defined in the script.
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
	wpLogin();
}
```

### `script_115.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [26]
- **Snippet:**
```js
// The script does not export an `options` object, so no performance thresholds are defined.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    // No more than 1% of requests should fail.
    'http_req_failed': ['rate<0.01'],
    // 95% of requests must finish within 500ms.
    'http_req_duration': ['p(95)<500'],
    // Checks should have a success rate of at least 99%.
    'checks': ['rate>0.99'],
  },
};
```

### `script_116.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [43, 44, 45, 55, 56, 57, 58, 59, 60, 71, 72, 73, 74, 75, 76, 77]
- **Snippet:**
```js
let courseRes = http.get(`${BASE_URL}/api/courses`, {
  headers: { Authorization: `Bearer ${token}` },
});
...
let orderRes = http.post(`${BASE_URL}/api/orders`, payload, {
  headers: { ... },
});
...
let balRes = http.get(`${BASE_URL}/api/payments/balance`, {
  headers: { ... },
});
```
- **Refactored:**
```js
let courseRes = http.get(`${BASE_URL}/api/courses`, {
  headers: { Authorization: `Bearer ${token}` },
  tags: { name: 'get_courses', role: role, endpoint: '/api/courses' },
});
...
let orderRes = http.post(`${BASE_URL}/api/orders`, payload, {
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${token}`,
  },
  tags: { name: 'create_order', role: 'customer', endpoint: '/api/orders' },
});
...
let balRes = http.get(`${BASE_URL}/api/payments/balance`, {
  headers: {
    Authorization: `Bearer ${token}`,
    'X-User-Id': 'sm8SaZl5PxOJSapuwlS5fce4KS53',
    'X-User-Role': 'prophet',
  },
  tags: { name: 'get_balance', role: 'prophet', endpoint: '/api/payments/balance' },
});
```

### `script_116.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [43, 46, 47, 55, 61, 64, 65, 66, 71, 78]
- **Snippet:**
```js
let courseRes = http.get(`${BASE_URL}/api/courses`, { headers: { Authorization: `Bearer ${token}` } });
check(courseRes, { 'get courses status 200': (r) => r.status === 200 });
courseTrend.add(courseRes.timings.duration);
```
- **Refactored:**
```js
// GET courses
const courseTags = { endpoint: '/api/courses', operation: 'get_courses', role };
let courseRes = http.get(`${BASE_URL}/api/courses`, {
  headers: { Authorization: `Bearer ${token}` },
  tags: courseTags,
});
check(courseRes, { 'get courses status 200': (r) => r.status === 200 }, courseTags);
courseTrend.add(courseRes.timings.duration, courseTags);

// CREATE order (customer)
if (!isProphet) {
  const orderTags = { endpoint: '/api/orders', operation: 'create_order', role: 'customer' };
  const payload = JSON.stringify({
    courseId: 'test-course-id',
    roomId: 'test-room-id',
  });
  let orderRes = http.post(`${BASE_URL}/api/orders`, payload, {
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${token}`,
    },
    tags: orderTags,
  });
  check(orderRes, {
    'order create ok': (r) => r.status === 201 || r.status === 200,
  }, orderTags)
    ? successCount.add(1, orderTags)
    : failCount.add(1, orderTags);
  orderTrend.add(orderRes.timings.duration, orderTags);
}

// GET prophet balance
if (isProphet) {
  const balanceTags = { endpoint: '/api/payments/balance', operation: 'get_balance', role: 'prophet' };
  let balRes = http.get(`${BASE_URL}/api/payments/balance`, {
    headers: {
      Authorization: `Bearer ${token}`,
      'X-User-Id': 'sm8SaZl5PxOJSapuwlS5fce4KS53',
      'X-User-Role': 'prophet',
    },
    tags: balanceTags,
  });
  check(balRes, { 'get balance ok': (r) => r.status === 200 }, balanceTags);
}
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
let courseRes = http.get(`${BASE_URL}/api/courses`, {
    headers: { Authorization: `Bearer ${token}` },
    tags: { name: 'GetCourses' }, // Tag added to group metrics for this endpoint
  });
```

### `script_117.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 191]
- **Snippet:**
```js
export class HttpClient { ... }
```
- **Refactored:**
```js
// Add thresholds to the exported options object or in the script that uses this HttpClient
export const options = {
  thresholds: {
    http_req_duration: ['p(95)<500', 'p(99)<1000'],
    http_req_failed: ['rate<0.01'],
    checks: ['rate>0.99']
  }
};

export class HttpClient { ... }
```

### `script_117.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 11]
- **Snippet:**
```js
import http from 'k6/http';
import { check, fail } from 'k6';

export class HttpClient {
```
- **Refactored:**
```js
import http from 'k6/http';
import { check, fail } from 'k6';

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99']
  }
};

export class HttpClient {
  // existing implementation
}
```

### `script_117.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [54, 82]
- **Snippet:**
```js
tags: params.tags || {}
...
const result = check(response, {
  [checkName]: checkFn
});
```
- **Refactored:**
```js
// Refactor the HttpClient class to automatically tag requests and checks for better analysis.

// 1. Update buildParams to accept 'path' and add it as a default 'name' tag.
buildParams(params = {}, path) {
  const result = {
    headers: { ...this.headers, ...(params.headers || {}) },
    timeout: params.timeout || this.timeout,
    tags: { name: path, ...(params.tags || {}) },
  };
  // ... rest of the function remains the same
  return result;
}

// 2. Update validateResponse to pass the request's tags to the check.
validateResponse(response, method, url, options = {}) {
  // ...
  const result = check(response, {
    [checkName]: checkFn
  }, options.tags); // Pass tags to the check function
  // ... rest of the function remains the same
}

// 3. Update the main request method to pass the necessary parameters.
request(method, path, body = null, params = {}) {
  const url = this.buildUrl(path);
  const requestParams = this.buildParams(params, path); // Pass path for tagging
  
  // ... http.request call using requestParams ...
  
  this.validateResponse(response, method, url, requestParams); // Pass full params with tags
  
  return response;
}
```

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
// In setup():
export function setup() {
  initPools(); // runs once globally, not once per VU
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
import { generateEvent, generateMetricRequest, generateBulkEvents, loadPools } from './lib/data-generator.js';

// Load or build large data pools once per k6 process and share them across VUs.
const dataPools = new SharedArray('data-pools', () => loadPools());

export default function (data) {
  const event = generateEvent(data.timestampMode, dataPools);
  const bulkRequest = generateBulkEvents(200, data.timestampMode, dataPools);
  const metricsQuery = generateMetricRequest(rangeType, dataPools);
}
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
The `initPools()` function is called in the init context, causing it to run once for every virtual user. This is inefficient and can significantly increase memory usage and test startup time. It should be moved to the `setup` function, which runs only once before the test begins.

javascript
// Remove line 14
// initPools();

export function setup() {
  console.log('=== Stress Test Configuration ===');
  initPools(); // Move initialization here to run once for the test

  const baseUrl = __ENV.BASE_URL || 'http://localhost:50051';
  // ... rest of setup code
}

```

### `script_119.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 154]
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
		http_req_duration: ['p(95)<2000'],
		'http_req_duration{name:"Shopper - wc-ajax=add_to_cart"}': ['p(95)<2000'],
		'http_req_duration{name:"Shopper - View Cart"}': ['p(95)<2000'],
		'http_req_duration{name:"Shopper - wc-ajax=apply_coupon"}': ['p(95)<2000'],
		'http_req_duration{name:"Shopper - Update Cart"}': ['p(95)<2000'],
	},
};

export default function () {
	cartApplyCoupon();
}
```

### `script_119.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [32, 152]
- **Snippet:**
```js
export function cartApplyCoupon() {
...
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
	},
};

export function cartApplyCoupon() {
	// existing function body
}

export default function () {
	cartApplyCoupon();
}
```

### `script_119.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [31]
- **Snippet:**
```js
import { getDefaultProduct } from '../../utils.js';

export function cartApplyCoupon() {
```
- **Refactored:**
```js
import { getDefaultProduct } from '../../utils.js';

export const options = {
	thresholds: {
		'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
		'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
	},
};

export function cartApplyCoupon() {
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
// Move mobileNumber generation, payload construction, and file reading inside the default function
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
    // open() must remain in init context as it is only allowed there,
    // but avoid heavy JSON.stringify or random generation in init context.
    // ...
}
```

**Smell 4: Not using tags**

- **Lines:** [43, 50, 64, 72, 110, 122, 134, 141, 148, 158, 170, 176, 195, 210]
- **Snippet:**
```js
const sendOtpResponse = http.post(`${baseUrl}/users/v1/public/send-otp`, sentPayload, { headers });
const verifyOtp = http.post(`${baseUrl}/users/v1/public/verify-otp`, verifyPayload, { headers });
const profileGet = http.get(`${baseUrl}/users/v1/profile`, { headers });
// ... all other http calls lack tags
```
- **Refactored:**
```js
// Add tags to each request to enable filtering and grouping in metrics
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

const profilePatch = http.patch(
    `${baseUrl}/users/v1/profile`,
    JSON.stringify({ "name": "SaloniS" }),
    { headers, tags: { name: 'profile-patch', group: 'Personal Details' } }
);
// ... apply similar tags to all remaining http calls
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
Move the file opening to the `setup` lifecycle function, which runs only once before the test. Then, pass the data to the default function.

export function setup() {
  const fileData = open('./download.pdf', 'b');
  return { file: fileData };
}

export default function(data) {
  //... inside 'Health Records' group
  const fd = new FormData();
  fd.append("type", "health_records");
  fd.append("file", http.file(data.file, 'download.pdf', 'application/pdf'));
  //...
}
```

**Smell 4: Not using tags**

- **Lines:** [134, 141, 148, 195, 210]
- **Snippet:**
```js
const getdownloadToken = http.get(`${baseUrl}/uploads/v1/download/download-token?customerDocumentId=${customerDocumentId}`,
            { headers });
```
- **Refactored:**
```js
Add a `name` tag to group requests with dynamic URL parameters. This prevents high-cardinality tags and improves metric aggregation.

const getdownloadToken = http.get(`${baseUrl}/uploads/v1/download/download-token?customerDocumentId=${customerDocumentId}`,
    {
        headers,
        tags: { name: '/uploads/v1/download/download-token' }
    });
```

### `script_120.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [167]
- **Snippet:**
```js
'profile update responds': (r) => r.status === 200 || r.status === 400,
```
- **Refactored:**
```js
'profile update status is 200': (r) => r.status === 200,
```

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
		http_req_failed: ['rate<0.01'],
		http_req_duration: ['p(95)<2000'],
		'http_req_duration{name:"Shopper - My Account Login Page"}': ['p(95)<2000'],
		'http_req_duration{name:"Shopper - Login to My Account"}': ['p(95)<2000'],
		'http_req_duration{name:"Shopper - wc-ajax=get_refreshed_fragments"}': ['p(95)<2000'],
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
		http_req_duration: ['p(95)<500'],
		checks: ['rate>0.99'],
	},
};

export default function () {
	myAccount();
}
```

**Smell 4: Not using tags**

- **Lines:** [102, 103, 104, 105, 106, 107, 108]
- **Snippet:**
```js
response = http.post(
	`${ base_url }/?wc-ajax=get_refreshed_fragments`,
	{
		headers: requestHeadersPost,
		tags: { name: 'Shopper - wc-ajax=get_refreshed_fragments' },
	}
);
```
- **Refactored:**
```js
response = http.post(
	`${ base_url }/?wc-ajax=get_refreshed_fragments`,
	null,
	{
		headers: requestHeadersPost,
		tags: { name: 'Shopper - wc-ajax=get_refreshed_fragments' },
	}
);
```

### `script_121.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [117]
- **Snippet:**
```js
export default function () {
	myAccount();
}
```
- **Refactored:**
```js
import { sleep, check, group } from 'k6';
// ... other imports

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
    checks: ['rate>0.99'], // 99% of checks should pass
  },
};

export function myAccount() {
  // ... rest of the code
```

### `script_122.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [36, 74, 101]
- **Snippet:**
```js
const loginRes = http.post(`${baseUrl}/api/auth/login`, loginPayload, {
  headers: { 'Content-Type': 'application/json' },
  timeout: '10s',
});
...
const getUserRes = http.get(`${baseUrl}/api/auth/me`, {
  headers: authHeaders,
  timeout: '10s',
});
...
const updateRes = http.put(`${baseUrl}/api/users`, JSON.stringify(updateData), {
  headers: authHeaders,
  timeout: '10s',
});
```
- **Refactored:**
```js
const loginRes = http.post(`${baseUrl}/api/auth/login`, loginPayload, {
  headers: { 'Content-Type': 'application/json' },
  timeout: '10s',
  tags: { name: 'login', endpoint: '/api/auth/login', flow: 'auth' },
});
...
const getUserRes = http.get(`${baseUrl}/api/auth/me`, {
  headers: authHeaders,
  timeout: '10s',
  tags: { name: 'get_user', endpoint: '/api/auth/me', flow: 'user' },
});
...
const updateRes = http.put(`${baseUrl}/api/users`, JSON.stringify(updateData), {
  headers: authHeaders,
  timeout: '10s',
  tags: { name: 'update_user', endpoint: '/api/users', flow: 'user' },
});
```

### `script_122.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [36, 37, 38, 39, 43, 54, 74, 75, 76, 77, 79, 90, 101, 102, 103, 104, 106, 110]
- **Snippet:**
```js
const loginRes = http.post(`${baseUrl}/api/auth/login`, loginPayload, {
  headers: { 'Content-Type': 'application/json' },
  timeout: '10s',
});

check(loginRes, { ... });

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
const loginTags = { flow: 'Login', endpoint: 'POST /api/auth/login' };
const loginRes = http.post(`${baseUrl}/api/auth/login`, loginPayload, {
  headers: { 'Content-Type': 'application/json' },
  timeout: '10s',
  tags: loginTags,
});
check(loginRes, {
  'login status is 200/201': (r) => r.status === 200 || r.status === 201,
  'login response time < 5000ms': (r) => r.timings.duration < 5000,
  'has access token': (r) => {
    try {
      const body = r.json();
      return body && body.access_token !== undefined;
    } catch (e) {
      return false;
    }
  },
}, loginTags);

const getUserTags = { flow: 'Get User', endpoint: 'GET /api/auth/me' };
const getUserRes = http.get(`${baseUrl}/api/auth/me`, {
  headers: authHeaders,
  timeout: '10s',
  tags: getUserTags,
});
check(getUserRes, {
  'get user status is 200': (r) => r.status === 200,
  'get user response time < 3000ms': (r) => r.timings.duration < 3000,
  'user has profile data': (r) => {
    try {
      const profile = r.json();
      return profile && profile.id !== undefined;
    } catch (e) {
      return false;
    }
  },
}, getUserTags);

const updateUserTags = { flow: 'Update User', endpoint: 'PUT /api/users' };
const updateRes = http.put(`${baseUrl}/api/users`, JSON.stringify(updateData), {
  headers: authHeaders,
  timeout: '10s',
  tags: updateUserTags,
});
check(updateRes, {
  'update user successful': (r) => r.status === 200 || r.status === 400,
  'update user response time < 3000ms': (r) => r.timings.duration < 3000,
  'update user handled': (r) => r.status !== 500,
}, updateUserTags);
```

### `script_122.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [36, 74, 101]
- **Snippet:**
```js
const loginRes = http.post(`${baseUrl}/api/auth/login`, loginPayload, {
  headers: { 'Content-Type': 'application/json' },
  timeout: '10s',
});
```
- **Refactored:**
```js
/*
 Although `group` automatically adds a 'group' tag, explicitly tagging each request with a unique name provides more granular control for filtering and analyzing results.
*/

// Refactored login request (line 36)
const loginRes = http.post(`${baseUrl}/api/auth/login`, loginPayload, {
  headers: { 'Content-Type': 'application/json' },
  timeout: '10s',
  tags: { name: 'Login' },
});

// Refactored get user request (line 74)
const getUserRes = http.get(`${baseUrl}/api/auth/me`, {
  headers: authHeaders,
  timeout: '10s',
  tags: { name: 'GetUser' },
});

// Refactored update user request (line 101)
const updateRes = http.put(`${baseUrl}/api/users`, JSON.stringify(updateData), {
  headers: authHeaders,
  timeout: '10s',
  tags: { name: 'UpdateUser' },
});
```

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
    { headers, tags: { name: 'direct_rest_payload', endpoint: '/camel/api/payload', service: 'main_service' } }
  );

  const clientResponse = http.post(
    `${CLIENT_BASE_URL}/api/benchmark/rest`,
    JSON.stringify(payload),
    { headers, tags: { name: 'client_rest_benchmark', endpoint: '/api/benchmark/rest', service: 'client_service' } }
  );
```

### `script_123.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [64, 67, 70, 71, 73, 80, 83, 87, 90, 93]
- **Snippet:**
```js
const directResponse = http.post(
  `${MAIN_SERVICE_URL}/camel/api/payload`,
  JSON.stringify(payload),
  { headers }
);

restRequests.add(1);
restResponseTime.add(directResponse.timings.duration);

const directSuccess = check(directResponse, { ... });

const clientResponse = http.post(
  `${CLIENT_BASE_URL}/api/benchmark/rest`,
  JSON.stringify(payload),
  { headers }
);

const clientSuccess = check(clientResponse, { ... });
```
- **Refactored:**
```js
const directTags = {
  service: 'main-service',
  endpoint: '/camel/api/payload',
  protocol: 'REST',
};

const directResponse = http.post(
  `${MAIN_SERVICE_URL}/camel/api/payload`,
  JSON.stringify(payload),
  { headers, tags: directTags }
);

restRequests.add(1, directTags);
restResponseTime.add(directResponse.timings.duration, directTags);

const directSuccess = check(directResponse, {
  'Direct REST status is 200': (r) => r.status === 200,
  'Direct REST response time < 3000ms': (r) => r.timings.duration < 3000,
  'Direct REST has response': (r) => r.body && r.body.length > 0,
}, directTags);

if (!directSuccess) {
  restErrorRate.add(1, directTags);
  console.log(`Direct REST failed: ${directResponse.status} - ${directResponse.body}`);
} else {
  restErrorRate.add(0, directTags);
}

const clientTags = {
  service: 'client-service',
  endpoint: '/api/benchmark/rest',
  protocol: 'REST',
};

const clientResponse = http.post(
  `${CLIENT_BASE_URL}/api/benchmark/rest`,
  JSON.stringify(payload),
  { headers, tags: clientTags }
);

const clientSuccess = check(clientResponse, {
  'Client REST status is 200': (r) => r.status === 200,
  'Client REST response time < 5000ms': (r) => r.timings.duration < 5000,
  'Client REST has valid response': (r) => {
    try {
      const data = JSON.parse(r.body);
      return data.restResult && data.restResult.success === true;
    } catch (e) {
      return false;
    }
  },
}, clientTags);
```

### `script_123.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [64, 70, 71, 80, 83, 87]
- **Snippet:**
```js
  // Test direct REST endpoint
  const directResponse = http.post(
    `${MAIN_SERVICE_URL}/camel/api/payload`,
    JSON.stringify(payload),
    { headers }
  );

  restRequests.add(1);
  restResponseTime.add(directResponse.timings.duration);

  // ...

  // Test client service REST endpoint
  const clientResponse = http.post(
    `${CLIENT_BASE_URL}/api/benchmark/rest`,
    JSON.stringify(payload),
    { headers }
  );
```
- **Refactored:**
```js
  // Test direct REST endpoint
  const directTags = { name: 'DirectREST', endpoint: 'main_service' };
  const directResponse = http.post(
    `${MAIN_SERVICE_URL}/camel/api/payload`,
    JSON.stringify(payload),
    { headers, tags: directTags }
  );

  restRequests.add(1, directTags);
  restResponseTime.add(directResponse.timings.duration, directTags);

  // ...

  // Test client service REST endpoint
  const clientTags = { name: 'ClientREST', endpoint: 'client_service' };
  const clientResponse = http.post(
    `${CLIENT_BASE_URL}/api/benchmark/rest`,
    JSON.stringify(payload),
    { headers, tags: clientTags }
  );
```

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
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    'checks': ['rate>0.99']
  }
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
const response = http.get(url.toString(), { tags: { name: 'search_customer', endpoint: '/api/customer/fake/search' } });
```

### `script_124.js` — CHATGPT

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

- **Lines:** [12, 15]
- **Snippet:**
```js
const response = http.get(url.toString());
const customers = response.json();

check(customers, {
```
- **Refactored:**
```js
const response = http.get(url.toString(), {
  tags: { endpoint: 'customer_fake_search', flow: 'customer_search' }
});

check(response, {
  'status is 200': (r) => r.status === 200,
  'response is JSON': (r) => r.headers['Content-Type'] && r.headers['Content-Type'].includes('application/json')
});

const customers = response.json();

check(customers, {
  'All customers have a full name': (c) => c.every(customer => customer['full-name']),
  'All full names contain the search string (case-insensitive)': (c) => c.every(customer => customer['full-name'].toLowerCase().includes(nameToSearch.toLowerCase()))
});
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
    endpoint: 'customer_fake_search',
    flow: 'customer_search'
  }
});
```

### `script_124.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 6]
- **Snippet:**
```js
// The script is missing an 'options' export to define test thresholds.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'checks': ['rate>0.99']
  },
};

// The rest of the script follows...
```

**Smell 3: Not checking requests**

- **Lines:** [12, 15]
- **Snippet:**
```js
const response = http.get(url.toString());
const customers = response.json();

check(customers, {
```
- **Refactored:**
```js
const response = http.get(url.toString());

check(response, {
  'is status 200': (r) => r.status === 200,
});

if (response.status === 200) {
  const customers = response.json();
  check(customers, {
    'All customers have a full name': (c) =>
      c.every((customer) => customer['full-name']),
    'All full names contain the search string (case-insensitive)': (c) =>
      c.every((customer) =>
        customer['full-name'].toLowerCase().includes(nameToSearch.toLowerCase())
      ),
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
  tags: {
    name: 'SearchCustomersByName',
  },
});
```

### `script_125.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
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
const res = http.get('https://quickpizza.grafana.com/api/cookies', { tags: { name: 'get_cookies', endpoint: '/api/cookies' } });
```

### `script_125.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [1, 18]
- **Snippet:**
```js
// No export const options = { thresholds: ... } is defined in this script
```
- **Refactored:**
```js
import http from 'k6/http';
import { check } from 'k6';

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
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
  const res = http.get('https://quickpizza.grafana.com/api/cookies');

  check(res, {
    'has status 200': (r) => r.status === 200,
    'cookie has correct value': (r) => r.json().cookies.my_cookie == 'hello world',
  });
}
```

**Smell 4: Not using tags**

- **Lines:** [12, 14]
- **Snippet:**
```js
const res = http.get('https://quickpizza.grafana.com/api/cookies');

check(res, {
  'has status 200': (r) => r.status === 200,
  'cookie has correct value': (r) => r.json().cookies.my_cookie == 'hello world',
});
```
- **Refactored:**
```js
const tags = { endpoint: 'cookies', flow: 'cookie_validation' };
const res = http.get('https://quickpizza.grafana.com/api/cookies', { tags });

check(res, {
  'has status 200': (r) => r.status === 200,
  'cookie has correct value': (r) => r.json().cookies.my_cookie == 'hello world',
}, tags);
```

### `script_125.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
- **Snippet:**
```js
// The script lacks an 'options' export with a 'thresholds' object.
```
- **Refactored:**
```js
import http from 'k6/http';
import { check } from 'k6';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'checks': ['rate>0.99'],           // the rate of successful checks should be higher than 99%
  },
};

export default function () { ... }
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
    tags: { name: 'GetCookiesAPI' },
  });
```

### `script_126.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
- **Snippet:**
```js
export function contacts(baseUrl) { ... }
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
  group('Contacts flow', function () {
    let res = http.get(`${baseUrl}/contacts.php`);
    contactsLatency.add(res.timings.duration);
    sleep(1);

    res = http.get(`${baseUrl}/`);
    contactsLatency.add(res.timings.duration);
    sleep(1);
  });
}
```

**Smell 3: Not checking requests**

- **Lines:** [10, 15]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/contacts.php`);
    res = http.get(`${baseUrl}/`);
```
- **Refactored:**
```js
import { check } from 'k6';

// Inside the group:
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
    res = http.get(`${baseUrl}/`);
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/contacts.php`, { tags: { name: 'contacts_page', flow: 'contacts' } });
contactsLatency.add(res.timings.duration, { name: 'contacts_page' });
sleep(1);

res = http.get(`${baseUrl}/`, { tags: { name: 'home_page', flow: 'contacts' } });
contactsLatency.add(res.timings.duration, { name: 'home_page' });
sleep(1);
```

### `script_126.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** []
- **Snippet:**
```js
No export const options with thresholds is defined in the provided code.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    contact_duration: ['p(95)<500'],
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
import { group, sleep, check } from 'k6';

let res = http.get(`${baseUrl}/contacts.php`);
check(res, {
  'contacts page status is 200': (r) => r.status === 200,
});

res = http.get(`${baseUrl}/`);
check(res, {
  'home page status is 200': (r) => r.status === 200,
});
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
let res = http.get(`${baseUrl}/contacts.php`, {
  tags: { flow: 'contacts', endpoint: 'contacts_page' },
});
contactsLatency.add(res.timings.duration, { flow: 'contacts', endpoint: 'contacts_page' });

res = http.get(`${baseUrl}/`, {
  tags: { flow: 'contacts', endpoint: 'home_page' },
});
contactsLatency.add(res.timings.duration, { flow: 'contacts', endpoint: 'home_page' });
```

### `script_126.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 20]
- **Snippet:**
```js
The script does not export an `options` object, and therefore defines no success criteria (thresholds) for the test.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'contact_duration': ['p(90) < 800'], // 90% of requests for this flow should be below 800ms
  },
};

```

**Smell 3: Not checking requests**

- **Lines:** [10, 15]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/contacts.php`);
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
let res = http.get(`${baseUrl}/contacts.php`);
check(res, { 'status is 200': (r) => r.status === 200 });
```

**Smell 4: Not using tags**

- **Lines:** [10, 12, 15, 17]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/contacts.php`);
// add duration property to metric
contactsLatency.add(res.timings.duration);
```
- **Refactored:**
```js
// By adding tags to requests, you can filter metrics for each specific endpoint.

let res = http.get(`${baseUrl}/contacts.php`, {
  tags: { endpoint: 'contacts' },
});
// ...
res = http.get(`${baseUrl}/`, {
  tags: { endpoint: 'homepage' },
});
```

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
}), { headers: { 'Content-Type': 'application/json' }, tags: { name: 'login', endpoint: '/api/user/login' } });

const res = http.get(`${DEFAULT_URL}/amount`, { headers, tags: { name: 'getUserPoints', endpoint: '/amount' } });
```

### `script_127.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [10, 12, 24]
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
const loginRes = http.post(`${DEFAULT_URL}/api/user/login`, JSON.stringify({
  name: '백현명'
}), {
  headers: { 'Content-Type': 'application/json' },
  tags: { endpoint: 'login', flow: 'auth' }
});

const res = http.get(`${DEFAULT_URL}/amount`, {
  headers,
  tags: { endpoint: 'amount', flow: 'point_charge' }
});
```

### `script_127.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5]
- **Snippet:**
```js
export {options};
```
- **Refactored:**
```js
export const options = {
  // ... other existing options from ../common/option.js
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
    'checks': ['rate>0.99']
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [10, 24]
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
const loginRes = http.post(`${DEFAULT_URL}/api/user/login`, JSON.stringify({
    name: '백현명'
  }), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'Login' }
  });

//...

const res = http.get(`${DEFAULT_URL}/amount`, {
    headers,
    tags: { name: 'GetAmount' }
  });
```

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
const healthRes = http.get(`${BASE_URL}/health`, { tags: { name: 'health_check', endpoint: '/health' } })
  const predictionRes = http.request('POST', `${BASE_URL}/project-predict`, payload, { tags: { name: 'project_predict', endpoint: '/project-predict' } })
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
const healthParams = { tags: { endpoint: 'health', flow: 'healthcheck' } };
const healthRes = http.get(`${BASE_URL}/health`, healthParams);
check(healthRes, {
  'is 200': (r) => r.status === 200
}, { endpoint: 'health', flow: 'healthcheck' });

const payload = JSON.stringify(generator(CACHE_RATE));
const predictionParams = {
  tags: { endpoint: 'project-predict', flow: 'prediction' },
  headers: { 'Content-Type': 'application/json' }
};
const predictionRes = http.request('POST', `${BASE_URL}/project-predict`, payload, predictionParams);
check(predictionRes, {
  'is 200': (r) => r.status === 200
}, { endpoint: 'project-predict', flow: 'prediction' });
```

### `script_128.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [46, 52]
- **Snippet:**
```js
const healthRes = http.get(`${BASE_URL}/health`)
// ...
const predictionRes = http.request('POST', `${BASE_URL}/project-predict`, payload)
```
- **Refactored:**
```js
export default () => {
  const healthRes = http.get(`${BASE_URL}/health`, {
    tags: { name: 'HealthCheck' },
  });
  check(healthRes, {
    'is 200': (r) => r.status === 200
  });

  const payload = JSON.stringify(generator(CACHE_RATE));
  const params = {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'Prediction' },
  };
  const predictionRes = http.request('POST', `${BASE_URL}/project-predict`, payload, params);
  check(predictionRes, {
    'is 200': (r) => r.status === 200
  });
};
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
  tags: { name: 'GetAllCrocodiles' },
});
// ...
const res2 = http.get('https://test-api.k6.io/public/crocodiles/1/', {
  tags: { name: 'GetCrocodileByID' },
});
```

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
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<2000'],
    checks: ['rate>0.99']
  }
};
```

**Smell 3: Not checking requests**

- **Lines:** [30, 93, 140, 200, 250, 303, 356, 410, 463, 516, 569]
- **Snippet:**
```js
postman[Request]({
  name: "Registration",
  ...
  post(response) {
    var is201Response = responseCode.code === 201;
    tests["Response code is 201 OK - Registration"] = is201Response;
    ...
  }
});
```
- **Refactored:**
```js
postman[Request]({
  name: "Registration",
  ...
  post(response) {
    var is201Response = responseCode.code === 201;
    tests["Response code is 201 OK - Registration"] = is201Response;
    check(response, {
      'Registration status is 201': () => responseCode.code === 201,
    });
    ...
  }
});
```

**Smell 4: Not using tags**

- **Lines:** [30, 93, 140, 200, 250, 303, 356, 410, 463, 516, 569]
- **Snippet:**
```js
postman[Request]({
  name: "Registration",
  method: "POST",
  address: "{{APIURL}}/users",
  headers: { ... },
  ...
});
```
- **Refactored:**
```js
postman[Request]({
  name: "Registration",
  method: "POST",
  address: "{{APIURL}}/users",
  headers: { ... },
  tags: { endpoint: 'registration', flow: 'auth', method: 'POST' },
  ...
});
```

### `script_13.js` — CHATGPT

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
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99']
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [30, 93, 140, 200, 250, 303, 356, 410, 463, 516, 569]
- **Snippet:**
```js
postman[Request]({
  name: "Registration",
  method: "POST",
  options: { timeout: timeout },
  address: "{{APIURL}}/users"
});
```
- **Refactored:**
```js
postman[Request]({
  name: "Registration",
  method: "POST",
  options: {
    timeout: timeout,
    tags: {
      flow: "registration_and_authentication",
      endpoint: "registration",
      operation: "create_user"
    }
  },
  address: "{{APIURL}}/users"
});

postman[Request]({
  name: "Login and Remember Token",
  method: "POST",
  options: {
    timeout: timeout,
    tags: {
      flow: "registration_and_authentication",
      endpoint: "login",
      operation: "authenticate_user"
    }
  },
  address: "{{APIURL}}/users/login"
});
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
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks': ['rate>0.99']             // 99% of checks should pass
  }
};
```

**Smell 3: Not checking requests**

- **Lines:** [69, 71, 74]
- **Snippet:**
```js
var is201Response = responseCode.code === 201;

        tests["Response code is 201 OK - Registration"] = is201Response;
        
        if (!environment.isIntegrationTest && is201Response) {
          var responseJSON = JSON.parse(responseBody);
```
- **Refactored:**
```js
post(response) {
        const is201Response = check(response, {
          "Response code is 201 OK - Registration": (r) => r.status === 201,
        });

        if (is201Response) {
          const responseJSON = response.json();

          check(responseJSON, {
            'Response contains "user" property': (json) => json.hasOwnProperty("user"),
          });
        }
      }
```

**Smell 4: Not using tags**

- **Lines:** [30, 31, 33]
- **Snippet:**
```js
postman[Request]({
      name: "Registration",
      id: "2024-02-23-06-45-22-022",
      method: "POST",
```
- **Refactored:**
```js
import http from 'k6/http';

// ... inside default function ...

const url = `${pm.globals.get('APIURL')}/users`;
const payload = JSON.stringify({
  user: {
    email: pm.globals.get('EMAIL'),
    password: pm.globals.get('PASSWORD'),
    username: pm.globals.get('USERNAME'),
  },
});
const params = {
  headers: {
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
  },
  tags: {
    name: 'Registration', // For backward compatibility with dashboards
    endpoint: '/users',
  },
};

const res = http.post(url, payload, params);
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
const response2 = http.get('https://test-api.k6.io/public/crocodiles/1/', { tags: { name: 'get_crocodile_by_id', endpoint: '/public/crocodiles/1/' } });
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

### `script_130.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [14]
- **Snippet:**
```js
const response1 = http.get('https://test-api.k6.io/public/crocodiles/');
```
- **Refactored:**
```js
const response1 = http.get('https://test-api.k6.io/public/crocodiles/', { tags: { name: 'GetAllCrocodiles' } });
```

**Smell 4: Not using tags**

- **Lines:** [22]
- **Snippet:**
```js
const response2 = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
const response2 = http.get('https://test-api.k6.io/public/crocodiles/1/', { tags: { name: 'GetCrocodileById' } });
```

### `script_131.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [66, 81]
- **Snippet:**
```js
let response = http.get(`${BASE_URL}/health`);
...
response = http.post(`${BASE_URL}/orders`, JSON.stringify(order), {
```
- **Refactored:**
```js
let response = http.get(`${BASE_URL}/health`, { tags: { name: 'health_check', endpoint: '/health' } });
...
response = http.post(`${BASE_URL}/orders`, JSON.stringify(order), {
  headers: {
    'Content-Type': 'application/json',
  },
  tags: { name: 'create_order', endpoint: '/orders' },
});
```

### `script_131.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [66, 67, 73, 81, 87, 101]
- **Snippet:**
```js
let response = http.get(`${BASE_URL}/health`);
let healthCheckPassed = check(response, { ... });
errorRate.add(1);
response = http.post(`${BASE_URL}/orders`, JSON.stringify(order), { headers: { 'Content-Type': 'application/json' } });
const orderSuccess = check(response, { ... });
```
- **Refactored:**
```js
const healthTags = { endpoint: 'health', method: 'GET', flow: 'create_order' };
let response = http.get(`${BASE_URL}/health`, { tags: healthTags });
let healthCheckPassed = check(response, {
  'health check status is 200': (r) => r.status === 200,
  'health check response time < 500ms': (r) => r.timings.duration < 500,
}, healthTags);

if (!healthCheckPassed) {
  errorRate.add(1, healthTags);
  sleep(1);
  return;
}

const orderTags = { endpoint: 'orders', method: 'POST', flow: 'create_order' };
response = http.post(`${BASE_URL}/orders`, JSON.stringify(order), {
  headers: {
    'Content-Type': 'application/json',
  },
  tags: orderTags,
});

const orderSuccess = check(response, {
  'order creation status is 201 or 422': (r) => r.status === 201 || r.status === 422,
  'order creation response time < 10s': (r) => r.timings.duration < 10000,
  'response has valid JSON': (r) => {
    try {
      JSON.parse(r.body);
      return true;
    } catch (e) {
      return false;
    }
  },
}, orderTags);

if (!orderSuccess) {
  errorRate.add(1, orderTags);
}
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

### `script_133.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
- **Snippet:**
```js
export function coinflip(baseUrl) { ... }
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'coinflip_duration': ['p(95)<500', 'avg<300'],
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
// ...
res = http.get(`${baseUrl}/flip_coin.php?bet=tails`);
```
- **Refactored:**
```js
import { check, group, sleep } from 'k6';

// ...

group('Coinflip game', function () {
  let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`);
  check(res, {
    'heads: status is 200': (r) => r.status === 200,
    'heads: body contains result': (r) => r.body && r.body.length > 0,
  });
  coinflipLatency.add(res.timings.duration);
  sleep(1);
  res = http.get(`${baseUrl}/flip_coin.php?bet=tails`);
  check(res, {
    'tails: status is 200': (r) => r.status === 200,
    'tails: body contains result': (r) => r.body && r.body.length > 0,
  });
  coinflipLatency.add(res.timings.duration);
  sleep(1);
});
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
let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`, {
  tags: { name: 'flip_coin_heads', bet: 'heads' },
});
coinflipLatency.add(res.timings.duration, { bet: 'heads' });
sleep(1);
res = http.get(`${baseUrl}/flip_coin.php?bet=tails`, {
  tags: { name: 'flip_coin_tails', bet: 'tails' },
});
coinflipLatency.add(res.timings.duration, { bet: 'tails' });
sleep(1);
```

### `script_133.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** []
- **Snippet:**
```js
No export const options = { thresholds: ... } is defined in the provided code.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    coinflip_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [10, 15]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`);
res = http.get(`${baseUrl}/flip_coin.php?bet=tails`);
```
- **Refactored:**
```js
import { group, sleep, check } from 'k6';

export function coinflip(baseUrl) {
  group('Coinflip game', function () {
    let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`);
    check(res, {
      'heads response status is 200': (r) => r.status === 200,
      'heads response body is not empty': (r) => r.body && r.body.length > 0,
    });

    coinflipLatency.add(res.timings.duration);
    sleep(1);

    res = http.get(`${baseUrl}/flip_coin.php?bet=tails`);
    check(res, {
      'tails response status is 200': (r) => r.status === 200,
      'tails response body is not empty': (r) => r.body && r.body.length > 0,
    });

    coinflipLatency.add(res.timings.duration);
    sleep(1);
  });
}
```

**Smell 4: Not using tags**

- **Lines:** [10, 12, 15, 17]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`);
coinflipLatency.add(res.timings.duration);
res = http.get(`${baseUrl}/flip_coin.php?bet=tails`);
coinflipLatency.add(res.timings.duration);
```
- **Refactored:**
```js
export function coinflip(baseUrl) {
  group('Coinflip game', function () {
    let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`, {
      tags: { endpoint: 'flip_coin', bet: 'heads', flow: 'coinflip' },
    });
    coinflipLatency.add(res.timings.duration, { endpoint: 'flip_coin', bet: 'heads', flow: 'coinflip' });
    sleep(1);

    res = http.get(`${baseUrl}/flip_coin.php?bet=tails`, {
      tags: { endpoint: 'flip_coin', bet: 'tails', flow: 'coinflip' },
    });
    coinflipLatency.add(res.timings.duration, { endpoint: 'flip_coin', bet: 'tails', flow: 'coinflip' });
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

export let options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'coinflip_duration': ['p(90)<400'], // 90% of coinflip actions should be below 400ms
  },
};

const coinflipLatency = new Trend('coinflip_duration');

export function coinflip(baseUrl) { // ...
```

**Smell 3: Not checking requests**

- **Lines:** [10, 15]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`);
```
- **Refactored:**
```js
import http from 'k6/http';
import { Trend } from 'k6/metrics';
import { group, sleep, check } from 'k6';

//...

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
```

**Smell 4: Not using tags**

- **Lines:** [12, 17]
- **Snippet:**
```js
coinflipLatency.add(res.timings.duration);
```
- **Refactored:**
```js
// ...
  group('Coinflip game', function () {
    let res = http.get(`${baseUrl}/flip_coin.php?bet=heads`);
    // add duration property and a tag to the metric
    coinflipLatency.add(res.timings.duration, { bet: 'heads' });
    sleep(1);

    res = http.get(`${baseUrl}/flip_coin.php?bet=tails`);
    // add duration property and a tag to the metric
    coinflipLatency.add(res.timings.duration, { bet: 'tails' });
    sleep(1);
  });
// ...
```

### `script_134.js` — CLAUDE

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
    'http_req_duration{group:::requisição por id}': ['p(95) < 500'],
    'http_req_failed': ['rate < 0.01'],
    'http_req_duration': ['p(95) < 500']
  }
```

**Smell 4: Not using tags**

- **Lines:** [14, 22]
- **Snippet:**
```js
const response1 = http.get('http://test-api.k6.io/public/crocodiles/')
...
const response2 = http.get('http://test-api.k6.io/public/crocodiles/1/')
```
- **Refactored:**
```js
const response1 = http.get('http://test-api.k6.io/public/crocodiles/', { tags: { name: 'get_all_crocodiles', endpoint: '/public/crocodiles/' } })
...
const response2 = http.get('http://test-api.k6.io/public/crocodiles/1/', { tags: { name: 'get_crocodile_by_id', endpoint: '/public/crocodiles/:id' } })
```

### `script_134.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [14, 22]
- **Snippet:**
```js
const response1 = http.get('http://test-api.k6.io/public/crocodiles/')
const response2 = http.get('http://test-api.k6.io/public/crocodiles/1/')
```
- **Refactored:**
```js
const response1 = http.get('http://test-api.k6.io/public/crocodiles/', {
  tags: { endpoint: 'get_all_crocodiles', flow: 'crocodiles' }
})
check(response1, {
  'status code é 200 get all': (res) => res.status === 200
}, { endpoint: 'get_all_crocodiles', flow: 'crocodiles' })

const response2 = http.get('http://test-api.k6.io/public/crocodiles/1/', {
  tags: { endpoint: 'get_crocodile_by_id', flow: 'crocodiles' }
})
check(response2, {
  'status code é 200 get id': (res) => res.status === 200
}, { endpoint: 'get_crocodile_by_id', flow: 'crocodiles' })
```

### `script_134.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [14, 22]
- **Snippet:**
```js
const response1 = http.get('http://test-api.k6.io/public/crocodiles/')
// ...
const response2 = http.get('http://test-api.k6.io/public/crocodiles/1/')
```
- **Refactored:**
```js
// Request 1 refactored
const response1 = http.get('http://test-api.k6.io/public/crocodiles/', {
  tags: { name: 'GetAllCrocodiles' },
});

// Request 2 refactored
const response2 = http.get('http://test-api.k6.io/public/crocodiles/1/', {
  tags: { name: 'GetCrocodileById' },
});
```

### `script_136.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 27]
- **Snippet:**
```js
export default function() { ... }
```
- **Refactored:**
```js
export let options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    'checks': ['rate>0.99'],
  },
};
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
let response = http.get('https://test.k6.io/my_messages.php', { tags: { name: 'get_messages', endpoint: 'my_messages' } });
...
response = http.post('http://test.k6.io/login.php', { login: username, password: password, csrftoken: csrfToken }, { tags: { name: 'post_login', endpoint: 'login' } });
```

### `script_136.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [1, 27]
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
    checks: ['rate>0.95'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [9, 10, 22, 23]
- **Snippet:**
```js
let response = http.get('https://test.k6.io/my_messages.php');
check(response, { ... });
response = http.post('http://test.k6.io/login.php', { login: username, password: password, csrftoken: csrfToken });
check(response, { ... });
```
- **Refactored:**
```js
const messagesTags = { endpoint: 'my_messages', flow: 'auth' };
let response = http.get('https://test.k6.io/my_messages.php', { tags: messagesTags });
check(response, {
  'is Unauthorized': r => r.body.includes('Unauthorized'),
}, messagesTags);

const loginTags = { endpoint: 'login', flow: 'auth' };
response = http.post(
  'http://test.k6.io/login.php',
  { login: username, password: password, csrftoken: csrfToken },
  { tags: loginTags }
);
check(response, {
  'is status 200': r => r.status === 200,
  'Successful login': r => r.body.includes('successfully authorized'),
}, loginTags);
```

### `script_136.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 27]
- **Snippet:**
```js
The script is missing an `export const options` block with a `thresholds` property to define pass/fail criteria for the test.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    'checks': ['rate>0.99'], // 99% of checks must succeed
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [9, 22]
- **Snippet:**
```js
let response = http.get('https://test.k6.io/my_messages.php');
// ...
response = http.post('http://test.k6.io/login.php', { login: username, password: password, csrftoken: csrfToken });
```
- **Refactored:**
```js
let response = http.get('https://test.k6.io/my_messages.php', {
  tags: { name: 'GetMessagesPage' },
});
// ...
response = http.post(
  'http://test.k6.io/login.php',
  { login: username, password: password, csrftoken: csrfToken },
  { tags: { name: 'LoginPage' } }
);
```

### `script_137.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
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
    'checks': ['rate>0.99'],
  },
};

export default function () {
```

**Smell 4: Not using tags**

- **Lines:** [5]
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
    tags: { name: 'set_cookie', endpoint: '/api/cookies' },
  });
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
    tags: { endpoint: 'set_cookie', flow: 'cookies' },
  });
  const jar = http.cookieJar();
  const cookies = jar.cookiesForURL('https://quickpizza.grafana.com/api/cookies');
  check(res, {
    'has cookie my_cookie': () => cookies.my_cookie.length > 0,
    'cookie has correct value': () => cookies.my_cookie[0] === 'hello world',
  }, { endpoint: 'set_cookie', flow: 'cookies' });
}
```

**Smell 4: Not using tags**

- **Lines:** [5, 6, 7, 10, 11, 12, 13]
- **Snippet:**
```js
const res = http.post('https://quickpizza.grafana.com/api/cookies?my_cookie=hello%20world', {
  redirects: 0,
});
...
check(res, {
  'has cookie \'my_cookie\'': () => cookies.my_cookie.length > 0,
  'cookie has correct value': () => cookies.my_cookie[0] === 'hello world',
});
```
- **Refactored:**
```js
const res = http.post('https://quickpizza.grafana.com/api/cookies?my_cookie=hello%20world', null, {
  redirects: 0,
  tags: { endpoint: 'set_cookie', flow: 'cookies' },
});

check(res, {
  'has cookie my_cookie': () => cookies.my_cookie.length > 0,
  'cookie has correct value': () => cookies.my_cookie[0] === 'hello world',
}, { endpoint: 'set_cookie', flow: 'cookies' });
```

### `script_137.js` — GEMINI

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
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<200'], // 95% of requests should be below 200ms
  },
};

export default function () {
```

**Smell 3: Not checking requests**

- **Lines:** [10, 11, 12, 13]
- **Snippet:**
```js
check(res, {
    'has cookie \'my_cookie\'': () => cookies.my_cookie.length > 0,
    'cookie has correct value': () => cookies.my_cookie[0] === 'hello world',
  });
```
- **Refactored:**
```js
check(res, {
    'status is 200': (r) => r.status === 200,
    'has cookie \'my_cookie\'': () => cookies.my_cookie.length > 0,
    'cookie has correct value': () => cookies.my_cookie[0] === 'hello world',
  });
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
    tags: { name: 'SetCookieAPI' },
  });
```

### `script_138.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 63]
- **Snippet:**
```js
// No 'export const options = { thresholds: { ... } }' defined anywhere in the file
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

### `script_138.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [16]
- **Snippet:**
```js
No k6 options.thresholds are defined in the script.
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

### `script_138.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1]
- **Snippet:**
```js
The script does not export an `options` object with a `thresholds` property. Without thresholds, the test provides no clear pass/fail criteria, which can lead to false confidence in performance, especially in automated CI/CD pipelines.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    // No more than 1% of requests should fail.
    http_req_failed: ['rate<0.01'],
    // 95% of requests should complete within 800ms.
    http_req_duration: ['p(95)<800'],
  },
};

/* ... The rest of the script follows ... */
```

### `script_140.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [34, 50]
- **Snippet:**
```js
let res = http.get('https://test.k6.io/' + (execution.scenario.iterationInTest === 7 ? 'foo': ''));
  res = http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
let res = http.get('https://test.k6.io/' + (execution.scenario.iterationInTest === 7 ? 'foo' : ''), { tags: { name: 'home_page' } });
  res = http.get('https://test.k6.io/news.php', { tags: { name: 'news_page' } });
```

**Smell 3: Not checking requests**

- **Lines:** [50, 53]
- **Snippet:**
```js
res = http.get('https://test.k6.io/news.php');

  // updating custom metric, newsPageResponse
  newsPageResponseTrend.add(res.timings.duration);
```
- **Refactored:**
```js
res = http.get('https://test.k6.io/news.php', { tags: { name: 'news_page' } });

  check(res, {
    'news page status is 200': (r) => r.status === 200,
    'news page contains expected content': (r) => r.body.includes('News')
  });

  // updating custom metric, newsPageResponse
  newsPageResponseTrend.add(res.timings.duration);
```

### `script_140.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [50]
- **Snippet:**
```js
res = http.get('https://test.k6.io/news.php');
```
- **Refactored:**
```js
res = http.get('https://test.k6.io/news.php', { tags: { endpoint: 'news' } });
check(res, {
  'news page status is 200': (r) => r.status === 200,
  'news page body is not empty': (r) => r.body && r.body.length > 0
}, { endpoint: 'news' });
newsPageResponseTrend.add(res.timings.duration, { endpoint: 'news' });
```

**Smell 4: Not using tags**

- **Lines:** [34, 40, 43, 50, 53]
- **Snippet:**
```js
let res = http.get('https://test.k6.io/' + (execution.scenario.iterationInTest === 7 ? 'foo': ''));
myCounter.add(1)
check(res, { ... });
res = http.get('https://test.k6.io/news.php');
newsPageResponseTrend.add(res.timings.duration);
```
- **Refactored:**
```js
let endpoint = execution.scenario.iterationInTest === 7 ? 'foo' : 'home';
let res = http.get(`https://test.k6.io/${endpoint === 'foo' ? 'foo' : ''}`, {
  tags: { endpoint }
});

myCounter.add(1, { endpoint });

check(res, {
  'response status is 200': (r) => r.status === 200,
  'page contains expected message': (r) => r.body.includes('Collection of simple web-pages suitable for load testing.')
}, { endpoint });

sleep(1);

res = http.get('https://test.k6.io/news.php', {
  tags: { endpoint: 'news' }
});

check(res, {
  'news page status is 200': (r) => r.status === 200,
  'news page body is not empty': (r) => r.body && r.body.length > 0
}, { endpoint: 'news' });

newsPageResponseTrend.add(res.timings.duration, { endpoint: 'news' });
```

### `script_140.js` — GEMINI

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
  tags: { name: 'homepage' },
});
...
res = http.get('https://test.k6.io/news.php', {
  tags: { name: 'news' },
});
```

### `script_143.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4]
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
    'checks': ['rate>0.99']
  }
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
const res = http.get('https://dummyjson.com/todos', { tags: { name: 'semua_todo', endpoint: '/todos' } })
...
const res = http.get('https://dummyjson.com/todos/'+i, { tags: { name: 'detail_todo', endpoint: '/todos/:id' } })
```

### `script_143.js` — CHATGPT

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
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99']
  }
}

export default function () {
  // test logic
}
```

**Smell 4: Not using tags**

- **Lines:** [6, 8, 15, 17]
- **Snippet:**
```js
const res = http.get('https://dummyjson.com/todos')
check(res, {
  'statusnya 200': r => r.status === 200
})

const res = http.get('https://dummyjson.com/todos/'+i)
check(res, {
  'request detail statusnya 200': r => r.status === 200
})
```
- **Refactored:**
```js
group('semua todo', function () {
  const tags = { endpoint: 'todos', flow: 'semua_todo' }
  const res = http.get('https://dummyjson.com/todos', { tags })

  check(res, {
    'statusnya 200': r => r.status === 200
  }, tags)
})

group('detail todo', function () {
  for (let i = 0; i < 5; i++) {
    const tags = { endpoint: 'todo_detail', flow: 'detail_todo', todo_id: String(i) }
    const res = http.get('https://dummyjson.com/todos/' + i, { tags })

    check(res, {
      'request detail statusnya 200': r => r.status === 200
    }, tags)
  }
})
```

### `script_143.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 23]
- **Snippet:**
```js
The script does not export an `options` object with a `thresholds` property. Without thresholds, the test will always pass in a CI/CD environment, regardless of the system's performance.
```
- **Refactored:**
```js
import { check, group } from 'k6'
import http from 'k6/http'

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
    'checks': ['rate>0.99'],
  },
};

export default function () {
  // ... rest of the script
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
const getAllTodosRes = http.get('https://dummyjson.com/todos', {
  tags: { name: 'GetAllTodos' },
});
...
const getTodoByIdRes = http.get(`https://dummyjson.com/todos/${i}`, {
  tags: { name: 'GetTodoByID' },
});
```

### `script_144.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 66]
- **Snippet:**
```js
The entire script defines no 'export const options = { thresholds: { ... } }' block anywhere in the code.
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
  tags: { name: 'GET /cart', endpoint: 'cart' },
});

// In addItem():
let params = {
  redirects: 0,
  tags: { name: 'POST /cart/add/:sku', endpoint: 'cart_add' },
};
if (this.headers) {
  params.headers = this.headers;
}
const response = http.post(`${EnvironmentUtil.getStorefrontUrl()}/cart/add/${sku}`, payload, params);
```

### `script_144.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [1, 66]
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

- **Lines:** [16, 30, 31, 32, 38]
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
    tags: { endpoint: 'cart_get', flow: 'cart' },
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
    tags: { endpoint: 'cart_add', flow: 'cart', sku },
  };

  if (this.headers) {
    params.headers = this.headers;
  }

  const response = http.post(`${EnvironmentUtil.getStorefrontUrl()}/cart/add/${sku}`, payload, params);

  addErrorToCounter(
    check(response, {
      [`Add item to cart [${EnvironmentUtil.getStorefrontUrl()}/cart/add/${sku}] was successful`]: (r) =>
        r.status === 302 && r.body,
    })
  );

  return response;
}
```

### `script_144.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** []
- **Snippet:**
```js
The provided code is missing the exported 'options' object where thresholds are defined. Without thresholds, the test will always pass in a CI/CD environment, regardless of the system's performance.
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

**Smell 4: Not using tags**

- **Lines:** [16, 38]
- **Snippet:**
```js
const response = http.get(`${EnvironmentUtil.getStorefrontUrl()}/cart`, { headers: this.headers });
// ...
const response = http.post(`${EnvironmentUtil.getStorefrontUrl()}/cart/add/${sku}`, payload, params);
```
- **Refactored:**
```js
get() {
    const params = {
        headers: this.headers,
        tags: { name: 'getCart' },
    };
    const response = http.get(`${EnvironmentUtil.getStorefrontUrl()}/cart`, params);
    // ...
}

addItem(sku, token, productOfferReference = null) {
    // ...
    let params = {
        redirects: 0,
        tags: { name: 'addItemToCart' },
    };
    // ...
    const response = http.post(`${EnvironmentUtil.getStorefrontUrl()}/cart/add/${sku}`, payload, params);
    // ...
}
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
        { duration: '2m', target: rampVus },
        { duration: '3m', target: rampVus },
        { duration: '3m', target: maxVus },
        { duration: '3m', target: maxVus },
        { duration: '2m', target: rampVus },
        { duration: '3m', target: rampVus },
        { duration: '2m', target: 0 },
    ],
    thresholds: {
        http_req_duration: ['p(95)<500'],
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

- **Lines:** [297, 344, 399, 405, 411, 416, 422, 427, 437, 448, 452, 457, 462, 467, 477, 483]
- **Snippet:**
```js
var res = http.post(OpenIdConnect.TokenEndpoint, auth_form_data,
    {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    });
// ...
"comments": {
    method: "GET",
    url: ServiceEndpoints.GatewayApi + "UserProfile/" + user.hdid + "/Comment",
    params: params(user),
},
```
- **Refactored:**
```js
var res = http.post(OpenIdConnect.TokenEndpoint, auth_form_data,
    {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        tags: { name: 'authenticate', endpoint: 'token' },
    });
// ...
"comments": {
    method: "GET",
    url: ServiceEndpoints.GatewayApi + "UserProfile/" + user.hdid + "/Comment",
    params: Object.assign({}, params(user), { tags: { name: 'comments', endpoint: 'UserProfile/Comment' } }),
},
"encounter": {
    method: "GET",
    url: ServiceEndpoints.Encounter + "Encounter/" + user.hdid,
    params: Object.assign({}, params(user), { tags: { name: 'encounter', endpoint: 'Encounter' } }),
},
"immz": {
    method: "GET",
    url: ServiceEndpoints.Immunization + "Immunization?hdid=" + user.hdid,
    params: Object.assign({}, params(user), { tags: { name: 'immunization', endpoint: 'Immunization' } }),
},
"labs": {
    method: "GET",
    url: ServiceEndpoints.Laboratory + "Laboratory/LaboratoryOrders?hdid=" + user.hdid,
    params: Object.assign({}, params(user), { tags: { name: 'labs', endpoint: 'LaboratoryOrders' } }),
},
"meds": {
    method: "GET",
    url: ServiceEndpoints.Medication + "MedicationStatement/" + user.hdid,
    params: Object.assign({}, params(user), { tags: { name: 'medications', endpoint: 'MedicationStatement' } }),
},
"notes": {
    method: "GET",
    url: ServiceEndpoints.GatewayApi + "Note/" + user.hdid,
    params: Object.assign({}, params(user), { tags: { name: 'notes', endpoint: 'Note' } }),
},
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
        { duration: "2m", target: rampVus }, // simulate ramp-up of traffic from 1 users over a few minutes.
        { duration: "3m", target: rampVus }, // stay at number of users for several minutes
        { duration: "3m", target: maxVus }, // ramp-up to users peak for some minutes (peak hour starts)
        { duration: "3m", target: maxVus }, // stay at users for short amount of time (peak hour)
        { duration: "2m", target: rampVus }, // ramp-down to lower users over 3 minutes (peak hour ends)
        { duration: "3m", target: rampVus }, // continue for additional time
        { duration: "2m", target: 0 }, // ramp-down to 0 users
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
        'errors': ['rate<0.01'],
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [233, 234]
- **Snippet:**
```js
let response = http.get(ConfigurationUrl);
if (response.status == 200) {
```
- **Refactored:**
```js
let response = http.get(ConfigurationUrl);
check(response, {
    'configuration retrieved successfully': (r) => r.status === 200,
});
if (response.status == 200) {
```

**Smell 4: Not using tags**

- **Lines:** [398, 432]
- **Snippet:**
```js
"comments": {
    method: "GET",
    url: ServiceEndpoints.GatewayApi + "UserProfile/" + user.hdid + "/Comment",
    params: params(user),
},
```
- **Refactored:**
```js
"comments": {
    method: "GET",
    url: ServiceEndpoints.GatewayApi + "UserProfile/" + user.hdid + "/Comment",
    params: {
        headers: params(user).headers,
        tags: {
            name: "timeline-comments",
        },
    },
},
```

### `script_146.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [6]
- **Snippet:**
```js
var f = JSON.parse(open("../userwrite/json/user.post.k6.json"));
```
- **Refactored:**
```js
// For small data sets, it is more performant to embed the data directly in the script.
// This avoids the overhead of file I/O during test initialization.
const userData = [
  { "name": "k6 user 1", "job": "tester" },
  { "name": "k6 user 2", "job": "explorer" }
];

var payload = new SharedArray("users", function () {
  return userData; 
});
```

**Smell 3: Not checking requests**

- **Lines:** [34]
- **Snippet:**
```js
http.post(url,  JSON.stringify(payload), params);
```
- **Refactored:**
```js
import http from 'k6/http';
import { check } from 'k6';
// ...

// The original code had an early `return`, making the http.post call unreachable.
// The refactored version removes it and adds a check to validate the response.
const res = http.post(url, JSON.stringify(payload[0]), params);
check(res, {
  'API response status is 201': (r) => r.status === 201,
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
// Adding tags to requests allows for more granular filtering and analysis of metrics.
var params = {
  headers: {
    'Content-Type': 'application/json',
  },
  tags: {
    name: 'CreateUser',
  },
};

http.post(url,  JSON.stringify(payload[0]), params);
```

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
const response = http.get(url, { headers, tags: { name: 'basic_fast_endpoint', endpoint: '/api/basic/fast' } });
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
        'GET /api/basic/fast status is 200': (res) => res.status === 200,
        'GET /api/basic/fast returns JSON': (res) => res.headers['Content-Type'] && res.headers['Content-Type'].includes('application/json'),
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
export default function () {
    const url = `${BASE_URL}/api/basic/fast`;
    const params = {
        headers: { 'Accept': 'application/json' },
        tags: {
            endpoint: 'basic_fast',
            method: 'GET',
            flow: 'basic',
        },
    };

    const response = http.get(url, params);

    sleep(1);
}
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
// ...
const response = http.get(url, { headers });
check(response, {
    'status is 200': (r) => r.status === 200,
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
const response = http.get(url, {
  headers,
  tags: { name: 'GetFastEndpoint' },
});
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

### `script_149.js` — GEMINI

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
  ...test_options, // Keep existing options from the import
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    'checks': ['rate>0.99'], // 99% of checks must pass
  },
};
```

### `script_15.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [121, 153, 199, 231, 249, 260, 302, 314, 326, 343]
- **Snippet:**
```js
const res = http.get(`${BASE_URL}/api/v1/assets`, { 
  headers,
  timeout: '2s',
});
// and all other http calls across rateLimitTest, connectionExhaustionTest, largePayloadTest, memoryLeakTest, cascadingFailureTest
```
- **Refactored:**
```js
// Example for rateLimitTest — apply the same pattern to all other HTTP calls
const res = http.get(`${BASE_URL}/api/v1/assets`, {
  headers,
  timeout: '2s',
  tags: { scenario: 'rate_limit_test', endpoint: 'GET /api/v1/assets' },
});

// connectionExhaustionTest
batch.push(
  http.get(`${BASE_URL}/api/v1/assets?page=${i + 1}&limit=100&include=metadata,versions`, {
    headers,
    timeout: '30s',
    tags: { scenario: 'connection_exhaustion', endpoint: 'GET /api/v1/assets' },
  })
);

// largePayloadTest
const res = http.post(`${BASE_URL}/api/v1/assets`, payload, {
  headers,
  timeout: '30s',
  tags: { scenario: 'large_payload_stress', endpoint: 'POST /api/v1/assets' },
});

// memoryLeakTest — create
const createRes = http.post(`${BASE_URL}/api/v1/assets`, JSON.stringify({...}), {
  headers, timeout: '10s',
  tags: { scenario: 'memory_leak_test', endpoint: 'POST /api/v1/assets' },
});
// memoryLeakTest — patch
http.patch(`${BASE_URL}/api/v1/assets/${assetId}/metadata`, JSON.stringify({...}), {
  headers, timeout: '5s',
  tags: { scenario: 'memory_leak_test', endpoint: 'PATCH /api/v1/assets/metadata' },
});
// memoryLeakTest — delete
const deleteRes = http.del(`${BASE_URL}/api/v1/assets/${assetId}`, null, {
  headers, timeout: '5s',
  tags: { scenario: 'memory_leak_test', endpoint: 'DELETE /api/v1/assets' },
});

// cascadingFailureTest — search
const res = http.post(`${BASE_URL}/api/v1/search/advanced`, JSON.stringify(complexQuery), {
  headers, timeout: '10s',
  tags: { scenario: 'cascading_failure', endpoint: 'POST /api/v1/search/advanced' },
});
// cascadingFailureTest — projects tree
const res = http.get(`${BASE_URL}/api/v1/projects/tree?depth=10&include=assets,metadata,permissions`, {
  headers, timeout: '10s',
  tags: { scenario: 'cascading_failure', endpoint: 'GET /api/v1/projects/tree' },
});
// cascadingFailureTest — bulk export
const res = http.post(`${BASE_URL}/api/v1/assets/bulk/export`, JSON.stringify({...}), {
  headers, timeout: '30s',
  tags: { scenario: 'cascading_failure', endpoint: 'POST /api/v1/assets/bulk/export' },
});
// cascadingFailureTest — analytics
const res = http.get(`${BASE_URL}/api/v1/analytics/usage?groupBy=...`, {
  headers, timeout: '15s',
  tags: { scenario: 'cascading_failure', endpoint: 'GET /api/v1/analytics/usage' },
});
```

**Smell 3: Not checking requests**

- **Lines:** [149, 151, 152, 153, 154, 155, 156, 157, 158, 161, 162, 163, 164, 165, 166, 167, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257]
- **Snippet:**
```js
// connectionExhaustionTest: batch requests are made but never checked with check()
batch.forEach((res) => {
  if (res.status === 0) {
    apiTimeouts.add(1);
  } else if (res.status >= 500) {
    apiErrors.add(1);
  }
});

// memoryLeakTest: patch requests inside the loop are never checked
for (let i = 0; i < 10; i++) {
  http.patch(
    `${BASE_URL}/api/v1/assets/${assetId}/metadata`,
    JSON.stringify({ additionalData: randomString(5000), iteration: i }),
    { headers, timeout: '5s' }
  );
}
```
- **Refactored:**
```js
// connectionExhaustionTest: add check() for each batched response
batch.forEach((res, index) => {
  check(res, {
    [`batch request ${index} status 2xx`]: (r) => r.status >= 200 && r.status < 300,
  });
  if (res.status === 0) {
    apiTimeouts.add(1);
  } else if (res.status >= 500) {
    apiErrors.add(1);
  }
});

// memoryLeakTest: capture patch response and add check()
for (let i = 0; i < 10; i++) {
  const patchRes = http.patch(
    `${BASE_URL}/api/v1/assets/${assetId}/metadata`,
    JSON.stringify({ additionalData: randomString(5000), iteration: i }),
    { headers, timeout: '5s' }
  );
  check(patchRes, {
    'metadata patch successful': (r) => r.status === 200 || r.status === 204,
  });
  if (patchRes.status === 0) {
    apiTimeouts.add(1);
  } else if (patchRes.status >= 500) {
    apiErrors.add(1);
  }
}
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
batch.forEach((res, index) => {
    const success = check(res, {
      [`batch request ${index} status is 200`]: (r) => r.status === 200,
    });

    if (!success) {
      if (res.status === 0) {
        apiTimeouts.add(1);
      } else if (res.status >= 500) {
        apiErrors.add(1);
      }
    }
  });
```

**Smell 4: Not using tags**

- **Lines:** [302, 303, 304, 305, 306]
- **Snippet:**
```js
const res = http.post(
        `${BASE_URL}/api/v1/search/advanced`,
        JSON.stringify(complexQuery),
        { headers, timeout: '10s' }
      );
```
- **Refactored:**
```js
const res = http.post(
        `${BASE_URL}/api/v1/search/advanced`,
        JSON.stringify(complexQuery),
        { 
          headers, 
          timeout: '10s',
          tags: { name: 'AdvancedSearch' }
        }
      );
```

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
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: `SYNC-${task}`, endpoint: `/SYNC-${task}` },
})
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
        tags: { endpoint: `SYNC-${task}`, operation: body.operation },
    }
);
```

### `script_150.js` — GEMINI

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

### `script_151.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [59]
- **Snippet:**
```js
let res = http.get(SEAT_LOOKUP_ENDPOINT, { headers });
```
- **Refactored:**
```js
let res = http.get(SEAT_LOOKUP_ENDPOINT, { headers, tags: { name: 'seat_lookup', endpoint: 'GET /concerts/1/dates/2025-03-30/seats' } });
```

### `script_151.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [14, 18, 19, 20, 21, 22, 23, 24]
- **Snippet:**
```js
let res = http.post(TOKEN_ISSUE_ENDPOINT, JSON.stringify({ userId: i, concertId: 1 }), {
    headers: { 'Content-Type': 'application/json' },
});

if (res.status === 201) {
    let responseBody = JSON.parse(res.body);
    let token = responseBody?.data?.token;
    if (token) {
        tokens.push(token);
    }
}
```
- **Refactored:**
```js
let res = http.post(TOKEN_ISSUE_ENDPOINT, JSON.stringify({ userId: i, concertId: 1 }), {
    headers: { 'Content-Type': 'application/json' },
    tags: { endpoint: 'token_issue', flow: 'setup' },
});

const ok = check(res, {
    'token issue status is 201': (r) => r.status === 201,
    'token exists': (r) => {
        try {
            return !!JSON.parse(r.body)?.data?.token;
        } catch (e) {
            return false;
        }
    },
}, { endpoint: 'token_issue', flow: 'setup' });

if (ok) {
    let responseBody = JSON.parse(res.body);
    tokens.push(responseBody.data.token);
}
```

**Smell 4: Not using tags**

- **Lines:** [14, 15, 16, 59, 61, 62, 63, 64]
- **Snippet:**
```js
let res = http.post(TOKEN_ISSUE_ENDPOINT, JSON.stringify({ userId: i, concertId: 1 }), {
    headers: { 'Content-Type': 'application/json' },
});
...
let res = http.get(SEAT_LOOKUP_ENDPOINT, { headers });

check(res, {
    'status is 200': (r) => r.status === 200,
    'response time is < 2000ms': (r) => r.timings.duration < 2000,
});
```
- **Refactored:**
```js
let res = http.post(TOKEN_ISSUE_ENDPOINT, JSON.stringify({ userId: i, concertId: 1 }), {
    headers: { 'Content-Type': 'application/json' },
    tags: { endpoint: 'token_issue', flow: 'setup' },
});

let res = http.get(SEAT_LOOKUP_ENDPOINT, {
    headers,
    tags: { endpoint: 'seat_lookup', flow: 'seat_lookup' },
});

check(res, {
    'status is 200': (r) => r.status === 200,
    'response time is < 2000ms': (r) => r.timings.duration < 2000,
}, { endpoint: 'seat_lookup', flow: 'seat_lookup' });
```

### `script_151.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [59]
- **Snippet:**
```js
let res = http.get(SEAT_LOOKUP_ENDPOINT, { headers });
```
- **Refactored:**
```js
let res = http.get(SEAT_LOOKUP_ENDPOINT, {
    headers,
    tags: {
        name: 'SeatLookupAPI',
    },
});
```

### `script_152.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
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

export default function () {
  const url = `${BASE_URL}/api/basic/fast-random`;
  const headers = { 'Accept': 'application/json' };

  const response = http.get(url, { headers });

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
import { check, sleep } from 'k6';

// inside default function:
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
const response = http.get(url, { headers, tags: { name: 'fast-random', endpoint: '/api/basic/fast-random' } });
```

### `script_152.js` — CHATGPT

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
  const url = `${BASE_URL}/api/basic/fast-random`;
  const headers = { 'Accept': 'application/json' };
  const response = http.get(url, { headers });
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

const response = http.get(url, { headers });
check(response, {
  'status is 200': (r) => r.status === 200,
  'response is JSON': (r) => r.headers['Content-Type'] && r.headers['Content-Type'].includes('application/json')
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
const response = http.get(url, {
  headers,
  tags: {
    endpoint: 'fast-random',
    flow: 'basic'
  }
});
```

### `script_152.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 13]
- **Snippet:**
```js
The script does not export an `options` object with a `thresholds` property. Without thresholds, the test will always pass in a CI/CD environment, regardless of the system's performance.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<200'], // 95% of requests should be below 200ms
  },
};
// This options object should be added to the init context of the script.
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
const response = http.get(url, {
    headers,
    tags: { name: 'FastRandomAPI' },
});
```

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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        'checks': ['rate>0.99']
    }
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
const res = http.get('http://test.k6.io/', { tags: { name: 'homepage', endpoint: '/' } })
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
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99']
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [10, 12]
- **Snippet:**
```js
const res = http.get('http://test.k6.io/')

check(res, {
    'status code é 200': (r) => r.status === 200
});
```
- **Refactored:**
```js
const tags = { endpoint: 'home', flow: 'homepage' };
const res = http.get('http://test.k6.io/', { tags });

check(res, {
    'status code is 200': (r) => r.status === 200
}, tags);
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
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<200'], // 95% of requests should be below 200ms
    },
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
      tags: {
        name: 'Homepage',
      },
    });
```

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
    'http_req_duration{url:/api/products/details}': ['p(95)<300'],
    'http_req_duration{url:/api/products/prices}': ['p(95)<300'],
    'http_req_duration{url:/api/products/catalog/us}': ['p(95)<300'],
    'http_req_duration{url:/api/products/catalog/uk}': ['p(95)<300'],
    'http_req_duration{url:/api/products/catalog/de}': ['p(95)<300'],
    'http_reqs': ['rate>500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [41, 42, 43, 44]
- **Snippet:**
```js
const url = getRandomUrl();
const res = http.get(`${API_URL}${url}`);

check(res, { 'status is 200': (r) => r.status === 200 });
```
- **Refactored:**
```js
const url = getRandomUrl();
const res = http.get(`${API_URL}${url}`, { tags: { endpoint: url } });

check(res, { 'status is 200': (r) => r.status === 200 }, { tags: { endpoint: url } });
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
    'http_req_duration{endpoint:products}': ['p(95)<300'],
    http_reqs: ['rate>=500'],
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [42, 44]
- **Snippet:**
```js
const res = http.get(`${API_URL}${url}`);

check(res, { 'status is 200': (r) => r.status === 200 });
```
- **Refactored:**
```js
const tags = { endpoint: 'products', route: url };
const res = http.get(`${API_URL}${url}`, { tags });

check(res, { 'status is 200': (r) => r.status === 200 }, tags);
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
    'http_req_duration': ['p(95)<300'], // P95 duration should be under 300ms
    'http_reqs': ['rate>500'],          // Throughput should be at least 500 reqs/s
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
    tags: { name: url },
  });
```

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
    'checks': ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [10, 11]
- **Snippet:**
```js
let res = http.get('http://localhost:8080/');
check(res, { 'status is 200': (r) => r.status === 200 });
```
- **Refactored:**
```js
let res = http.get('http://localhost:8080/', { tags: { name: 'homepage', endpoint: '/' } });
check(res, { 'status is 200': (r) => r.status === 200 }, { tags: { name: 'homepage', endpoint: '/' } });
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
    checks: ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [10, 11]
- **Snippet:**
```js
let res = http.get('http://localhost:8080/');
check(res, { 'status is 200': (r) => r.status === 200 });
```
- **Refactored:**
```js
const tags = { endpoint: 'home', flow: 'homepage' };
let res = http.get('http://localhost:8080/', { tags });
check(res, { 'status is 200': (r) => r.status === 200 }, tags);
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
        http_req_failed: ['rate<0.01'],
        'checks': ['rate>0.99']
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
        tags: { name: 'create_user', endpoint: '/v-fluent-res/users', method: 'POST' }
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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.95']
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
    tags: { endpoint: 'create_user_validation', method: 'POST', flow: 'user_creation' }
});

check(response, {
    "response code was 400 or 409": (res) => res.status === 400 || res.status === 409
}, { endpoint: 'create_user_validation', flow: 'user_creation' });
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
        'http_req_failed': ['rate<0.01'],
        'checks': ['rate>0.99']
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

// Inside the 'Checkout' group:
const checkoutResponse = checkoutResource.checkout();
check(checkoutResponse, {
  'checkout status is 201': (r) => r.status === 201,
  'checkout response has orderReference': (r) => JSON.parse(r.body).data.attributes.orderReference !== undefined,
});
orderReference = JSON.parse(checkoutResponse.body).data.attributes.orderReference;

// Inside the 'Cart Reorder' group:
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
// Add tags to each request to allow filtering and grouping of metrics per endpoint/flow.
// Example for the checkout request:
const checkoutResponse = checkoutResource.checkout({ tags: { name: 'checkout', group: 'Checkout', testId: 'SAPI15' } });

// Example for the reorder request:
const response = cartReorderResource.reorder({ tags: { name: 'cart_reorder', group: 'Cart Reorder', testId: 'SAPI15' } });

// Example for the auth request (if supported by the utility):
bearerToken = AuthUtil.getInstance().getBearerToken(customerEmail, { tags: { name: 'authorization', group: 'Authorization', testId: 'SAPI15' } });
```

### `script_158.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [53, 58, 59]
- **Snippet:**
```js
orderReference = JSON.parse(checkoutResource.checkout().body).data.attributes.orderReference;
// ...
const response = cartReorderResource.reorder();
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
import { check } from 'k6'; // Add this import

// ... inside default function
const checkoutResponse = checkoutResource.checkout();
check(checkoutResponse, { 'Checkout successful': (r) => r.status < 400 });
// Use .json() for safer parsing
orderReference = checkoutResponse.json().data.attributes.orderReference;

// ...
const response = cartReorderResource.reorder();
if (check(response, { 'Reorder successful': (r) => r.status < 400 })) {
  // Only add metric for successful requests
  metrics[testConfiguration.metrics[0]].add(response.timings.duration);
}
```

**Smell 4: Not using tags**

- **Lines:** [53, 58, 59]
- **Snippet:**
```js
const checkoutResource = new CheckoutResource(idCart, customerEmail, bearerToken);
orderReference = JSON.parse(checkoutResource.checkout().body).data.attributes.orderReference;
// ...
const response = cartReorderResource.reorder();
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
// Assuming resource methods can pass params to the underlying k6/http request
const checkoutResource = new CheckoutResource(idCart, customerEmail, bearerToken);
const checkoutResponse = checkoutResource.checkout({ tags: { name: 'Checkout' } });
orderReference = checkoutResponse.json().data.attributes.orderReference;

// ...
const cartReorderResource = new CartReorderResource(orderReference, bearerToken);
const response = cartReorderResource.reorder({ tags: { name: 'CartReorder' } });

// Add tags to custom metrics for better observability
metrics[testConfiguration.metrics[0]].add(response.timings.duration, { name: 'CartReorder' });
```

### `script_16.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [18]
- **Snippet:**
```js
const USERNAME = `${randomString(10)}@example.com`;
```
- **Refactored:**
```js
// Move USERNAME generation inside setup() or the default function to avoid executing it in the init context per VU
export function setup() {
  const USERNAME = `${randomString(10)}@example.com`;
  const PASSWORD = 'secret';
  // ... rest of setup logic
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
    http_req_failed: ['rate<0.01'],       // Less than 1% of requests should fail
    http_req_duration: ['p(95)<500'],     // 95% of requests should complete below 500ms
    'checks': ['rate>0.99'],              // More than 99% of checks should pass
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
  {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'Login' },
  }
);

const loginOk = check(loginRes, {
  'login status is 200': (r) => r.status === 200,
  'login returned token': (r) => Boolean(r.json('token')),
});

if (!loginOk) {
  fail(`Unable to log in: ${loginRes.status} ${loginRes.body}`);
}

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
const setupRequestConfig = (name) => ({
  headers: { 'Content-Type': 'application/json' },
  tags: { name },
});

const res = http.post(
  `${BASE_URL}/api/users`,
  JSON.stringify({
    username: USERNAME,
    password: PASSWORD,
  }),
  setupRequestConfig('RegisterUser')
);

const loginRes = http.post(
  `${BASE_URL}/api/users/token/login`,
  JSON.stringify({
    username: USERNAME,
    password: PASSWORD,
  }),
  setupRequestConfig('Login')
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
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
    checks: ['rate>0.99'], // 99% of checks should pass
  },
};
```

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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
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
const res = http.get(url, { tags: { name: 'get_concerts', endpoint: '/concerts' } });
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
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [14, 16, 17, 18]
- **Snippet:**
```js
const res = http.get(url);

const success = check(res, {
    'status is 200': (r) => r.status === 200,
});
```
- **Refactored:**
```js
const params = {
    tags: {
        endpoint: 'concerts_by_date',
        flow: 'browse_concerts',
    },
};
const res = http.get(url, params);

const success = check(res, {
    'status is 200': (r) => r.status === 200,
}, {
    endpoint: 'concerts_by_date',
    flow: 'browse_concerts',
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
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
        'checks': ['rate>0.99'], // 99% of checks should pass
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
        name: 'GetConcertsByDate',
    },
});
```

### `script_161.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
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

export default function () {
  // existing code
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
import { check, sleep } from 'k6';
import http from 'k6/http';

const BASE_URL = 'http://localhost:8888/alphamart';

export default function () {
  const response = http.get(`${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`);

  check(response, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
  });

  console.log('Response status code: ' + response.status);
  console.log('Response headers: ' + JSON.stringify(response.headers));
  console.log('Response body: ' + response.body);

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
const response = http.get(`${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`, {
  tags: { name: 'EchoEndpoint', endpoint: '/api/basic/echo' },
});
```

### `script_161.js` — CHATGPT

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
const response = http.get(`${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`);
```
- **Refactored:**
```js
import { sleep, check } from 'k6';
import http from 'k6/http';

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
const params = {
  tags: {
    endpoint: 'basic_echo',
    flow: 'echo',
  },
};

const response = http.get(
  `${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`,
  params
);
```

### `script_161.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 14]
- **Snippet:**
```js
The script does not export an `options` object with a `thresholds` property. The entire script is missing this configuration.
```
- **Refactored:**
```js
import { sleep } from 'k6';
import http from 'k6/http';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [7, 11]
- **Snippet:**
```js
const response = http.get(`${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`);

  console.log("Response status code: " + response.status);
  console.log("Response headers: " + JSON.stringify(response.headers));
  console.log("Response body: " + response.body);
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
const response = http.get(
    `${BASE_URL}/api/basic/echo?color=blue&month=january&month=february&amount=1000`,
    {
      tags: { name: 'EchoAPI' },
    }
  );
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
// Move the database connection opening inside the default function or setup function to avoid costly operations in the init context.
// Option 1: Open connection inside the default function (per VU):
export default () => {
  const db = sql.open('postgres', pgConnectionString)
  // ... rest of the function
  db.close()
}

// Option 2: Use setup() to open the connection once and pass it via data (if the extension supports it):
export function setup() {
  const db = sql.open('postgres', pgConnectionString)
  return { db }
}

export default (data) => {
  const db = data.db
  // ... rest of the function
}
```

**Smell 3: Not checking requests**

- **Lines:** [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]
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
```
- **Refactored:**
```js
try {
  const result = db.exec(
    'insert into positions (stud_id,first_name,last_name,title,reports_to,timestamp,location,email) ' +
      `values(${name}, 'Virtual ${name}', 'User ${name}', 'Load Tester', 1, ${Date.now()}, st_point(-73.946${x}, 40.807${y}), 'vu${name}@chinookcorp.com');`
  )
  const insertSucceeded = check(result, {
    'insert affected at least 1 row': (r) => r && r.rowsAffected() >= 1,
  })
  myFailRate.add(!insertSucceeded)
  if (!insertSucceeded) {
    counterFailed.add(1)
  }
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
// Use k6 tags to annotate the operation for better metric filtering and grouping.
import { tagWithCurrentStageIndex } from 'k6/execution'

// Apply tags via group or by setting exec tags:
group('pg_insert_position', () => {
  const tags = { operation: 'insert', table: 'positions', testRun: testRun }
  insertTrend.add(exFinish - exStart, tags)
  myFailRate.add(false, tags)
  counterInserts.add(1, tags)
  // Since sql.exec does not natively support k6 tags, annotate the surrounding metrics:
  db.exec(
    'insert into positions (stud_id,first_name,last_name,title,reports_to,timestamp,location,email) ' +
      `values(${name}, 'Virtual ${name}', 'User ${name}', 'Load Tester', 1, ${Date.now()}, st_point(-73.946${x}, 40.807${y}), 'vu${name}@chinookcorp.com');`
  )
})
```

### `script_162.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [62, 65, 66, 69, 70]
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
      const tags = { query: 'insert_positions' };
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
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
    'checks': ['rate>0.99']
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
const res = http.post('http://localhost:3000/guestUser/logIn', payload, { headers, tags: { name: 'login', endpoint: '/guestUser/logIn' } });
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
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99']
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 24, 25, 26]
- **Snippet:**
```js
const res = http.post('http://localhost:3000/guestUser/logIn', payload, { headers });

check(res, {
  'status is 200/400/401': (r) => [200, 400, 401].includes(r.status),
});
```
- **Refactored:**
```js
const params = {
  headers,
  tags: {
    endpoint: 'guest_login',
    flow: 'rate_limit_not_breach'
  }
};

const res = http.post('http://localhost:3000/guestUser/logIn', payload, params);

check(res, {
  'status is 200/400/401': (r) => [200, 400, 401].includes(r.status),
}, {
  endpoint: 'guest_login',
  flow: 'rate_limit_not_breach'
});
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
  vus: 1,                // 1 virtual user = 1 IP
  iterations: 10,        // Send only 10 requests total
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'checks': ['rate>0.99']          // 99% of checks must pass
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
const res = http.post('http://localhost:3000/guestUser/logIn', payload, { 
  headers, 
  tags: { 
    name: 'UserLogin' 
  } 
});
```

### `script_165.js` — CLAUDE

**Smell 1: Costly operations in the init context**

- **Lines:** [25, 26, 27, 28]
- **Snippet:**
```js
const fixture = new CategoryFixture({
  categoryCount: 1,
  productCount: 100,
});
```
- **Refactored:**
```js
// Move fixture instantiation inside setup() and pass data to default function
export function setup() {
  const fixture = new CategoryFixture({
    categoryCount: 1,
    productCount: 100,
  });
  return fixture.getData();
}
```

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
import { check } from 'k6';

const response = categoryPage.get(category.url, {
  'label[]': 'KSixTestLabel',
  'color[]': 'Black',
  brand: 'Nike',
  ipp: 36,
});

check(response, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
```

**Smell 4: Not using tags**

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
const response = categoryPage.get(category.url, {
  'label[]': 'KSixTestLabel',
  'color[]': 'Black',
  brand: 'Nike',
  ipp: 36,
}, { tags: { name: 'S25_get_category', group: 'Category Filter Products', endpoint: category.url } });
```

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
    const tags = { endpoint: 'category_filter_products', group: 'Category', test_id: testConfiguration.id };
    const response = categoryPage.get(category.url, {
      'label[]': 'KSixTestLabel',
      'color[]': 'Black',
      brand: 'Nike',
      ipp: 36,
    }, { tags });

    check(response, {
      'category filter products status is 200': (r) => r.status === 200,
      'category filter products response body is not empty': (r) => r.body && r.body.length > 0,
    }, tags);

    metrics[testConfiguration.metrics[0]].add(response.timings.duration, tags);
  });
}
```

**Smell 4: Not using tags**

- **Lines:** [43, 44, 45, 46, 47, 48, 50]
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
    const tags = { endpoint: 'category_filter_products', group: 'Category', test_id: testConfiguration.id };
    const response = categoryPage.get(category.url, {
      'label[]': 'KSixTestLabel',
      'color[]': 'Black',
      brand: 'Nike',
      ipp: 36,
    }, { tags });

    metrics[testConfiguration.metrics[0]].add(response.timings.duration, tags);
  });
}
```

### `script_165.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [25, 26, 27, 28]
- **Snippet:**
```js
const fixture = new CategoryFixture({
  categoryCount: 1,
  productCount: 100,
});
```
- **Refactored:**
```js
// The CategoryFixture should not be instantiated in the init context because
// it runs this potentially expensive operation once per VU.
// Instead, create it in the setup function to ensure data generation
// happens only once for the entire test run.

export function setup() {
  const fixture = new CategoryFixture({
    categoryCount: 1,
    productCount: 100,
  });
  return fixture.getData();
}

// Note: The default function must be updated to use the data from setup,
// as the 'fixture' instance will no longer be available in the VU context.
// e.g., const category = data[__VU % data.length];
```

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

check(response, {
  'status is 200': (r) => r.status === 200,
});

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```

**Smell 4: Not using tags**

- **Lines:** [50]
- **Snippet:**
```js
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
// Adding tags to the custom metric allows for more granular analysis,
// for example, filtering results by the specific category URL.
metrics[testConfiguration.metrics[0]].add(response.timings.duration, {
  endpoint: category.url
});
```

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
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    'checks': ['rate>0.99'],
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
])

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
])

check(responses[0], {
    'Homepage status is 200': (r) => r.status === 200,
    'Homepage successfully loaded': (r) => r.body.includes("Collection of simple web-pages suitable for load testing"),
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
    ['GET', domain + '/', null, { tags: { name: 'homepage' } }],
    ['GET', domain + '/static/css/site.css', null, { tags: { name: 'site_css' } }],
    ['GET', domain + '/static/js/prisms.js', null, { tags: { name: 'prisms_js' } }],
    ['GET', domain + '/static/favicon.ico', null, { tags: { name: 'favicon' } }]
])
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
    checks: ['rate>0.95'],
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
  ['GET', domain + '/', null, { tags: { endpoint: 'homepage' } }],
  ['GET', domain + '/static/css/site.css', null, { tags: { endpoint: 'site_css' } }],
  ['GET', domain + '/static/js/prisms.js', null, { tags: { endpoint: 'prisms_js' } }],
  ['GET', domain + '/static/favicon.ico', null, { tags: { endpoint: 'favicon' } }],
]);

check(responses[0], {
  'homepage status is 200': (r) => r.status === 200,
  'homepage body is correct': (r) => r.body.includes('Collection of simple web-pages suitable for load testing'),
});
check(responses[1], {
  'site css status is 200': (r) => r.status === 200,
});
check(responses[2], {
  'prisms js status is 200': (r) => r.status === 200,
});
check(responses[3], {
  'favicon status is 200': (r) => r.status === 200,
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
  ['GET', domain + '/', null, { tags: { endpoint: 'homepage', flow: 'browse_static_assets' } }],
  ['GET', domain + '/static/css/site.css', null, { tags: { endpoint: 'site_css', flow: 'browse_static_assets' } }],
  ['GET', domain + '/static/js/prisms.js', null, { tags: { endpoint: 'prisms_js', flow: 'browse_static_assets' } }],
  ['GET', domain + '/static/favicon.ico', null, { tags: { endpoint: 'favicon', flow: 'browse_static_assets' } }],
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
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
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
    ])

  check(responses[0], {
    'Homepage successfully loaded': (r) => r.body.includes("Collection of simple web-pages suitable for load testing"),
  });
```
- **Refactored:**
```js
check(responses[0], {
    'Homepage status is 200': (r) => r.status === 200,
    'Homepage content is correct': (r) => r.body.includes("Collection of simple web-pages suitable for load testing"),
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
        {
            method: 'GET',
            url: domain + '/',
            params: { tags: { name: 'Homepage' } },
        },
        {
            method: 'GET',
            url: domain + '/static/css/site.css',
            params: { tags: { name: 'CSS' } },
        },
        {
            method: 'GET',
            url: domain + '/static/js/prisms.js',
            params: { tags: { name: 'JS' } },
        },
        {
            method: 'GET',
            url: domain + '/static/favicon.ico',
            params: { tags: { name: 'Favicon' } },
        },
    ]);
```

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
const resCo = httppost("A-2048", {
    operation: "test",
})
check(resCo, { 'A status was 200': (r) => r.status == 200 });
```
- **Refactored:**
```js
const resCo = http.post(`${hostprefix}/SYNC-A-2048`, JSON.stringify({ operation: 'test' }), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'SYNC-A-2048', endpoint: '/SYNC-A-2048' },
});
check(resCo, { 'A status was 200': (r) => r.status == 200 }, { tags: { name: 'SYNC-A-2048' } });
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
        tags: { endpoint: `SYNC-${task}`, method: 'POST', task },
    }
);

export default function () {
    const task = 'A-2048';
    const resCo = httppost(task, {
        operation: 'test',
    });
    check(resCo, { 'A status was 200': (r) => r.status === 200 }, { endpoint: `SYNC-${task}`, task });
}
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
        http_req_failed: ['rate<0.01'], // http errors should be less than 1%
        http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
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
)
```

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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500']
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
    const res = http.get('https://example.com');
    check(res, {
        'status is 200': (r) => r.status === 200,
        'response body is not empty': (r) => r.body && r.body.length > 0
    });
    sleep(1);
}
```

**Smell 4: Not using tags**

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
export default function (data) {
    console.log('-- VU stage --');
    const res = http.get('https://example.com', {
        tags: { name: 'homepage', endpoint: '/index' }
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
        // Example thresholds (adjust as needed for actual requests)
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<200'], // 95% of requests must complete below 200ms
    },
};
```

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
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    'checks': ['rate>0.99'],
  },
};
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
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.95'],
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
const loginPage = http.get(`${BASE_URL}/login`, { tags: { endpoint: 'login_page', flow: 'login' } });
const loginAction = http.post(
  `${BASE_URL}/loginAction`,
  {
    username: 'user1',
    password: 'password',
  },
  { tags: { endpoint: 'login_action', flow: 'login' } }
);
const homePage = http.get(`${BASE_URL}/`, { tags: { endpoint: 'home_page', flow: 'navigate' } });
const categoryPage = http.get(`${BASE_URL}/category`, { tags: { endpoint: 'category_page', flow: 'navigate' } });
const productPage = http.get(`${BASE_URL}/product`, { tags: { endpoint: 'product_page', flow: 'navigate' } });
const logoutAction = http.post(`${BASE_URL}/loginAction?logout=`, null, { tags: { endpoint: 'logout_action', flow: 'logout' } });
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
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [13, 16, 24, 27, 30, 35]
- **Snippet:**
```js
const homePage = http.get(`${BASE_URL}/`);
```
- **Refactored:**
```js
group('Navigate', () => {
    const homePage = http.get(`${BASE_URL}/`, { tags: { name: 'HomePage' } });
    check(homePage, { 'Home page loaded': (r) => r.status === 200 });

    const categoryPage = http.get(`${BASE_URL}/category`, { tags: { name: 'CategoryPage' } });
    check(categoryPage, { 'Category page loaded': (r) => r.status === 200 });

    const productPage = http.get(`${BASE_URL}/product`, { tags: { name: 'ProductPage' } });
    check(productPage, { 'Product page loaded': (r) => r.status === 200 });
  });
```

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
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    'checks': ['rate>0.99'],
  },
};
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

- **Lines:** [11, 14, 15, 16]
- **Snippet:**
```js
let response = http.get('https://gqfnc7ztrujstj3fyuzjdzjb2u0nqvus.lambda-url.us-east-2.on.aws');

check(response, {
  'is status 200': (r) => r.status === 200,
});
```
- **Refactored:**
```js
const params = {
  tags: {
    endpoint: 'lambda_root',
    flow: 'default_get',
  },
};

let response = http.get('https://gqfnc7ztrujstj3fyuzjdzjb2u0nqvus.lambda-url.us-east-2.on.aws', params);

check(response, {
  'is status 200': (r) => r.status === 200,
}, {
  endpoint: 'lambda_root',
  flow: 'default_get',
});
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
    // Fail the test if the error rate is higher than 1%
    http_req_failed: ['rate<0.01'],
    // Fail the test if the 95th percentile of response time is longer than 500ms
    http_req_duration: ['p(95)<500'], 
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
let response = http.get('https://gqfnc7ztrujstj3fyuzjdzjb2u0nqvus.lambda-url.us-east-2.on.aws', {
    tags: { name: 'PublicAPI' },
  });
```

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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500']
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
const urlRes = http.get('https://test-api.k6.io', { tags: { name: 'homepage', endpoint: 'get_root' } })
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
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99']
    }
}
```

**Smell 4: Not using tags**

- **Lines:** [12, 14, 15, 16]
- **Snippet:**
```js
const urlRes = http.get('https://test-api.k6.io')
check(urlRes, {
    "response code was 200": (res) => res.status == 200
});
```
- **Refactored:**
```js
const params = {
    tags: {
        endpoint: 'home',
        flow: 'root_page'
    }
};
const urlRes = http.get('https://test-api.k6.io', params);
check(urlRes, {
    'response code was 200': (res) => res.status === 200
}, {
    endpoint: 'home',
    flow: 'root_page'
});
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
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<200'], // 95% of requests should be below 200ms
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
    tags: { name: 'PublicAPITest' },
});
```

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
    'checks': ['rate>0.99'],
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
const res = http.get(`http://backend-ellis-jodus-reyes.us-east-1.elasticbeanstalk.com/purchasesTest/provider/${providerId}?from="${from}"&to="${to}"`, { headers, tags: { name: 'GetProviderPurchases', endpoint: '/purchasesTest/provider' } });
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
      endpoint: 'provider_purchases',
      flow: 'provider_purchases_lookup',
      method: 'GET'
    }
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
  scenarios: {
    my_scenario1: {
      executor: 'constant-arrival-rate',
      duration: '60s', // total duration
      preAllocatedVUs: 50, // to allocate runtime resources

      rate: 1200, // number of constant iterations given `timeUnit`
      timeUnit: '60s',
    },
  },
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
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
    tags: { name: 'GetProviderPurchases' },
  });
```

### `script_174.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
const response = http.get(url);
```
- **Refactored:**
```js
const response = http.get(url, { tags: { name: 'GetAllEmployees', endpoint: '/api/CacheCartelAPI/GetAllEmployees' } });
```

### `script_174.js` — CHATGPT

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
const response = http.get(url);
```
- **Refactored:**
```js
const url = 'http://localhost:12082/api/CacheCartelAPI/GetAllEmployees';
const params = {
  tags: {
    endpoint: 'GetAllEmployees',
    flow: 'employee-cache',
  },
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
const response = http.get(url, {
      tags: { name: 'GetAllEmployees' },
    });
```

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
        'http_req_duration': ['p(95)<500'],
        'http_req_failed': ['rate<0.01'],
        'checks': ['rate>0.99']
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
const urlRes = http.get('https://test-api.k6.io', { tags: { name: 'homepage', endpoint: 'GET /' } })
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

- **Lines:** [13, 15, 16, 17]
- **Snippet:**
```js
const urlRes = http.get('https://test-api.k6.io')
check(urlRes, {
    "response code was 200": (res) => res.status == 200
});
```
- **Refactored:**
```js
const tags = { endpoint: 'home', flow: 'homepage' };
const urlRes = http.get('https://test-api.k6.io', { tags });
check(urlRes, {
    'response code was 200': (res) => res.status === 200
}, tags);
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
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<200'], // 95% of requests should be below 200ms
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
    tags: { name: 'PublicAPITest' },
});
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
const tags = { operation: 'insert', table: 'positions', scenario: 'supavisor_single_insert' };
const exStart = new Date();
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

### `script_176.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [67, 70, 71, 74, 75]
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
const tags = { query: 'single_insert' };

// ...

myFailRate.add(false, tags);

// in catch block
myFailRate.add(true, tags);
counterFailed.add(1, tags);

// ...

counterInserts.add(1, tags);
insertTrend.add(exFinish - exStart, tags);
```

### `script_177.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
const response = http.get(url);
```
- **Refactored:**
```js
const response = http.get(url, { tags: { name: 'GetAllEmployees', endpoint: '/api/cartelAPI/GetAllEmployees' } });
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
    api: 'cartelAPI',
    endpoint: 'GetAllEmployees',
    flow: 'get_all_employees'
  }
});

runChecks(response);
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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        'checks{check:A status was 200}': ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [19, 22, 23, 24, 25]
- **Snippet:**
```js
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {headers: { 'Content-Type': 'application/json' }})
```
- **Refactored:**
```js
const httppost = (task, body) => http.post(`${hostprefix}/SYNC-${task}`, JSON.stringify(body), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: `SYNC-${task}`, endpoint: `/SYNC-${task}` }
})
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
        tags: { endpoint: `SYNC-${task}`, operation: body.operation },
    }
);

check(resCo, { 'A status was 200': (r) => r.status === 200 }, { endpoint: 'SYNC-G-3300', operation: 'test' });
```

### `script_178.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5]
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
    tags: { name: `SYNC-${task}` }
})
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
export const options = {
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
  ...test_options, // Preserves other options from the imported module
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    'checks': ['rate>0.99']             // over 99% of checks must pass
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
orderReference = responseJson.data.attributes.orderReference;
```
- **Refactored:**
```js
import { check } from 'k6';

// ... inside the 'Checkout' group
const response = checkoutResource.checkout();
const wasSuccessful = check(response, {
  'POST checkout returns status 200': (r) => r.status === 200,
});

if (!wasSuccessful) {
  // Handle error, e.g., fail the iteration
  fail('Checkout request failed');
}

const responseJson = JSON.parse(response.body);
orderReference = responseJson.data.attributes.orderReference;
```

**Smell 4: Not using tags**

- **Lines:** [82, 89, 101]
- **Snippet:**
```js
metrics['SAPI16_post_cart_reorder'].add(response.timings.duration);
```
- **Refactored:**
```js
// ... inside the 'Start Order Amendment' group
const response = orderAmendmentResource.amendOrder();
const responseJson = JSON.parse(response.body);
metrics['SAPI16_post_cart_reorder'].add(response.timings.duration, {
  order_reference: orderReference
});
reorderedIdCart = responseJson.data.id;
```

### `script_186.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [30, 33]
- **Snippet:**
```js
const res = http.get('https://test-api.k6.io/public/crocodiles/1/');

  const randomNum = generateRandom(min, max);
  GaugeContentSize.add(res.body.length+randomNum);
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

const randomNum = generateRandom(min, max);
GaugeContentSize.add(res.body.length + randomNum);
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
  tags: { name: 'GetCrocodile', endpoint: '/public/crocodiles/1/' },
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
    'GET crocodile 1 returns 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
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
export default function () {
  const tags = { endpoint: 'get_crocodile_by_id', flow: 'crocodile_details' };

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
export default function () {
  const res = http.get('https://test-api.k6.io/public/crocodiles/1/');
  check(res, { 'status is 200': (r) => r.status === 200 });

  const randomNum = generateRandom(min, max);
  GaugeContentSize.add(res.body.length + randomNum);
  sleep(1);
}
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

### `script_188.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 50]
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
// ...
const res = http.post(`${BASE_URL}/api/customer/fake`, payload, params);
check(res, {
  'status is 200 or 201': (r) => r.status === 200 || r.status === 201,
  'response body is not empty': (r) => r.body && r.body.length > 0,
});
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
    },
};
http.post(`${BASE_URL}/api/customer/fake`, payload, params);
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
// Avoid loading/parsing a large JSON fixture in init when possible.
// Generate lightweight test data per iteration instead, or use a much smaller preprocessed fixture.
function generateCustomerFake() {
    const uniqueId = `${__VU}-${__ITER}-${Date.now()}`;
    return {
        email: `customer-${uniqueId}@example.com`,
        firstName: 'Test',
        lastName: `User${uniqueId}`
    };
}

export default function () {
    const customer = generateCustomerFake();
    const contactDetail = customer.email;
    const fullName = `${customer.firstName} ${customer.lastName}`;
}
```

**Smell 2: Do not use thresholds**

- **Lines:** [22]
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
        checks: ['rate>0.99']
    }
};

export default function () {
    // test logic
}
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
    'POST /api/customer/fake status is 200 or 201': (r) => r.status === 200 || r.status === 201,
    'POST /api/customer/fake response is not empty': (r) => r.body && r.body.length > 0
});
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
        endpoint: 'POST /api/customer/fake',
        flow: 'create_fake_customer'
    }
};

const res = http.post(`${BASE_URL}/api/customer/fake`, payload, params);
```

### `script_188.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [22]
- **Snippet:**
```js
export default function () {
```
- **Refactored:**
```js
import { sleep } from 'k6';
import { SharedArray } from 'k6/data';
import http from 'k6/http';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
};

// ... rest of the script
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
// ...

const res = http.post(`${BASE_URL}/api/customer/fake`, payload, params);
check(res, {
    'response code was 201 (Created)': (r) => r.status == 201,
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

### `script_19.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [110, 112, 120]
- **Snippet:**
```js
const binFile = open('zh.wav', 'b');
const paddledata = {
  audio: encoding.b64encode(binFile),
  //...
};
let paddle_model = {
  //...
  body: JSON.stringify(paddledata),
  //...
};
```
- **Refactored:**
```js
/* Data is prepared once in the setup function, not per-VU in init context. */
export function setup() {
  const binFile = open('zh.wav', 'b');
  const paddledata = {
    audio: encoding.b64encode(binFile),
    audio_format: "wav",
    sample_rate: 16000,
    lang: "zh_cn",
  };
  return { paddleBody: JSON.stringify(paddledata) };
}

/* The VU function then receives this data as an argument. */
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
import http from 'k6/http';

export function shufflenet() {
  const res = http.get(shufflenet_model.url);
  check(res, {
    'shufflenet: status is 200': (r) => r.status === 200,
  });
}
```

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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500']
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

**Smell 4: Not using tags**

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
export default function (data) {
    console.log('-- VU stage --');
    const res = http.get('https://your-endpoint.com', {
        tags: { name: 'main_endpoint', flow: 'default' }
    });
    check(res, { 'status is 200': (r) => r.status === 200 }, { tags: { name: 'main_endpoint' } });
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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500']
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
        // Iteration duration should be less than 1.1s (sleep(1) + overhead)
        'iteration_duration': ['p(95)<1100'],
    },
};
```

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
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500', 'p(99)<1000'],
    'response_time': ['p(95)<500'],
    'checks': ['rate>0.95'],
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
    { headers, tags: { name: 'CreateUser', endpoint: '/v2/user', method: 'POST' } }
  );
```

### `script_192.js` — CHATGPT

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
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500', 'p(99)<1000'],
    checks: ['rate>0.95'],
    response_time: ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [31, 32, 33, 34, 35, 38, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
- **Snippet:**
```js
const res = http.post(
  'https://petstore.swagger.io/v2/user',
  payload,
  { headers }
);

responseTime.add(res.timings.duration);

check(res, { ... });
```
- **Refactored:**
```js
const tags = { endpoint: 'create_user', flow: 'user_creation', method: 'POST' };

const res = http.post(
  'https://petstore.swagger.io/v2/user',
  payload,
  { headers, tags }
);

responseTime.add(res.timings.duration, tags);

check(res, {
  'Status is 200': (r) => r.status === 200,
  'Response time < 500ms': (r) => r.timings.duration < 500,
}, tags);
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
  vus: 250, // Jumlah VUs
  iterations: 250,
  thresholds: {
    'http_req_failed': ['rate<0.01'],             // http errors should be less than 1%
    'response_time{expected_response:true}': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks{Status is 200}': ['rate>0.95'],       // >95% of checks for status 200 must pass
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [31, 32, 33, 34, 35, 38]
- **Snippet:**
```js
const res = http.post(
  'https://petstore.swagger.io/v2/user',
  payload,
  { headers }
);

// Menyimpan metrik tambahan
responseTime.add(res.timings.duration);
```
- **Refactored:**
```js
const res = http.post(
  'https://petstore.swagger.io/v2/user',
  payload,
  {
    headers,
    tags: { name: 'CreateUser' },
  }
);

// Menyimpan metrik tambahan
responseTime.add(res.timings.duration, { endpoint: 'CreateUser' });
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

// Inside default function:
let result;
try {
  result = db.exec(
    `insert into load_messages(room_id) values('room${getRandomInt(0, rooms)}');`
  );
  check(result, {
    'insert succeeded': (r) => r !== null && r !== undefined,
  });
} catch (e) {
  check(null, { 'insert succeeded': () => false });
}
```

**Smell 4: Not using tags**

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
// Tag the metric when recording the insert counter and wrap execution with tagged context
import { tagWithCurrentStageIndex } from 'k6/execution';

// Use custom tags on the counter to identify the operation
counterInserts.add(1, { operation: 'insert', table: 'load_messages' });

// Alternatively, set tags via group or by passing tags to the metric:
// counterInserts.add(1, { endpoint: 'db_insert', room: `room${roomId}` });
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
    // Ensure at least 99% of the target insert rate is met.
    'inserts': [`count>=${rate * baseDuration * 0.99}`],
    // Ensure 95% of insert operations complete within 500ms.
    'sql_req_duration': ['p(95)<500'],
  },
}
```

**Smell 4: Not using tags**

- **Lines:** [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75]
- **Snippet:**
```js
export default () => {
  // ...
  db.exec(
    `insert into load_messages(room_id) values('room${getRandomInt(
      0,
      rooms
    )}');`
  )
  // ...
  counterInserts.add(1)
  // ...
}
```
- **Refactored:**
```js
import { group } from 'k6' // Make sure to add this import

export default () => {
  let rand = 0
  if (virtualUsers > 1) {
    rand = getRandomInt(0, virtualUsers)
    sleep(rand / rate)
  }

  const roomId = `room${getRandomInt(0, rooms)}`

  // Group operations to tag built-in and custom metrics together.
  group('DB_Insert_Message', function () {
    const start = new Date()
    // Pass the query as a parameter to avoid SQL injection risks
    db.exec(`insert into load_messages(room_id) values($1);`, roomId)
    const finish = new Date()
    // Add a tag to the custom metric for granular analysis.
    counterInserts.add(1, { room: roomId })
    sleep((virtualUsers - rand) / rate - (finish - start) / 1000)
  })
}
```

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
        'http_req_duration': ['p(95)<2000', 'p(99)<2500'],
        'http_req_failed': ['rate<0.01'],
        'checks': ['rate>0.99'],
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
    tags: { name: 'GetFlows', endpoint: 'flow-service', vertical: 'k12' },
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
export let options = {
    vus: 2000,
    duration: '10s',
    thresholds: {
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500', 'p(99)<1000'],
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
const requestTags = {
    endpoint: 'get_flows',
    vertical: 'k12',
    segment: '101',
    modality: 'after_purchase',
    product: '10091',
};

let res = http.get(`${baseUrl}/flow-service/api/v1/flows?vertical=k12&segment=101&modality=after_purchase&product=10091`, {
    headers: headers,
    tags: requestTags,
});

check(res, {
    'status is 200': (r) => r.status === 200,
}, requestTags);
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
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
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
    },
});
```

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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        'checks': ['rate>0.99'],
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
const res = http.post('http://localhost:5000/api/cadastro', body, { headers: headers, tags: { name: 'cadastro', endpoint: '/api/cadastro' } });
```

### `script_196.js` — CHATGPT

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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.95'],
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
        endpoint: 'cadastro',
        method: 'POST',
        flow: 'user_registration',
    },
};

const res = http.post('http://localhost:5000/api/cadastro', body, params);
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
    vus: 1,
    iterations: 20,
    thresholds: {
        http_req_failed: ['rate<0.01'], // less than 1% of requests should fail
        http_req_duration: ['p(95)<500'], // 95th percentile of response times must be below 500ms
        'checks{status é 201 ou 409}': ['rate>0.99'], // over 99% of checks must pass
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
const res = http.post('http://localhost:5000/api/cadastro', body, {
        headers: headers,
        tags: { name: 'CreateUserAPI' },
    });
```

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
let res = http.get(`${baseUrl}/discovery-service/api/v1/products/ghore-boshe-spoken-english/free-products?lang=bn`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/discovery-service/api/v1/products/ghore-boshe-spoken-english/free-products?lang=bn`, {
    headers: headers,
    tags: { name: 'GetFreeProducts', endpoint: 'free-products', service: 'discovery-service' },
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
        endpoint: 'free-products',
        flow: 'product-discovery',
        method: 'GET'
    }
});

check(res, {
    'status is 200': (r) => r.status === 200,
    'response time <= 500ms': (r) => r.timings.duration <= 500,
}, {
    endpoint: 'free-products',
    flow: 'product-discovery'
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
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
        'http_req_failed': ['rate<0.01'],   // HTTP error rate should be less than 1%
        'checks': ['rate>0.99'] // 99% of checks should pass
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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<200'],
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
    tags: { name: 'get_product', endpoint: 'products' }
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
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<200'],
    checks: ['rate>0.99']
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
    endpoint: 'get_product_by_id',
    flow: 'product_lookup'
  }
});

check(getProduct, {
  'status is 200': (r) => r.status === 200,
  'response time < 200ms': (r) => r.timings.duration < 200
}, {
  endpoint: 'get_product_by_id',
  flow: 'product_lookup'
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
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
        'checks': ['rate>0.95'], // 95% of checks must pass
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
    'http_req_failed': ['rate<0.01']
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]
- **Snippet:**
```js
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
const requests = {
    'Get_books': {
      method: 'GET',
      url: url + 'books',
      params: { ...params, tags: { name: 'Get_books', endpoint: 'books', method: 'GET' } },
    },
    'Add Book': {
      method: 'POST',
      url: url + 'books',
      params: { ...params, tags: { name: 'Add Book', endpoint: 'books', method: 'POST' } },
      body: addBookBody,
    },
    'Add Order': {
      method: 'POST',
      url: url + 'orders?bookIsbn=11111111&firstName=Gaetano',
      params: { ...params, tags: { name: 'Add Order', endpoint: 'orders', method: 'POST' } },
      body: null
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
    { duration: '10s', target: 0 }
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
    'Get_books error': ['rate<0.01'],
    'Add Book error': ['rate<0.01'],
    'Add Order error': ['rate<0.01'],
    Get_books: ['p(95)<500'],
    'Add Book': ['p(95)<500'],
    'Add Order': ['p(95)<500']
  }
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
      tags: { endpoint: 'books', operation: 'get_books', flow: 'book_catalog' },
    },
  },
  'Add Book': {
    method: 'POST',
    url: url + 'books',
    params: {
      ...baseParams,
      tags: { endpoint: 'books', operation: 'add_book', flow: 'book_catalog' },
    },
    body: addBookBody,
  },
  'Add Order': {
    method: 'POST',
    url: url + 'orders?bookIsbn=11111111&firstName=Gaetano',
    params: {
      ...baseParams,
      tags: { endpoint: 'orders', operation: 'add_order', flow: 'ordering' },
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
    'http_req_duration': ['p(95)<500'],
    'Get_books error': ['rate<0.01'],
    'Add Book error': ['rate<0.01']
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [5, 6, 63, 64, 65, 66, 67]
- **Snippet:**
```js
const getTrend = new Trend('Get_books');
const getErrorRate = new Rate('Get_books error');
...
check(getResp, {
  'status is 200': (r) => r.status === 200,
}) || getErrorRate.add(1);

getTrend.add(getResp.timings.duration);
```
- **Refactored:**
```js
// In init context
const responseTimeTrend = new Trend('response_time');
const errorRate = new Rate('error_rate');

// In default function
const tags = { endpoint: 'get_books' };
check(getResp, { 'status is 200': (r) => r.status === 200 }, tags) || errorRate.add(1, tags);
responseTimeTrend.add(getResp.timings.duration, tags);
```

### `script_201.js` — CHATGPT

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
    checks: ['rate>0.99']
  }
};
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
    'http_req_failed': ['rate<0.01'],      // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
  },
};
```

### `script_202.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [101]
- **Snippet:**
```js
const response = http.request(method, path, body, { tags });
```
- **Refactored:**
```js
const requestTags = {
  name, // Add a default tag for the endpoint name
  ...tags // Merge with any user-provided tags
};
const response = http.request(method, path, body, { tags: requestTags });
```

### `script_203.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [12]
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
  },
};
```

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
    'insert succeeded': (r) => r.status === 201 || r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
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
    tags: { name: 'insert_store', endpoint: '/mongo-embedded-schema' },
});
```

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
        endpoint: 'mongo-embedded-schema',
        operation: 'create-store',
    },
});
```

### `script_203.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [12]
- **Snippet:**
```js
export let options = test_options;
```
- **Refactored:**
```js
import { test_options, path } from './options.js';

export let options = {
    ...test_options, // Spread to include imported options
    thresholds: {
        http_req_failed: ['rate<0.01'], // http errors should be less than 1%
        http_req_duration: ['p(95)<500'], // 95% of requests must complete below 500ms
    },
};
```

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
    'is status 201': (r) => r.status === 201
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
        'http_req_duration': ['p(95)<2000', 'p(99)<2500'],
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
    tags: { name: 'GetProductVariants', endpoint: '/discovery-service/api/v1/products/ssc-23-smp-sci/variants' }
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
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99']
    }
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
        endpoint: 'product_variants',
        flow: 'discovery_service'
    }
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
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
        'checks': ['rate>0.99'], // 99% of checks must pass
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

// wrap the exec call and check for errors
let result;
try {
  result = db.exec(
    `insert into rls_messages (domain) values ('${
      domains[getRandomInt(0, 5)]
    }');`
  );
  check(result, {
    'insert succeeded': (r) => r !== null && r !== undefined,
  });
} catch (e) {
  check(null, { 'insert succeeded': () => false });
}
```

**Smell 4: Not using tags**

- **Lines:** [59, 60, 61, 62, 63, 65]
- **Snippet:**
```js
db.exec(
  `insert into rls_messages (domain) values ('${
    domains[getRandomInt(0, 5)]
  }');`
)
counterInserts.add(1)
```
- **Refactored:**
```js
db.exec(
  `insert into rls_messages (domain) values ('${
    domains[getRandomInt(0, 5)]
  }');`,
  { tags: { operation: 'insert', table: 'rls_messages' } }
)
counterInserts.add(1, { operation: 'insert', table: 'rls_messages' })
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
    'inserts': ['count>1000', 'rate>100'],
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
import { check, sleep } from 'k6'; // Add 'check' to imports
// ... in the default function
try {
  db.exec(
    `insert into rls_messages (domain) values ('${domains[getRandomInt(0, 5)]}');`
  );
  check(true, { 'database insert succeeded': (v) => v });
} catch (e) {
  check(false, { 'database insert succeeded': (v) => v });
  console.error(e.message);
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
// ... inside the default function
const domainToInsert = domains[getRandomInt(0, 5)];
db.exec(
  `insert into rls_messages (domain) values ('${domainToInsert}');`
);
// ...
counterInserts.add(1, { domain: domainToInsert });
```

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
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
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
    tags: { name: 'get_concert_seats', endpoint: '/concerts/:id/dates/:date/seats' },
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
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99'],
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [14, 15, 16, 17, 18, 19, 21, 23, 24, 25]
- **Snippet:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json',
        'X-Queue-Token': '...'
    }
};

const res = http.get(url, params);

const success = check(res, {
    'status is 200': (r) => r.status === 200,
});
```
- **Refactored:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json',
        'X-Queue-Token': 'eyJjb25jZXJ0SWQiOjEsInRva2VuVXVpZCI6IjJjZDg5ZGY3LWI4MzMtNDgwMS1iNDFhLTZjN2Q4NmU1ZjI0YyJ9'
    },
    tags: {
        endpoint: 'concert_seats',
        flow: 'seat_lookup',
        method: 'GET'
    }
};

const res = http.get(url, params);

const success = check(res, {
    'status is 200': (r) => r.status === 200,
}, {
    endpoint: 'concert_seats',
    flow: 'seat_lookup'
});
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
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should complete below 500ms
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
        name: 'GetAvailableSeats',
    },
};

const res = http.get(url, params);
```

### `script_207.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [11]
- **Snippet:**
```js
const response = http.get(url);
```
- **Refactored:**
```js
const response = http.get(url, { tags: { name: 'GetAllEmployees', endpoint: '/api/controllerAPI/GetAllEmployees' } });
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
    endpoint: 'GetAllEmployees',
    flow: 'get_all_employees'
  }
});
```

### `script_207.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 7]
- **Snippet:**
```js
import { options } from '../share/k6Options.js';
...
export { options };
```
- **Refactored:**
```js
export const options = {
  stages: [
    { duration: '1m', target: 20 },
  ],
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
  },
};
```

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
const response = postStoreOrder.execute();
```
- **Refactored:**
```js
const response = postStoreOrder.execute({ tags: { name: 'PostStoreOrder', endpoint: '/store/order' } });
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
const response = postStoreOrder.execute();
check(response, {
    'Create store order Status is 200': (r) => r.status === 200,
});
```
- **Refactored:**
```js
const tags = { endpoint: 'POST /store/order', flow: 'create_store_order' };
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
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<200'], // 95% of requests should be below 200ms
    },
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
// The request made inside postStoreOrder.execute() should be tagged for better metric filtering.
// Example: http.post(url, payload, { tags: { name: 'CreateOrder' } });
const response = postStoreOrder.execute();

// Tag checks to group their pass/fail results by endpoint or flow.
check(response, {
    'Create store order Status is 200': (r) => r.status === 200,
}, { endpoint: 'store_order' });
```

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

**Smell 3: Not checking requests**

- **Lines:** [11, 12, 13, 14]
- **Snippet:**
```js
export default function(){
    console.log("testando o k6");
    sleep(1);
}
```
- **Refactored:**
```js
import { check, sleep } from 'k6';
import http from 'k6/http';

export default function(){
    const res = http.get('https://your-target-url.com');
    check(res, {
        'status is 200': (r) => r.status === 200,
        'response time < 500ms': (r) => r.timings.duration < 500
    });
    sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [11, 12, 13, 14]
- **Snippet:**
```js
export default function(){
    console.log("testando o k6");
    sleep(1);
}
```
- **Refactored:**
```js
import { check, sleep } from 'k6';
import http from 'k6/http';

export default function(){
    const res = http.get('https://your-target-url.com', {
        tags: { name: 'homepage', flow: 'main' }
    });
    check(res, {
        'status is 200': (r) => r.status === 200
    }, { tags: { name: 'homepage' } });
    sleep(1);
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
        iteration_duration: ['p(95)<1000'],
        iterations: ['count>0']
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
        // The duration of each iteration should be less than 1.1 seconds (1s sleep + 100ms buffer).
        'iteration_duration': ['p(95)<1100'],
    },
}
```

### `script_21.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 51]
- **Snippet:**
```js
export const deleteIndex = function(...) { ... }
export const saveMovies = function(...) { ... }
export const existMovies = function(...) { ... }
```
- **Refactored:**
```js
// Add thresholds in the exported options object, either in this module or in the main script that imports these functions:
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
    'checks': ['rate>0.99'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [10, 14, 31, 45]
- **Snippet:**
```js
let res = http.get(`${host}/${index}`);
res = http.del(`${host}/${index}`);
let res = http.post(`${host}/${index}/_doc/${uuidv4()}`, JSON.stringify(movie), { headers: { 'Content-Type': 'application/json' } });
let res = http.get(`${host}/_cat/indices?format=json&pretty=true`);
```
- **Refactored:**
```js
// deleteIndex: add tags to http calls
let res = http.get(`${host}/${index}`, { tags: { name: 'check_index_exists', index: index } });
res = http.del(`${host}/${index}`, { tags: { name: 'delete_index', index: index } });

// saveMovies: add tags to http call
let res = http.post(
  `${host}/${index}/_doc/${uuidv4()}`,
  JSON.stringify(movie),
  { headers: { 'Content-Type': 'application/json' }, tags: { name: 'save_movie', index: index } }
);

// existMovies: add tags to http call
let res = http.get(`${host}/_cat/indices?format=json&pretty=true`, { tags: { name: 'exist_movies' } });
```

### `script_21.js` — CHATGPT

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
    checks: ['rate>0.99'],
  },
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
let res = http.get(`${host}/${index}`, { tags: { endpoint: 'get_index', index } });

check(res, {
  'get index returned 200 or 404': (r) => r.status === 200 || r.status === 404,
});

if (res.status === 200) {
  res = http.del(`${host}/${index}`, { tags: { endpoint: 'delete_index', index } });
  check(res, {
    'status was 200': (r) => r.status === 200,
    'Response message 200 OK': (r) => r.status_text === '200 OK',
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
http.get(`${host}/${index}`, { tags: { endpoint: 'get_index', index } });
http.del(`${host}/${index}`, { tags: { endpoint: 'delete_index', index } });
http.post(
  `${host}/${index}/_doc/${uuidv4()}`,
  JSON.stringify(movie),
  {
    headers: { 'Content-Type': 'application/json' },
    tags: { endpoint: 'save_movie', index },
  }
);
http.get(`${host}/_cat/indices?format=json&pretty=true`, { tags: { endpoint: 'cat_indices' } });
```

### `script_21.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4]
- **Snippet:**
```js
// The script does not define an 'options' object with performance thresholds.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
    'checks{group:"Delete index movies"}': ['rate>0.99'],
    'checks{group:"Save movies to Elasticsearch"}': ['rate>0.99']
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [10, 14, 31, 45]
- **Snippet:**
```js
let res = http.post(`${host}/${index}/_doc/${uuidv4()}`, JSON.stringify(movie), { headers: { 'Content-Type': 'application/json' } });
```
- **Refactored:**
```js
let res = http.post(`${host}/${index}/_doc/${uuidv4()}`, JSON.stringify(movie), {
  headers: { 'Content-Type': 'application/json' },
  tags: { name: 'SaveMovie' },
});
```

### `script_210.js` — CHATGPT

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

### `script_210.js` — GEMINI

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
  ...test_options, // Keep existing options from the import
  thresholds: {
    'http_req_failed': ['rate<0.01'], // Fail test if error rate > 1%
    'http_req_duration': ['p(95)<500'], // 95th percentile response time must be < 500ms
    'checks': ['rate>0.99'], // >99% of checks must pass
  },
};
```

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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
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
        tags: { name: 'create_user', endpoint: '/v-fail/users' }
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
        checks: ["rate>0.95"],
        http_req_duration: ["p(95)<500"]
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [20, 21, 22, 24, 25, 26, 27]
- **Snippet:**
```js
const response = http.post(`${apiUrl}/v-fail/users`, JSON.stringify(request), {
    headers: { "Content-Type": "application/json" }
});

check(response, {
    "response code was 400": (res) => res.status == 400,
    "response code was 409": (res) => res.status == 409
})
```
- **Refactored:**
```js
const response = http.post(`${apiUrl}/v-fail/users`, JSON.stringify(request), {
    headers: { "Content-Type": "application/json" },
    tags: { endpoint: "create_user_validation_failure", method: "POST" }
});

check(response, {
    "response code was 400 or 409": (res) => res.status === 400 || res.status === 409
}, {
    endpoint: "create_user_validation_failure",
    flow: "negative_user_creation"
});
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
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
    },
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
    tags: {
        name: 'CreateUser-Fail',
    },
});
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
  // It's assumed test_options contains VU and duration settings
  ...test_options,
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks{status is 200}': ['rate>0.99'], // over 99% of status checks should pass
  },
};
```

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
  tags: { name: 'GetCrocodile', endpoint: '/public/crocodiles/1/' },
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
import { sleep, check } from 'k6';

export default function () {
  const resp = http.get('https://test-api.k6.io/public/crocodiles/1/');

  check(resp, {
    'GET crocodile by id returned 200': (r) => r.status === 200,
  });

  errorRate.add(resp.status >= 400);

  sleep(1);
}
```

**Smell 4: Not using tags**

- **Lines:** [26, 28]
- **Snippet:**
```js
const resp = http.get('https://test-api.k6.io/public/crocodiles/1/');

errorRate.add(resp.status >= 400);
```
- **Refactored:**
```js
export default function () {
  const tags = { endpoint: 'get_crocodile_by_id', flow: 'public_crocodiles' };

  const resp = http.get('https://test-api.k6.io/public/crocodiles/1/', {
    tags,
  });

  errorRate.add(resp.status >= 400, tags);

  sleep(1);
}
```

### `script_214.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [28]
- **Snippet:**
```js
errorRate.add(resp.status >= 400);
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const isSuccessful = check(resp, {
  'status is 200': (r) => r.status === 200,
});
errorRate.add(!isSuccessful);
```

**Smell 4: Not using tags**

- **Lines:** [26]
- **Snippet:**
```js
const resp = http.get('https://test-api.k6.io/public/crocodiles/1/');
```
- **Refactored:**
```js
const resp = http.get('https://test-api.k6.io/public/crocodiles/1/', { tags: { name: 'GetPublicCrocodile' } });
```

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
    'checks{scenario:default}': ['rate>0.99']
  }
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
  }), { tags: { name: 'CreateMessage', endpoint: '/api/messages', method: 'POST' } });
```

### `script_215.js` — CHATGPT

**Smell 2: Do not use thresholds**

- **Lines:** [5, 6, 7, 8, 9, 10, 11, 12, 13]
- **Snippet:**
```js
export const options = {
  stages: [...],
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
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99']
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [16, 23]
- **Snippet:**
```js
const res = http.post(`${BASE_URL}/api/messages`, JSON.stringify({...}));
check(res, { ['Create message Success'] : (r) => r.status === 200 });
```
- **Refactored:**
```js
const payload = JSON.stringify({
  authorId: 'test-user-id',
  content: `
    some content number ${Math.floor(Math.random() * 9000 + 1000)} posted from k6
  `
});

const params = {
  headers: { 'Content-Type': 'application/json' },
  tags: { endpoint: 'create_message', flow: 'messages' }
};

const res = http.post(`${BASE_URL}/api/messages`, payload, params);

check(res, {
  'Create message Success': (r) => r.status === 200
}, { endpoint: 'create_message', flow: 'messages' });
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
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks{["Create message Success"]}': ['rate>0.99'], // 99% of checks must pass
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
const params = {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'CreateMessage' },
  };

  const res = http.post(`${BASE_URL}/api/messages`, JSON.stringify({
    authorId: 'test-user-id',
    content: `
      some content number ${Math.floor(Math.random() * 9000 + 1000)} posted from k6
    `
  }), params);
```

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
        'http_req_failed': ['rate<0.05'],
        'checks': ['rate>0.95'],
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
let res = http.post(url, payload, { headers, tags: { name: 'post_pet_by_id', endpoint: '/pet/:id' } });
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
        endpoint: 'postPetById',
        flow: 'pet_update',
        pet_id: String(petId),
    },
});

check(res, {
    'Status is acceptable': (r) => [200, 400, 404, 405, 414, 415, 429, 500].includes(r.status),
    'Response time < 500ms': (r) => r.timings.duration < 500,
}, {
    endpoint: 'postPetById',
    flow: 'pet_update',
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
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
        'checks': ['rate>0.99']              // 99% of checks must pass
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
            name: 'UpdatePetWithFormData',
        },
    });
```

### `script_217.js` — CLAUDE

**Smell 4: Not using tags**

- **Lines:** [58]
- **Snippet:**
```js
let res = http.get(SEAT_LOOKUP_ENDPOINT, { headers });
```
- **Refactored:**
```js
let res = http.get(SEAT_LOOKUP_ENDPOINT, { headers, tags: { name: 'seat_lookup', endpoint: 'concerts_seats' } });
```

### `script_217.js` — CHATGPT

**Smell 3: Not checking requests**

- **Lines:** [14]
- **Snippet:**
```js
let res = http.post(TOKEN_ISSUE_ENDPOINT, JSON.stringify({ userId: i, concertId: 1 }), {
    headers: { 'Content-Type': 'application/json' },
});
```
- **Refactored:**
```js
let res = http.post(
    TOKEN_ISSUE_ENDPOINT,
    JSON.stringify({ userId: i, concertId: 1 }),
    {
        headers: { 'Content-Type': 'application/json' },
        tags: { endpoint: 'token_issue', flow: 'setup' },
    }
);

const ok = check(res, {
    'token issue status is 201': (r) => r.status === 201,
    'token issue response has token': (r) => {
        try {
            return !!JSON.parse(r.body)?.data?.token;
        } catch (e) {
            return false;
        }
    },
}, { endpoint: 'token_issue', flow: 'setup' });

if (ok) {
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

let res = http.get(SEAT_LOOKUP_ENDPOINT, { headers });
```
- **Refactored:**
```js
let res = http.post(
    TOKEN_ISSUE_ENDPOINT,
    JSON.stringify({ userId: i, concertId: 1 }),
    {
        headers: { 'Content-Type': 'application/json' },
        tags: { endpoint: 'token_issue', flow: 'setup' },
    }
);

let res = http.get(SEAT_LOOKUP_ENDPOINT, {
    headers,
    tags: { endpoint: 'seat_lookup', flow: 'seat_lookup' },
});

check(res, {
    'status is 200': (r) => r.status === 200,
    'response time is < 2000ms': (r) => r.timings.duration < 2000,
}, { endpoint: 'seat_lookup', flow: 'seat_lookup' });
```

### `script_217.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [58]
- **Snippet:**
```js
let res = http.get(SEAT_LOOKUP_ENDPOINT, { headers });
```
- **Refactored:**
```js
let params = {
    headers: headers,
    tags: { name: 'SeatLookupAPI' }
};
let res = http.get(SEAT_LOOKUP_ENDPOINT, params);
```

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
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
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
    tags: { name: 'post-user', endpoint: '/post' },
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
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
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
const res = http.post('https://httpbin.test.k6.io/post', payload, {
  headers,
  tags: {
    endpoint: 'httpbin_post',
    flow: 'create_user',
  },
});

check(res, {
  'Post status is 200': (r) => r.status === 200,
  'Post Content-Type header': (r) => r.headers['Content-Type'] === 'application/json',
  'Post response name': (r) => r.status === 200 && r.json().json.name === user.username,
}, {
  endpoint: 'httpbin_post',
  flow: 'create_user',
});
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
    'checks': ['rate>0.99'], // check success rate should be >99%
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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
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
    tags: { name: 'GetPrograms', endpoint: 'programs', type: 'admission' }
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
export let options = {
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
        endpoint: 'programs',
        flow: 'admission_programs',
        method: 'GET'
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
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
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
        name: 'GetPrograms',
    },
});
```

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
    'http_req_failed': ['rate<0.01']
  }
};
```

**Smell 4: Not using tags**

- **Lines:** [38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56]
- **Snippet:**
```js
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
const requests = {
    'Get_books': {
      method: 'GET',
      url: url +'books',
      params: { ...params, tags: { name: 'Get_books', endpoint: 'books', method: 'GET' } },
    },
    'Add Book': {
      method: 'POST',
      url: url+'books',
      params: { ...params, tags: { name: 'Add_Book', endpoint: 'books', method: 'POST' } },
      body: addBookBody,
    },
    'Add Order': {
      method: 'POST',
      url: url + 'orders?bookIsbn=11111111&firstName=Gaetano',
      params: { ...params, tags: { name: 'Add_Order', endpoint: 'orders', method: 'POST' } },
      body: null
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
    { duration: "10s", target: `${__ENV.USERS}` },
    { duration: "100s", target: `${__ENV.USERS}` },
    { duration: "10s", target: 0 }
  ],
  thresholds: {
    http_req_failed: ['rate<0.01'],
    checks: ['rate>0.99'],
    'Get_books': ['p(95)<500'],
    'Add Book': ['p(95)<800'],
    'Add Order': ['p(95)<800'],
    'Get_books error': ['rate<0.01'],
    'Add Book error': ['rate<0.01'],
    'Add Order error': ['rate<0.01']
  }
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
      tags: { endpoint: 'books', operation: 'get_books' },
    },
  },
  'Add Book': {
    method: 'POST',
    url: url + 'books',
    params: {
      ...baseParams,
      tags: { endpoint: 'books', operation: 'add_book' },
    },
    body: addBookBody,
  },
  'Add Order': {
    method: 'POST',
    url: url + 'orders?bookIsbn=11111111&firstName=Gaetano',
    params: {
      ...baseParams,
      tags: { endpoint: 'orders', operation: 'add_order' },
    },
    body: null,
  }
};
```

### `script_22.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [14]
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
    'Get_books error': ['rate<0.05'],    // Custom error rate for Get_books should be less than 5%
    'Add Book error': ['rate<0.05'],     // Custom error rate for Add Book should be less than 5%
    'Add Order error': ['rate<0.05']     // Custom error rate for Add Order should be less than 5%
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [38]
- **Snippet:**
```js
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
  const requests = {
      'Get_books': {
        method: 'GET',
        url: url +'books',
        params: { 
          ...params, 
          tags: { name: 'GetBooks' } 
        },
      },
      'Add Book': {
        method: 'POST',
        url: url+'books',
        params: { 
          ...params, 
          tags: { name: 'AddBook' } 
        },
        body: addBookBody,
      },
      'Add Order': {
        method: 'POST',
        url: url + 'orders?bookIsbn=11111111&firstName=Gaetano',
        params: { 
          ...params, 
          tags: { name: 'AddOrder' } 
        },
        body: null
      }
    };
```

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
let res = http.get(`${baseUrl}/cart-service/api/v1/carts?identifier=658ad45415e59054c0983e52`, {
    headers: headers
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/cart-service/api/v1/carts?identifier=658ad45415e59054c0983e52`, {
    headers: headers,
    tags: { name: 'GetCart', endpoint: '/cart-service/api/v1/carts' }
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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500'],
        checks: ['rate>0.99']
    }
};
```

**Smell 4: Not using tags**

- **Lines:** [21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
- **Snippet:**
```js
let res = http.get(`${baseUrl}/cart-service/api/v1/carts?identifier=658ad45415e59054c0983e52`, {
    headers: headers
});

check(res, {
    'status is 200': (r) => r.status === 200,
    'status is 502': (r) => r.status === 502,
    'status is 503': (r) => r.status === 503,
    'status is 500': (r) => r.status === 500,
    'status is 520': (r) => r.status === 520,
    'status is 521': (r) => r.status === 521,
    'status is 522': (r) => r.status === 522,
    'response time > 200ms': (r) => r.timings.duration > 100,
});
```
- **Refactored:**
```js
let res = http.get(`${baseUrl}/cart-service/api/v1/carts?identifier=658ad45415e59054c0983e52`, {
    headers: headers,
    tags: {
        endpoint: 'get_cart',
        flow: 'cart'
    }
});

check(res, {
    'status is 200': (r) => r.status === 200,
    'response time <= 200ms': (r) => r.timings.duration <= 200
}, {
    endpoint: 'get_cart',
    flow: 'cart'
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
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
- **Snippet:**
```js
check(res, {
    'status is 200': (r) => r.status === 200,
    'status is 502': (r) => r.status === 502,
    'status is 503': (r) => r.status === 503,
    'status is 500': (r) => r.status === 500,
    'status is 520': (r) => r.status === 520,
    'status is 521': (r) => r.status === 521,
    'status is 522': (r) => r.status === 522,
    'response time > 200ms': (r) => r.timings.duration > 100,
});
```
- **Refactored:**
```js
check(res, {
    'status is 200': (r) => r.status === 200,
});
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
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500', 'p(99)<1000'],
    'checks': ['rate>0.99'],
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
const res = http.get(url, {
  tags: {
    name: 'findByStatus',
    status: status,
    endpoint: '/v2/pet/findByStatus',
  },
});
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
    response_time: ['p(95)<500'],
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [25, 28, 34]
- **Snippet:**
```js
const res = http.get(url);
responseTime.add(res.timings.duration);
check(res, { ... });
```
- **Refactored:**
```js
const tags = { endpoint: 'findByStatus', status };
const res = http.get(url, { tags });
responseTime.add(res.timings.duration, tags);
check(res, {
  'Status is 200': (r) => r.status === 200,
  'Response time < 500ms': (r) => r.timings.duration < 500,
}, tags);
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
  vus: 10,
  duration: '10m',
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'checks{Status is 200}': ['rate>0.99'], // >99% of requests must be successful
    'response_time': ['p(95)<500'],      // 95th percentile of response time must be below 500ms
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
    status: status,
    name: 'GetPetByStatus',
  },
};

// Kirim request ke API
const res = http.get(url, params);

// Menyimpan metrik tambahan
responseTime.add(res.timings.duration, { status: status });
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

// inside the group callback:
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
  tags: { endpoint: 'concrete-products', group: testConfiguration.group, testId: testConfiguration.id },
});
```

### `script_224.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [36]
- **Snippet:**
```js
const response = concreteProductsResource.get(product.sku);
```
- **Refactored:**
```js
import { check } from 'k6'; // Add this import at the top

// ... in default function
const response = concreteProductsResource.get(product.sku);

check(response, {
  'GET concrete product status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [36]
- **Snippet:**
```js
const response = concreteProductsResource.get(product.sku);
```
- **Refactored:**
```js
// Assuming ConcreteProductsResource.get() accepts a params object for tagging
const response = concreteProductsResource.get(product.sku, {
  tags: { name: testConfiguration.metrics[0] }, // Tag with the same name as the metric
});
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
    http_req_duration: ['p(95)<500'],  // 95% of requests must complete below 500ms
    http_req_failed: ['rate<0.01'],     // Error rate must be less than 1%
    checks: ['rate>0.99'],              // More than 99% of checks must pass
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
const res = http.get('http://api:3000/', { tags: { name: 'Homepage' } });
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
        'checks{status was 200}': ['rate>0.99'],
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
let res = http.get('http://localhost:3000/endpoint', {
    tags: { name: 'MainEndpoint' },
});
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
// Move file reading to the init context (outside default function)
const fileData = open('D:/Document/Semester 8/SQA/swagger-petstore-sqa/pet_s3/cat.jpeg', 'b');

export default function () {
  let baseUrl = 'https://petstore.swagger.io/v2/pet';
  const petId = __VU;
  const url = `${baseUrl}/${petId}/uploadImage`;

  const payload = {
    file: http.file(fileData, 'cat.jpeg', 'image/jpeg'),
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
    http_req_failed: ['rate<0.05'],
    http_req_duration: ['p(95)<2000'],
    'checks{check:✅ Status is 200 (Success)}': ['rate>0.90'],
    total_failures: ['count<10'],
    check_slow_response: ['count<50'],
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
    name: 'upload_pet_image',
    endpoint: 'POST /pet/:id/uploadImage',
  },
});
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
    'http_req_failed': ['rate<0.05'], // http errors should be less than 5%
    'http_req_duration': ['p(95)<2000'], // 95% of requests must complete below 2000ms
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
    name: 'uploadPetImage',
  },
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
import { test_options, path } from './options.js';

export let options = Object.assign({}, test_options, {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration{name:GET}': ['p(95)<500'], // 95% of requests to this endpoint must be below 500ms
  },
});
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
const res = http.get('https://quickpizza.grafana.com', { tags: { name: 'quickpizza_home', endpoint: '/' } });
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
let res = http.get('https://www.cruzeiro.com.br/', { tags: { name: 'homepage', endpoint: '/' } });
```

### `script_232.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 5, 6, 7, 8, 9, 10]
- **Snippet:**
```js
export let options = {
  stages: [
    { duration: '30s', target: 10 }, // Sobe para 10 usuários em 30 segundos
    { duration: '1m', target: 50 },  // Mantém 50 usuários por 1 minuto
    { duration: '30s', target: 0 },  // Reduz para 0 usuários em 30 segundos
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
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
    'checks': ['rate>0.99'], // 99% of checks must pass
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
export let options = {
  ...test_options,
  thresholds: {
    'http_req_failed': ['rate<0.01'],    // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'],  // 95% of requests should be below 500ms
    'checks': ['rate>0.99']             // 99% of checks should pass
  },
};
```

### `script_234.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 32]
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
    }
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
import { check } from 'k6';

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(95)<200'], // 95% of requests should be below 200ms
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [25, 26]
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
request.push({
    method: 'GET',
    url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
    params: {
        headers: params.headers,
        tags: { name: 'SearchUser' },
    }
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
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'checks': ['rate>=0.99'], // 99% or more of checks must pass
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
      name: 'CreateUser',
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
        name: 'CreateMember',
        endpoint: '/api/members',
    },
};

let response = http.post('http://localhost:8080/api/members', body, params);
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
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
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
        name: 'CreateMemberAPI',
    },
};

let response = http.post('http://localhost:8080/api/members', body, params);
```

### `script_237.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8]
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
import { check } from 'k6';

const response = http.get(BASE_URL);
check(response, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
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
const response = http.get(BASE_URL, { tags: { name: 'homepage', endpoint: 'GET /' } });
```

### `script_237.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4]
- **Snippet:**
```js
export default function() {
```
- **Refactored:**
```js
import http from 'k6/http'
import { sleep } from 'k6'

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
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
import { check } from 'k6';
// ...
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

// inside the group:
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
const response = productPage.get(product.url, {
  tags: { name: 'S8_get_product', group: testConfiguration.group },
});

metrics[testConfiguration.metrics[0]].add(response.timings.duration, {
  tags: { name: 'S8_get_product', group: testConfiguration.group },
});
```

### `script_238.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [26, 27, 28, 35]
- **Snippet:**
```js
const fixture = FullProductFixture.createFixture({
  productCount: testConfiguration.vus ?? EnvironmentUtil.getRampVus(),
});

// ...

export default function (data) {
  const product = fixture.iterateData(data);

```
- **Refactored:**
```js
export function setup() {
  // Fixture creation is moved from the init context to setup,
  // ensuring it runs only once for the entire test.
  const fixture = FullProductFixture.createFixture({
    productCount: testConfiguration.vus ?? EnvironmentUtil.getRampVus(),
  });
  return fixture.getData(); // Return the complete dataset
}

export default function (data) {
  // Use a standard k6 pattern to select an item from the setup data.
  const product = data[(__VU - 1) % data.length];
  // ... rest of the function
}
```

**Smell 3: Not checking requests**

- **Lines:** [39, 41]
- **Snippet:**
```js
const response = productPage.get(product.url);

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
import { group, check } from 'k6'; // Ensure 'check' is imported

// ... inside the default function
const response = productPage.get(product.url);

const isSuccessful = check(response, {
  'status is 200': (r) => r.status === 200,
});

if (isSuccessful) {
  // Only add metrics for successful responses
  metrics[testConfiguration.metrics[0]].add(response.timings.duration);
}
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
// Assuming productPage.get accepts k6 params object
const requestTags = { name: 'S8_get_product' };
const response = productPage.get(product.url, { tags: requestTags });

// Add the same tags to the custom metric for consistent reporting
metrics[testConfiguration.metrics[0]].add(response.timings.duration, requestTags);
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
const res = http.get(__ENV.URL, { tags: { name: 'homepage', endpoint: 'GET /' } });
```

### `script_239.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1]
- **Snippet:**
```js
// The script does not define an 'options' object with thresholds.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<200'], // 95% of requests should complete below 200ms
  },
};
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
        'status was 200': (r) => r.status == 200,
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

export default function(){
    const res = http.get(__ENV.URL, {
        tags: {
            name: 'Homepage',
        },
    });
    sleep(1);
}
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
		'http_req_duration': ['p(95)<500'],
		'http_req_failed': ['rate<0.01'],
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
				if(signUpRes.status !== 200){
```
- **Refactored:**
```js
let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, { headers: headers });
check(verifyOTPres, {
	'verifyOTP status is 200': (r) => r.status === 200,
	'verifyOTP response time < 200ms': (r) => r.timings.duration < 200,
});

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
	tags: { name: 'userExists', endpoint: '/v1/userExists' },
});

let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, {
	headers: headers,
	tags: { name: 'verifyOTP', endpoint: '/v1/verifyOTP' },
});

let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
	headers: headers,
	tags: { name: 'signup', endpoint: '/v1/signup' },
});
```

### `script_24.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [14]
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
        // Ramp up to 1 VUs for 5 second
        { duration: "10s", target: 100 },
		{ duration: "10s", target: 100 },
      ],
    thresholds: {
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
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
			if(verifyOTPres.status !== 200){
                // ...
			}
			else if(verifyOTPres.json().status === "OK"){
				//-----------------------SignUP API-----------------------//
				let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
					headers: headers});
					if(signUpRes.status !== 200){
                        // ...
                    }
            }
```
- **Refactored:**
```js
		let verifyOTPres = http.post(`${baseUrl}/v1/verifyOTP`, verifyJSON, {
			headers: headers});

        check(verifyOTPres, {
            'verifyOTP status is 200': (r) => r.status === 200,
        });

			if(verifyOTPres.status !== 200){
                // ...
			}
			else if(verifyOTPres.json().status === "OK"){
				//-----------------------SignUP API-----------------------//
				let signUpRes = http.post(`${baseUrl}/v1/signup`, signupJSON, {
					headers: headers});

                check(signUpRes, {
                    'signup status is 200': (r) => r.status === 200,
                });

					if(signUpRes.status !== 200){
                        // ...
                    }
            }
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
    tags: { name: 'GetPrograms', endpoint: '/k12-course-service/api/v1/programs' },
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
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
        'checks': ['rate>0.99'], // 99% of checks should pass
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
        name: 'GetProgramsByBatch',
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
    'checks': ['rate>0.95'],
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
const res = http.get(url, {
  headers,
  tags: { name: 'user_logout', endpoint: '/v2/user/logout', method: 'GET' },
});
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
    // 95% of requests must complete below 500ms
    'http_req_duration': ['p(95)<500'],
    // The rate of successful checks for 'Status is 200' must be over 99%
    'checks{Status is 200}': ['rate>0.99'],
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
const res = http.get(url, {
  headers,
  tags: { name: 'UserLogout' },
});

// Menyimpan metrik tambahan
responseTime.add(res.timings.duration, { name: 'UserLogout' });
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
    'http_req_duration': ['p(95)<500', 'p(99)<1000'],
    'checks': ['rate>0.95'],
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
  tags: { name: 'PostPetById', endpoint: '/v2/pet/:id' },
});
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
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'checks{\'Status is 200\'}': ['rate>0.95'], // 95% of checks for status 200 should pass
    'response_time': ['p(95)<500'], // 95% of response times should be below 500ms
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
  const params = {
    tags: {
      name: 'CreatePet', // Tag for identifying the specific request
    },
  };

  // Kirim request POST dengan form data dan tag
  const res = http.post(url, payload, params);

  // Menyimpan metrik tambahan dengan tag
  responseTime.add(res.timings.duration, { name: 'CreatePet' });
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

// inside the group callback:
const response = guestCartsResource.addItem(null, product.sku, 1);

check(response, {
  'add guest cart item status is 2xx': (r) => r.status >= 200 && r.status < 300,
  'add guest cart item response has data': (r) => r.json('data') !== null,
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
  tags: { name: 'SAPI31_post_guest_cart_items', group: testConfiguration.group },
});
```

### `script_245.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [43]
- **Snippet:**
```js
const response = guestCartsResource.addItem(null, product.sku, 1);
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const response = guestCartsResource.addItem(null, product.sku, 1);
check(response, {
  'item added to cart successfully (status 201)': (r) => r.status === 201,
});
```

**Smell 4: Not using tags**

- **Lines:** [43]
- **Snippet:**
```js
const response = guestCartsResource.addItem(null, product.sku, 1);
```
- **Refactored:**
```js
// Assuming the `addItem` method in `GuestCartsResource` is modified to accept a `params` object
const params = {
  tags: {
    name: testConfiguration.metrics[0], // e.g., 'SAPI31_post_guest_cart_items'
  },
};
const response = guestCartsResource.addItem(null, product.sku, 1, params);
```

### `script_247.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
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

### `script_247.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
- **Snippet:**
```js
The script does not define an `options` object with a `thresholds` property. Without thresholds, the test will always pass in a CI/CD environment, regardless of the system's performance.
```
- **Refactored:**
```js
import { sleep } from 'k6';
import http from 'k6/http';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<200'], // 95% of requests should be below 200ms
  },
};

const BASE_URL = 'http://localhost:8888/alphamart';

// ...
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

  const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);

  check(response, {
    'DELETE request has status 204': (r) => r.status === 204,
  });

// ...
```

**Smell 4: Not using tags**

- **Lines:** [14]
- **Snippet:**
```js
const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);
```
- **Refactored:**
```js
// ...

export default function () {
  const params = {
    headers: {
      'my-header-one': 'hello',
      'my-header-two': 'world',
    },
    tags: {
      name: 'DeleteEcho',
    },
  };

  const response = http.del(BASE_URL + "/api/basic/echo?user-id=9090", null, params);

// ...
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
const resCo = http.post(`${hostprefix}/SYNC-G-4096`, JSON.stringify({ operation: "test" }), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'SYNC-G-4096', endpoint: '/SYNC-G-4096' },
});
check(resCo, { 'A status was 200': (r) => r.status == 200 }, { tags: { name: 'SYNC-G-4096' } });
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
)
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
    'response_time': ['p(95)<500', 'p(99)<1000'],
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
  tags: { name: 'delete_pet', endpoint: '/v2/pet/:id' },
});
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
  vus: 1600, // Jumlah VUs
  iterations: 1600,
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    'checks': ['rate>0.95'], // 95% of checks must pass
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

### `script_25.js` — CLAUDE

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
    'latency_trend': ['p(95)<500', 'p(99)<1000'],
    'received_updates': ['count>0'],
    'checks': ['rate>0.95'],
    'ws_connecting': ['p(95)<1000'],
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
const res = ws.connect(URL, {}, (socket) => { ... })
check(msg, { 'subscribed to realtime': ... })
check(msg, { 'got realtime notification': ... })
check(res, { 'status is 101': ... })
```
- **Refactored:**
```js
const res = ws.connect(URL, { tags: { name: 'ws_realtime_connect' } }, (socket) => {
  // ...
  check(msg, { 'subscribed to realtime': (msg) =>
    msg.topic === 'realtime:any' && msg.payload.status === 'ok'
  }, { tags: { check_type: 'subscription', channel: 'realtime:any' } })
  // ...
  check(msg, { 'got realtime notification': (msg) => msg.topic === 'realtime:any' },
    { tags: { check_type: 'postgres_changes', channel: 'realtime:any' } })
})
check(res, { 'status is 101': (r) => r && r.status === 101 },
  { tags: { check_type: 'ws_handshake', name: 'ws_realtime_connect' } })
```

### `script_25.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [26, 30]
- **Snippet:**
```js
const to = {}
...
export const options = {
  ...
  thresholds: to,
  ...
}
```
- **Refactored:**
```js
export const options = {
  ...
  thresholds: {
    // 99% of checks should pass
    'checks': ['rate>0.99'],
    // 95% of WebSocket connections should be established within 1s
    'ws_connecting': ['p(95)<1000'],
    // Latency for 95% of received updates should be below 500ms
    'latency_trend': ['p(95)<500'],
  },
  ...
}
```

### `script_250.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [23, 32, 33, 34, 35, 36]
- **Snippet:**
```js
const response = http.get('http://test.k6.io');
...
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
    tags: { name: 'homepage', endpoint: '/' },
});
```

### `script_250.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [23]
- **Snippet:**
```js
const response = http.get('http://test.k6.io');
```
- **Refactored:**
```js
const response = http.get('http://test.k6.io', {
      tags: { name: 'PublicCrocodilesHomepage' },
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

// Inside the group:
const response = checkoutResource.checkout();
const success = check(response, {
  'checkout status is 200 or 201': (r) => r.status === 200 || r.status === 201,
  'checkout response has body': (r) => r.body && r.body.length > 0,
});
if (success) {
  metrics[testConfiguration.metrics[0]].add(response.timings.duration);
}
```

**Smell 4: Not using tags**

- **Lines:** [57]
- **Snippet:**
```js
const response = checkoutResource.checkout();
```
- **Refactored:**
```js
// Pass tags when making the request inside CheckoutResource, or apply tags at call site:
const response = checkoutResource.checkout({ tags: { name: 'POST_checkout', group: testConfiguration.group, testId: testConfiguration.id } });
```

### `script_251.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [35]
- **Snippet:**
```js
let fixture = new CheckoutFixture(fixtureConfig);
```
- **Refactored:**
```js
// Move fixture instantiation into the setup function so it runs only once per test, not once per VU.
export function setup() {
  const fixture = new CheckoutFixture(fixtureConfig);
  return fixture.getData(); // Return all test data
}

// In the default function, use the data array passed from setup.
export default function (data) {
  // Select data for the current VU, e.g., using a modulo operator for safety
  const customer = data[exec.vu.idInTest % data.length];
  // ...
}
```

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
// ...
const response = checkoutResource.checkout();
const isSuccess = check(response, {
  'is status 200': (r) => r.status === 200,
});

// Only add metrics for successful requests
if (isSuccess) {
    metrics[testConfiguration.metrics[0]].add(response.timings.duration);
}
```

**Smell 4: Not using tags**

- **Lines:** [57]
- **Snippet:**
```js
const response = checkoutResource.checkout();
```
- **Refactored:**
```js
// Assuming checkoutResource.checkout() is a wrapper that can pass params to an underlying k6 http request.
// Pass a 'tags' object to enrich the metrics for better observability.
const response = checkoutResource.checkout({
  tags: {
    name: 'SAPI7_PostCheckout',
  },
});
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

- **Lines:** [22, 24]
- **Snippet:**
```js
let res = http.post('http://localhost:5680/api/v1/auth/token', data)

check(res, { 'success login': (r) => r.status === 200 })
```
- **Refactored:**
```js
let res = http.post('http://localhost:5680/api/v1/auth/token', data, {
  tags: { name: 'auth_token', endpoint: '/api/v1/auth/token' },
})

check(res, { 'success login': (r) => r.status === 200 }, { tags: { name: 'auth_token' } })
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
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<200'], // 95% of requests should be below 200ms
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
let res = http.post('http://localhost:5680/api/v1/auth/token', data, { tags: { name: 'Login' } });
```

### `script_253.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 32]
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

### `script_253.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [3]
- **Snippet:**
```js
// No options or thresholds are defined in the script.
```
- **Refactored:**
```js
import http from 'k6/http';
import { check } from 'k6';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95 percent of response times must be below 500ms
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
request.push({
    method: 'GET',
    url: 'http://social-net:8080/user/search?first_name=И&second_name=Брагина',
    params: {
        ...params,
        tags: { name: 'UserSearch' }
    }
});
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
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95 percent of response times must be below 500ms
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
  tags: { name: 'CreatePayload' }, // Tag added to group metrics for this endpoint
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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<2000'],
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
        // For an invalid payload, expect over 99% of requests to return HTTP 400.
        'checks{Status is 400}': ['rate>0.99'],
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
    tags: { name: 'CreateUserWithArray-Invalid' },
};

let res = http.post(url, invalidPayload, params);
```

### `script_257.js` — CLAUDE

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

// inside the group callback:
const response = catalogSearchResource.get({ q: product.sku });

check(response, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
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
const response = catalogSearchResource.get(
  { q: product.sku },
  { tags: { name: 'catalog_search', group: testConfiguration.group, endpoint: 'GET /catalog-search' } }
);
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
// In init context:
let fixture;

// In setup function:
export function setup() {
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
import { check } from 'k6';
// ...
const response = catalogSearchResource.get({ q: product.sku });

check(response, {
  'status is 200': (r) => r.status === 200,
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
// Assuming the resource method forwards k6 HTTP params
const params = {
  tags: {
    name: 'SAPI_CatalogSearch',
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
const res = http.get('https://www.google.com', {
  tags: { name: 'google_homepage', endpoint: 'GET_root' },
});
```

### `script_259.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 18]
- **Snippet:**
```js
The entire script lacks an `options` object with a `thresholds` property, meaning the test will always pass regardless of the system's performance.
```
- **Refactored:**
```js
import { sleep } from 'k6';
import exec from 'k6/execution';
import http from 'k6/http';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
};

// ... rest of the script
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
import exec from 'k6/execution';
import http from 'k6/http';

// ...

export default function () {
    const res = http.get('https://www.google.com');
    check(res, {
        'status is 200': (r) => r.status === 200,
    });

    // ...
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
  tags: { name: 'GoogleHomepage' },
});
```

### `script_26.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5]
- **Snippet:**
```js
import k6 from 'k6';
import http from 'k6/http';
```
- **Refactored:**
```js
import k6 from 'k6';
import http from 'k6/http';

export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],
    http_req_duration: ['p(95)<500'],
    checks: ['rate>0.99'],
  },
};
```

### `script_26.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1]
- **Snippet:**
```js
The script lacks an exported `options` object with a `thresholds` configuration. The entire file is implicated.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
  },
};

import k6 from 'k6';
import http from 'k6/http';
```

**Smell 3: Not checking requests**

- **Lines:** [1031]
- **Snippet:**
```js
const response = http.request(...args);
```
- **Refactored:**
```js
    const response = http.request(...args);
    // Add a default check to ensure the request was successful, even if no post-request script is provided.
    k6.check(response, {
        'default: status was 2xx': (r) => r.status >= 200 && r.status < 300,
    });
    if (post) {
```

**Smell 4: Not using tags**

- **Lines:** [1075, 1076, 1077]
- **Snippet:**
```js
if (tags && typeof tags === 'object') {
    config.options.tags = tags;
  }
```
- **Refactored:**
```js
  config.options = options || {};
  
  // Automatically add the request name as a tag for better metric filtering.
  // Then merge any additional user-provided tags.
  const defaultTags = { name: name || evaluate(address) };
  config.options.tags = Object.assign(defaultTags, tags);
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
  ...test_options, // Preserves existing options from the import
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // <1% of requests should fail
    'http_req_duration': ['p(95)<250'], // 95th percentile response time must be <250ms
    'checks': ['rate>0.99']            // >99% of checks must succeed
  }
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
    tags: { name: 'GetNotices', endpoint: 'notices', service: 'notice-service' }
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
check(res, {
    'status is 200': (r) => r.status === 200,
});
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
        name: 'GetNotices-v1' // Add a tag to identify this specific request
    }
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
    // The rate of successful inserts must be at least 1 per second.
    'inserts': ['rate>=1'],
  },
}
```

**Smell 4: Not using tags**

- **Lines:** [77]
- **Snippet:**
```js
counterInserts.add(1)
```
- **Refactored:**
```js
counterInserts.add(1, { room_id: room })
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

// inside default function:
const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
check(res, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0,
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
  tags: { name: 'homepage', endpoint: '/' },
});
```

### `script_265.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 9]
- **Snippet:**
```js
import http from 'k6/http';
import { sleep } from 'k6';

// k6 run -e MY_HOSTNAME=test.k6.io 8-env.js

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
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<200'], // 95% of requests should be below 200ms
  },
};

export default function () {
  const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
  sleep(1);
}
```

**Smell 3: Not checking requests**

- **Lines:** [7, 8]
- **Snippet:**
```js
const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
  sleep(1);
```
- **Refactored:**
```js
const res = http.get(`https://${__ENV.MY_HOSTNAME}`);
  check(res, { 'status is 200': (r) => r.status === 200 });
  sleep(1);
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

### `script_266.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [56, 62, 64, 65, 70, 71]
- **Snippet:**
```js
checkoutResource.checkout();
...
const response = ordersResource.all();
orderId = JSON.parse(response.body).data[0].id;
metrics['SAPI38_get_orders'].add(response.timings.duration);
...
const response = ordersResource.get(orderId, [...]);
metrics['SAPI39_get_orders_details'].add(response.timings.duration);
```
- **Refactored:**
```js
import { check } from 'k6';

// In 'Place orders' group:
group('Place orders', () => {
  const checkoutResource = new CheckoutResource(idCart, customerEmail, bearerToken);
  const checkoutResponse = checkoutResource.checkout();
  check(checkoutResponse, {
    'checkout status is 201': (r) => r.status === 201,
  });
});

// In 'Get orders' group:
group('Get orders', () => {
  const ordersResource = new OrdersResource(bearerToken);
  const response = ordersResource.all();
  check(response, {
    'get orders status is 200': (r) => r.status === 200,
    'get orders body has data': (r) => JSON.parse(r.body).data.length > 0,
  });
  orderId = JSON.parse(response.body).data[0].id;
  metrics['SAPI38_get_orders'].add(response.timings.duration);
});

// In 'Get order details' group:
group('Get order details', () => {
  const ordersResource = new OrdersResource(bearerToken);
  const response = ordersResource.get(orderId, ['order-shipments', 'concrete-products', 'abstract-products']);
  check(response, {
    'get order details status is 200': (r) => r.status === 200,
  });
  metrics['SAPI39_get_orders_details'].add(response.timings.duration);
});
```

**Smell 4: Not using tags**

- **Lines:** [56, 62, 70]
- **Snippet:**
```js
checkoutResource.checkout();
...
const response = ordersResource.all();
...
const response = ordersResource.get(orderId, ['order-shipments', 'concrete-products', 'abstract-products']);
```
- **Refactored:**
```js
// Pass tags as request params inside each resource call or at the call site:

// In 'Place orders' group:
group('Place orders', () => {
  const checkoutResource = new CheckoutResource(idCart, customerEmail, bearerToken);
  checkoutResource.checkout({ tags: { name: 'checkout', group: 'Order', testId: 'SAPI38' } });
});

// In 'Get orders' group:
group('Get orders', () => {
  const ordersResource = new OrdersResource(bearerToken);
  const response = ordersResource.all({ tags: { name: 'get_orders', group: 'Order', testId: 'SAPI38' } });
  orderId = JSON.parse(response.body).data[0].id;
  metrics['SAPI38_get_orders'].add(response.timings.duration);
});

// In 'Get order details' group:
group('Get order details', () => {
  const ordersResource = new OrdersResource(bearerToken);
  const response = ordersResource.get(orderId, ['order-shipments', 'concrete-products', 'abstract-products'], { tags: { name: 'get_order_details', group: 'Order', testId: 'SAPI39' } });
  metrics['SAPI39_get_orders_details'].add(response.timings.duration);
});
```

### `script_266.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [62, 70]
- **Snippet:**
```js
const response = ordersResource.all();
// ...
const response = ordersResource.get(orderId, ['order-shipments', 'concrete-products', 'abstract-products']);
```
- **Refactored:**
```js
import { check } from 'k6';
// ...
const allOrdersResponse = ordersResource.all();
check(allOrdersResponse, {
  'GET /orders status is 200': (r) => r.status === 200,
});
// ...
const orderDetailsResponse = ordersResource.get(orderId, ['order-shipments', 'concrete-products', 'abstract-products']);
check(orderDetailsResponse, {
  'GET /orders/{id} status is 200': (r) => r.status === 200,
});
```

**Smell 4: Not using tags**

- **Lines:** [65, 71]
- **Snippet:**
```js
metrics['SAPI38_get_orders'].add(response.timings.duration);
// ...
metrics['SAPI39_get_orders_details'].add(response.timings.duration);
```
- **Refactored:**
```js
metrics['SAPI38_get_orders'].add(response.timings.duration, { name: 'SAPI38_get_orders' });
// ...
metrics['SAPI39_get_orders_details'].add(response.timings.duration, { name: 'SAPI39_get_orders_details' });
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
        http_req_failed: ['rate<0.01'],
        http_req_duration: ['p(95)<500', 'p(99)<1000'],
        'checks': ['rate>0.99'],
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
        'checks': ['rate>0.95'],             // 95% of checks must pass
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
        tags: { name: 'create_user', endpoint: '/v-throw/users', method: 'POST' }
    });
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
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500']
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
    tags: { name: 'CreateUser-Invalid' }
});
```

### `script_269.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [6]
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

// inside default function:
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
http.get('https://self-signed.badssl.com/', { tags: { name: 'self-signed-badssl', endpoint: 'home' } });
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
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
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
  tags: { name: 'BadSSL-Homepage' },
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
        'http_req_duration': ['p(95)<1000'],
        'http_req_failed': ['rate<0.1'],
        'check_success': ['count>0'],
        'check_fail_500': ['count<10'],
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
        endpoint: '/v2/user/login'
    }
};
...
res = http.get(url, params);
```

### `script_27.js` — GEMINI

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
        { duration: '2m', target: 70 },
        { duration: '6m', target: 700 },
        { duration: '2m', target: 70 },
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<2000'], // 95% of requests should be below 2s
        'checks': ['rate>0.98'], // 98% of checks should pass
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [32, 42]
- **Snippet:**
```js
const params = {
    headers: {
        'Content-Type': 'application/json'
    }
};

let res;
// ...
try {
    res = http.get(url, params);
} catch (error) {
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
// ...
try {
    res = http.get(url, params);
} catch (error) {
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
const response = http.post(url, { cookies }, { tags: { name: 'logout', endpoint: endpoint } });
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
const params = {
    cookies: cookies,
    tags: {
        name: 'Logout',
    },
};
const response = http.post(url, null, params);
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
http.get('https://www.google.com', { tags: { name: 'google_homepage', endpoint: 'GET_root' } });
```

### `script_271.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 15]
- **Snippet:**
```js
The script does not export an `options` object with a `thresholds` property, making it impossible to programmatically determine if the test passed or failed based on metric criteria.
```
- **Refactored:**
```js
import { randomIntBetween } from "https://jslib.k6.io/k6-utils/1.1.0/index.js";
import { sleep } from 'k6';
import exec from 'k6/execution';
import http from 'k6/http';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // 1% of requests are allowed to fail
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
import { check } from 'k6';
// ... in default function
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
  tags: { 
    name: 'Homepage' 
  },
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
export let options = {
  ...test_options,
  thresholds: {
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<200'],
    'checks': ['rate>0.99'],
  },
};
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
            ...
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
const resCo = httppost("G-1536", {
    operation: "test",
})
check(resCo, { 'A status was 200': (r) => r.status == 200 });
```
- **Refactored:**
```js
const resCo = http.post(`${hostprefix}/SYNC-G-1536`, JSON.stringify({ operation: 'test' }), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'SYNC-G-1536', endpoint: '/SYNC-G-1536' },
});
check(resCo, { 'A status was 200': (r) => r.status == 200 }, { tags: { name: 'SYNC-G-1536' } });
```

### `script_273.js` — GEMINI

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
    tags: { name: `SYNC-${task}` }
})
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
    'http_req_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01'],
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
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks': ['rate>0.99'], // 99% of checks must pass
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
let response = http.get('https://gqfnc7ztrujstj3fyuzjdzjb2u0nqvus.lambda-url.us-east-2.on.aws', { tags: { name: 'GetLambdaURL' } });
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
            ...
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

### `script_277.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5]
- **Snippet:**
```js
export const options = {
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
        'checks': ['rate>0.99'],           // 99% of checks should pass
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
// Move the database connection inside the default function or setup() to avoid opening it in the init context.
// Option 1: Open in setup() and pass connection info via data, or open per VU in the default function:
export default () => {
  const db = sql.open('postgres', pgConnectionString)
  // ... rest of the function
  db.close()
}
// Option 2: Use setup() to validate connectivity and manage lifecycle more explicitly,
// while opening the connection inside the default function per VU.
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
// Add tags to the trend and counter metrics to enable filtering and grouping in results.
// Since db.exec() is not an HTTP request, use tags on the custom metrics instead:
insertTrend.add(exFinish - exStart, { operation: 'insert', table: 'positions' })
counterInserts.add(1, { operation: 'insert', table: 'positions' })
counterFailed.add(1, { operation: 'insert', table: 'positions' })
myFailRate.add(true, { operation: 'insert', table: 'positions' })
myFailRate.add(false, { operation: 'insert', table: 'positions' })
```

### `script_278.js` — GEMINI

**Smell 4: Not using tags**

- **Lines:** [62, 65, 66, 69, 70]
- **Snippet:**
```js
try {
  db.exec(
    'insert into positions...'
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
const tags = { name: 'pg_single_insert' };
try {
  db.exec(
    'insert into positions...'
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
      duration: '90s', // total duration
      preAllocatedVUs: 50, // to allocate runtime resources

      rate: 50, // number of constant iterations given `timeUnit`
      timeUnit: '1s',
    },
  },
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks': ['rate>0.99'], // 99% of checks must pass
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

### `script_28.js` — CLAUDE

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
// Reading and parsing the file is unavoidable in the init context, but the mapping/filtering
// can be made leaner. The main concern is the heavy loop creating 150 metric objects upfront.
// Only create panel metrics for panels actually used, or cap MAX_PANEL_ID to a realistic value.

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

// Reduce MAX_PANEL_ID to a realistic bound or use a lazy-init pattern
const MAX_PANEL_ID = 50; // Adjust to actual expected panel count
const panelMetrics = {};
for (let panelId = 1; panelId <= MAX_PANEL_ID; panelId++) {
    panelMetrics[panelId] = {
        responseTime: new Trend(`panel_response_time_${panelId}`, true),
        successRate: new Rate(`panel_success_rate_${panelId}`, true),
        failureRate: new Rate(`panel_failure_rate_${panelId}`, true)
    };
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
        'checks': ['rate>0.95'],
        'http_req_failed': ['rate<0.05']
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
  return users; // Pass the data to the default function
}

// In the default function, receive the data from setup()
export default function (users) {
    let user = users[__VU - 1];
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
        'http_req_duration': ['p(95)<1500'], // 95% of requests should be below 1500ms
        'dashboard_response_time': ['p(90)<800'], // 90% of dashboard loads should be below 800ms
        'checks': ['rate>0.99'], // 99% of checks should pass
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
    tags: { name: 'authenticateUser', endpoint: AUTH_ENDPOINT },
};
let authResponse = http.post(`${BASE_URL}${AUTH_ENDPOINT}`, authPayload, authHeaders);
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
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
        'checks': ['rate>0.99'] // 99% of checks must pass
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
    tags: { name: 'AuthenticateUser' }, // Tag the request by its name
};

let authResponse = http.post(`${BASE_URL}${AUTH_ENDPOINT}`, authPayload, authParams);
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
let response = http.get('https://test-api.k6.io/public/crocodiles/', { tags: { name: 'GetCrocodiles', endpoint: '/public/crocodiles/' } })
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
import { sleep, check } from 'k6';
import http from 'k6/http';

// ... inside the main function
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
let response = http.get('https://test-api.k6.io/public/crocodiles/', {
    tags: { name: 'PublicCrocs' },
});
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
        'checks': ['rate>0.99'],
        'http_req_failed': ['rate<0.01']
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
const response = storeOrderGetService.execute({ tags: { name: 'GetStoreOrderById', endpoint: '/store/order' } });
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
        'http_req_duration': ['p(95)<200'], // 95% of requests must complete below 200ms
        'checks': ['rate>0.99'], // 99% of checks must pass
    },
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
    const params = {
        tags: {
            name: 'GetStoreOrderByID',
        },
    };
    // Refactoring assumes the service method can pass params to the underlying http request
    const response = storeOrderGetService.execute(params);
    check(response, {
        'Get store order by Id Status is 200': (r) => r.status === 200,
    }, params.tags); // Tag checks for more granular pass/fail metrics
}
```

### `script_285.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [47, 48, 49, 50]
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
  'response has data': (r) => r.json('data') !== undefined,
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
  tags: { name: 'SAPI32_get_carts_by_id', group: testConfiguration.group },
});
```

### `script_285.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [27, 31, 33, 34, 37, 38]
- **Snippet:**
```js
const fixture = new CartFixture({
  customerCount: testConfiguration.vus ?? EnvironmentUtil.getRampVus(),
  cartCount: 1,
  itemCount: 70,
});

export function setup() {
  return fixture.getData();
}

export default function (data) {
  const { customerEmail, idCart } = fixture.iterateData(data, exec.vu.idInTest, 0);
  //...
```
- **Refactored:**
```js
export function setup() {
  const fixture = new CartFixture({
    customerCount: testConfiguration.vus ?? EnvironmentUtil.getRampVus(),
    cartCount: 1,
    itemCount: 70,
  });
  const data = fixture.getData();
  return { data, fixture };
}

export default function (setupData) {
  const { data, fixture } = setupData;
  const { customerEmail, idCart } = fixture.iterateData(data, exec.vu.idInTest, 0);
  //...
}
```

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
// ...
const response = cartsResource.get(idCart, ['items']);

check(response, {
  'GET cart by ID is successful (200)': (r) => r.status === 200,
});

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```

**Smell 4: Not using tags**

- **Lines:** [49]
- **Snippet:**
```js
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
const tags = { name: testConfiguration.metrics[0] };
metrics[testConfiguration.metrics[0]].add(response.timings.duration, tags);
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
    'inserts': ['count > 0'],
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

// inside default function:
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

// Attach tags to the metric increments and wrap the exec with tagged context:
counterInserts.add(1, { operation: 'insert', table: 'rls_messages_authenticated' });

// For SQL operations, use k6 group or annotate surrounding metrics with tags:
// e.g., counterInserts.add(1, { query: 'insert', domain: domains[getRandomInt(0, 5)] });
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
    // Ensure the rate of successful inserts meets 95% of the target rate.
    'inserts': [`rate>=${rate * 0.95}`],
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
counterInserts.add(1, { query: 'insert_rls_messages' })
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
let res = http.get('https://quickpizza.grafana.com', { tags: { name: 'quickpizza_homepage', endpoint: '/' } });
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
    'http_req_failed': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
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
// ...
const response = checkoutResource.checkout();
const isSuccessful = check(response, {
  'Checkout successful (status 2xx)': (r) => r.status >= 200 && r.status < 300,
});

if (!isSuccessful) {
  // Abort the iteration if the check fails to prevent subsequent errors
  return;
}

const responseJson = JSON.parse(response.body);
orderReference = responseJson.data.attributes.orderReference;
```

**Smell 4: Not using tags**

- **Lines:** [82, 89, 101]
- **Snippet:**
```js
metrics['SAPI21_delete_carts'].add(response.timings.duration);
```
- **Refactored:**
```js
const tags = { name: 'SAPI21_delete_carts' };
metrics['SAPI21_delete_carts'].add(response.timings.duration, tags);
```

### `script_289.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 31]
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
```

**Smell 3: Not checking requests**

- **Lines:** [24, 28, 29, 30, 31]
- **Snippet:**
```js
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

- **Lines:** [16, 17, 18, 19, 20, 21]
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

### `script_289.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [11]
- **Snippet:**
```js
The script lacks an `options` object with a `thresholds` definition. Without it, the test will always pass, regardless of the system's performance.
```
- **Refactored:**
```js
import http from 'k6/http';
import { check } from 'k6';

export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should complete below 500ms
  },
};

// ...
```

**Smell 3: Not checking requests**

- **Lines:** [24, 28, 29, 30]
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
// Move heavy file parsing into a dedicated setup() function so it runs once globally,
// then pass the result to the default function via shared data.
export function setup() {
    const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
    const users = usersRaw
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

export default function (data) {
    const users = data.users;
    // ... rest of the default function
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
        'checks': ['rate>0.95']
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
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<1000'], // 95% of requests must complete below 1s
        'dashboard_success_rate': ['rate>0.99'], // success rate for dashboard metadata should be > 99%
        'checks': ['rate>0.99'] // check success rate should be > 99%
    }
};
```

### `script_290.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [54, 55, 56, 57, 61, 62, 63]
- **Snippet:**
```js
const response = cartsResource.get(idCart, ['items']);
    const bodyJson = JSON.parse(response.body);
    skuForRemove = bodyJson.included[0].attributes.sku;
  });

  group(testConfiguration.group, () => {
    const response = cartsResource.removeItem(idCart, skuForRemove);
    metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
import { check } from 'k6';

// Inside 'Gets customer cart info' group:
const response = cartsResource.get(idCart, ['items']);
check(response, {
  'get cart status is 200': (r) => r.status === 200,
  'cart has included items': (r) => {
    const body = JSON.parse(r.body);
    return body.included && body.included.length > 0;
  },
});
const bodyJson = JSON.parse(response.body);
skuForRemove = bodyJson.included[0].attributes.sku;

// Inside testConfiguration.group group:
const response = cartsResource.removeItem(idCart, skuForRemove);
check(response, {
  'remove cart item status is 204': (r) => r.status === 204,
});
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
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
// Assuming CartsResource methods accept a params/tags argument, pass tags to each request:
const response = cartsResource.get(idCart, ['items'], { tags: { name: 'GetCartInfo', group: 'Cart', testId: 'SAPI34' } });
...
const response = cartsResource.removeItem(idCart, skuForRemove, { tags: { name: 'DeleteCartItem', group: 'Cart', testId: 'SAPI34' } });

// If tags must be set via k6 directly, use tagWithCurrentStageIndex or pass params in the underlying http calls:
// e.g., http.del(url, null, { tags: { name: 'DeleteCartItem', group: 'Cart', testId: 'SAPI34' } });
```

### `script_290.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [61, 63]
- **Snippet:**
```js
const response = cartsResource.removeItem(idCart, skuForRemove);

metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
import { check } from 'k6';

// ... in the default function
const response = cartsResource.removeItem(idCart, skuForRemove);

if (check(response, { 'item removed successfully': (r) => r.status === 204 })) {
  metrics[testConfiguration.metrics[0]].add(response.timings.duration);
}
```

**Smell 4: Not using tags**

- **Lines:** [63]
- **Snippet:**
```js
metrics[testConfiguration.metrics[0]].add(response.timings.duration);
```
- **Refactored:**
```js
metrics[testConfiguration.metrics[0]].add(response.timings.duration, {
  name: testConfiguration.metrics[0],
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
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests should complete below 500ms
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
const res = http.post("http://localhost:3000/api", payload, { headers, tags: { name: 'APIPost' } });
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
	//executor: 'shared-iterations',
	// iterations: 1,
	// vus: 1,
    // duration: '20s',
    stages: [
        // Ramp up to 1 VUs for 5 second
        { duration: "1s", target: 5000 },
      ],
    thresholds: {
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<200'], // 95% of requests must complete below 200ms
        'checks': ['rate>0.99'], // 99% of checks must pass
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
    'http_req_duration': ['p(95)<500', 'p(99)<1000'],
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
const res = http.put(url, payload, { headers, tags: { name: 'update_user', endpoint: '/v2/user/:username' } });
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
    'response_time': ['p(95)<500'], // 95th percentile of custom metric should be below 500ms
    'checks': ['rate>0.99'], // >99% of checks should pass
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
  const res = http.put(url, payload, {
    headers,
    tags: {
      name: 'UpdateUser',
    },
  });

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
check(res1, { 'home status 200': (r) => r.status === 200 });

const res2 = http.get('https://quickpizza.grafana.com/contacts.php');
check(res2, { 'contacts status 200': (r) => r.status === 200 });

const res3 = http.get('https://quickpizza.grafana.com/news.php');
check(res3, { 'news status 200': (r) => r.status === 200 });
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
http.get('https://quickpizza.grafana.com/test.k6.io/', { tags: { name: 'home' } });
http.get('https://quickpizza.grafana.com/contacts.php', { tags: { name: 'contacts' } });
http.get('https://quickpizza.grafana.com/news.php', { tags: { name: 'news' } });
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
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
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
import http from 'k6/http';
import { sleep, check } from 'k6';

export default () => {
    const res1 = http.get('https://quickpizza.grafana.com/test.k6.io/');
    check(res1, { 'status is 200': (r) => r.status === 200 });
    sleep(1);
    const res2 = http.get('https://quickpizza.grafana.com/contacts.php');
    check(res2, { 'status is 200': (r) => r.status === 200 });
    sleep(2);
    const res3 = http.get('https://quickpizza.grafana.com/news.php');
    check(res3, { 'status is 200': (r) => r.status === 200 });
    sleep(2);
};
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
import http from 'k6/http';
import { sleep } from 'k6';

export default () => {
    http.get('https://quickpizza.grafana.com/test.k6.io/', {
      tags: { name: 'Homepage' },
    });
    sleep(1);
    http.get('https://quickpizza.grafana.com/contacts.php', {
      tags: { name: 'Contacts' },
    });
    sleep(2);
    http.get('https://quickpizza.grafana.com/news.php', {
      tags: { name: 'News' },
    });
    sleep(2);
};
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
        'http_req_duration': ['p(95)<1000'],
        'http_req_failed': ['rate<0.05'],
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
        'http_req_failed': ['rate<0.01'], // HTTP errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
        'checks{name:"✅ Status is 200 (Success)"}': ['rate>0.99'], // Over 99% of requests must be successful
        'check_slow_response': ['count < 10'], // Less than 10 slow responses in total
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
        name: 'UserLogout' // Tag to identify this specific request in results
    }
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
  tags: { name: 'DeleteStore', endpoint: 'delete-store', db: dbType }
});
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

export let options = Object.assign({}, test_options, {
  thresholds: {
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks': ['rate>0.99'],             // 99% of checks should pass
  },
});
```

**Smell 3: Not checking requests**

- **Lines:** [62]
- **Snippet:**
```js
const res = http.del(`${url}/${store.id}`);
```
- **Refactored:**
```js
const res = http.del(`${url}/${store.id}`);
check(res, {
    'teardown: status is 200': (r) => r.status === 200
});
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
    return { ... grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10) };
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
// Reading and parsing a large file with split+map+filter and creating 150*3=450 custom metric objects in the init context is expensive.
// For the file parsing, ensure the file is as small as possible and consider lazy parsing inside default().
// For panel metrics, limit pre-created metrics or create them lazily:
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

// Instead of eagerly creating 450 metric objects, use a smaller set of shared metrics
// and rely on tags (panelId) to differentiate panels at query time:
const panelResponseTime = new Trend('panel_response_time', true);
const panelSuccessRate = new Rate('panel_success_rate', true);
const panelFailureRate = new Rate('panel_failure_rate', true);
// Then in the forEach, use: panelResponseTime.add(dur, {...panelTags}); etc.
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
        'panel_response_time': ['p(95)<3000'],
        'panel_success_rate': ['rate>0.95'],
        'checks': ['rate>0.95']
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
// Reading and parsing data should be done in the setup function, which runs only once.
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

// The default function receives the data from setup().
// The VU number can be used to select a user.
export default function (data) {
    let user = data.users[__VU - 1];
    // ... rest of the function
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
        'http_req_duration': ['p(95)<1500'], // 95% of requests should be below 1.5s
        'checks': ['rate>0.99'], // 99% of checks should pass
        'dashboard_response_time': ['p(95)<1000'] // 95% of dashboard metadata loads should be below 1s
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
        'http_req_duration': ['p(95)<1000'],
        'http_req_failed': ['rate<0.05'],
        'check_success': ['count>0'],
        'check_fail_500': ['count<10'],
        'check_slow_response': ['count<50'],
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
        method: 'PUT'
    }
};
```

### `script_33.js` — GEMINI

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
        { duration: '10s', target: 365 },  // Load normal
        { duration: '30s', target: 3650 }, // Lonjakan (simulasi kegagalan)
        { duration: '20s', target: 365 },  // Pemulihan (cek kapan kembali ke normal)
    ],
    thresholds: {
        'http_req_failed': ['rate<0.01'], // Fail if more than 1% of requests return an error
        'http_req_duration': ['p(95)<1500'], // Fail if 95th percentile response time is > 1.5s
        'checks{name:"✅ Status is 200 (Success)"}': ['rate>0.95'], // Fail if success rate is less than 95%
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
            name: 'UpdateUser' 
        }
    };

    // ...

    try {
        res = http.put(url, payload, params);
    } //...
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
        'http_req_duration': ['p(95)<2000'],
        'http_req_failed': ['rate<0.05'],
        'checks': ['rate>0.90'],
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
res = http.get(url, { tags: { name: 'get_store_order', endpoint: 'store_order' } });
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
        { duration: '2m', target: 70 },
        { duration: '6m', target: 700 },
        { duration: '2m', target: 70 },
    ],
    thresholds: {
        'http_req_failed': ['rate<0.05'], // Fail if error rate is higher than 5%
        'http_req_duration': ['p(95)<1500'], // 95% of requests must complete below 1.5s
        'checks': ['rate>0.98'], // Over 98% of checks must pass
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
    tags: { name: 'GetOrderById' },
});
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
    http_req_duration: ['p(95)<2000'],
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
  tags: { name: 'video_chunk', loop: i <= 5 ? 'first_batch' : 'second_batch' },
});
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
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    'checks{is status 200}': ['rate>0.99'], // 99% of status 200 checks should pass
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
// In the first loop (lines 13-20)
const res = http.get(videoPath + String(i).padStart(5, '0') + '.ts', {
  tags: { name: 'VideoStreaming', phase: 'initial_load' },
});

// In the second loop (lines 21-29)
const res = http.get(videoPath + String(i).padStart(5, '0') + '.ts', {
  tags: { name: 'VideoStreaming', phase: 'continued_streaming' },
});
```

### `script_36.js` — CLAUDE

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
// Reading and parsing the file is acceptable in init context via open(),
// but the heavy map+filter chain and creation of 150*3=450 custom metric objects
// all run once per VU in init. Reduce metric object creation by using shared
// metric objects with tags instead of per-panel metric instances:

const usersRaw = open('/home/vunet/user_creation_k6/user_cookies.txt').split('\n');
const users = usersRaw.reduce((acc, line) => {
    if (!line.trim()) return acc;
    const [username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry] = line.split(',');
    if (vunetSession && xVuNetHTTPInfo && grafanaSessionExpiry) {
        acc.push({ username, password, vunetSession, xVuNetHTTPInfo, grafanaSessionExpiry: parseInt(grafanaSessionExpiry, 10) });
    }
    return acc;
}, []);

// Replace 450 metric objects with a single set of shared metrics tagged by panelId:
const panelResponseTime = new Trend('panel_response_time', true);
const panelSuccessRate = new Rate('panel_success_rate', true);
const panelFailureRate = new Rate('panel_failure_rate', true);

// Then in the default function, pass panelId as a tag:
panelResponseTime.add(panelRes.timings.duration, { ...panelTags, panelId: panelId.toString() });
panelSuccessRate.add(panelRes.status === 200, { ...panelTags, panelId: panelId.toString() });
panelFailureRate.add(panelRes.status !== 200, { ...panelTags, panelId: panelId.toString() });
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
        'panel_response_time': ['p(95)<3000'],
        'panel_success_rate': ['rate>0.95'],
        'checks': ['rate>0.95']
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
    }).filter(user => user.username && user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
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
        'http_req_duration{endpoint:dashboard}': ['p(95)<500'], // 95% of dashboard metadata requests should be below 500ms
        'checks': ['rate>0.99'], // >99% of all checks should pass
        'dashboard_success_rate': ['rate>0.99'] // success rate for dashboard metadata calls should be > 99%
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
    'Get_books': ['p(95)<500', 'p(99)<1000'],
    'Get_books error': ['rate<0.01'],
    'http_req_duration': ['p(95)<500'],
    'http_req_failed': ['rate<0.01']
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
      name: 'Get_books',
      endpoint: '/books/simple'
    }
  };
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
    'Get_books error': ['rate<0.01'], // <1% errors
    'Get_books': ['p(95)<200'], // 95% of requests must complete below 200ms
  },
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
const requests = {
    'Get_books': {
      method: 'GET',
      url: url + 'books/simple',
      params: {
        headers: {
          'Content-Type': 'application/json',
        },
        tags: { name: 'GetBooksSimple' },
      },
    }
  };
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
      endpoint: 'api/orders/async/1',
    },
  };
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
    'Get_Orders_Async': ['p(95)<500'], // 95th percentile response time must be below 500ms
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
      name: 'GetOrdersAsync',
    },
  };
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
  { tags: { name: 'auth_login', endpoint: 'auth' } }
);

const other_resp = http.get(
  'https://test-api.k6.io/public/crocodiles/1/',
  { tags: { name: 'get_crocodile', endpoint: 'crocodiles' } }
);
```

### `script_40.js` — CLAUDE

**Smell 3: Not checking requests**

- **Lines:** [18, 22]
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

// ... in default function
let res = http.get('https://quickpizza.grafana.com/test.k6.io/');
check(res, { 'main page status is 200': (r) => r.status === 200 });

// ...

res = http.get('https://quickpizza.grafana.com/news.php');
check(res, { 'news page status is 200': (r) => r.status === 200 });
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
let res = http.get('https://quickpizza.grafana.com/test.k6.io/', {
    tags: { name: 'MainPage' },
});

// ...

res = http.get('https://quickpizza.grafana.com/news.php', {
    tags: { name: 'NewsPage' },
});
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

**Smell 3: Not checking requests**

- **Lines:** [4052, 4053, 4054, 4055, 4056, 4057, 4058]
- **Snippet:**
```js
const eventRes = http.post('http://localhost:3000/user/organizer/createEvent', JSON.stringify(payload), {
    headers: { 'Content-Type': 'application/json' },
});

check(eventRes, {
    'event created': (r) => r.status === 200,
});
```
- **Refactored:**
```js
const token = loginRes.json('token');
const eventRes = http.post('http://localhost:3000/user/organizer/createEvent', JSON.stringify(payload), {
    headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`,
    },
});

check(eventRes, {
    'event created': (r) => r.status === 200,
    'event response has body': (r) => r.body && r.body.length > 0,
    'event response is not 4xx': (r) => r.status < 400,
    'event response is not 5xx': (r) => r.status < 500,
});
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
    // ... more than 4000 lines of hardcoded data
];
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

// Create a 'users.json' file with the user data.
// The data will be loaded once and shared across all VUs, saving memory.
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
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<1500'], // 95% of requests must complete below 1.5s
        'checks': ['rate>0.99'],           // 99% of checks must pass
        'participation_400': ['count==0'],    // No 400 errors expected
        'participation_500': ['count==0'],    // No 500 errors expected
    },
};
```

**Smell 4: Not using tags**

- **Lines:** [4026, 4031, 4052, 4054]
- **Snippet:**
```js
const loginRes = http.post('http://localhost:3000/guestUser/logIn', JSON.stringify({
    // ...
}), {
    headers: { 'Content-Type': 'application/json' },
});

// ...

const eventRes = http.post('http://localhost:3000/user/organizer/createEvent', JSON.stringify(payload), {
    headers: { 'Content-Type': 'application/json' },
});
```
- **Refactored:**
```js
// Refactored login request with tags
const loginRes = http.post('http://localhost:3000/guestUser/logIn', JSON.stringify({
    email: user.email,
    password: password,
}), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'Login' },
});

// Refactored event creation request with tags
const eventRes = http.post('http://localhost:3000/user/organizer/createEvent', JSON.stringify(payload), {
    headers: { 'Content-Type': 'application/json' },
    tags: { name: 'CreateEvent' },
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
        'http_req_duration': ['p(95)<1000'],
        'http_req_failed': ['rate<0.1'],
        'checks': ['rate>0.9'],
        'total_failures': ['count<10'],
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
        'http_req_failed': ['rate<0.05'], // Fail if more than 5% of requests fail
        'http_req_duration': ['p(95)<1000'], // 95% of requests should be faster than 1s
        'checks': ['rate>0.95'], // More than 95% of checks must pass
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
    tags: { // Add tags to group metrics for this request
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
// These lines remain in the init context (which is correct for `open`),
// but be aware that parsing a large CSV with papaparse for every VU initialization
// can be expensive. To mitigate, ensure the file is as small as needed and
// consider SharedArray to parse only once across all VUs:
import { SharedArray } from 'k6/data';
const userTokenData = new SharedArray('users', function() {
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
		http_req_failed: ['rate<0.01'],
		http_req_duration: ['p(95)<200'],
		'checks': ['rate>0.99'],
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
	tags: { name: 'token_validate', endpoint: '/auth/v1/token/validate' }
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

export function setup() {
  // setup runs once for the whole test
  const parsedData = papaparse.parse(open('../loginSuccess.csv')).data;
  // SharedArray is memory-efficient for passing data to VUs
  return new SharedArray('userTokens', function () {
    return parsedData;
  });
}

// In default function, receive the data from setup
export default function(userTokenData) {
  // ... rest of the code
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
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
        'checks': ['rate>0.99'],           // 99% of checks must pass
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
    'http_req_failed': ['rate<0.01'], // less than 1% of requests should fail
    'http_req_duration': ['p(95)<500'], // 95th percentile of request duration must be below 500ms
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
// Add 'check' to imports: import { sleep, check } from 'k6';
const urlRes = http.get('https://test-api.k6.io');
check(urlRes, { 'status was 200': (r) => r.status == 200 });
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
  tags: { name: 'K6-Test-API-Homepage' },
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
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<200'], // 95% of requests should be below 200ms
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
const res = http.put(url+`/29145037094`,JSON.stringify(data), { headers: headers } );
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
http.put(url+`/29145037094`,JSON.stringify(data), {
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
http.get('https://test.k6.io', {
    tags: { name: 'homepage', endpoint: 'test.k6.io' },
});
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
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<300'], // 95% of requests should be below 300ms
    },
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
import { check } from 'k6';
// ...
export default function () {
    const res = http.get('https://test.k6.io');
    check(res, {
        'status is 200': (r) => r.status === 200,
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
http.get('https://test.k6.io', {
    tags: { name: 'PublicMainPage' },
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
    http_req_duration: ['p(95)<2000'],
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
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
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
    ['GET', `${BASE_URL}/...`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/...`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/...`, null, { tags: { name: 'PublicCrocs' } }],
  ]);
```
- **Refactored:**
```js
import http from 'k6/http';
import { sleep, check } from 'k6';

// ... options ...

export default function () {
  const BASE_URL = 'http://$domain_ba_aplic';

  const responses = http.batch([
    ['GET', `${BASE_URL}/...`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/...`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/...`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/...`, null, { tags: { name: 'PublicCrocs' } }],
    ['GET', `${BASE_URL}/...`, null, { tags: { name: 'PublicCrocs' } }],
  ]);

  responses.forEach(res => {
    check(res, {
        'status was 200': (r) => r.status === 200,
    });
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
// Keep file open in init context (this is acceptable and recommended)
const image = open('car.jpg', 'b');
const gateway = 'http://10.103.51.65:8080';

export default function () {
  // Move FormData construction and body preparation inside the VU function
  // to avoid sharing mutable state across VUs and to ensure each VU
  // builds its own FormData instance independently
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
    http_req_duration: ['p(95)<500'],
    http_req_failed: ['rate<0.01'],
    checks: ['rate>0.99'],
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

- **Lines:** [19, 20, 21, 22]
- **Snippet:**
```js
const image = open('car.jpg', 'b');
const fd = new FormData();
fd.append('payload', http.file(image, 'image.png', 'image/png'));
let resnet = {
        method: 'POST',
        // ...
        body: fd.body(), 
        // ...
};
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

// Load file data once using a SharedArray to be memory-efficient
const imageData = new SharedArray('car image', function () {
  return open('car.jpg', 'b');
});

export default function () {
  // Construct the form data inside the VU iteration
  const fd = new FormData();
  fd.append('payload', http.file(imageData, 'image.png', 'image/png'));

  const res = http.post('http://localhost:5000/predict', fd.body(), {
    headers: { 'Content-Type': 'multipart/form-data; boundary=' + fd.boundary },
  });
  // ...
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
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
  },
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
      name: 'ImagePrediction',
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
const res = http.get('https://test.k6.io/contacts.php', {
  tags: { name: 'contacts', endpoint: '/contacts.php' },
});
```

### `script_56.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4, 13]
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
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
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
import http from 'k6/http';
import { sleep, check } from 'k6';

// ... options ...

export default function () {
  const res = http.get('https://test.k6.io/contacts.php');
  check(res, {
    'is status 200': (r) => r.status === 200,
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
// These lines are acceptable for file reading in init context (open() is init-only),
// but the papaparse.parse() call is a heavy computation that runs once per VU.
// To minimize cost, ensure the CSV is as small as possible and consider caching
// or pre-processing the data outside of k6. If parsing must happen here, it cannot
// be moved to the default function, but be aware this is expensive per VU.
// Alternatively, use SharedArray to parse only once across all VUs:
import { SharedArray } from 'k6/data';
const userTokenData = new SharedArray('userTokens', function () {
    const csvData = open('../logsCSV/exam/accessToken.csv');
    return papaparse.parse(csvData).data;
});
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
        'http_req_failed': ['rate<0.01'],        // Less than 1% of requests should fail
        'http_req_duration': ['p(95)<200'],      // 95% of requests should be below 200ms
        'checks': ['rate>0.99'],                 // More than 99% of checks should pass
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
        name: 'GetGroupExams',
        endpoint: '/exam-service/v1/group-exams',
        service: 'exam-service'
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
// Move file reading and parsing to the setup function, which runs only once.
export function setup() {
  const csvData = open('../logsCSV/exam/accessToken.csv');
  const userTokenData = papaparse.parse(csvData).data;
  return { tokens: userTokenData };
}

// Access the parsed data in the default function via the 'data' parameter.
export default function(data) {
    let i = __ITER;
    let userToken = data.tokens[i][2];
    // ... rest of the script
}
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
        'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
        'checks': ['rate>0.99'],           // 99% of checks should pass
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
        name: 'GetGroupExams', // Descriptive name for the request
    },
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
http.get('https://test.k6.io/contacts.php', {
    tags: { name: 'contacts', endpoint: '/contacts.php' },
});
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
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<200'],
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
// Keep only the static file read in init context
const image = open('car.jpg', 'b');
const gateway = 'http://10.103.51.65:8080';

export default function () {
  // Build FormData inside the VU function to avoid shared mutable state
  const fd = new FormData();
  fd.append('payload', http.file(image, 'image.png', 'image/png'));
  const params = {
    headers: {
      'Content-Type': 'multipart/form-data; boundary=' + fd.boundary
    },
    tags: { endpoint: 'resnet_predict' }
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
const resnetParams = {
  headers: {
    'Content-Type': 'multipart/form-data; boundary=' + fd.boundary
  },
  tags: { endpoint: 'resnet_predict', method: 'POST' }
};
const res = http.post(resnet.url, resnet.body, resnetParams);
```

### `script_61.js` — GEMINI

**Smell 1: Costly operations in the init context**

- **Lines:** [19, 20, 21, 22]
- **Snippet:**
```js
const image = open('car.jpg', 'b');
const fd = new FormData();
fd.append('payload', http.file(image, 'image.png', 'image/png'));
let resnet = {
        method: 'POST',
        //...
};
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

// The image file is read only once and shared between all VUs.
const image = new SharedArray('car image', function () {
  return open('car.jpg', 'b');
});

export default function () {
  const fd = new FormData();
  fd.append('payload', http.file(image, 'image.png', 'image/png'));
  
  const resnet = {
    method: 'POST',
    url: 'http://localhost:5000/predict',
    body: fd.body(),
    params: {
      headers: {
        'Content-Type': 'multipart/form-data; boundary=' + fd.boundary
      },
    },
  };

  const res = http.post(resnet.url, resnet.body, resnet.params);
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
    'http_req_duration': ['p(95)<500'], // 95% of requests should complete within 500ms
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [27, 28, 29, 30, 31, 34]
- **Snippet:**
```js
        params: {
            headers: {
	      'Content-Type': 'multipart/form-data; boundary=' + fd.boundary 
	    },
        },
// ...
  const res = http.post(resnet.url, resnet.body, resnet.params)
```
- **Refactored:**
```js
        params: {
            headers: {
	      'Content-Type': 'multipart/form-data; boundary=' + fd.boundary 
	    },
            tags: {
              name: 'ResNetPrediction',
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
const res = http.get('https://test.k6.io/contacts.php', {
  tags: { name: 'contacts', endpoint: 'contacts.php' },
});
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
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
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
export default function () {
  const res = http.get('https://test.k6.io/contacts.php');
  check(res, { 'status was 200': (r) => r.status == 200 });
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
http.get('https://test.k6.io/contacts.php', {
  tags: { name: 'ContactsPage' },
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
const res = http.get('https://quickpizza.grafana.com/test.k6.io/', {
    tags: { name: 'HomePage', endpoint: '/test.k6.io/' }
});
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
    check(res, { 'status was 200': (r) => r.status == 200 });
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

### `script_69.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [4]
- **Snippet:**
```js
export const options = {
```
- **Refactored:**
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
    thresholds: {
        http_req_failed: ['rate<0.01'], // http errors should be less than 1%
        http_req_duration: ['p(95)<200'], // 95% of requests must complete below 200ms
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
const res = http.get('https://test.k6.io/contacts.php', {
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
    tags: { name: 'quickpizza_home', endpoint: '/' }
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
        'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    },
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
import { check } from 'k6';

// inside default function:
const res = http.get('http://test.k6.io');
check(res, {
  'status is 200': (r) => r.status === 200,
  'response body is not empty': (r) => r.body && r.body.length > 0
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
  tags: { name: 'homepage', endpoint: 'test.k6.io' }
});
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
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
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

//... in default function
const res = http.get('http://test.k6.io');
check(res, { 'status was 200': (r) => r.status == 200 });
```

**Smell 4: Not using tags**

- **Lines:** [18]
- **Snippet:**
```js
http.get('http://test.k6.io');
```
- **Refactored:**
```js
//... in default function
http.get('http://test.k6.io', {
  tags: { name: 'PublicHomepage' },
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
shufflenet_http_duration.add(res[0].timings.duration);
```

**Smell 4: Not using tags**

- **Lines:** [16, 17, 18, 19, 20, 21]
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
          tags: { name: 'shufflenet', endpoint: '/function/shufflenet/' },
        },
};
let res = http.batch([paddle]);
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
    'http_req_failed': ['rate<0.01'], // <1% errors
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
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
  'shufflenet response status is 200': (r) => r.status === 200,
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
          tags: { name: 'ShuffleNet' },
        },
};
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
http.get('https://test.k6.io/contacts.php', {
    tags: { name: 'contacts', endpoint: '/contacts.php' },
});
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
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<200'],
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

// in default function
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
    tags: { name: 'ContactsPage' },
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
  tags: { name: 'homepage', endpoint: 'GET_test_k6_io' },
});
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
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
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
        'http_req_failed': ['rate<0.01'],
        'http_req_duration': ['p(95)<500'],
        'success_rate': ['rate>0.99'],
        'requests_trend': ['p(99)<1000'],
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

const response = http.get('http://test.k6.io');

const passed = check(response, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
    'response time < 500ms': (r) => r.timings.duration < 500,
});
successRate.add(passed);
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
        'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
        'success_rate': ['rate>0.99'], // custom success rate should be > 99%
    },
};
```

**Smell 3: Not checking requests**

- **Lines:** [20, 29, 30, 31, 32, 33]
- **Snippet:**
```js
const response = http.get('http://test.k6.io');

// ...

// Record the success or failure of the request
if (response.status === 200) {
    successRate.add(true);
} else {
    successRate.add(false);
}
```
- **Refactored:**
```js
import http from 'k6/http';
import { check } from 'k6';
// ...

export default function () {
    const response = http.get('http://test.k6.io');

    const isSuccessful = check(response, {
        'status is 200': (r) => r.status === 200,
    });

    successRate.add(isSuccessful);

    // ...
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
import { check } from 'k6';

const res = http.get('https://test-api.k6.io');
check(res, {
    'status is 200': (r) => r.status === 200,
    'response body is not empty': (r) => r.body && r.body.length > 0,
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
http.get('https://test-api.k6.io', {
    tags: { name: 'homepage', endpoint: 'test-api-root' },
});
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
        http_req_failed: ['rate<0.01'],   // http errors should be less than 1%
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
// ...
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
const res = http.get('https://test-api.k6.io', {
  tags: { name: 'Homepage' },
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

// inside default function:
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
  tags: { name: 'get_test_endpoint', endpoint: '/rest/v1/test' },
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
    'http_req_failed': ['rate<0.01'],   // http errors should be less than 1%
    'http_req_duration': ['p(95)<200'], // 95% of requests should be below 200ms
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

//... inside default function
const response = http.get(endpoint, {headers:  headers});

check(response, {
    'is status 200': (r) => r.status === 200,
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

### `script_85.js` — CLAUDE

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
// Read the file content once (open() is init-context only, which is correct),
// but defer the heavy parsing/mapping/filtering to a lazy init pattern
// or at minimum keep it simple and avoid chaining complex transformations inline.
// If the file is very large, consider pre-processing it outside k6.
// Minimal improvement: separate steps for clarity and avoid repeated re-parsing.
const rawContent = open('/home/vunet/user_creation_k6/user_cookies_module.txt');
const allUsers = rawContent
  .split('\n')
  .filter(line => line.trim().length > 0)
  .map(line => {
    const parts = line.split(',');
    return {
      username: parts[0],
      password: parts[1],
      accessToken: parts[2],
      vunetSession: parts[3],
      xVuNetHTTPInfo: parts[4],
      grafanaSessionExpiry: parseInt(parts[5], 10),
      dashboardName: 'Linux%20-%20CPU%20Utilization'
    };
  })
  .filter(user => user.accessToken && user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
// NOTE: For very large files, pre-process outside k6 and pass a smaller, already-filtered file.
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
    'alert_execution_response_time': ['p(95)<2000', 'p(99)<5000'],
    'alert_execution_success_rate': ['rate>0.95'],
    'http_req_failed': ['rate<0.05'],
    'checks': ['rate>0.95']
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
    // ... mapping logic
  })
  .filter(user => user.accessToken && user.vunetSession && user.xVuNetHTTPInfo && user.grafanaSessionExpiry);
```
- **Refactored:**
```js
import { SharedArray } from 'k6/data';

// Use SharedArray to ensure the file is read and processed only once for the entire test run, 
// not once per VU. This is much more memory-efficient.
const allUsers = new SharedArray('allUsers', function () {
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
        dashboardName: "Linux%20-%20CPU%20Utilization"
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
    // 99% of requests must complete within 2 seconds
    'alert_execution_response_time': ['p(99)<2000'],
    // The success rate must be higher than 99%
    'alert_execution_success_rate': ['rate>0.99'],
    // All checks must pass
    'checks': ['rate==1.0'],
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
// ...
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
  tags: { name: 'quickpizza_home', endpoint: 'GET_home' },
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
    // No more than 1% of requests should fail
    'http_req_failed': ['rate<0.01'],
    // 95% of requests should be below 500ms
    'http_req_duration': ['p(95)<500'], 
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
// At the top of the script, import the 'check' function
import { check } from 'k6';

// In the default function, check the response status
const res = http.get('https://quickpizza.grafana.com');
check(res, {
  'status is 200': (r) => r.status === 200,
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
// Add tags to each request's params to enable filtering and grouping in metrics

const paramsLogin = { headers: { 'Content-Type': 'application/json' }, timeout: '600s', tags: { name: 'Login' } };
const res_login = http.post(url, login, paramsLogin);

const paramsAbVenda = { headers: { 'Content-Type': 'application/json' }, timeout: '600s', tags: { name: 'AbrirVenda' } };
const res_abvenda = http.post(abrirVenda, ab_venda, paramsAbVenda);

const paramsPgEntidade = { headers: { 'Content-Type': 'application/json' }, timeout: '600s', tags: { name: 'PesquisaGeralEntidade' } };
let res_pgentidade = http.get(`${pesquisaGeralEntidade}?${searchParams.toString()}`, paramsPgEntidade);

const paramsDEntidade = { headers: { 'Content-Type': 'application/json' }, timeout: '600s', tags: { name: 'DefinirEntidade' } };
const res_dentidade = http.post(definirEntidade, d_entidade, paramsDEntidade);

const paramsLRapido = { headers: { 'Content-Type': 'application/json' }, timeout: '600s', tags: { name: 'LancarRapido' } };
const res_lrapido = http.post(lancarRapido, l_rapido, paramsLRapido);

const paramsPagDinheiro = { headers: { 'Content-Type': 'application/json' }, timeout: '600s', tags: { name: 'PagamentoDinheiro' } };
const res_pagdinheiro = http.post(pagDinheiro, pag_dinheiro, paramsPagDinheiro);

const paramsGdEmissao = { headers: { 'Content-Type': 'application/json' }, timeout: '600s', tags: { name: 'GetDadosEmissaoDocFiscal' } };
let res_gdemissaoDocFiscal = http.get(`${getDadosEmissaoDocFiscal}?${gd_emissaoDocFiscal.toString()}`, paramsGdEmissao);

const paramsGNotaFiscal = { headers: { 'Content-Type': 'application/json' }, timeout: '600s', tags: { name: 'GerarNotaFiscal' } };
const res_gnotaFiscal = http.post(gerarNotaFiscal, g_notaFiscal, paramsGNotaFiscal);
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
// ...
const res_abvenda = http.post(abrirVenda, ab_venda, params);
```
- **Refactored:**
```js
const baseParams = {
  headers: {
    'Content-Type': 'application/json',
  },
  'Timeout': '600s'
};

// Add a 'tags' property to distinguish metrics for each request
const res_login = http.post(url, login, Object.assign({ tags: { name: 'Login' } }, baseParams));
// ...
const res_abvenda = http.post(abrirVenda, ab_venda, Object.assign({ tags: { name: 'AbrirVenda' } }, baseParams));
```

### `script_93.js` — CLAUDE

**Smell 2: Do not use thresholds**

- **Lines:** [1, 2, 3, 4, 5]
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
    checks: ['rate>0.99']
  }
};

export default function () {
```

**Smell 3: Not checking requests**

- **Lines:** [12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 113, 114, 115, 116, 117, 118, 119, 120, 121]
- **Snippet:**
```js
http.post(`${URL}/user/register/`, ...);
// no check

let res = http.post(`${URL}/auth/token/login/`, ...);
// no check

http.get(`${URL}/my/crocodiles/`, ...);
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
check(res, { 'get crocodiles status is 200': (r) => r.status === 200 });

res = http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ name: 'Updated Random croc', sex: 'M', date_of_birth: '1900-10-28' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' } });
check(res, { 'put status is 200': (r) => r.status === 200 });

res = http.patch(`${URL}/my/crocodiles/${newCrocodileId}/`, JSON.stringify({ sex: 'F' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' } });
check(res, { 'patch status is 200': (r) => r.status === 200 });

res = http.del(`${URL}/my/crocodiles/${newCrocodileId}/`, null, { headers: { Authorization: 'Bearer ' + accessToken } });
check(res, { 'delete status is 204': (r) => r.status === 204 });
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

- **Lines:** [1]
- **Snippet:**
```js
// The script does not define an `options` object with a `thresholds` property.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    http_req_failed: ['rate<0.01'],   // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
    'checks': ['rate>0.99'],          // 99% of checks should pass
  },
};
```

**Smell 3: Not checking requests**

- **Lines:** [12, 20]
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

- **Lines:** [12, 20]
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
            name: 'UserRegistration'
        }
    }
);
```

### `script_94.js` — GEMINI

**Smell 3: Not checking requests**

- **Lines:** [96]
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
    'create crocodile status is 201': (r) => r.status === 201
});

const newCrocodileId = res.json().id;
```

**Smell 4: Not using tags**

- **Lines:** [39, 56, 80, 96, 116, 132, 156, 178]
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
            name: 'RegisterUser'
        }
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
    'browser_web_vital_lcp': ['p(75) < 2500'],
    'browser_web_vital_fid': ['p(75) < 100'],
    'checks': ['rate > 0.95'],
  },
};

export default function () {
    browser();
}
```

**Smell 4: Not using tags**

- **Lines:** [19, 28, 47, 58, 76, 88, 99, 116]
- **Snippet:**
```js
page.goto(domain);
page.waitForLoadState('networkidle');
...
element = page.$('//a[contains(.,"register")]');
element.click();
```
- **Refactored:**
```js
// Add tags to page navigations and key interactions to allow metric filtering by step
page.goto(domain, { waitUntil: 'networkidle' });
check(page, { 'browser-01a-Homepage': (p) => p.$('//p[@class="description"]').textContent().includes('Collection of HTTP and WebSocket APIs demonstrating the power of k6') }, { tags: { step: '01-Homepage' } });

// For each step, pass tags to checks:
check(page, { 'browser-02a-Register page': (p) => p.$('//div[@class="response-info"]').textContent().includes('HTTP 405 Method Not Allowed') }, { tags: { step: '02-Register' } });

check(page, { 'browser-02b-Register-submit': (p) => p.$('//div[@class="response-info"]').textContent().includes(accountUsername) }, { tags: { step: '02-Register-Submit' } });

check(page, { 'browser-03a-Login page': (p) => p.$('//div[@id="div_id_username"]').textContent().includes('Username') }, { tags: { step: '03-Login' } });

check(page, { 'browser-03b-Login-submit': (p) => p.$('//li[@class="dropdown"]').textContent().includes(accountUsername) }, { tags: { step: '03-Login-Submit' } });

check(page, { 'browser-04a-My Crocodiles page': (p) => p.$('//div[@id="content"]').textContent().includes('Crocs belonging to the authenticated user') }, { tags: { step: '04-MyCrocodiles' } });

check(page, { 'browser-05a-New croc submitted': (p) => p.$('//div[@class="response-info"]').textContent().includes('2012-06-02') }, { tags: { step: '05-NewCroc' } });
```

### `script_95.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [5]
- **Snippet:**
```js
// The script lacks an 'options' export with a 'thresholds' object to define pass/fail criteria for the test.
```
- **Refactored:**
```js
import { sleep, check } from 'k6';
import launcher from "k6/x/browser";
import { vu } from 'k6/execution';
import { randomIntBetween } from "https://jslib.k6.io/k6-utils/1.0.0/index.js";

export const options = {
  thresholds: {
    'checks': ['rate>0.99'], // Over 99% of checks must pass
    'browser_web_vital_lcp': ['p(95) < 2500'], // LCP for 95% of VUs must be below 2.5s
    'browser_web_vital_fid': ['p(95) < 100'], // FID for 95% of VUs must be below 100ms
  },
};
```

**Smell 4: Not using tags**

- **Lines:** [18, 19, 20, 21, 22, 23, 24, 25]
- **Snippet:**
```js
// 01-Homepage
page.goto(domain);
page.waitForLoadState('networkidle');
sleep(Math.random() * 5+3);
check(page, {
    'browser-01a-Homepage': (p) => p.$('//p[@class="description"]').textContent().includes("Collection of HTTP and WebSocket APIs demonstrating the power of k6"),
});
page.screenshot({ path: `screenshots/01a-homepage.png` });
```
- **Refactored:**
```js
// Add 'group' to the k6 import on line 1:
// import { sleep, check, group } from 'k6';

group('01 - Homepage', function () {
    page.goto(domain, { waitUntil: 'networkidle' });
    sleep(Math.random() * 5+3);
    check(page, {
        'Homepage loaded successfully': (p) => p.$('//p[@class="description"]').textContent().includes("Collection of HTTP and WebSocket APIs demonstrating the power of k6"),
    });
    page.screenshot({ path: `screenshots/01a-homepage.png` });
});
```

### `script_96.js` — CLAUDE

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

let res = http.post(`${URL}/auth/token/login/`, ...);

http.get(`${URL}/my/crocodiles/`, ...);

res = http.post(`${URL}/my/crocodiles/`, ...);

res = http.put(`${URL}/my/crocodiles/${newCrocodileId}/`, ...);

res = http.patch(`${URL}/my/crocodiles/${newCrocodileId}/`, ...);
```
- **Refactored:**
```js
const registerRes = http.post(`${URL}/user/register/`, JSON.stringify(credentials), { headers: { 'Content-Type': 'application/json' } });
check(registerRes, { 'register status is 201': (r) => r.status === 201 });

let res = http.post(`${URL}/auth/token/login/`, JSON.stringify({ username: credentials.username, password: credentials.password }), { headers: { 'Content-Type': 'application/json' } });
check(res, { 'login status is 200': (r) => r.status === 200, 'has access token': (r) => r.json().access !== undefined });

const listRes = http.get(`${URL}/my/crocodiles/`, { headers: { Authorization: 'Bearer ' + accessToken } });
check(listRes, { 'list crocodiles status is 200': (r) => r.status === 200 });

res = http.post(`${URL}/my/crocodiles/`, JSON.stringify({ name: 'Random croc', sex: 'M', date_of_birth: '1900-10-28' }), { headers: { Authorization: 'Bearer ' + accessToken, 'Content-Type': 'application/json' } });
check(res, { 'create crocodile status is 201': (r) => r.status === 201 });

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
    http_req_failed: ['rate<0.01'], // http errors should be less than 1%
    http_req_duration: ['p(95)<500'], // 95% of requests should be below 500ms
  },
};

const URL= 'http://localhost:8000';
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
                name: 'RegisterUser',
            },
        }
    );
```

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
		http_req_failed: ['rate<0.01'],
		http_req_duration: ['p(95)<2000'],
		'checks': ['rate>0.99'],
	},
};

export default function () {
	orders();
}
```

### `script_97.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 199]
- **Snippet:**
```js
The script lacks an `export const options` block. Without it, there are no defined success or failure criteria for the test, which can lead to false confidence in performance, especially in automated CI/CD environments.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    // No more than 1% of requests should fail.
    http_req_failed: ['rate<0.01'],
    // 95% of requests should complete within 800ms.
    http_req_duration: ['p(95)<800'],
    // All checks must pass.
    checks: ['rate==1.0'],
  },
};

/* ... rest of the script ... */

export function orders( includeTests = {} ) {
  // ...
}

export default function () {
	orders();
}
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

### `script_98.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1]
- **Snippet:**
```js
The script does not export an `options` object with a `thresholds` property. Without thresholds, the test will always be reported as successful in a CI/CD environment, regardless of the system's performance.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    'http_req_failed': ['rate<0.01'], // http errors should be less than 1%
    'http_req_duration': ['p(95)<500'], // 95% of requests should be below 500ms
    'checks': ['rate>0.99'], // 99% of checks should pass
    'http_req_duration{name:Merchant - WC-Admin}': ['p(95)<1000'] // p(95) for the main page should be less than 1s
  },
};

/* The rest of the script follows */
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

### `script_99.js` — GEMINI

**Smell 2: Do not use thresholds**

- **Lines:** [1, 504]
- **Snippet:**
```js
The script does not contain an `export const options` block, and therefore defines no thresholds to validate if the test passed or failed based on performance metrics.
```
- **Refactored:**
```js
export const options = {
  thresholds: {
    // 95% of requests must complete within 2000ms.
    'http_req_duration': ['p(95)<2000'],
    // No more than 1% of requests should fail.
    'http_req_failed': ['rate<0.01'],
    // All checks should pass.
    'checks': ['rate==1.0'],
  },
};

// The rest of the script follows...
```
