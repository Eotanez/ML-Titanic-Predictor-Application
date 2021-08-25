d3.csv('data/test.csv').then( function(mData){
 
    
    d3.select("tbody")
    .selectAll("tr")
    .data(mData)
    .enter()
    .append("tr")
     .html(function(d) {
        return `<td>${d.PassengerId}</td><td>${d.Name}</td><td>${d.Sex}</td><td>${d.Age}</td><td>${d.Ticket}</td><td>${d.Fare}</td><td>${d.Embarked}</td>`;
    });

    var data = mData;

    var tbody = d3.select("tbody");
   
    var columns = ["PassengerId", "Name", "Sex", "Age", "Ticket", "Fare","Embarked"]

    var populate = (dataInput) => {

        dataInput.forEach(valOf => {
            var row = tbody.append("tr");
            columns.forEach(column => row.append("td").text(valOf[column])
            )
        });
    }
});

