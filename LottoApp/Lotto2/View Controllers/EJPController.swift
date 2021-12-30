//
//  EJPController.swift
//  Lotto2
//
//  Created by Swantewit on 18/09/2021.
//

import UIKit

class EuroJackpotController: UIViewController {

    @IBOutlet var tableView: UITableView!
    
    var finalResults = [String]()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView.dataSource = self
        
        // Do any additional setup after loading the view.
    
    }
    
    func allTogether(_ SetB:Set<Int>, _ Scope:ClosedRange<Int>) -> (Set<Int>){

        func iterateAndRemove2() -> (Set<Int>, Set<Int>){
        
            var numbers = SetB
            let scope = Scope
        
            var results = Set<Int>()
        
            for _ in scope{
                let randomNumbers = numbers.randomElement()!
                results.insert(randomNumbers)
                numbers.remove(randomNumbers)
            }
        
            return (numbers, results)
        }

        let runFunction = iterateAndRemove2()
        let functionResult = runFunction.1

        return (functionResult)
    }
    
    @IBAction func euroJackpotRandomize(_ sender: Any) {
        
        let it = allTogether(Set(1...50), 1...5)
        let that = allTogether(Set(1...10), 1...2)

        let euJpStrngM = it.map(String.init).joined(separator: ", ")
        let euJpStrngS = that.map(String.init).joined(separator: ", ")

        finalResults = [euJpStrngM, euJpStrngS]
        tableView.reloadData()
    
    }
    
    
}

extension EuroJackpotController: UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return finalResults.count
    }
        
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) ->UITableViewCell {
        let cell  = tableView.dequeueReusableCell(withIdentifier: "cell", for: indexPath)
        
        cell.textLabel?.textAlignment = .center
        cell.textLabel?.text = finalResults[indexPath.row]
        
        
        return cell
    }
    
}
        
    
