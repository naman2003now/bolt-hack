import output from './output.json' assert {type: 'json'};

var table = document.getElementById("table")

function gen_table_row(device_report){
    var row = document.createElement("tr")
    
    var device_name = document.createElement("td")
    device_name.innerHTML = device_report.hostname
    row.appendChild(device_name)
    
    var risk = document.createElement("td")
    risk.classList.add(device_report.risk)
    row.appendChild(risk)
     
    var report_url = document.createElement("td")
    report_url.innerHTML = `<a href="${device_report.report_url}">${device_report.report_url}</a>`
    row.appendChild(report_url)
     
    var timestamp = document.createElement("td")
    timestamp.innerHTML = device_report.timestamp
    row.appendChild(timestamp)
     
    return row
}

output.map((device_report) => {
    table.appendChild(gen_table_row(device_report))
}) 