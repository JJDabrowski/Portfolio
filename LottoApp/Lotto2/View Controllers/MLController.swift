//
//  MLController.swift
//  Lotto2
//
//  Created by Swantewit on 18/09/2021.
//

import UIKit

class SmallLottoController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }
    
    /* Couldn't fix the shortened names here fast, was getting errors on AppDelegate*/
    
    @IBOutlet weak var mlResult: UILabel!
    
    func iterateAndRemove() -> (Set<Int>, Set<Int>){
        var numbers = Set<Int>(1...42)
        var results = Set<Int>()
        for _ in 1...5{
            let randomNumber = numbers.randomElement()!
            results.insert(randomNumber)
            numbers.remove(randomNumber)
        }
    return (numbers, results)
    }
    
    
    @IBAction func mlRand(_ sender: Any) {
        
        let functionRun = iterateAndRemove()
        let functionResult = functionRun.1
        
        let smallLottoString = functionResult.map(String.init).joined(separator: ", ")
        
        mlResult.text = smallLottoString
    }
    
    
    @IBAction func switchViews(_ sender: UIButton){
    }
    
    /* Couldn't fix the polish name here fast; was getting error*/
    
    @IBAction func wroc(_ sender: Any) {
    }
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
