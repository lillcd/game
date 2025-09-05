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
        "word_pairs": [("Sonic","Leg"),("Pass","Hell's"),("For","Fifty"),("Doctor","French"),("MBE","Port"),("Abroad","Guest"),("Lizard","Albert"),("Counter","Under"),("Greek","Double")],
        "correct_blocks": ["block7","block2","block8","block6"],
        "start_word": "Airport",
        "end_word":   "Eyes",
    }
}





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
    return new_html





def validate_layout(payload):
    blocks = payload.get("blocks", [])
    block_ids = {b["id"] for b in blocks}
    required = rounds[current_round]['correct_blocks']
    # ✅ check correct set of blocks
    if set(block_ids) != set(required):
      st.write("❌ Incorrect")
      # print(required)
      # print(block_ids)
      missing = required - block_ids
      extras = block_ids - required
      # if missing: print("Missing:", ", ".join(sorted(missing)))
      # if extras:  print("Extra:",   ", ".join(sorted(extras)))
      return {"success": False}
    # valid positions
    valid_positions_1 = {(0, 240), (80, 320), (-40, 200), (40, 280)}
    valid_positions_2 = {(240, 0), (320, 80), (280, 40), (360, 120)}
    coords = {b["id"]: (b["x"], b["y"]) for b in blocks}
    key1 = coords.get(rounds[current_round]['correct_blocks'][0])
    key2 = coords.get(rounds[current_round]['correct_blocks'][-1])
    if key1 in valid_positions_1 and key2 in valid_positions_2:
        st.write("✅ Correct!")
        return {"success": True}
    else:
        st.write("❌ Incorrect")
        # print(key1)
        return {"success": False}



# Hidden text_area to receive data from JS
st.markdown("""
<style>
.stTextArea { display: none; }
</style>
""", unsafe_allow_html=True)

data_json = st.text_area("Hidden Data", value="", key="hidden_data", label_visibility="collapsed", height=50)

         
            
            

