import 'package:flutter/material.dart';
import 'package:flutter_expensetracker/models/expense.dart';
import 'package:flutter_expensetracker/widget/expenses_list/expense_item.dart';

class ExpenseList extends StatelessWidget {
  const ExpenseList({super.key, required this.expenses});
  final List<Expense> expenses;

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: expenses.length,
      itemBuilder: (context, index) => ExpenseItem(expenses[index]),
    );
  }
}
