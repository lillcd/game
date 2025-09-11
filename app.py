# Copyright (c) 2025 Christopher Lilly
# All rights reserved.
# Unauthorized use or distribution is prohibited.

#@title 🚀 Game

import random
import json
import streamlit as st
import streamlit.components.v1 as components


rounds = {
    "r1": {
        "word_pairs": [("Fax","History"),("Finger","Grass"),("Break","Car"),("Spain","Plum"),("Chair","Green"),("Trick","Bow"),("Camp","Wind"),("Coffee","Happy"),("Puppet","New")],
        "correct_blocks": ["block6","block3","block7","block9"],
        "start_word": "Top",
        "end_word":   "Cow",
    },
    "r2": {
        "word_pairs": [("Rev","Keith"),("Elephant","Double"),("Williams","Engine"),("Once","House"),("Bell","Rotten"),("Studio","Freddie"),("Worm","Capri"),("Attacks","Google"),("Sega","Biscuit")],
        "correct_blocks": ["block8","block7","block6","block1"],
        "start_word": "Bruno",
        "end_word":   "River",
    },
    "r3": {
        "word_pairs": [("Day","Golden"),("Lit","Latin"),("Number","Pen"),("Pollution","Road"),("Club","Key"),("Walker","Call"),("Courage","Johnny"),("Dresser","Go"),("Orthodox","Irvine")],
        "correct_blocks": ["block9","block8","block7","block2"],
        "start_word": "White",
        "end_word":   "Football",
    },
    "r4": {
        "word_pairs": [("Night","Big"),("Red","Black"),("Bowl","Candle"),("Boat","Sour"),("Dresser","Go"),("File","Cloud"),("Car","Sad"),("Mac","Top"),("Hyacinth","Key")],
        "correct_blocks": ["block1","block8","block4","block2","block9"],
        "start_word": "Carbon",
        "end_word":   "Green",
    },
    "r5": {
        "word_pairs": [("Location","Boutique"),("Grim","Ball"),("Plate","Pill"),("Rail","Sweet"),("Pence","VW"),("Rose","Nine"),("California","Ford"),("Course","Amazon"),("Oasis","Happen")],
        "correct_blocks": ["block5","block8","block1","block7"],
        "start_word": "Iron",
        "end_word":   "Nevada",
    },
    "r6": {
        "word_pairs": [("Away","War"),("Small","County"),("Enough","Inner"),("Sergeant","Miami"),("Dust","MC"),("Oak","Eleven"),("Paris","Nissan"),("Tesla","Cloud"),("Captain","Monkey")],
        "correct_blocks": ["block4","block9","block1","block5"],
        "start_word": "Fire",
        "end_word":   "Head",
    },
    "r7": {
        "word_pairs": [("Sonic","Leg"),("Mark","Hell's"),("For","Fifty"),("Doctor","French"),("MBE","Port"),("Abroad","Guest"),("Lizard","Albert"),("Counter","Under"),("Greek","Double")],
        "correct_blocks": ["block7","block2","block8","block6"],
        "start_word": "Airport",
        "end_word":   "Eyes",
    },
    "r8": {
        "word_pairs": [("Ball","Secret"),("South","Police"),("Guys","Matchbox"),("Coffee","Neptune"),("Sisters","U"),("Clarity","People"),("Gecko","Witty"),("CV","Famous"),("Shampoo","Arm")],
        "correct_blocks": ["block7","block2","block8","block6"],
        "start_word": "After",
        "end_word":   "Questions",
    },
    "r9": {
        "word_pairs": [("Berry","Cold"),("West","News"),("Reliant","Golden"),("Tea","Mars"),("X","Harris"),("Teeth","Turtle"),("Rake","Magnolia"),("Tomb","Jaw"),("Tail","Sheryl")],
        "correct_blocks": ["block3","block1","block6","block9"],
        "start_word": "Round",
        "end_word":   "Bar",
    },
    "r10": {
        "word_pairs": [("South","Warm"),("Dread","Freaky"),("Addams","Super"),("Snickers","Loop"),("ABC","Bridge"),("Ad","Cyber"),("Tunnel","Keyboard"),("Hip","Arch"),("Blues","Ash")],
        "correct_blocks": ["block2","block6","block9","block3"],
        "start_word": "Ski",
        "end_word":   "Job",
    },
    "r11": {
        "word_pairs": [("Wind","Keys"),("Digger","Pump"),("Percy","Vehicle"),("Whistle","Top"),("Deft","Leer"),("Lining","Fools"),("Cake","Party"),("Pass","Ropes"),("Maiden","Biscuit")],
        "correct_blocks": ["block6","block2","block9","block4"],
        "start_word": "Quick",
        "end_word":   "Monkeys",
    },
    "r12": {
        "word_pairs": [("Pack","Kick"),("Digger","Pump"),("Mulder","British"),("Whistle","Top"),("Deft","Leer"),("Lining","Fools"),("Cake","Party"),("Shorts","Wile E"),("Clip","Cry")],
        "correct_blocks": ["block3","block9","block1","block8"],
        "start_word": "Silver",
        "end_word":   "Ugly",
    },
    "r13": {
        "word_pairs": [("Juice","Dragon"),("Robot","Tech"),("Bat","Gypsy"),("Orchestra","Hallow"),("Metal","Pork"),("Habit","Weapon"),("Ball","Dung"),("Line","Jiminy"),("Graph","Mower")],
        "correct_blocks": ["block8","block3","block7","block8"],
        "start_word": "Queen",
        "end_word":   "Fish",
    },
    "r14": {
        "word_pairs": [("Martin","Loaf"),("Whites","Arm"),("Day","Lawn"),("Pablo","Mull"),("Bell","Jiminy"),("Habitat","Fool"),("Bicuit","Member"),("With","Shadow"),("Tyre","Floor")],
        "correct_blocks": ["block5","block2","block8","block3"],
        "start_word": "Stage",
        "end_word":   "Elbow",
    }
}





