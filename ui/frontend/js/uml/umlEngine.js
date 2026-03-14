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

  function renderDetails(nodeId,mode){
    if (!contentEl) return

    const node = (GRAPH_DATA.nodes || []).find(n => n.id === nodeId)
    const structure = GRAPH_DATA.structure || {}

    const fileInfo = structure[nodeId] || {}

    const layer = fileInfo.layer || fileInfo.type || "Unknown layer"
    const imports = fileInfo.imports || []
    const exports = fileInfo.exports || []

    const modeLabel = mode === "preview" ? "Preview" : "Selected"

    titleEl.textContent = nodeId

    let html = ""
    html += '<div class="sectionTitle">'+modeLabel+' node</div>'
    html += "<div>"+layer+"</div>"

    if (imports.length){
      html += '<div class="sectionTitle">Imports</div>'
      html += "<code>"+imports.join("\\n")+"</code>"
    }

    if (exports.length){
      html += '<div class="sectionTitle">Exports</div>'
      html += "<code>"+exports.join("\\n")+"</code>"
    }

    if (!imports.length && !exports.length){
      html += '<p class="placeholder">No additional metadata is available for this node.</p>'
    }

    contentEl.innerHTML = html
  }

  function showNodeDetails(nodeId){
    renderDetails(nodeId,"selected")
    ensureOpen()
  }

  function previewNode(nodeId){
    // only update text, don't force panel visible if user hid it
    if (!panel.classList.contains("visible")) return
    renderDetails(nodeId,"preview")
  }

  function clearPreview(){
    // no-op for now to keep last context
  }

  return {
    showNodeDetails,
    previewNode,
    clearPreview
  }
})()