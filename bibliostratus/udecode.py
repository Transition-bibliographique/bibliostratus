# coding: utf-8

convert_diacritics = [
    ['ª', 'Á', 'á', 'À', 'à', 'Ă', 'ă', 'Ắ', 'ắ', 'Ằ', 'ằ',
     'Ẵ', 'ẵ', 'Ẳ', 'ẳ', 'Â', 'â', 'Ấ', 'ấ', 'Ầ', 'ầ', 'Ẫ',
     'ẫ', 'Ẩ', 'ẩ', 'Ǎ', 'ǎ', 'Å', 'å', 'Ǻ', 'ǻ', 'Ä', 'ä',
     'Ã', 'ã', 'Ą', 'ą', 'Ā', 'ā', 'Ả', 'ả', 'Ȁ', 'ȁ', 'Ȃ',
     'ȃ', 'Ạ', 'ạ', 'Ặ', 'ặ', 'Ậ', 'ậ', 'Ḁ', 'ḁ', 'Æ', 'æ',
     'Ǽ', 'ǽ', 'ẚ', 'Ⱥ', 'Ḃ', 'ḃ', 'Ḅ', 'ḅ', 'Ḇ', 'ḇ', 'Ć',
     'ć', 'Ĉ', 'ĉ', 'Č', 'č', 'Ċ', 'ċ', 'Ç', 'ç', 'Ḉ', 'ḉ',
     'Ȼ', 'ȼ', 'Ď', 'ď', 'Ḋ', 'ḋ', 'Ḑ', 'ḑ', 'Ḍ', 'ḍ', 'Ḓ',
     'ḓ', 'Ḏ', 'ḏ', 'Đ', 'đ', 'Ð', 'ð', 'Ǳ', 'ǲ', 'ǳ', 'Ǆ',
     'ǅ', 'ǆ', 'É', 'é', 'È', 'è', 'Ĕ', 'ĕ', 'Ê', 'ê', 'Ế',
     'ế', 'Ề', 'ề', 'Ễ', 'ễ', 'Ể', 'ể', 'Ě', 'ě', 'Ë', 'ë',
     'Ẽ', 'ẽ', 'Ė', 'ė', 'Ȩ', 'ȩ', 'Ḝ', 'ḝ', 'Ę', 'ę', 'Ē',
     'ē', 'Ḗ', 'ḗ', 'Ḕ', 'ḕ', 'Ẻ', 'ẻ', 'Ȅ', 'ȅ', 'Ȇ', 'ȇ',
     'Ẹ', 'ẹ', 'Ệ', 'ệ', 'Ḙ', 'ḙ', 'Ḛ', 'ḛ', 'Ḟ', 'ḟ', 'ƒ',
     'Ǵ', 'ǵ', 'Ğ', 'ğ', 'Ĝ', 'ĝ', 'Ġ', 'ġ', 'Ģ', 'ģ', 'Ḡ',
     'ḡ', 'Ĥ', 'ĥ', 'Ḧ', 'ḧ', 'Ḣ', 'ḣ', 'Ḩ', 'ḩ', 'Ḥ', 'ḥ',
     'Ḫ', 'ḫ', 'ẖ', 'Ħ', 'ħ', 'Í', 'í', 'Ì', 'ì', 'Ĭ', 'ĭ',
     'Î', 'î', 'Ǐ', 'ǐ', 'Ï', 'ï', 'Ḯ', 'ḯ', 'Ĩ', 'ĩ', 'İ',
     'Į', 'į', 'Ī', 'ī', 'Ỉ', 'ỉ', 'Ȉ', 'ȉ', 'Ȋ', 'ȋ', 'Ị',
     'ị', 'Ḭ', 'ḭ', 'Ĳ', 'ĳ', 'ı', 'Ĵ', 'ĵ', 'Ḱ', 'ḱ', 'Ķ',
     'ķ', 'Ḳ', 'ḳ', 'Ḵ', 'ḵ', 'Ĺ', 'ĺ', 'Ľ', 'ľ', 'Ļ', 'ļ',
     'Ḷ', 'ḷ', 'Ḹ', 'ḹ', 'Ḽ', 'ḽ', 'Ḻ', 'ḻ', 'Ł', 'ł', 'Ŀ',
     'ŀ', 'Ǉ', 'ǈ', 'ǉ', 'Ƚ', 'Ḿ', 'ḿ', 'Ṁ', 'ṁ', 'Ṃ', 'ṃ',
     'Ń', 'ń', 'Ǹ', 'ǹ', 'Ň', 'ň', 'Ñ', 'ñ', 'Ṅ', 'ṅ', 'Ņ',
     'ņ', 'Ṇ', 'ṇ', 'Ṋ', 'ṋ', 'Ṉ', 'ṉ', 'Ǌ', 'ǋ', 'ǌ', 'º',
     'Ó', 'ó', 'Ò', 'ò', 'Ŏ', 'ŏ', 'Ô', 'ô', 'Ố', 'ố', 'Ồ',
     'ồ', 'Ỗ', 'ỗ', 'Ổ', 'ổ', 'Ǒ', 'ǒ', 'Ö', 'ö', 'Ȫ', 'ȫ',
     'Ő', 'ő', 'Õ', 'õ', 'Ṍ', 'ṍ', 'Ṏ', 'ṏ', 'Ȭ', 'ȭ', 'Ȯ',
     'ȯ', 'Ȱ', 'ȱ', 'Ø', 'ø', 'Ǿ', 'ǿ', 'Ō', 'ō', 'Ṓ', 'ṓ',
     'Ṑ', 'ṑ', 'Ỏ', 'ỏ', 'Ȍ', 'ȍ', 'Ȏ', 'ȏ', 'Ơ', 'ơ', 'Ớ',
     'ớ', 'Ờ', 'ờ', 'Ỡ', 'ỡ', 'Ở', 'ở', 'Ợ', 'ợ', 'Ọ', 'ọ',
     'Ộ', 'ộ', 'Œ', 'œ', 'Ṕ', 'ṕ', 'Ṗ', 'ṗ', 'Ŕ', 'ŕ', 'Ř',
     'ř', 'Ṙ', 'ṙ', 'Ŗ', 'ŗ', 'Ȑ', 'ȑ', 'Ȓ', 'ȓ', 'Ṛ', 'ṛ',
     'Ṝ', 'ṝ', 'Ṟ', 'ṟ', 'Ś', 'ś', 'Ṥ', 'ṥ', 'Ŝ', 'ŝ', 'Š',
     'š', 'Ṧ', 'ṧ', 'Ṡ', 'ṡ', 'Ş', 'ş', 'Ṣ', 'ṣ', 'Ṩ', 'ṩ',
     'Ș', 'ș', 'ſ', 'ẛ', 'ß', 'ẞ', 'ȿ', 'Ť', 'ť', 'ẗ', 'Ṫ',
     'ṫ', 'Ţ', 'ţ', 'Ṭ', 'ṭ', 'Ț', 'ț', 'Ṱ', 'ṱ', 'Ṯ', 'ṯ',
     'Ŧ', 'ŧ', 'Ⱦ', 'Ú', 'ú', 'Ù', 'ù', 'Ŭ', 'ŭ', 'Û', 'û',
     'Ǔ', 'ǔ', 'Ů', 'ů', 'Ü', 'ü', 'Ǘ', 'ǘ', 'Ǜ', 'ǜ', 'Ǚ',
     'ǚ', 'Ǖ', 'ǖ', 'Ű', 'ű', 'Ũ', 'ũ', 'Ṹ', 'ṹ', 'Ų', 'ų',
     'Ū', 'ū', 'Ṻ', 'ṻ', 'Ủ', 'ủ', 'Ȕ', 'ȕ', 'Ȗ', 'ȗ', 'Ư',
     'ư', 'Ứ', 'ứ', 'Ừ', 'ừ', 'Ữ', 'ữ', 'Ử', 'ử', 'Ự', 'ự',
     'Ụ', 'ụ', 'Ṳ', 'ṳ', 'Ṷ', 'ṷ', 'Ṵ', 'ṵ', 'Ṽ', 'ṽ', 'Ṿ',
     'ṿ', 'Ẃ', 'ẃ', 'Ẁ', 'ẁ', 'Ŵ', 'ŵ', 'ẘ', 'Ẅ', 'ẅ', 'Ẇ',
     'ẇ', 'Ẉ', 'ẉ', 'Ẍ', 'ẍ', 'Ẋ', 'ẋ', 'Ý', 'ý', 'Ỳ', 'ỳ',
     'Ŷ', 'ŷ', 'ẙ', 'ÿ', 'Ÿ', 'Ỹ', 'ỹ', 'Ẏ', 'ẏ', 'Ȳ', 'ȳ',
     'Ỷ', 'ỷ', 'Ỵ', 'ỵ', 'Ź', 'ź', 'Ẑ', 'ẑ', 'Ž', 'ž', 'Ż',
     'ż', 'Ẓ', 'ẓ', 'Ẕ', 'ẕ', 'ɀ', 'Þ', 'þ'],
    ['a', 'A', 'a', 'A', 'a', 'A', 'a', 'A', 'a', 'A', 'a',
     'A', 'a', 'A', 'a', 'A', 'a', 'A', 'a', 'A', 'a', 'A',
     'a', 'A', 'a', 'A', 'a', 'A', 'a', 'A', 'a', 'A', 'a',
     'A', 'a', 'A', 'a', 'A', 'a', 'A', 'a', 'A', 'a', 'A',
     'a', 'A', 'a', 'A', 'a', 'A', 'a', 'A', 'a', 'A', 'e',
     'a', 'e', 'A', 'e', 'a', 'e', 'a', 'A', 'B', 'b', 'B',
     'b', 'B', 'b', 'C', 'c', 'C', 'c', 'C', 'c', 'C', 'c',
     'C', 'c', 'C', 'c', 'C', 'c', 'D', 'd', 'D', 'd', 'D',
     'd', 'D', 'd', 'D', 'd', 'D', 'd', 'DZ', 'Dz', 'dz', 'DZ',
     'DZ', 'dz', 'E', 'e', 'E', 'e', 'E', 'e', 'E', 'e', 'E',
     'e', 'E', 'e', 'E', 'e', 'E', 'e', 'E', 'e', 'E', 'e', 'E',
     'e', 'E', 'e', 'E', 'e', 'E', 'e', 'E', 'e', 'E', 'e', 'E',
     'e', 'E', 'e', 'E', 'e', 'E', 'e', 'E', 'e', 'E', 'e', 'E',
     'e', 'E', 'e', 'E', 'e', 'F', 'f', 'f', 'G', 'g', 'G', 'g',
     'G', 'g', 'G', 'g', 'G', 'g', 'G', 'g', 'H', 'h', 'H', 'h',
     'H', 'h', 'H', 'h', 'H', 'h', 'H', 'h', 'h', 'H', 'h', 'I',
     'i', 'I', 'i', 'I', 'i', 'I', 'i', 'I', 'i', 'I', 'i', 'I',
     'i', 'I', 'i', 'I', 'I', 'i', 'I', 'i', 'I', 'i', 'I', 'i',
     'I', 'i', 'I', 'i', 'I', 'i', 'IJ', 'ij', 'i', 'J', 'j', 'K',
     'k', 'K', 'k', 'K', 'k', 'K', 'k', 'L', 'l', 'L', 'l', 'L',
     'l', 'L', 'l', 'L', 'l', 'L', 'l', 'L', 'l', 'L', 'l', 'L',
     'l', 'LJ', 'Lj', 'lj', 'L', 'M', 'm', 'M', 'm', 'M', 'm', 'N',
     'n', 'N', 'n', 'N', 'n', 'N', 'n', 'N', 'n', 'N', 'n', 'N',
     'n', 'N', 'n', 'N', 'n', 'NJ', 'Nj', 'nj', 'o', 'O', 'o', 'O',
     'o', 'O', 'o', 'O', 'o', 'O', 'o', 'O', 'o', 'O', 'o', 'O',
     'o', 'O', 'o', 'O', 'o', 'O', 'o', 'O', 'o', 'O', 'o', 'O',
     'o', 'O', 'o', 'O', 'o', 'O', 'o', 'O', 'o', 'O', 'o', 'O',
     'o', 'O', 'o', 'O', 'o', 'O', 'o', 'O', 'o', 'O', 'o', 'O',
     'o', 'O', 'o', 'O', 'o', 'O', 'o', 'O', 'o', 'O', 'o', 'O',
     'o', 'O', 'o', 'O', 'o', 'OE', 'oe', 'P', 'p', 'P', 'p', 'R',
     'r', 'R', 'r', 'R', 'r', 'R', 'r', 'R', 'r', 'R', 'r', 'R',
     'r', 'R', 'r', 'R', 'r', 'S', 's', 'S', 's', 'S', 's', 'S',
     's', 'S', 's', 'S', 's', 'S', 's', 'S', 's', 'S', 's', 'S',
     's', 's', 's', 'ss', 'Ss', 's', 'T', 't', 't', 'T', 't', 'T',
     't', 'T', 't', 'T', 't', 'T', 't', 'T', 't', 'T', 't', 'T',
     'U', 'u', 'U', 'u', 'U', 'u', 'U', 'u', 'U', 'u', 'U', 'u',
     'U', 'u', 'U', 'u', 'U', 'u', 'U', 'u', 'U', 'u', 'U', 'u',
     'U', 'u', 'U', 'u', 'U', 'u', 'U', 'u', 'U', 'u', 'U', 'u',
     'U', 'u', 'U', 'u', 'U', 'u', 'U', 'u', 'U', 'u', 'U', 'u',
     'U', 'u', 'U', 'u', 'U', 'u', 'U', 'u', 'U', 'u', 'U', 'u',
     'V', 'v', 'V', 'v', 'W', 'w', 'W', 'w', 'W', 'w', 'w', 'W',
     'w', 'W', 'w', 'W', 'w', 'X', 'x', 'X', 'x', 'Y', 'y', 'Y',
     'y', 'Y', 'y', 'y', 'y', 'Y', 'Y', 'y', 'Y', 'y', 'Y', 'y',
     'Y', 'y', 'Y', 'y', 'Z', 'z', 'Z', 'z', 'Z', 'z', 'Z', 'z',
     'Z', 'z', 'Z', 'z', 'z', 'Th', 'th']
]

