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
    console.log("validation started");
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
    valid_positions_1 = {(0, 180), (60, 240), (-30, 150), (30, 210)}
    valid_positions_2 = {(180, 0), (240, 60), (210, 30), (270, 90)}
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
<style>.stTextArea { display: none; }</style>
""", unsafe_allow_html=True)

data_json = st.text_area("Hidden Data", value="", key="hidden_data", label_visibility="collapsed", height=50)

         
            
            

html_code = """
<style>
body { padding: 0px; margin: 0px; font-family: sans-serif; }
.grid-container { display: grid; grid-template-columns: repeat(6, 60px); grid-template-rows: repeat(5, 60px); width: max-content; }
.grid-cell { width: 60px; height: 60px; background-color: #eee; border: 1px solid #ccc; box-sizing: border-box; position: relative; }
.draggable { width: 120px; height: 60px; background-color: #2E2E2E; cursor: grab; position: absolute; z-index: 10; border-radius: 7px; user-select: none; transition: transform-origin: center center; transform 0.25s ease; }
.rotate-handle { width: 19px; height: 19px; background: none; position: absolute; cursor: pointer; z-index: 20; }
.top-left { top: 0px; left: 0px; }
.top-right { top: 0px; right: 0px; }
.bottom-left { bottom: 0px; left: 0px; }
.bottom-right { bottom: 0px; right: 0px; }
.wrd { color: #ffffff; font-size: 13.5px; position: absolute; top: 50%; width: 49%; text-align: center; text-anchor: middle; line-height: 0px; }
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
    console.log("drag start fired");
    if (isRotating) return;
    isDragging = true;
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
    dragOffset.x = clientX - (rect.left + rect.width / 2);
    dragOffset.y = clientY - (rect.top + rect.height / 2);
  };
  block.addEventListener('mousedown', handleDragStart);
  block.addEventListener('touchstart', handleDragStart, { passive: false });
});

// Mouse move: handle drag or rotation
function handleMove(e) {
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
  // Update hidden Streamlit textarea with JSON string
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
	console.log("Updating textarea");
	const wrapper = window.parent.document.querySelector('div[data-testid="stTextArea"]');
	const streamlitTextarea = wrapper ? wrapper.querySelector('textarea') : null;
	if(streamlitTextarea) {
      streamlitTextarea.value = JSON.stringify(blocks);
      streamlitTextarea.dispatchEvent(new Event('input', { bubbles: true }));
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

# --- Layout: Buttons side by side ---
col1, spacer, col2 = st.columns([1, 4, 1])  # Spacer pushes col2 to the right

with col1:
    if st.button("New game"):
        st.session_state.show_text = False
        st.session_state.round_html = render_round()  # <-- YOUR FUNCTION

with col2:
    if st.button("Submit"):
        if data_json:
            try:
                payload = json.loads(data_json)
                result = validate_layout(payload)
                if result["success"]:
                    st.success("✅ Correct!")
                else:
                    st.error("❌ Incorrect")
            except Exception as e:
                st.error(f"Invalid JSON data: {e}")

# --- Display game (HTML blocks) ---
if st.session_state.round_html:
    components.html(st.session_state.round_html, height=582)
                
if st.session_state.show_text:
    st.title("💡 Welcome to the game!")
    st.write("Make your way across the board from left to right by dragging and dropping the dominoes.")