//
//  DLController.swift
//  Lotto2
//
//  Created by Swantewit on 18/09/2021.
//

import UIKit

class BigLottoController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
        
    }
    
    @IBOutlet weak var bigLottoResult: UILabel!
    
    //A function to randomize the X numbers from Y set
    
    func iterateAndRemove() -> (Set<Int>, Set<Int>){
        var numbers = Set<Int>(1...49)
        var results = Set<Int>()
        for _ in 1...6{
            let randomNumbers = numbers.randomElement()!
            results.insert(randomNumbers)
            numbers.remove(randomNumbers)
        }
    return (numbers, results)
    }


    @IBAction func randomize(_ sender: Any) {
        
        //call the randomizing function and the first Set from its results
        let runFunction = iterateAndRemove()
        let result = runFunction.1
        
        //change set to String without square brackets
        let theString = result.map(String.init).joined(separator: ", ")
        
        bigLottoResult.text = theString
        
    }
    
    
    @IBAction func switchViews(_ sender: UIButton){
    }
    
   
    @IBAction func goBack(_ sender: Any) {
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
