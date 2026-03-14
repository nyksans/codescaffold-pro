function initMinimap(){
  const miniContainer = document.getElementById("minimap")
  if (!miniContainer || !AppState.graph) return

  const miniNodes = new vis.DataSet(GRAPH_DATA.nodes)
  const miniEdges = new vis.DataSet(GRAPH_DATA.edges)

  const miniNetwork = new vis.Network(
    miniContainer,
    {nodes:miniNodes,edges:miniEdges},
    {
      physics:false,
      interaction:false
    }
  )

  AppState.minimap = miniNetwork

  const viewportEl = document.getElementById("minimapViewport")

  function updateViewport(){
    if (!viewportEl) return
    const rect = miniContainer.getBoundingClientRect()
    const scale = AppState.graph.getScale()

    // basic approximation: smaller scale => larger viewport rect
    const width = Math.max(40,Math.min(rect.width*0.8,180/scale))
    const height = Math.max(30,Math.min(rect.height*0.7,120/scale))

    viewportEl.style.width = width + "px"
    viewportEl.style.height = height + "px"

    const center = AppState.graph.getViewPosition()
    const normX = 0.5 + center.x/4500
    const normY = 0.5 + center.y/4500

    viewportEl.style.left = (rect.width*normX - width/2) + "px"
    viewportEl.style.top = (28 + rect.height*normY - height/2 - 14) + "px"
  }

  AppState.graph.on("dragEnd",updateViewport)
  AppState.graph.on("zoom",updateViewport)
  AppState.graph.on("afterDrawing",updateViewport)

  miniContainer.addEventListener("click",function(e){
    const rect = miniContainer.getBoundingClientRect()
    const x = (e.clientX-rect.left)/rect.width
    const y = (e.clientY-rect.top)/rect.height

    AppState.graph.moveTo({
      position:{
        x:(x-0.5)*4500,
        y:(y-0.5)*4500
      },
      animation:{duration:250,easing:"easeInOutQuad"}
    })

    updateViewport()
  })

  // initial fit for minimap
  miniNetwork.once("stabilizationIterationsDone",function(){
    miniNetwork.fit()
  })
}