def simple_check(block_ids):
    nums = [int(b.replace("block", "")) for b in block_ids]  # e.g., [7, 2, 8, 6]
    encoded = [n * 31 for n in nums]  # e.g., [217, 62, 248, 186]
    return encoded
    
    
    
def render_round():
    global current_round
    current_round = random.choice(list(rounds.keys()))
    # print("🎲 Chosen round:", current_round)
    new_html = html_code
    for i, (w1, w2) in enumerate(rounds[current_round]['word_pairs'], start=1):
        new_html = new_html.replace(f"__BLOCK{i}_WORD1__", w1)
        new_html = new_html.replace(f"__BLOCK{i}_WORD2__", w2)
    new_html = (new_html
        .replace("__START_WORD__", rounds[current_round]['start_word'])
        .replace("__END_WORD__",   rounds[current_round]['end_word'])
    )
    # Compute checksum of correct_blocks JSON string
    correct_blocks = rounds[current_round]["correct_blocks"]
    answer_check = simple_check(correct_blocks)
    # Inject checksum into HTML as a script tag (you can place it near the end)
    inject_script = f'<script>const blockref = {json.dumps(answer_check)};</script>'
    return inject_script + new_html




# Hidden text_area to receive data from JS
st.markdown("""
<style>.stTextArea { display: none; } .stVerticalBlock { gap: 0.5rem !important; max-width: 360px !important; } div[data-testid="stLayoutWrapper"] { max-width: 360px; } .stMainBlockContainer { padding-bottom: 50px !important; }</style>
""", unsafe_allow_html=True)

         
            
            

