let ARR = []

function getTreeDatas(data) {
    data.forEach(element => {
        if (element.child.length > 0) {
            getTreeDatas(element.child)
        }
        ARR.push({
            id: element.id,
            name: element.name
        });
    });
}

/*
let sample_data = [{
        id: 1,
        name: "askkrr",
        child: [{
                id: 2,
                name: "hkdeim",
                child: [{
                    id: 3,
                    name: "aigmzk",
                    child: []
                }]
            },
            {
                id: 4,
                name: "gimic",
                child: []
            }
        ]
    },
    {
        id: 11,
        name: "askkrrb",
        child: []
    }
]
*/
export function getTreeList(data) {
    ARR = []
    getTreeDatas(data)
    return ARR
}



export function treeDataAdd(id, treeobjectJson, childObjectData) {

    console.log("treeDataAddメソッド↓")
    console.log(childObjectData)
    console.log(JSON.parse(treeobjectJson));


    let obj = JSON.parse(treeobjectJson);
    obj.forEach(element => {
        if (element.id == id) {
            element.child.push(childObjectData)
        } else {
            if (element.child.length > 0) {
                const json = JSON.stringify(element.child)
                element.child = treeDataAdd(id, json, childObjectData)
            }
        }
    });

    console.log(obj);
    console.log("treeDataAddメソッド↑")

    return obj
}