xml_entities2chars = {
"&#33;": "!",
"&#35;": "#",
"&#36;": "$",
"&#37;": "%",
"&#38;": "&",
"&#39;": "'",
"&#40;": "(",
"&#41;": ")",
"&#42;": "*",
"&#43;": "+",
"&#44;": ",",
"&#45;": "-",
"&#46;": ".",
"&#47;": "/",
"&#48;": "0",
"&#49;": "1",
"&#50;": "2",
"&#51;": "3",
"&#52;": "4",
"&#53;": "5",
"&#54;": "6",
"&#55;": "7",
"&#56;": "8",
"&#57;": "9",
"&#58;": ":",
"&#59;": ";",
"&#60;": "<",
"&#61;": "=",
"&#62;": ">",
"&#63;": "?",
"&#64;": "@",
"&#65;": "A",
"&#66;": "B",
"&#67;": "C",
"&#68;": "D",
"&#69;": "E",
"&#70;": "F",
"&#71;": "G",
"&#72;": "H",
"&#73;": "I",
"&#74;": "J",
"&#75;": "K",
"&#76;": "L",
"&#77;": "M",
"&#78;": "N",
"&#79;": "O",
"&#80;": "P",
"&#81;": "Q",
"&#82;": "R",
"&#83;": "S",
"&#84;": "T",
"&#85;": "U",
"&#86;": "V",
"&#87;": "W",
"&#88;": "X",
"&#89;": "Y",
"&#90;": "Z",
"&#91;": "[",
"&#92;": "\",
"&#93;": "]",
"&#94;": "^",
"&#95;": "_",
"&#96;": "`",
"&#97;": "a",
"&#98;": "b",
"&#99;": "c",
"&#100;": "d",
"&#101;": "e",
"&#102;": "f",
"&#103;": "g",
"&#104;": "h",
"&#105;": "i",
"&#106;": "j",
"&#107;": "k",
"&#108;": "l",
"&#109;": "m",
"&#110;": "n",
"&#111;": "o",
"&#112;": "p",
"&#113;": "q",
"&#114;": "r",
"&#115;": "s",
"&#116;": "t",
"&#117;": "u",
"&#118;": "v",
"&#119;": "w",
"&#120;": "x",
"&#121;": "y",
"&#122;": "z",
"&#123;": "{",
"&#124;": "|",
"&#125;": "}",
"&#126;": "~",
"&#192;": "À",
"&#193;": "Á",
"&#194;": "Â",
"&#195;": "Ã",
"&#196;": "Ä",
"&#197;": "Å",
"&#198;": "Æ",
"&#199;": "Ç",
"&#200;": "È",
"&#201;": "É",
"&#202;": "Ê",
"&#203;": "Ë",
"&#204;": "Ì",
"&#205;": "Í",
"&#206;": "Î",
"&#207;": "Ï",
"&#208;": "Ð",
"&#209;": "Ñ",
"&#210;": "Ò",
"&#211;": "Ó",
"&#212;": "Ô",
"&#213;": "Õ",
"&#214;": "Ö",
"&#216;": "Ø",
"&#217;": "Ù",
"&#218;": "Ú",
"&#219;": "Û",
"&#220;": "Ü",
"&#221;": "Ý",
"&#222;": "Þ",
"&#223;": "ß",
"&#224;": "à",
"&#225;": "á",
"&#226;": "â",
"&#227;": "ã",
"&#228;": "ä",
"&#229;": "å",
"&#230;": "æ",
"&#231;": "ç",
"&#232;": "è",
"&#233;": "é",
"&#234;": "ê",
"&#235;": "ë",
"&#236;": "ì",
"&#237;": "í",
"&#238;": "î",
"&#239;": "ï",
"&#240;": "ð",
"&#241;": "ñ",
"&#242;": "ò",
"&#243;": "ó",
"&#244;": "ô",
"&#245;": "õ",
"&#246;": "ö",
"&#248;": "ø",
"&#249;": "ù",
"&#250;": "ú",
"&#251;": "û",
"&#252;": "ü",
"&#253;": "ý",
"&#254;": "þ",
"&#255;": "ÿ",
"&#160;": "",
"&#161;": "¡",
"&#162;": "¢",
"&#163;": "£",
"&#164;": "¤",
"&#165;": "¥",
"&#166;": "¦",
"&#167;": "§",
"&#168;": "¨",
"&#169;": "©",
"&#170;": "ª",
"&#171;": "«",
"&#172;": "¬",
"&#173;": "­",
"&#174;": "®",
"&#175;": "¯",
"&#176;": "°",
"&#177;": "±",
"&#178;": "²",
"&#179;": "³",
"&#180;": "´",
"&#181;": "µ",
"&#182;": "¶",
"&#184;": "¸",
"&#185;": "¹",
"&#186;": "º",
"&#187;": "»",
"&#188;": "¼",
"&#189;": "½",
"&#190;": "¾",
"&#191;": "¿",
"&#215;": "×",
"&#247;": "÷",
"&#8704;": "∀",
"&#8706;": "∂",
"&#8707;": "∃",
"&#8709;": "∅",
"&#8711;": "∇",
"&#8712;": "∈",
"&#8713;": "∉",
"&#8715;": "∋",
"&#8719;": "∏",
"&#8721;": "∑",
"&#8722;": "−",
"&#8727;": "∗",
"&#8730;": "√",
"&#8733;": "∝",
"&#8734;": "∞",
"&#8736;": "∠",
"&#8743;": "∧",
"&#8744;": "∨",
"&#8745;": "∩",
"&#8746;": "∪",
"&#8747;": "∫",
"&#8756;": "∴",
"&#8776;": "≈",
"&#8800;": "≠",
"&#8801;": "≡",
"&#8804;": "≤",
"&#8805;": "≥",
"&#8834;": "⊂",
"&#8835;": "⊃",
"&#8838;": "⊆",
"&#8839;": "⊇",
"&#8869;": "⊥",
"&#913;": "Α",
"&#914;": "Β",
"&#915;": "Γ",
"&#916;": "Δ",
"&#917;": "Ε",
"&#918;": "Ζ",
"&#919;": "Η",
"&#920;": "Θ",
"&#921;": "Ι",
"&#922;": "Κ",
"&#923;": "Λ",
"&#924;": "Μ",
"&#925;": "Ν",
"&#926;": "Ξ",
"&#927;": "Ο",
"&#928;": "Π",
"&#929;": "Ρ",
"&#931;": "Σ",
"&#932;": "Τ",
"&#933;": "Υ",
"&#934;": "Φ",
"&#935;": "Χ",
"&#936;": "Ψ",
"&#937;": "Ω",
"&#945;": "α",
"&#946;": "β",
"&#947;": "γ",
"&#948;": "δ",
"&#949;": "ε",
"&#950;": "ζ",
"&#951;": "η",
"&#952;": "θ",
"&#953;": "ι",
"&#954;": "κ",
"&#955;": "λ",
"&#956;": "μ",
"&#957;": "ν",
"&#958;": "ξ",
"&#959;": "ο",
"&#960;": "π",
"&#961;": "ρ",
"&#962;": "ς",
"&#963;": "σ",
"&#964;": "τ",
"&#965;": "υ",
"&#966;": "φ",
"&#967;": "χ",
"&#968;": "ψ",
"&#969;": "ω",
"&#977;": "ϑ",
"&#978;": "ϒ",
"&#982;": "ϖ",
"&#338;": "Œ",
"&#339;": "œ",
"&#352;": "Š",
"&#353;": "š",
"&#376;": "Ÿ",
"&#402;": "ƒ",
"&#710;": "ˆ",
"&#8211;": "–",
"&#8212;": "—",
"&#8216;": "‘",
"&#8217;": "’",
"&#8218;": "‚",
"&#8220;": "“",
"&#8221;": "”",
"&#8222;": "„",
"&#8224;": "†",
"&#8225;": "‡",
"&#8226;": "•",
"&#8230;": "…",
"&#8240;": "‰",
"&#8242;": "′",
"&#8243;": "″",
"&#8249;": "‹",
"&#8250;": "›",
"&#8254;": "‾",
"&#8364;": "€",
"&#8482;": "™",
"&#8592;": "←",
"&#8593;": "↑",
"&#8594;": "→",
"&#8595;": "↓",
"&#8596;": "↔",
"&#9674;": "◊",
"&#9824;": "♠",
"&#9827;": "♣",
"&#9829;": "♥",
"&#9830;": "♦"   
}

def udecode(string):
    for el in string:
        try:
            i = convert_diacritics[0].index(el)
            string = string.replace(el, convert_diacritics[1][i])
        except ValueError:
            pass
    return string