html_code = """
<style>
body { padding: 0px; margin: 0px; font-family: sans-serif; }
.grid-container { display: grid; grid-template-columns: repeat(6, 60px); grid-template-rows: repeat(5, 60px); width: max-content; }
.grid-cell { width: 60px; height: 60px; background-color: #eee; border: 1px solid #ccc; box-sizing: border-box; position: relative; }
.draggable { width: 120px; height: 60px; background-color: #2E2E2E; cursor: grab; position: absolute; z-index: 10; border-radius: 7px; user-select: none; transition: transform-origin: center center; transform 0.25s ease; }
.rotate-handle { width: 20px; height: 20px; background: none; position: absolute; cursor: pointer; z-index: 20; }
.top-left { top: 0px; left: 0px; }
.top-right { top: 0px; right: 0px; }
.bottom-left { bottom: 0px; left: 0px; }
.bottom-right { bottom: 0px; right: 0px; }
.wrd { color: #ffffff; font-size: 13px; position: absolute; top: 50%; width: 49%; text-align: center; text-anchor: middle; line-height: 0px; }
.lwrd { left: 0; }
.rwrd { right: 0; }
#arena { width: 100%; height: 582px; }
#block1 { transform: rotate(7deg); top: 317px; left: 5px; }
#block2 { transform: rotate(-44deg); top: 342px; left: 114px; }
#block3 { transform: rotate(-7deg); top: 310px; left: 235px; }
#block4 { transform: rotate(16deg); top: 393px; left: 4px; }
#block5 { transform: rotate(0deg); top: 377px; left: 242px; }
#block6 { transform: rotate(-70deg); top: 487px; left: -8px; }
#block7 { transform: rotate(24deg); top: 430px; left: 161px; }
#block8 { transform: rotate(-9deg); top: 498px; left: 95px; }
#block9 { transform: rotate(-36deg); top: 490px; left: 240px; }
.dvdr { position: absolute; background-color: #ffffff; height: 52px; top: 4px; left: 58px; width: 2px; }
.strtfnsh { position: absolute; width: 60px; height: 60px; background-color: #2E2E2E; }
#strt { left: 0px; top: 240px; border-radius: 0px 7px 7px 0px; }
#fnsh { left: 300px; top: 0px; border-radius: 7px 0px 0px 7px; }
.strtfnsh .wrd { width: 100% !important; }
@keyframes solvedGlow { 0% { box-shadow: 0 0 0px rgba(0, 255, 0, 0); } 20% { box-shadow: 0 0 12px 4px rgba(0, 255, 0, 0.8); } 100% { box-shadow: 0 0 0px rgba(0, 255, 0, 0); } }
.block.slvd { animation: solvedGlow 2.5s ease-out; }
</style>
<div id="arena">
<div class="grid-container" id="grid">
<!-- Create 30 grid cells -->
<script>
for (let i = 0; i < 30; i++) {
let cell = document.createElement('div');
cell.className = 'grid-cell';
document.getElementById('grid').appendChild(cell);
}
</script>
</div>
<div id="game">
<!-- Start and finish -->
<div class="strtfnsh" id="strt">
<div class="wrd rwrd">__START_WORD__</div>
</div>
<div class="strtfnsh" id="fnsh">
<div class="wrd rwrd">__END_WORD__</div>
</div>
<!-- Draggable blocks -->
<div class="draggable block" id="block1" draggable="true">
<div class="rotate-handle top-left"></div>
<div class="rotate-handle top-right"></div>
<div class="rotate-handle bottom-left"></div>
<div class="rotate-handle bottom-right"></div>
<div class="wrd lwrd">__BLOCK1_WORD1__</div>
<div class="wrd rwrd">__BLOCK1_WORD2__</div>
<div class="dvdr"></div>
</div>
<div class="draggable block" id="block2" draggable="true">
<div class="rotate-handle top-left"></div>
<div class="rotate-handle top-right"></div>
<div class="rotate-handle bottom-left"></div>
<div class="rotate-handle bottom-right"></div>
<div class="wrd lwrd">__BLOCK2_WORD1__</div>
<div class="wrd rwrd">__BLOCK2_WORD2__</div>
<div class="dvdr"></div>
</div>
<div class="draggable block" id="block3" draggable="true">
<div class="rotate-handle top-left"></div>
<div class="rotate-handle top-right"></div>
<div class="rotate-handle bottom-left"></div>
<div class="rotate-handle bottom-right"></div>
<div class="wrd lwrd">__BLOCK3_WORD1__</div>
<div class="wrd rwrd">__BLOCK3_WORD2__</div>
<div class="dvdr"></div>
</div>
<div class="draggable block" id="block4" draggable="true">
<div class="rotate-handle top-left"></div>
<div class="rotate-handle top-right"></div>
<div class="rotate-handle bottom-left"></div>
<div class="rotate-handle bottom-right"></div>
<div class="wrd lwrd">__BLOCK4_WORD1__</div>
<div class="wrd rwrd">__BLOCK4_WORD2__</div>
<div class="dvdr"></div>
</div>
<div class="draggable block" id="block5" draggable="true">
<div class="rotate-handle top-left"></div>
<div class="rotate-handle top-right"></div>
<div class="rotate-handle bottom-left"></div>
<div class="rotate-handle bottom-right"></div>
<div class="wrd lwrd">__BLOCK5_WORD1__</div>
<div class="wrd rwrd">__BLOCK5_WORD2__</div>
<div class="dvdr"></div>
</div>
<div class="draggable block" id="block6" draggable="true">
<div class="rotate-handle top-left"></div>
<div class="rotate-handle top-right"></div>
<div class="rotate-handle bottom-left"></div>
<div class="rotate-handle bottom-right"></div>
<div class="wrd lwrd">__BLOCK6_WORD1__</div>
<div class="wrd rwrd">__BLOCK6_WORD2__</div>
<div class="dvdr"></div>
</div>
<div class="draggable block" id="block7" draggable="true">
<div class="rotate-handle top-left"></div>
<div class="rotate-handle top-right"></div>
<div class="rotate-handle bottom-left"></div>
<div class="rotate-handle bottom-right"></div>
<div class="wrd lwrd">__BLOCK7_WORD1__</div>
<div class="wrd rwrd">__BLOCK7_WORD2__</div>
<div class="dvdr"></div>
</div>
<div class="draggable block" id="block8" draggable="true">
<div class="rotate-handle top-left"></div>
<div class="rotate-handle top-right"></div>
<div class="rotate-handle bottom-left"></div>
<div class="rotate-handle bottom-right"></div>
<div class="wrd lwrd">__BLOCK8_WORD1__</div>
<div class="wrd rwrd">__BLOCK8_WORD2__</div>
<div class="dvdr"></div>
</div>
<div class="draggable block" id="block9" draggable="true">
<div class="rotate-handle top-left"></div>
<div class="rotate-handle top-right"></div>
<div class="rotate-handle bottom-left"></div>
<div class="rotate-handle bottom-right"></div>
<div class="wrd lwrd">__BLOCK9_WORD1__</div>
<div class="wrd rwrd">__BLOCK9_WORD2__</div>
<div class="dvdr"></div>
</div>
</div>
</div>

<script>
console.log("Received answer check:", blockref);
const arena = document.getElementById("arena");
const grid = document.getElementById('grid');
const rect = grid.getBoundingClientRect();
const blocks = document.querySelectorAll('.block');
let activeBlock = null;
let isDragging = false;
let dragOffset = { x: 0, y: 0 };
let isRotating = false;
let rotationStartAngle = 0;
let liveRotation = 0;
// Store each block’s rotation separately
const blockState = new Map(); // block -> { rotation }

blocks.forEach(block => {
  blockState.set(block, { rotation: 0 });
// Rotation handle(s)
  const rotateHandles = block.querySelectorAll('.rotate-handle');
  rotateHandles.forEach(handle => {
    const handleRotateStart = (e) => {
      e.preventDefault();
      isRotating = true;
      activeBlock = block;
      let clientX, clientY;
      if (e.type === 'touchstart') {
        const touch = e.touches[0];
        clientX = touch.clientX;
        clientY = touch.clientY;
        if (e.cancelable) e.preventDefault();
      } else {
        clientX = e.clientX;
        clientY = e.clientY;
      }
      const rect = block.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;
      const dx = clientX - centerX;
      const dy = clientY - centerY;
      rotationStartAngle = Math.atan2(dy, dx) * (180 / Math.PI);
      if (rotationStartAngle < 0) rotationStartAngle += 360;
    };
    handle.addEventListener('mousedown', handleRotateStart);
    handle.addEventListener('touchstart', handleRotateStart, { passive: false });
  });
// Dragging
  const handleDragStart = (e) => {
    if (e.cancelable) e.preventDefault();
    if (e.target.classList.contains('rotate-handle')) return; // 👈 Skip if rotate handle
    console.log("drag start fired s");
    if (isRotating) return;
    isDragging = true;
    activeBlock = block;
    let clientX, clientY;
    if (e.type === 'touchstart') {
      const touch = e.touches[0];
      clientX = touch.clientX;
      clientY = touch.clientY;
    } else {
      clientX = e.clientX;
      clientY = e.clientY;
    }
    const rect = block.getBoundingClientRect();
    dragOffset.x = clientX - (rect.left + rect.width / 2);
    dragOffset.y = clientY - (rect.top + rect.height / 2);
  };
  block.addEventListener('mousedown', handleDragStart);
  block.addEventListener('touchstart', handleDragStart, { passive: false });
});

// Mouse move: handle drag or rotation
function handleMove(e) {
  if (!activeBlock || (!isDragging && !isRotating)) return;
  if (!activeBlock) return;
  let clientX, clientY;
  if (e.type === 'touchmove') {
    const touch = e.touches[0];
    clientX = touch.clientX;
    clientY = touch.clientY;
    if (e.cancelable) e.preventDefault(); // optional: prevent scrolling
  } else {
    clientX = e.clientX;
    clientY = e.clientY;
  }
  if (isRotating) {
    const rect = activeBlock.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    const dx = clientX - centerX;
    const dy = clientY - centerY;
    let currentAngle = Math.atan2(dy, dx) * (180 / Math.PI);
    if (currentAngle < 0) currentAngle += 360;
    let angleDiff = currentAngle - rotationStartAngle;
    const { rotation } = blockState.get(activeBlock);
    liveRotation = (rotation + angleDiff + 360) % 360;
    activeBlock.style.transform = `rotate(${liveRotation}deg)`;
  } else if (isDragging) {
    const rect = grid.getBoundingClientRect();
    const newCenterX = clientX - dragOffset.x;
    const newCenterY = clientY - dragOffset.y;
    const width = activeBlock.offsetWidth;
    const height = activeBlock.offsetHeight;
    const x = newCenterX - width / 2 - rect.left;
    const y = newCenterY - height / 2 - rect.top;
    const { rotation } = blockState.get(activeBlock);
    activeBlock.style.left = x + 'px';
    activeBlock.style.top = y + 'px';
    activeBlock.style.transform = `rotate(${rotation}deg)`;
  }
}
document.addEventListener('mousemove', handleMove);
document.addEventListener('touchmove', handleMove, { passive: false });

// Mouse up: snap and finalize rotation
function handleEnd(e) {
  console.log("mouseup fired");
  if (!activeBlock) return;
  const state = blockState.get(activeBlock);
  if (isDragging) {
    const cellSize = 60;
    let rot = state.rotation % 360;
    if (rot < 0) rot += 360;
    const grid = document.getElementById("grid");
    const rect = grid.getBoundingClientRect();
    let left = parseFloat(activeBlock.style.left) - rect.left || 0;
    let top = parseFloat(activeBlock.style.top) - rect.top || 0;
    let offsetX = (rot === 90 || rot === 270) ? 30 : 0;
    let offsetY = (rot === 90 || rot === 270) ? 30 : 0;
    const blockWidth = rot % 180 === 0 ? activeBlock.offsetWidth : activeBlock.offsetHeight;
    const blockHeight = rot % 180 === 0 ? activeBlock.offsetHeight : activeBlock.offsetWidth;
    const maxX = grid.clientWidth - blockWidth;
    const maxY = (rot === 90 || rot === 270) ? grid.clientHeight - blockHeight + 60 : grid.clientHeight - blockHeight;
    const minY = (rot === 90 || rot === 270) ? 60 : 0;
    const gridBottom = grid.clientHeight;
    if (top <= gridBottom) {
    // ✅ Inside grid: snap to nearest cell
      const snapX = Math.min(maxX, Math.max(0, Math.round((left + offsetX) / cellSize) * cellSize));
      const snapY = Math.min(maxY, Math.max(minY, Math.round((top + offsetY) / cellSize) * cellSize));
      activeBlock.style.left = (snapX + rect.left - offsetX) + 'px';
      activeBlock.style.top = (snapY + rect.top - offsetY) + 'px';
    } else {
    // ❌ Below grid: leave it where the user dropped it
      activeBlock.style.left = (left + rect.left) + 'px';
      activeBlock.style.top = (top + rect.top) + 'px';
    }
    isDragging = false;
  }
  if (isRotating) {
    state.rotation = Math.round(liveRotation / 90) * 90;
    activeBlock.style.transform = `rotate(${state.rotation}deg)`;
    isRotating = false;
  }
  activeBlock = null;
  const validPositions = [[{ x: 0, y: 180 },{ x: 60, y: 120 },{ x: 120, y: 60 },{ x: 180, y: 0 }],[{ x: 0, y: 180 },{ x: 60, y: 120 },{ x: 120, y: 60 },{ x: 240, y: 60 }],[{ x: 0, y: 180 },{ x: 60, y: 120 },{ x: 120, y: 60 },{ x: 210, y: 30 }],[{ x: 0, y: 180 },{ x: 60, y: 120 },{ x: 180, y: 120 },{ x: 240, y: 60 }],[{ x: 0, y: 180 },{ x: 60, y: 120 },{ x: 180, y: 120 },{ x: 210, y: 30 }],[{ x: 0, y: 180 },{ x: 60, y: 120 },{ x: 180, y: 120 },{ x: 270, y: 90 }],[{ x: 0, y: 180 },{ x: 60, y: 120 },{ x: 90, y: 30 },{ x: 180, y: 0 }],[{ x: 0, y: 180 },{ x: 60, y: 120 },{ x: 150, y: 90 },{ x: 180, y: 0 }],[{ x: 0, y: 180 },{ x: 60, y: 120 },{ x: 150, y: 90 },{ x: 240, y: 60 }],[{ x: 0, y: 180 },{ x: 60, y: 120 },{ x: 150, y: 90 },{ x: 150, y: 90 }],[{ x: 0, y: 180 },{ x: 120, y: 180 },{ x: 180, y: 120 },{ x: 240, y: 60 }],[{ x: 0, y: 180 },{ x: 120, y: 180 },{ x: 180, y: 120 },{ x: 210, y: 30 }],[{ x: 0, y: 180 },{ x: 120, y: 180 },{ x: 180, y: 120 },{ x: 270, y: 90 }],[{ x: 0, y: 180 },{ x: 120, y: 180 },{ x: 240, y: 180 },{ x: 270, y: 90 }],[{ x: 0, y: 180 },{ x: 120, y: 180 },{ x: 150, y: 90 },{ x: 180, y: 0 }],[{ x: 0, y: 180 },{ x: 120, y: 180 },{ x: 150, y: 90 },{ x: 240, y: 60 }],[{ x: 0, y: 180 },{ x: 120, y: 180 },{ x: 150, y: 90 },{ x: 210, y: 30 }],[{ x: 0, y: 180 },{ x: 120, y: 180 },{ x: 210, y: 150 },{ x: 240, y: 60 }],[{ x: 0, y: 180 },{ x: 120, y: 180 },{ x: 210, y: 150 },{ x: 210, y: 30 }],[{ x: 0, y: 180 },{ x: 120, y: 180 },{ x: 210, y: 150 },{ x: 270, y: 90 }],[{ x: 0, y: 180 },{ x: 30, y: 90 },{ x: 60, y: 0 },{ x: 180, y: 0 }],[{ x: 0, y: 180 },{ x: 30, y: 90 },{ x: 120, y: 60 },{ x: 180, y: 0 }],[{ x: 0, y: 180 },{ x: 30, y: 90 },{ x: 120, y: 60 },{ x: 240, y: 60 }],[{ x: 0, y: 180 },{ x: 30, y: 90 },{ x: 120, y: 60 },{ x: 210, y: 30 }],[{ x: 0, y: 180 },{ x: 30, y: 90 },{ x: 90, y: 30 },{ x: 180, y: 0 }],[{ x: 0, y: 180 },{ x: 90, y: 150 },{ x: 120, y: 60 },{ x: 180, y: 0 }],[{ x: 0, y: 180 },{ x: 90, y: 150 },{ x: 120, y: 60 },{ x: 240, y: 60 }],[{ x: 0, y: 180 },{ x: 90, y: 150 },{ x: 120, y: 60 },{ x: 90, y: 150 }],[{ x: 0, y: 180 },{ x: 90, y: 150 },{ x: 180, y: 120 },{ x: 240, y: 60 }],[{ x: 0, y: 180 },{ x: 90, y: 150 },{ x: 180, y: 120 },{ x: 210, y: 30 }],[{ x: 0, y: 180 },{ x: 90, y: 150 },{ x: 180, y: 120 },{ x: 270, y: 90 }],[{ x: 0, y: 180 },{ x: 90, y: 150 },{ x: 90, y: 30 },{ x: 180, y: 0 }],[{ x: 0, y: 180 },{ x: 90, y: 150 },{ x: 150, y: 90 },{ x: 180, y: 0 }],[{ x: 0, y: 180 },{ x: 90, y: 150 },{ x: 150, y: 90 },{ x: 240, y: 60 }],[{ x: 0, y: 180 },{ x: 90, y: 150 },{ x: 150, y: 90 },{ x: 210, y: 30 }],[{ x: 60, y: 240 },{ x: 120, y: 180 },{ x: 180, y: 120 },{ x: 240, y: 60 }],[{ x: 60, y: 240 },{ x: 120, y: 180 },{ x: 180, y: 120 },{ x: 210, y: 30 }],[{ x: 60, y: 240 },{ x: 120, y: 180 },{ x: 180, y: 120 },{ x: 270, y: 90 }],[{ x: 60, y: 240 },{ x: 120, y: 180 },{ x: 240, y: 180 },{ x: 270, y: 90 }],[{ x: 60, y: 240 },{ x: 120, y: 180 },{ x: 150, y: 90 },{ x: 180, y: 0 }],[{ x: 60, y: 240 },{ x: 120, y: 180 },{ x: 150, y: 90 },{ x: 240, y: 60 }],[{ x: 60, y: 240 },{ x: 120, y: 180 },{ x: 150, y: 90 },{ x: 210, y: 30 }],[{ x: 60, y: 240 },{ x: 120, y: 180 },{ x: 210, y: 150 },{ x: 240, y: 60 }],[{ x: 60, y: 240 },{ x: 120, y: 180 },{ x: 210, y: 150 },{ x: 210, y: 30 }],[{ x: 60, y: 240 },{ x: 120, y: 180 },{ x: 210, y: 150 },{ x: 270, y: 90 }],[{ x: 60, y: 240 },{ x: 180, y: 240 },{ x: 240, y: 180 },{ x: 270, y: 90 }],[{ x: 60, y: 240 },{ x: 180, y: 240 },{ x: 210, y: 150 },{ x: 240, y: 60 }],[{ x: 60, y: 240 },{ x: 180, y: 240 },{ x: 210, y: 150 },{ x: 210, y: 30 }],[{ x: 60, y: 240 },{ x: 180, y: 240 },{ x: 210, y: 150 },{ x: 270, y: 90 }],[{ x: 60, y: 240 },{ x: 180, y: 240 },{ x: 270, y: 210 },{ x: 270, y: 90 }],[{ x: 60, y: 240 },{ x: 90, y: 150 },{ x: 120, y: 60 },{ x: 180, y: 0 }],[{ x: 60, y: 240 },{ x: 90, y: 150 },{ x: 120, y: 60 },{ x: 240, y: 60 }],[{ x: 60, y: 240 },{ x: 90, y: 150 },{ x: 120, y: 60 },{ x: 210, y: 30 }],[{ x: 60, y: 240 },{ x: 90, y: 150 },{ x: 180, y: 120 },{ x: 240, y: 60 }],[{ x: 60, y: 240 },{ x: 90, y: 150 },{ x: 180, y: 120 },{ x: 210, y: 30 }],[{ x: 60, y: 240 },{ x: 90, y: 150 },{ x: 180, y: 120 },{ x: 270, y: 90 }],[{ x: 60, y: 240 },{ x: 90, y: 150 },{ x: 90, y: 30 },{ x: 180, y: 0 }],[{ x: 60, y: 240 },{ x: 90, y: 150 },{ x: 150, y: 90 },{ x: 180, y: 0 }],[{ x: 60, y: 240 },{ x: 90, y: 150 },{ x: 150, y: 90 },{ x: 240, y: 60 }],[{ x: 60, y: 240 },{ x: 90, y: 150 },{ x: 150, y: 90 },{ x: 210, y: 30 }],[{ x: 60, y: 240 },{ x: 150, y: 210 },{ x: 180, y: 120 },{ x: 240, y: 60 }],[{ x: 60, y: 240 },{ x: 150, y: 210 },{ x: 180, y: 120 },{ x: 210, y: 30 }],[{ x: 60, y: 240 },{ x: 150, y: 210 },{ x: 180, y: 120 },{ x: 270, y: 90 }],[{ x: 60, y: 240 },{ x: 150, y: 210 },{ x: 240, y: 180 },{ x: 270, y: 90 }],[{ x: 60, y: 240 },{ x: 150, y: 210 },{ x: 150, y: 90 },{ x: 180, y: 0 }],[{ x: 60, y: 240 },{ x: 150, y: 210 },{ x: 150, y: 90 },{ x: 240, y: 60 }],[{ x: 60, y: 240 },{ x: 150, y: 210 },{ x: 150, y: 90 },{ x: 210, y: 30 }],[{ x: 60, y: 240 },{ x: 150, y: 210 },{ x: 210, y: 150 },{ x: 240, y: 60 }],[{ x: 60, y: 240 },{ x: 150, y: 210 },{ x: 210, y: 150 },{ x: 210, y: 30 }],[{ x: 60, y: 240 },{ x: 150, y: 210 },{ x: 210, y: 150 },{ x: 270, y: 90 }],[{ x: -30, y: 150 },{ x: 0, y: 60 },{ x: 60, y: 0 },{ x: 180, y: 0 }],[{ x: -30, y: 150 },{ x: 0, y: 60 },{ x: 120, y: 60 },{ x: 180, y: 0 }],[{ x: -30, y: 150 },{ x: 0, y: 60 },{ x: 120, y: 60 },{ x: 240, y: 60 }],[{ x: -30, y: 150 },{ x: 0, y: 60 },{ x: 120, y: 60 },{ x: 210, y: 30 }],[{ x: -30, y: 150 },{ x: 0, y: 60 },{ x: 90, y: 30 },{ x: 180, y: 0 }],[{ x: -30, y: 150 },{ x: 60, y: 120 },{ x: 120, y: 60 },{ x: 180, y: 0 }],[{ x: -30, y: 150 },{ x: 60, y: 120 },{ x: 120, y: 60 },{ x: 240, y: 60 }],[{ x: -30, y: 150 },{ x: 60, y: 120 },{ x: 120, y: 60 },{ x: 210, y: 30 }],[{ x: -30, y: 150 },{ x: 60, y: 120 },{ x: 180, y: 120 },{ x: 240, y: 60 }],[{ x: -30, y: 150 },{ x: 60, y: 120 },{ x: 180, y: 120 },{ x: 210, y: 30 }],[{ x: -30, y: 150 },{ x: 60, y: 120 },{ x: 180, y: 120 },{ x: 270, y: 90 }],[{ x: -30, y: 150 },{ x: 60, y: 120 },{ x: 90, y: 30 },{ x: 180, y: 0 }],[{ x: -30, y: 150 },{ x: 60, y: 120 },{ x: 150, y: 90 },{ x: 180, y: 0 }],[{ x: -30, y: 150 },{ x: 60, y: 120 },{ x: 150, y: 90 },{ x: 240, y: 60 }],[{ x: -30, y: 150 },{ x: 60, y: 120 },{ x: 150, y: 90 },{ x: 210, y: 30 }],[{ x: -30, y: 150 },{ x: -30, y: 30 },{ x: 60, y: 0 },{ x: 180, y: 0 }],[{ x: -30, y: 150 },{ x: 30, y: 90 },{ x: 60, y: 0 },{ x: 180, y: 0 }],[{ x: -30, y: 150 },{ x: 30, y: 90 },{ x: 120, y: 60 },{ x: 180, y: 0 }],[{ x: -30, y: 150 },{ x: 30, y: 90 },{ x: 120, y: 60 },{ x: 240, y: 60 }],[{ x: -30, y: 150 },{ x: 30, y: 90 },{ x: 120, y: 60 },{ x: 210, y: 30 }],[{ x: -30, y: 150 },{ x: 30, y: 90 },{ x: 90, y: 30 },{ x: 180, y: 0 }],[{ x: 30, y: 210 },{ x: 60, y: 120 },{ x: 120, y: 60 },{ x: 180, y: 0 }],[{ x: 30, y: 210 },{ x: 60, y: 120 },{ x: 120, y: 60 },{ x: 240, y: 60 }],[{ x: 30, y: 210 },{ x: 60, y: 120 },{ x: 120, y: 60 },{ x: 210, y: 30 }],[{ x: 30, y: 210 },{ x: 60, y: 120 },{ x: 180, y: 120 },{ x: 240, y: 60 }],[{ x: 30, y: 210 },{ x: 60, y: 120 },{ x: 180, y: 120 },{ x: 210, y: 30 }],[{ x: 30, y: 210 },{ x: 60, y: 120 },{ x: 180, y: 120 },{ x: 270, y: 90 }],[{ x: 30, y: 210 },{ x: 60, y: 120 },{ x: 90, y: 30 },{ x: 180, y: 0 }],[{ x: 30, y: 210 },{ x: 60, y: 120 },{ x: 90, y: 30 },{ x: 180, y: 0 }],[{ x: 30, y: 210 },{ x: 60, y: 120 },{ x: 150, y: 90 },{ x: 180, y: 0 }],[{ x: 30, y: 210 },{ x: 60, y: 120 },{ x: 150, y: 90 },{ x: 240, y: 60 }],[{ x: 30, y: 210 },{ x: 60, y: 120 },{ x: 150, y: 90 },{ x: 210, y: 30 }],[{ x: 30, y: 210 },{ x: 120, y: 180 },{ x: 180, y: 120 },{ x: 240, y: 60 }],[{ x: 30, y: 210 },{ x: 120, y: 180 },{ x: 180, y: 120 },{ x: 210, y: 30 }],[{ x: 30, y: 210 },{ x: 120, y: 180 },{ x: 180, y: 120 },{ x: 270, y: 90 }],[{ x: 30, y: 210 },{ x: 120, y: 180 },{ x: 240, y: 180 },{ x: 270, y: 90 }],[{ x: 30, y: 210 },{ x: 120, y: 180 },{ x: 240, y: 180 },{ x: 270, y: 90 }],[{ x: 30, y: 210 },{ x: 120, y: 180 },{ x: 240, y: 180 },{ x: 270, y: 90 }],[{ x: 30, y: 210 },{ x: 120, y: 180 },{ x: 150, y: 90 },{ x: 180, y: 0 }],[{ x: 30, y: 210 },{ x: 120, y: 180 },{ x: 150, y: 90 },{ x: 240, y: 60 }],[{ x: 30, y: 210 },{ x: 120, y: 180 },{ x: 150, y: 90 },{ x: 210, y: 30 }],[{ x: 30, y: 210 },{ x: 120, y: 180 },{ x: 210, y: 150 },{ x: 240, y: 60 }],[{ x: 30, y: 210 },{ x: 120, y: 180 },{ x: 210, y: 150 },{ x: 210, y: 30 }],[{ x: 30, y: 210 },{ x: 120, y: 180 },{ x: 210, y: 150 },{ x: 270, y: 90 }],[{ x: 30, y: 210 },{ x: 30, y: 90 },{ x: 60, y: 0 },{ x: 180, y: 0 }],[{ x: 30, y: 210 },{ x: 30, y: 90 },{ x: 120, y: 60 },{ x: 180, y: 0 }],[{ x: 30, y: 210 },{ x: 30, y: 90 },{ x: 120, y: 60 },{ x: 240, y: 60 }],[{ x: 30, y: 210 },{ x: 30, y: 90 },{ x: 120, y: 60 },{ x: 210, y: 30 }],[{ x: 30, y: 210 },{ x: 30, y: 90 },{ x: 90, y: 30 },{ x: 180, y: 0 }],[{ x: 30, y: 210 },{ x: 90, y: 150 },{ x: 120, y: 60 },{ x: 180, y: 0 }],[{ x: 30, y: 210 },{ x: 90, y: 150 },{ x: 120, y: 60 },{ x: 240, y: 60 }],[{ x: 30, y: 210 },{ x: 90, y: 150 },{ x: 120, y: 60 },{ x: 210, y: 30 }],[{ x: 30, y: 210 },{ x: 90, y: 150 },{ x: 180, y: 120 },{ x: 240, y: 60 }],[{ x: 30, y: 210 },{ x: 90, y: 150 },{ x: 180, y: 120 },{ x: 210, y: 30 }],[{ x: 30, y: 210 },{ x: 90, y: 150 },{ x: 180, y: 120 },{ x: 270, y: 90 }],[{ x: 30, y: 210 },{ x: 90, y: 150 },{ x: 90, y: 30 },{ x: 180, y: 0 }],[{ x: 30, y: 210 },{ x: 90, y: 150 },{ x: 150, y: 90 },{ x: 180, y: 0 }],[{ x: 30, y: 210 },{ x: 90, y: 150 },{ x: 150, y: 90 },{ x: 240, y: 60 }],[{ x: 30, y: 210 },{ x: 90, y: 150 },{ x: 150, y: 90 },{ x: 210, y: 30 }]];
  const grid = document.getElementById("grid");
  const rect = grid.getBoundingClientRect();
  const blocks = Array.from(document.querySelectorAll(".block"))
  .filter(b => {
      if (!b.style.left || !b.style.top) return false;
      const bx = parseFloat(b.style.left) + b.offsetWidth / 2;
      const by = parseFloat(b.style.top) + b.offsetHeight / 2;
      return (
        bx >= rect.left &&
        bx <= rect.right &&
        by >= rect.top &&
        by <= rect.bottom
      );
    })
    .map(b => {
      const bx = parseFloat(b.style.left) - rect.left;
      const by = parseFloat(b.style.top) - rect.top;
      return { id: b.id, x: bx, y: by };
    });
    console.log("blockref:", blockref);
    console.log("blocks:", blocks);
    const divd = blockref.map(n => `block${n / 31}`);
    const usedIds = blocks.map(b => b.id);
    if (divd.every(id => usedIds.includes(id)) && usedIds.length === divd.length) {
    console.log("✅ Correct blocks used");
    const testCoords = divd.map(blockId => {
	const match = blocks.find(b => b.id === blockId);
	return match ? { x: Math.round(match.x), y: Math.round(match.y) } : null;
	});
	// console.log("testCoords (which is blocks but in the order of the sol Py provided):", testCoords);
	const isValidPosition = validPositions.some(validSet =>
	validSet.every((pos, i) =>
	pos.x === testCoords[i].x && pos.y === testCoords[i].y
	)
	);
	if (isValidPosition) {
    divd.forEach(id => document.getElementById(id)?.classList.add("slvd"));
    }
    } else {
    console.log("❌ Missing or incorrect blocks");
    }
}
document.addEventListener('mouseup', handleEnd);
document.addEventListener('touchend', handleEnd);



</script>

"""




if "show_text" not in st.session_state:
    st.session_state.show_text = True

if "round_html" not in st.session_state:
    st.session_state.round_html = ""

if st.button("New game"):
        st.session_state.show_text = False
        st.session_state.round_html = render_round()  # <-- YOUR FUNCTION

# --- Display game (HTML blocks) ---
if st.session_state.round_html:
    components.html(st.session_state.round_html, height=582)
                
if st.session_state.show_text:
    st.title("💡 Welcome to the game!")
    st.write("Make your way across the board from left to right by placing the dominoes in a line. Copyright (c) 2025 Chris Lilly")