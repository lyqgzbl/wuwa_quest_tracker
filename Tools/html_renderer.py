import json
from typing import Any

def render_html(dataset: dict[str, Any]) -> str:
    dataset_json = json.dumps(dataset, ensure_ascii=False).replace("</", r"<\/")
    
    return f"""<!doctype html>
<html lang="zh-CN" data-theme="auto">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>鸣潮 任务统计</title>
  <style>
    :root, [data-theme="light"] {{
      --bg: #fafafa;
      --bg-alpha: rgba(250, 250, 250, 0.65);
      --text: #2d3748;
      --text-muted: #718096;
      --card-bg: #ffffff;
      --card-hover: #f7fafc;
      --border: rgba(0, 0, 0, 0.06);
      --summary-bg: #ffffff;
      --summary-hover: #f1f5f9;
      --accent: #4f46e5;
      --accent-light: rgba(79, 70, 229, 0.1);
      --progress-bg: #e2e8f0;
      --progress-fill: linear-gradient(90deg, #6366f1, #4f46e5);
      --progress-full: linear-gradient(90deg, #10b981, #059669);
      --mark-bg: #fde047;
      --mark-text: #854d0e;
      --btn-bg: #ffffff;
      --btn-hover: #f8fafc;
      --btn-border: rgba(0, 0, 0, 0.1);
      --input-bg: #ffffff;
      --input-border: rgba(0, 0, 0, 0.1);
      --done-opacity: 0.55;
      --shadow-sm: 0 2px 4px rgba(0, 0, 0, 0.02);
      --shadow-md: 0 8px 16px -4px rgba(0, 0, 0, 0.05), 0 4px 8px -2px rgba(0, 0, 0, 0.02);
      --badge-bg: rgba(79, 70, 229, 0.1);
      --badge-text: #4f46e5;
      --card-gradient: linear-gradient(145deg, #ffffff, #fafafa);
      color-scheme: light;
    }}
    [data-theme="dark"] {{
      --bg: #0f172a;
      --bg-alpha: rgba(15, 23, 42, 0.65);
      --text: #f1f5f9;
      --text-muted: #94a3b8;
      --card-bg: #1e293b;
      --card-hover: #27344c;
      --border: rgba(255, 255, 255, 0.06);
      --summary-bg: #1e293b;
      --summary-hover: #2b3b54;
      --accent: #38bdf8;
      --accent-light: rgba(56, 189, 248, 0.15);
      --progress-bg: #334155;
      --progress-fill: linear-gradient(90deg, #0ea5e9, #38bdf8);
      --progress-full: linear-gradient(90deg, #22c55e, #4ade80);
      --mark-bg: #b45309;
      --mark-text: #fef08a;
      --btn-bg: #1e293b;
      --btn-hover: #293952;
      --btn-border: rgba(255, 255, 255, 0.1);
      --input-bg: #0f172a;
      --input-border: rgba(255, 255, 255, 0.1);
      --done-opacity: 0.45;
      --shadow-sm: 0 4px 6px rgba(0, 0, 0, 0.3);
      --shadow-md: 0 10px 20px -5px rgba(0, 0, 0, 0.4), 0 6px 10px -3px rgba(0, 0, 0, 0.2);
      --badge-bg: rgba(56, 189, 248, 0.15);
      --badge-text: #38bdf8;
      --card-gradient: linear-gradient(145deg, #1e293b, #151e2f);
      color-scheme: dark;
    }}
    @media (prefers-color-scheme: dark) {{
      [data-theme="auto"] {{
        --bg: #0f172a;
        --bg-alpha: rgba(15, 23, 42, 0.65);
        --text: #f1f5f9;
        --text-muted: #94a3b8;
        --card-bg: #1e293b;
        --card-hover: #27344c;
        --border: rgba(255, 255, 255, 0.06);
        --summary-bg: #1e293b;
        --summary-hover: #2b3b54;
        --accent: #38bdf8;
        --accent-light: rgba(56, 189, 248, 0.15);
        --progress-bg: #334155;
        --progress-fill: linear-gradient(90deg, #0ea5e9, #38bdf8);
        --progress-full: linear-gradient(90deg, #22c55e, #4ade80);
        --mark-bg: #b45309;
        --mark-text: #fef08a;
        --btn-bg: #1e293b;
        --btn-hover: #293952;
        --btn-border: rgba(255, 255, 255, 0.1);
        --input-bg: #0f172a;
        --input-border: rgba(255, 255, 255, 0.1);
        --done-opacity: 0.45;
        --shadow-sm: 0 4px 6px rgba(0, 0, 0, 0.3);
        --shadow-md: 0 10px 20px -5px rgba(0, 0, 0, 0.4), 0 6px 10px -3px rgba(0, 0, 0, 0.2);
        --badge-bg: rgba(56, 189, 248, 0.15);
        --badge-text: #38bdf8;
        --card-gradient: linear-gradient(145deg, #1e293b, #151e2f);
        color-scheme: dark;
      }}
    }}
    * {{ box-sizing: border-box; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, 'PingFang SC', sans-serif;
      margin: 0; padding: 0 16px 24px 16px;
      background: var(--bg); color: var(--text);
      line-height: 1.5;
      transition: background 0.5s ease, color 0.5s ease;
      -webkit-font-smoothing: antialiased;
    }}
    .container {{ max-width: 820px; margin: 0 auto; position: relative; }}
    .sticky-wrapper {{
      position: sticky; top: 0; z-index: 100;
      background: var(--bg-alpha);
      backdrop-filter: blur(24px) saturate(200%); -webkit-backdrop-filter: blur(24px) saturate(200%);
      margin: 0 -16px 20px -16px; padding: 16px 16px 12px 16px;
      border-bottom: 1px solid var(--border);
      transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .sticky-wrapper.scrolled {{
      padding: 8px 16px 8px 16px;
      box-shadow: var(--shadow-sm);
    }}
    .sticky-container {{ max-width: 820px; margin: 0 auto; }}
    header {{ display: flex; gap: 16px; align-items: center; flex-wrap: nowrap; margin-bottom: 12px; transition: all 0.4s ease; }}
    .sticky-wrapper.scrolled header {{ margin-bottom: 6px; }}
    header h2 {{ margin: 0; font-size: 24px; font-weight: 700; letter-spacing: -0.5px; transition: all 0.4s ease; white-space: nowrap; overflow: hidden; }}
    .sticky-wrapper.scrolled header h2 {{ width: 0; margin: 0; padding: 0; opacity: 0; font-size: 0; }}
    .overall-wrap {{ display: flex; align-items: center; gap: 12px; flex: 1; min-width: 200px; }}
    .overall-text {{ font-variant-numeric: tabular-nums; font-size: 14px; font-weight: 500; white-space: nowrap; }}
    .progress-bar {{
      flex: 1; height: 8px; min-width: 80px;
      background: var(--progress-bg); border-radius: 999px; overflow: hidden;
    }}
    .progress-bar-inner {{
      height: 100%; border-radius: 999px; background: var(--progress-fill);
      transition: width 0.8s ease-out, background 0.5s ease;
    }}
    .progress-bar-inner.full {{ background: var(--progress-full); }}
    .summary-progress {{
      display: inline-block; width: 64px; height: 6px;
      background: var(--progress-bg); border-radius: 999px; overflow: hidden;
      margin-left: 8px; vertical-align: middle;
    }}
    .summary-progress-inner {{
      display: block; height: 100%; border-radius: 999px; background: var(--progress-fill);
      transition: width 0.8s ease-out, background 0.5s ease;
    }}
    .summary-progress-inner.full {{ background: var(--progress-full); }}
    .toolbar {{
      display: flex; gap: 10px; align-items: center; flex-wrap: nowrap;
      transition: all 0.4s ease;
      overflow-x: auto; padding-bottom: 2px;
      -webkit-overflow-scrolling: touch; scrollbar-width: none;
    }}
    .toolbar::-webkit-scrollbar {{ display: none; }}
    .sticky-wrapper.scrolled .toolbar {{ gap: 8px; }}
    .search-wrap {{ position: relative; flex: 1; min-width: 240px; }}
    .search-icon {{
      position: absolute; left: 12px; top: 50%; transform: translateY(-50%);
      color: var(--text-muted); pointer-events: none;
    }}
    input[type="search"] {{
      width: 100%; padding: 10px 14px 10px 36px;
      border: 1px solid var(--input-border); border-radius: 10px;
      background: var(--input-bg); color: var(--text); font-size: 14px; outline: none;
      transition: all 0.3s ease; box-shadow: var(--shadow-sm);
    }}
    .sticky-wrapper.scrolled input[type="search"] {{ padding: 8px 12px 8px 32px; font-size: 13px; border-radius: 8px; }}
    input[type="search"]:focus {{
      border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-light);
    }}
    input[type="search"]::placeholder {{ color: var(--text-muted); }}
    .pill {{
      display: inline-flex; align-items: center; gap: 6px;
      padding: 8px 14px; border: 1px solid var(--btn-border); border-radius: 999px;
      background: var(--btn-bg); color: var(--text); font-size: 14px; font-weight: 500;
      cursor: pointer; user-select: none; transition: all 0.3s ease;
      box-shadow: var(--shadow-sm); white-space: nowrap; flex-shrink: 0;
    }}
    .sticky-wrapper.scrolled .pill {{ padding: 6px 12px; font-size: 13px; }}
    .pill:hover {{ background: var(--btn-hover); border-color: var(--text-muted); }}
    .pill input[type="checkbox"] {{ margin: 0; accent-color: var(--accent); width: 16px; height: 16px; cursor: pointer; pointer-events: none; transition: all 0.4s ease; }}
    .sticky-wrapper.scrolled .pill input[type="checkbox"] {{ width: 14px; height: 14px; }}
    .btn {{
      padding: 8px 14px; border: 1px solid var(--btn-border); border-radius: 10px;
      background: var(--btn-bg); color: var(--text); font-size: 14px; font-weight: 500;
      cursor: pointer; transition: all 0.3s ease; box-shadow: var(--shadow-sm);
      white-space: nowrap; flex-shrink: 0;
    }}
    .sticky-wrapper.scrolled .btn {{ padding: 6px 12px; font-size: 13px; border-radius: 8px; }}
    .btn:hover {{ background: var(--btn-hover); border-color: var(--text-muted); }}
    .btn-icon {{
      width: 36px; height: 36px; display: inline-flex; align-items: center; justify-content: center;
      border: 1px solid var(--btn-border); border-radius: 10px;
      background: var(--btn-bg); color: var(--text); font-size: 18px;
      cursor: pointer; transition: all 0.3s ease; box-shadow: var(--shadow-sm);
      flex-shrink: 0;
    }}
    .sticky-wrapper.scrolled .btn-icon {{ width: 30px; height: 30px; font-size: 16px; border-radius: 8px; }}
    .btn-icon:hover {{ background: var(--btn-hover); border-color: var(--text-muted); }}
    .tree {{ list-style: none; padding: 0; margin: 0; }}
    .tree > li {{ margin-bottom: 16px; }}
    details {{ margin: 0; border: 1px solid var(--border); border-radius: 14px; background: var(--summary-bg); box-shadow: var(--shadow-sm); overflow: hidden; transition: box-shadow 0.3s ease, border-color 0.3s ease; }}
    details:hover {{ box-shadow: var(--shadow-md); border-color: var(--accent-light); }}
    summary {{
      cursor: pointer; user-select: none; list-style: none;
      padding: 14px 18px; font-weight: 600; font-size: 16px;
      display: flex; align-items: center; gap: 10px; transition: background 0.3s ease;
    }}
    summary:hover {{ background: var(--summary-hover); }}
    summary::-webkit-details-marker {{ display: none; }}
    .chevron {{
      width: 20px; height: 20px; flex-shrink: 0; color: var(--text-muted);
      transition: transform 0.4s ease;
    }}
    details[open] > summary .chevron {{ transform: rotate(90deg); }}
    .summary-text {{ flex: 1; }}
    .summary-count {{
      font-size: 12px; font-weight: 600; font-variant-numeric: tabular-nums;
      background: var(--badge-bg); color: var(--badge-text);
      padding: 2px 8px; border-radius: 999px; white-space: nowrap;
    }}
    .node {{ border-top: 1px solid var(--border); background: var(--bg); padding: 12px; }}
    .node details {{ margin-bottom: 8px; border-radius: 12px; box-shadow: none; border-color: var(--border); }}
    .node details:last-child {{ margin-bottom: 0; }}
    .node summary {{ font-size: 15px; padding: 10px 14px; }}
    .ach-list {{ list-style: none; padding: 8px; margin: 0; background: var(--bg); }}
    .ach-item {{
      display: flex; gap: 14px; padding: 14px; margin-bottom: 8px;
      border-radius: 12px; background: var(--card-gradient); border: 1px solid var(--border);
      transition: all 0.4s ease; cursor: pointer;
      position: relative; overflow: hidden;
    }}
    .ach-item:last-child {{ margin-bottom: 0; }}
    .ach-item:hover {{ transform: translateY(-2px); box-shadow: var(--shadow-md); border-color: var(--accent-light); }}
    .ach-item-checkbox {{
      flex-shrink: 0; width: 22px; height: 22px; margin-top: 2px;
      border: 2px solid var(--text-muted); border-radius: 6px;
      display: flex; align-items: center; justify-content: center;
      transition: all 0.3s ease; background: var(--card-bg);
    }}
    .ach-item-checkbox svg {{
      width: 14px; height: 14px; color: white; opacity: 0; transform: scale(0.5);
      transition: all 0.4s ease;
    }}
    .ach-item.done .ach-item-checkbox {{ background: var(--accent); border-color: var(--accent); }}
    .ach-item.done .ach-item-checkbox svg {{ opacity: 1; transform: scale(1); }}
    .ach-content {{ flex: 1; transition: opacity 0.4s ease; }}
    .ach-title {{ font-weight: 600; font-size: 15px; transition: color 0.4s ease; }}
    .ach-desc {{ font-size: 13px; color: var(--text-muted); white-space: pre-wrap; margin-top: 4px; line-height: 1.5; }}
    .ach-item.done {{ background: var(--card-bg); opacity: var(--done-opacity); box-shadow: none; border-color: transparent; }}
    .ach-item.done:hover {{ transform: none; box-shadow: none; border-color: transparent; }}
    .ach-item.done .ach-title {{ text-decoration: line-through; color: var(--text-muted); }}
    .ach-item.active {{ background: rgba(245, 158, 11, 0.1); border-left: 3px solid #f59e0b; }}
    mark {{ background: var(--mark-bg); color: var(--mark-text); border-radius: 3px; padding: 0 2px; font-weight: 500; }}
    .scroll-top {{
      position: fixed; bottom: 24px; right: 24px; z-index: 90;
      width: 44px; height: 44px; border-radius: 50%;
      background: var(--bg-alpha); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
      border: 1px solid var(--border); color: var(--text);
      display: flex; align-items: center; justify-content: center;
      cursor: pointer; opacity: 0; transform: translateY(20px) scale(0.9); pointer-events: none;
      transition: all 0.4s ease; box-shadow: var(--shadow-md);
    }}
    .scroll-top.visible {{ opacity: 1; transform: translateY(0) scale(1); pointer-events: auto; }}
    .scroll-top:hover {{ background: var(--btn-hover); transform: translateY(-2px) scale(1.05); }}
    @media (max-width: 600px) {{
      body {{ padding: 0 12px 20px 12px; }}
      .sticky-wrapper {{ margin: 0 -12px 16px -12px; padding: 12px 12px 8px 12px; }}
      .sticky-wrapper.scrolled {{ padding: 6px 12px 6px 12px; }}
      header {{ gap: 10px; margin-bottom: 10px; }}
      .sticky-wrapper.scrolled header {{ margin-bottom: 6px; }}
      header h2 {{ font-size: 20px; }}
      .overall-wrap {{ min-width: 0; }}
      .overall-text {{ font-size: 13px; }}
      .progress-bar {{ min-width: 60px; }}
      .toolbar {{ gap: 8px; }}
      .sticky-wrapper.scrolled .toolbar {{ gap: 6px; }}
      .search-wrap {{ flex: 1 0 150px; min-width: 150px; width: auto; }}
      .sticky-wrapper.scrolled .search-wrap {{ flex: 1 0 130px; min-width: 130px; }}
      .sticky-wrapper.scrolled input[type="search"] {{ padding: 6px 10px 6px 28px; font-size: 13px; }}
      .sticky-wrapper.scrolled .search-icon {{ width: 14px; height: 14px; left: 8px; }}
      .pill, .btn {{ padding: 6px 12px; font-size: 13px; }}
      .sticky-wrapper.scrolled .pill, .sticky-wrapper.scrolled .btn {{ padding: 4px 10px; font-size: 12px; }}
      .btn-icon {{ width: 32px; height: 32px; font-size: 16px; }}
      .sticky-wrapper.scrolled .btn-icon {{ width: 28px; height: 28px; font-size: 14px; }}
      summary {{ padding: 10px 12px; font-size: 15px; }}
      .node {{ padding: 8px; }}
      .ach-item {{ padding: 10px; gap: 10px; }}
      .ach-list {{ padding: 2px; }}
      .summary-progress {{ width: 40px; }}
      .scroll-top {{ bottom: 16px; right: 16px; width: 40px; height: 40px; }}
    }}
  </style>
</head>
<body>
  <div class="sticky-wrapper">
    <div class="sticky-container">
      <header>
        <h2>任务统计</h2>
        <div class="overall-wrap">
          <span id="overall" class="overall-text"></span>
          <div class="progress-bar"><div id="overallBar" class="progress-bar-inner"></div></div>
        </div>
        <button id="themeBtn" class="btn-icon" type="button" title="切换主题"></button>
      </header>
      <div class="toolbar">
        <div class="search-wrap">
          <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <input id="q" type="search" placeholder="搜索任务名称或描述..." />
        </div>
        <label class="pill" style="cursor: pointer;"><input id="onlyTodo" type="checkbox" style="pointer-events: auto;" /> 仅未完成</label>
        <button id="exportBtn" class="btn" type="button">导出</button>
        <button id="importBtn" class="btn" type="button">导入</button>
        <input id="importFile" type="file" accept="application/json" style="display:none" />
      </div>
    </div>
  </div>

  <div class="container">
    <div id="app"></div>
  </div>

  <button id="scrollTopBtn" class="scroll-top" aria-label="返回顶部" title="返回顶部">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>
  </button>

<script>
const DATA = {dataset_json};
const STORE_KEY = 'wuwa_quest_completed';
const ACTIVE_KEY = 'wuwa_quest_active'; // Optional feature
const OPEN_CAT_KEY = 'wuwa_quest_open_cats';
const EXPORT_KEY = 'ww_quest_export_v1';

const CHEVRON_SVG = `<svg class="chevron" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>`;
const CHECK_SVG = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>`;

const THEME_ICONS = {{
  auto: `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>`,
  light: `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>`,
  dark: `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>`,
}};
const THEME_CYCLE = ['auto', 'light', 'dark'];
const THEME_KEY = 'ww_quest_theme_v1';

function getTheme() {{ return localStorage.getItem(THEME_KEY) || 'auto'; }}
function applyTheme(theme) {{
  document.documentElement.setAttribute('data-theme', theme);
  document.getElementById('themeBtn').innerHTML = THEME_ICONS[theme] || THEME_ICONS.auto;
  localStorage.setItem(THEME_KEY, theme);
}}
function cycleTheme() {{
  const cur = getTheme();
  const next = THEME_CYCLE[(THEME_CYCLE.indexOf(cur) + 1) % THEME_CYCLE.length];
  applyTheme(next);
}}
applyTheme(getTheme());
document.getElementById('themeBtn').addEventListener('click', cycleTheme);

function loadSet(key) {{
  try {{ return new Set(JSON.parse(localStorage.getItem(key) || '[]')); }}
  catch {{ return new Set(); }}
}}
function saveSet(key, set) {{ localStorage.setItem(key, JSON.stringify([...set])); }}

function exportProgress() {{
  const compSet = loadSet(STORE_KEY);
  const actSet = loadSet(ACTIVE_KEY);
  const openCats = loadSet(OPEN_CAT_KEY);

  const payload = {{
    schema: EXPORT_KEY,
    version: 1,
    exportedAt: new Date().toISOString(),
    diagnostics: {{ generatedBy: 'web_ui_export' }},
    // Put everything in "quests" for simplicity so it can be re-imported
    quests: {{
      completed: Array.from(compSet),
      active: Array.from(actSet)
    }},
    openCategories: Array.from(openCats)
  }};

  const blob = new Blob([JSON.stringify(payload, null, 2)], {{ type: 'application/json' }});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'wuwa_quest_progress.json';
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(url);
}}

function textIncludes(hay, needle) {{
  if (!needle) return true;
  return (hay || '').toLowerCase().includes(needle);
}}

function highlightText(text, needle) {{
  if (!needle || !text) return document.createTextNode(text || '');
  const lower = text.toLowerCase();
  const frag = document.createDocumentFragment();
  let start = 0;
  while (start < text.length) {{
    const idx = lower.indexOf(needle, start);
    if (idx === -1) {{
      frag.appendChild(document.createTextNode(text.slice(start)));
      break;
    }}
    if (idx > start) frag.appendChild(document.createTextNode(text.slice(start, idx)));
    const mark = document.createElement('mark');
    mark.textContent = text.slice(idx, idx + needle.length);
    frag.appendChild(mark);
    start = idx + needle.length;
  }}
  return frag;
}}

function computeCounts(cats, completedSet) {{
  let total = 0, done = 0;
  for (const c of cats) {{
    c._total = c.quests.length;
    c._done = 0;
    for (const q of c.quests) {{
      if (completedSet.has(q.id)) c._done++;
    }}
    total += c._total;
    done += c._done;
  }}
  return {{ total, done }};
}}

function makeProgressSpan(done, total) {{
  const wrap = document.createElement('span');
  wrap.className = 'summary-progress';
  const inner = document.createElement('span');
  inner.className = 'summary-progress-inner';
  const pct = total > 0 ? (done / total * 100) : 0;
  inner.style.width = pct + '%';
  if (done === total && total > 0) inner.classList.add('full');
  wrap.appendChild(inner);
  return wrap;
}}

function render() {{
  const completed = loadSet(STORE_KEY);
  const active = loadSet(ACTIVE_KEY);
  const openCats = loadSet(OPEN_CAT_KEY);
  const q = (document.getElementById('q').value || '').trim().toLowerCase();
  const onlyTodo = document.getElementById('onlyTodo').checked;

  const counts = computeCounts(DATA.categories || [], completed);
  document.getElementById('overall').textContent = counts.done + ' / ' + counts.total;
  const overallBar = document.getElementById('overallBar');
  overallBar.style.width = counts.total ? (counts.done / counts.total * 100) + '%' : '0%';
  if (counts.done === counts.total && counts.total > 0) overallBar.classList.add('full');
  else overallBar.classList.remove('full');

  const app = document.getElementById('app');
  app.innerHTML = '';

  if (!DATA.categories) return;

  const rootUl = document.createElement('ul');
  rootUl.className = 'tree';
  app.appendChild(rootUl);

  for (const cat of DATA.categories) {{
    let catHasAny = false;
    for (const quest of cat.quests) {{
      const isDone = completed.has(quest.id);
      const match = textIncludes(quest.name, q) || textIncludes(quest.desc, q);
      if (match && !(onlyTodo && isDone)) {{
        catHasAny = true;
        break;
      }}
    }}
    if ((q || onlyTodo) && !catHasAny) continue;

    const liCat = document.createElement('li');
    const catDetails = document.createElement('details');
    const catId = String(cat.id);
    catDetails.open = q ? true : openCats.has(catId);
    catDetails.addEventListener('toggle', () => {{
      const set = loadSet(OPEN_CAT_KEY);
      if (catDetails.open) set.add(catId); else set.delete(catId);
      saveSet(OPEN_CAT_KEY, set);
    }});

    const catSummary = document.createElement('summary');
    catSummary.innerHTML = CHEVRON_SVG;

    const catText = document.createElement('span');
    catText.className = 'summary-text';
    catText.textContent = cat.name;
    const catCount = document.createElement('span');
    catCount.className = 'summary-count';
    catCount.textContent = cat._done + ' / ' + cat._total;

    catSummary.appendChild(catText);
    catSummary.appendChild(catCount);
    catSummary.appendChild(makeProgressSpan(cat._done, cat._total));
    catDetails.appendChild(catSummary);

    const ul = document.createElement('ul');
    ul.className = 'ach-list';

    for (const quest of cat.quests) {{
      const isDone = completed.has(quest.id);
      const isActive = !isDone && active.has(quest.id);
      const match = textIncludes(quest.name, q) || textIncludes(quest.desc, q);
      if (!match) continue;
      if (onlyTodo && isDone) continue;

      const li = document.createElement('li');
      li.className = 'ach-item' + (isDone ? ' done' : '') + (isActive ? ' active' : '');

      li.addEventListener('click', () => {{
        const set = loadSet(STORE_KEY);
        if (set.has(quest.id)) set.delete(quest.id); else set.add(quest.id);
        saveSet(STORE_KEY, set);
        render();
      }});

      const customCb = document.createElement('div');
      customCb.className = 'ach-item-checkbox';
      customCb.innerHTML = CHECK_SVG;

      const content = document.createElement('div');
      content.className = 'ach-content';
      
      const title = document.createElement('div');
      title.className = 'ach-title';
      title.appendChild(highlightText(quest.name || '未知名称', q));
      
      const desc = document.createElement('div');
      desc.className = 'ach-desc';
      desc.appendChild(highlightText(quest.desc || '无描述', q));
      
      content.appendChild(title);
      content.appendChild(desc);

      li.appendChild(customCb);
      li.appendChild(content);
      ul.appendChild(li);
    }}

    catDetails.appendChild(ul);
    liCat.appendChild(catDetails);
    rootUl.appendChild(liCat);
  }}
}}

async function importFile(file) {{
  const text = await file.text();
  let payload;
  try {{ payload = JSON.parse(text); }} catch {{ alert('无效的 JSON 文件'); return; }}
  
  if (payload.schema !== 'ww_quest_export_v1') {{
    alert('不支持的数据格式！需要 wuwa_quest_dump.py 导出的 quest_export.json');
    return;
  }}
  
  const compSet = loadSet(STORE_KEY);
  const actSet = loadSet(ACTIVE_KEY);
  let addCount = 0;
  
  const processGroup = (grp) => {{
    if (!grp) return;
    if (Array.isArray(grp.completed)) {{
      for (const id of grp.completed) {{
        if (!compSet.has(id)) {{ compSet.add(id); addCount++; }}
        actSet.delete(id);
      }}
    }}
    if (Array.isArray(grp.active)) {{
      for (const id of grp.active) {{
        if (!compSet.has(id)) actSet.add(id);
      }}
    }}
  }};
  
  processGroup(payload.mainQuests);
  processGroup(payload.quests);
  processGroup(payload.dailyTasks);
  
  saveSet(STORE_KEY, compSet);
  saveSet(ACTIVE_KEY, actSet);
  
  alert(`导入成功！新增标记了 ${{addCount}} 个已完成任务。`);
  render();
}}

const scrollTopBtn = document.getElementById('scrollTopBtn');
const stickyWrapper = document.querySelector('.sticky-wrapper');

window.addEventListener('scroll', () => {{
  if (window.scrollY > 40) {{
    stickyWrapper.classList.add('scrolled');
  }} else {{
    stickyWrapper.classList.remove('scrolled');
  }}

  if (window.scrollY > 300) {{
    scrollTopBtn.classList.add('visible');
  }} else {{
    scrollTopBtn.classList.remove('visible');
  }}
}});

scrollTopBtn.addEventListener('click', () => {{
  window.scrollTo({{ top: 0, behavior: 'smooth' }});
}});

document.getElementById('q').addEventListener('input', render);
document.getElementById('onlyTodo').addEventListener('change', render);
document.getElementById('exportBtn').addEventListener('click', exportProgress);

document.getElementById('importBtn').addEventListener('click', () => document.getElementById('importFile').click());
document.getElementById('importFile').addEventListener('change', async (e) => {{
  const file = e.target.files && e.target.files[0];
  e.target.value = '';
  if (!file) return;
  await importFile(file);
}});

render();
</script>
</body>
</html>
"""
