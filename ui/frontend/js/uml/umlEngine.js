window.UML = (function(){
  const panel = document.getElementById("umlPanel")
  const titleEl = document.getElementById("umlTitle")
  const contentEl = document.getElementById("umlContent")
  const closeBtn = document.getElementById("umlClose")

  if (closeBtn && panel){
    closeBtn.onclick = function(){
      panel.classList.remove("visible")
    }
  }

  function ensureOpen(){
    if (!panel) return
    panel.classList.add("visible")
  }

  function renderDetails(nodeId, mode){
    if (!contentEl) return

    const node = (GRAPH_DATA.nodes || []).find(n => n.id === nodeId)
    const uml = node.umlDetails || { classes: [] }
    
    titleEl.textContent = nodeId
    let html = `<div class="sectionTitle">${mode === "preview" ? "Previewing" : "Selected"} File</div>`

    if (uml.classes.length === 0) {
      html += '<p class="placeholder">No classes or methods detected in this file.</p>'
    } else {
      uml.classes.forEach(cls => {
        html += `
          <div style="border: 1px solid #475569; margin-bottom: 15px; background: #1e293b;">
            <div style="background: #334155; padding: 5px; text-align: center; border-bottom: 1px solid #475569;">
              <b>${cls.name}</b>
            </div>
            <div style="padding: 5px; font-size: 0.85em; color: #cbd5e1; border-bottom: 1px dashed #475569;">
              ${cls.attributes.map(attr => `<div>+ ${attr}</div>`).join("") || "<i>(no attributes)</i>"}
            </div>
            <div style="padding: 5px; font-size: 0.85em; color: #fbbf24;">
              ${cls.methods.map(m => `<div>+ ${m}()</div>`).join("") || "<i>(no methods)</i>"}
            </div>
          </div>
        `
      })
    }

    contentEl.innerHTML = html
  }

  function showNodeDetails(nodeId){
    renderDetails(nodeId, "selected")
    ensureOpen()
  }

  function previewNode(nodeId){
    if (!panel.classList.contains("visible")) return
    renderDetails(nodeId, "preview")
  }

  function clearPreview(){
    // Keeping content to avoid flickering
  }

  return {
    showNodeDetails,
    previewNode,
    clearPreview
  }
})()