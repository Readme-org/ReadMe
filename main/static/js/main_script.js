document.getElementById("searchBtn").addEventListener("click", function() {
  let query = document.getElementById("searchInput").value;
  if(query) {
      alert('Mencari: ' + query);
  }
});