html_code = """
<style>
body { padding: 0px; margin: 0px; font-family: sans-serif; }
.grid-container { display: grid; grid-template-columns: repeat(6, 80px); grid-template-rows: repeat(5, 80px); width: max-content; }
.grid-cell { width: 80px; height: 80px; background-color: #eee; border: 1px solid #ccc; box-sizing: border-box; position: relative; }
.draggable { width: 160px; height: 80px; background-color: #2E2E2E; cursor: grab; position: absolute; z-index: 10; border-radius: 7px; user-select: none; transition: transform-origin: center center; transform 0.25s ease; }
.rotate-handle { width: 16px; height: 16px; background: none; position: absolute; cursor: pointer; z-index: 20; }
.top-left { top: 0px; left: 0px; }
.top-right { top: 0px; right: 0px; }
.bottom-left { bottom: 0px; left: 0px; }
.bottom-right { bottom: 0px; right: 0px; }
.wrd { color: #ffffff; font-size: 16px; position: absolute; top: 50%; width: 49%; text-align: center; text-anchor: middle; line-height: 0px; }
.lwrd { left: 0; }
.rwrd { right: 0; }
#arena { width: 100%; height: 820px; }
#block1 { transform: rotate(9deg); top: 425px; left: 65px; }
#block2 { transform: rotate(-7deg); top: 420px; left: 300px; }
#block3 { transform: rotate(-5deg); top: 515px; left: 4px; }
#block4 { transform: rotate(-44deg); top: 535px; left: 158px; }
#block5 { transform: rotate(2deg); top: 525px; left: 320px; }
#block6 { transform: rotate(-1deg); top: 635px; left: 20px; }
#block7 { transform: rotate(18deg); top: 625px; left: 320px; }
#block8 { transform: rotate(6deg); top: 730px; left: 55px; }
#block9 { transform: rotate(26deg); top: 690px; left: 220px; }
.dvdr { position: absolute; background-color: #ffffff; height: 72px; top: 4px; left: 78px; width: 2px; }
.strtfnsh { position: absolute; width: 80px; height: 80px; background-color: #2E2E2E; }
#strt { left: 0px; top: 320px; border-radius: 0px 7px 7px 0px; }
#fnsh { left: 400px; top: 0px; border-radius: 7px 0px 0px 7px; }
.strtfnsh .wrd { width: 100% !important; }
#submitBtn { width: 80px; position: absolute; left: 200px; top: 405px; }
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
const grid = document.getElementById('grid');
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
    handle.addEventListener('mousedown', (e) => {
      e.preventDefault();
      isRotating = true;
      activeBlock = block;
      const rect = block.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;
      const dx = e.clientX - centerX;
      const dy = e.clientY - centerY;
      rotationStartAngle = Math.atan2(dy, dx) * (180 / Math.PI);
      if (rotationStartAngle < 0) rotationStartAngle += 360;
    });
  });
// Dragging
  block.addEventListener('mousedown', (e) => {
    console.log("mousedown fired");
    if (isRotating) return;
    isDragging = true;
    activeBlock = block;
    const rect = block.getBoundingClientRect();
    dragOffset.x = e.clientX - (rect.left + rect.width / 2);
    dragOffset.y = e.clientY - (rect.top + rect.height / 2);
    e.preventDefault();
  });
});

// Mouse move: handle drag or rotation
document.addEventListener('mousemove', (e) => {
  if (!activeBlock) return;
  if (isRotating) {
    const rect = activeBlock.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;
    const dx = e.clientX - centerX;
    const dy = e.clientY - centerY;
    let currentAngle = Math.atan2(dy, dx) * (180 / Math.PI);
    if (currentAngle < 0) currentAngle += 360;
    let angleDiff = currentAngle - rotationStartAngle;
    const { rotation } = blockState.get(activeBlock);
    liveRotation = (rotation + angleDiff + 360) % 360;
    activeBlock.style.transform = `rotate(${liveRotation}deg)`;
  } else if (isDragging) {
    const rect = grid.getBoundingClientRect();
    const newCenterX = e.clientX - dragOffset.x;
    const newCenterY = e.clientY - dragOffset.y;
    const width = activeBlock.offsetWidth;
    const height = activeBlock.offsetHeight;
    const x = newCenterX - width / 2 - rect.left;
    const y = newCenterY - height / 2 - rect.top;
    const { rotation } = blockState.get(activeBlock);
    activeBlock.style.left = x + 'px';
    activeBlock.style.top = y + 'px';
    activeBlock.style.transform = `rotate(${rotation}deg)`;
  }
});

// Mouse up: snap and finalize rotation
document.addEventListener('mouseup', () => {
  console.log("mouseup fired");
  if (!activeBlock) return;
  const state = blockState.get(activeBlock);
  if (isDragging) {
    const rect = grid.getBoundingClientRect();
    const cellSize = 80;
    let rot = state.rotation % 360;
    if (rot < 0) rot += 360;
    let left = parseFloat(activeBlock.style.left) - rect.left || 0;
    let top = parseFloat(activeBlock.style.top) - rect.top || 0;
    let offsetX = (rot === 90 || rot === 270) ? 40 : 0;
    let offsetY = (rot === 90 || rot === 270) ? 40 : 0;
    const blockWidth = rot % 180 === 0 ? activeBlock.offsetWidth : activeBlock.offsetHeight;
    const blockHeight = rot % 180 === 0 ? activeBlock.offsetHeight : activeBlock.offsetWidth;
    const maxX = grid.clientWidth - blockWidth;
    const maxY = (rot === 90 || rot === 270) ? grid.clientHeight - blockHeight + 80 : grid.clientHeight - blockHeight;
    const minY = (rot === 90 || rot === 270) ? 80 : 0;
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
  // Update hidden Streamlit textarea with JSON string
  const grid = document.getElementById("grid");
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
	const streamlitTextarea = window.parent.document.querySelector('textarea[data-testid="stTextArea"]');
	if(streamlitTextarea) {
      streamlitTextarea.value = JSON.stringify(blocks);
      streamlitTextarea.dispatchEvent(new Event('input', { bubbles: true }));
    }
});

</script>

"""




if "show_text" not in st.session_state:
    st.session_state.show_text = True

if st.session_state.show_text:
    st.title("💡 Welcome to the game!")
    st.write("Make your way across the board from left to right by dragging and dropping the dominoes.")
    
if st.button("New game"):
    st.session_state.show_text = False
    a_round = render_round()
    components.html(a_round, height=820)

    if st.button("Submit"):
        if data_json:
            try:
                payload = json.loads(data_json)
                validate_layout(payload)
            except Exception as e:
                st.error(f"Invalid JSON data: {e}")          