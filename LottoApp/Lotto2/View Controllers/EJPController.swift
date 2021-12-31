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
    
    func allTogether(_ SetEuroJackPot:Set<Int>, _ Scope:ClosedRange<Int>) -> (Set<Int>){

        func iterateAndRemove2() -> (Set<Int>, Set<Int>){
        
            var numbers = SetEuroJackPot
            let euroJackPotScope = Scope
        
            var results = Set<Int>()
        
            for _ in euroJackPotScope{
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
        
        let finalResultMain = allTogether(Set(1...50), 1...5)
        let finalResultSecondary = allTogether(Set(1...10), 1...2)

        let euroJackPotStringMain = finalResultMain.map(String.init).joined(separator: ", ")
        let euroJackPotStringSecondary = finalResultSecondary.map(String.init).joined(separator: ", ")

        finalResults = [euroJackPotStringMain, euroJackPotStringSecondary]
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
        
    
