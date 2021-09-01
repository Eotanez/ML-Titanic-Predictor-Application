console.log("Got this far");
function getParameterByName(name, url = window.location.href) {
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}




d3.csv('https://data-bootcamp-titanic.s3.us-east-2.amazonaws.com/train.csv').then(function(mData){
    var Name = getParameterByName('Name');
    var Gender = getParameterByName('Gender'); 
    var Age = getParameterByName('Age'); 
    var Sibsp = getParameterByName('Sibsp'); 
    var Parch = getParameterByName('Parch'); 
    var Cost = getParameterByName('Cost'); 
    var Class = getParameterByName('Class'); 

    var filteredData = mData.filter(function(d) 
    { 

            if( Name != null && Name != "")
            { 
                if ( d["Name"] != Name) { 
                    return false;
                }
            } 

            if( Gender != null && Gender != "")
            { 
                if ( d["Sex"] != Gender) { 
                    return false;
                }
            } 

            if( Age != null && Age != "")
            { 
                if ( d["Age"] != Age) { 
                    return false;
                }
            } 
            if( Sibsp != null && Sibsp != "")
            { 
                if ( d["SibSp"] != Sibsp) {
                    return false;
                }
            } 
         

             if( Parch != null && Parch != "")
            { 
                if ( d["Parch"] != Parch) {
                    return false;
                }
            } 

            if( Cost != null && Cost != "")
            { 
                if ( d["Fare"] != Cost) {
                    return false;
                }
            }
             if( Class != null && Class != "")
            { 
                if ( d["Pclass"] != Class) {
                    return false;
                }
            }  


         


            return d;

        });


    d3.select("tbody")
    .selectAll("tr")
    .data(filteredData)
    .enter()
    .append("tr")
     .html(function(d) {
        return `<td>${d.PassengerId}</td><td>${d.Name}</td><td>${d.Sex}</td><td>${d.Age}</td><td>${d.Ticket}</td><td>${d.Fare}</td><td>${d.Embarked}</td><td>${d.Survived}</td>`;
    });

    var data = filteredData;

    var tbody = d3.select("tbody");
   
    var columns = ["PassengerId", "Name", "Sex", "Age", "Ticket", "Fare","Embarked","Survived"]

    var populate = (dataInput) => {

        dataInput.forEach(valOf => {
            var row = tbody.append("tr");
            columns.forEach(column => row.append("td").text(valOf[column])
            )
        });
    }
});

